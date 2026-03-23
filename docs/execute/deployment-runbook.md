# Deployment Runbook & CI/CD Procedures

> **Document Owner:** DevOps & Platform Engineering | **Last Updated:** 2026-03-18 | **Severity:** Operational — Follow procedures exactly

## Prerequisites Checklist

Before initiating any deployment, confirm the following:

- [x] You have `kubectl` access to the target cluster with `deploy` role
- [x] You are connected to the VPN (production deployments require `prod-vpn` profile)
- [ ] You have verified the CI pipeline is green on the `main` branch
- [ ] You have reviewed the changelog for breaking changes
- [ ] The deployment window is confirmed (no freeze in effect)
- [ ] You have notified `#deployments` Slack channel with the deployment intent
- [ ] Rollback procedure has been reviewed (see section below)
- [ ] On-call engineer is aware and available

---

## Environment Variables

### Required Configuration

| Variable | Description | Required | Example |
|----------|-----------|----------|---------|
| `APEI_ENV` | Target environment identifier | Yes | `production`, `staging`, `dev` |
| `APEI_CLUSTER` | Kubernetes cluster name | Yes | `prod-us-east-1`, `staging-eu-west-1` |
| `APEI_RELEASE_TAG` | Docker image tag to deploy | Yes | `v2.14.3`, `sha-a1b2c3d` |
| `APEI_NAMESPACE` | Kubernetes namespace | Yes | `apei-core`, `apei-ml` |
| `DATABASE_URL` | PostgreSQL connection string | Yes | `postgres://user:pass@host:5432/apei` |
| `KAFKA_BROKERS` | Comma-separated Kafka broker addresses | Yes | `kafka-0:9092,kafka-1:9092,kafka-2:9092` |
| `REDIS_URL` | Redis cluster connection string | Yes | `redis://redis-cluster:6379` |
| `VAULT_ADDR` | HashiCorp Vault server address | Yes | `https://vault.internal.apei.io:8200` |
| `VAULT_ROLE` | Vault AppRole for the deploying service | Yes | `deploy-prod-role` |
| `DD_API_KEY` | Datadog API key for metrics/logs | Yes | `dd-api-key-xxxxxxxx` |
| `SENTRY_DSN` | Sentry error tracking DSN | No | `https://key@sentry.apei.io/4` |
| `FEATURE_FLAGS_URL` | LaunchDarkly relay proxy URL | No | `http://ld-relay:8030` |
| `AI_MODEL_ENDPOINT` | ML inference service endpoint | Conditional | `http://ai-inference:8080/v1` |
| `SLACK_WEBHOOK_URL` | Deployment notification webhook | No | `https://hooks.slack.com/services/T.../B.../xxx` |

---

## Step-by-Step Deployment Procedure

### Phase 1: Pre-Deploy Verification

Run these checks before touching any infrastructure:

```bash
# 1. Verify you are targeting the correct cluster
kubectl config current-context
# Expected: arn:aws:eks:us-east-1:123456789:cluster/prod-us-east-1

# 2. Check current deployment status
kubectl -n apei-core get deployments -o wide
kubectl -n apei-core get pods --field-selector=status.phase!=Running

# 3. Verify the image exists in the registry
aws ecr describe-images \
  --repository-name apei/core-services \
  --image-ids imageTag=${APEI_RELEASE_TAG} \
  --query 'imageDetails[0].{Tag:imageTags[0],Pushed:imagePushedAt,Size:imageSizeInBytes}'

# 4. Run pre-deploy integration tests against staging
APEI_ENV=staging go test ./tests/integration/... -v -count=1 -timeout 5m

# 5. Check for active incidents or ongoing deploys
curl -s https://status.internal.apei.io/api/v1/incidents?status=active | jq '.incidents | length'
# Expected: 0
```

### Pre-Deploy Verification Checklist

- [ ] Cluster context is correct (production vs. staging)
- [ ] No pods in CrashLoopBackOff or Error state
- [ ] Target image tag exists in ECR and is the correct build
- [ ] Integration tests pass against staging
- [ ] No active incidents in the status page
- [ ] Database migrations have been applied (if any)

### Phase 2: Database Migrations (if applicable)

```bash
# Check pending migrations
kubectl -n apei-core exec -it deploy/migration-runner -- \
  apei-migrate status --env production

# Apply migrations with dry-run first
kubectl -n apei-core exec -it deploy/migration-runner -- \
  apei-migrate up --env production --dry-run

# Apply migrations for real
kubectl -n apei-core exec -it deploy/migration-runner -- \
  apei-migrate up --env production

# Verify migration state
kubectl -n apei-core exec -it deploy/migration-runner -- \
  apei-migrate status --env production
```

> **Warning:** Always apply migrations BEFORE deploying new application code. The new code expects the new schema to exist. Rolling back a migration after deployment is significantly harder.

### Phase 3: Rolling Deployment

```bash
# Set the new image tag for the target deployment
export SERVICE_NAME="workflow-engine"  # or: orchestrator, auth-service, etc.
export NEW_TAG="${APEI_RELEASE_TAG}"

# Update the deployment image
kubectl -n apei-core set image \
  deployment/${SERVICE_NAME} \
  ${SERVICE_NAME}=123456789.dkr.ecr.us-east-1.amazonaws.com/apei/${SERVICE_NAME}:${NEW_TAG}

# Monitor the rollout
kubectl -n apei-core rollout status deployment/${SERVICE_NAME} --timeout=300s

# Verify new pods are running
kubectl -n apei-core get pods -l app=${SERVICE_NAME} -o wide

# Check pod logs for startup errors
kubectl -n apei-core logs -l app=${SERVICE_NAME} --tail=50 --since=2m
```

### Phase 4: Post-Deploy Verification

```bash
# 1. Health check endpoints
curl -sf https://api.apei-platform.com/health | jq .
# Expected: {"status":"healthy","version":"2.14.3","uptime":"..."}

# 2. Run smoke tests
APEI_ENV=production go test ./tests/smoke/... -v -count=1 -timeout 3m

# 3. Check error rates in Datadog
curl -s "https://api.datadoghq.com/api/v1/query?query=avg:apei.http.error_rate{env:production}.rollup(avg,300)&from=$(date -d '10 min ago' +%s)&to=$(date +%s)" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" | jq '.series[0].pointlist[-1][1]'
# Expected: < 0.01 (1% error rate)

# 4. Verify Kafka consumer lag
kubectl -n apei-core exec -it deploy/kafka-tools -- \
  kafka-consumer-groups --bootstrap-server kafka:9092 \
  --group apei-workflow-processor --describe

# 5. Send deployment notification
curl -X POST "${SLACK_WEBHOOK_URL}" \
  -H "Content-Type: application/json" \
  -d "{\"text\":\"Deployment complete: ${SERVICE_NAME} ${NEW_TAG} to production. All health checks passing.\"}"
```

---

## Rollback Procedure

If post-deploy verification fails or anomalies are detected, initiate rollback immediately.

### Automatic Rollback (Preferred)

```bash
# 1. Undo the last rollout
kubectl -n apei-core rollout undo deployment/${SERVICE_NAME}

# 2. Monitor the rollback
kubectl -n apei-core rollout status deployment/${SERVICE_NAME} --timeout=300s

# 3. Verify the previous version is running
kubectl -n apei-core get deployment ${SERVICE_NAME} \
  -o jsonpath='{.spec.template.spec.containers[0].image}'

# 4. Run smoke tests against the rolled-back version
APEI_ENV=production go test ./tests/smoke/... -v -count=1 -timeout 3m
```

### Manual Rollback (if automatic fails)

```bash
# 1. Find the last known good image tag
kubectl -n apei-core rollout history deployment/${SERVICE_NAME}

# 2. Roll back to a specific revision
kubectl -n apei-core rollout undo deployment/${SERVICE_NAME} --to-revision=42

# 3. If the deployment is stuck, force-restart pods
kubectl -n apei-core delete pods -l app=${SERVICE_NAME} --grace-period=30

# 4. If pods won't start, scale down and investigate
kubectl -n apei-core scale deployment/${SERVICE_NAME} --replicas=0
# Investigate logs, then scale back up with fixed config
kubectl -n apei-core scale deployment/${SERVICE_NAME} --replicas=3
```

### Database Rollback (if migrations were applied)

```bash
# Check current migration version
kubectl -n apei-core exec -it deploy/migration-runner -- \
  apei-migrate status --env production

# Roll back the last N migrations
kubectl -n apei-core exec -it deploy/migration-runner -- \
  apei-migrate down --steps 1 --env production --dry-run

# Apply the rollback
kubectl -n apei-core exec -it deploy/migration-runner -- \
  apei-migrate down --steps 1 --env production
```

> **Critical:** Database rollbacks can cause data loss if the forward migration created new columns that received data. Always check with the Data Team before rolling back migrations.

---

## Monitoring Commands

### Real-Time Monitoring During Deployment

```bash
# Watch pod status in real time
watch -n 2 'kubectl -n apei-core get pods -l app=${SERVICE_NAME} -o wide'

# Stream logs from all pods of the service
kubectl -n apei-core logs -f -l app=${SERVICE_NAME} --max-log-requests=10 --prefix=true

# Monitor HTTP error rates (requires Datadog agent)
curl -s "https://api.datadoghq.com/api/v1/query?query=sum:apei.http.requests{env:production,status:5xx}.as_count()&from=$(date -d '5 min ago' +%s)&to=$(date +%s)" \
  -H "DD-API-KEY: ${DD_API_KEY}" | jq '.series[0].pointlist | map(.[1]) | add'

# Check resource usage
kubectl -n apei-core top pods -l app=${SERVICE_NAME}

# Monitor HPA scaling
kubectl -n apei-core get hpa ${SERVICE_NAME}-hpa --watch
```

### Key Dashboards

- **Service Overview:** `https://app.datadoghq.com/dash/apei-production`
- **Error Tracking:** `https://sentry.apei.io/organizations/apei/issues/`
- **Kafka Lag:** `https://app.datadoghq.com/dash/kafka-consumer-lag`
- **Infrastructure:** `https://grafana.internal.apei.io/d/k8s-overview`

---

## Incident Response Matrix

| Severity | Definition | Response Time | Escalation Path | On-Call Owner |
|----------|-----------|--------------|-----------------|---------------|
| **SEV-1** | Complete service outage; all users affected | 5 minutes | Immediately page VP Engineering + CTO | Primary on-call + Secondary on-call |
| **SEV-2** | Major feature degraded; >10% of users affected | 15 minutes | Page Engineering Manager after 30 min | Primary on-call |
| **SEV-3** | Minor feature degraded; <10% of users affected | 1 hour | Notify Engineering Manager via Slack | Primary on-call |
| **SEV-4** | Cosmetic issue or minor bug; workaround available | Next business day | Create JIRA ticket, assign to sprint | Triaged by Engineering Manager |

### Escalation Contacts

| Role | Primary | Secondary | Slack Handle |
|------|---------|-----------|-------------|
| On-Call Engineer | Rotating (PagerDuty) | Rotating (PagerDuty) | `@oncall-primary` |
| Engineering Manager | Jordan Park | Casey Nguyen | `@jordan.park` |
| VP Engineering | Morgan Rivera | — | `@morgan.rivera` |
| CTO | Alex Chen | — | `@alex.chen` |

---

## CI/CD Pipeline Overview

The deployment pipeline runs in GitHub Actions with the following stages:

```
┌──────────┐   ┌──────────┐   ┌───────────┐   ┌──────────┐   ┌──────────┐
│  Lint &  │──▶│  Unit    │──▶│Integration│──▶│  Build   │──▶│  Deploy  │
│  Format  │   │  Tests   │   │  Tests    │   │  & Push  │   │ (GitOps) │
└──────────┘   └──────────┘   └───────────┘   └──────────┘   └──────────┘
     │              │               │               │               │
   ~1 min        ~3 min          ~8 min          ~4 min         ~5 min
```

#### Pipeline Duration Targets

| Stage | Target | Current Average | Status |
|-------|--------|----------------|--------|
| Lint & Format | < 2 min | 1.2 min | On target |
| Unit Tests | < 5 min | 3.4 min | On target |
| Integration Tests | < 10 min | 8.1 min | On target |
| Build & Push | < 5 min | 4.2 min | On target |
| Deploy (staging) | < 5 min | 3.8 min | On target |
| Deploy (production) | < 10 min | 7.5 min | On target |
| **Total (to prod)** | **< 30 min** | **24.2 min** | **On target** |

---

<details>
<summary>Historical Deployment Issues & Lessons Learned</summary>

### Incident Log

#### 2026-03-02 — SEV-2: Workflow Engine OOM after v2.14.1 deploy

**What happened:** The workflow engine pods started hitting OOM (Out of Memory) kills approximately 20 minutes after deploying v2.14.1. The new version included a change to the in-memory workflow graph cache that did not account for workflows with >500 nodes.

**Root cause:** The graph serialization code allocated O(n^2) memory for adjacency lists. Large workflows (used by 3 enterprise customers) triggered memory spikes exceeding the 2GB pod limit.

**Resolution:** Rolled back to v2.14.0 within 8 minutes. Fix shipped in v2.14.2 with streaming graph construction (O(n) memory). Added a load test scenario with 1000-node workflows to the CI pipeline.

**Lesson:** Add memory profiling to CI for any changes touching the workflow engine hot path.

---

#### 2026-01-15 — SEV-3: Kafka consumer lag spike after deploy

**What happened:** After deploying the orchestrator v2.12.0, Kafka consumer lag for the `workflow.events` topic spiked to 500K messages. Processing resumed after 45 minutes but caused delayed workflow executions for affected users.

**Root cause:** The new version changed the Kafka consumer group ID (a typo in the config), causing the consumers to start reading from the earliest offset instead of the latest committed offset.

**Resolution:** Corrected the consumer group ID and redeployed. Added a CI check that validates consumer group IDs match the expected pattern.

**Lesson:** Consumer group IDs should be managed as constants in a shared config package, not as string literals in service configs.

---

#### 2025-11-20 — SEV-1: Database connection pool exhaustion

**What happened:** Production database became unresponsive at 14:32 UTC. All services dependent on PostgreSQL returned 503 errors. Outage lasted 23 minutes.

**Root cause:** A deploy of the notification service introduced a connection leak — database connections were acquired but not released in an error path. The connection pool (max 100 connections) was exhausted within 15 minutes under production load.

**Resolution:** Killed the leaking pods, restarted the notification service with the previous version. Fix implemented using `defer conn.Release()` pattern consistently. Added connection pool metrics alerting (alert if >80% utilized for >2 minutes).

**Lesson:** Every database operation must use `defer` to release connections. Added a linter rule to enforce this pattern.

</details>
