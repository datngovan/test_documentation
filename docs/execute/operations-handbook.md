# Operations Handbook

> **Document Owner:** Site Reliability Engineering | **Classification:** Internal | **Last Updated:** 2026-03-21

## 1. On-Call Operations

### 1.1 On-Call Responsibilities

#### 1.1.1 Primary On-Call

The primary on-call engineer is the first responder for all production alerts.

##### 1.1.1.1 Daily Routines

- **Morning health check (9:00 AM local time)**
  - Review overnight alerts:
    - Check PagerDuty incident log for any auto-resolved alerts
      - Auto-resolved within 5 min: usually transient, log for pattern review
      - Auto-resolved within 5–30 min: investigate root cause, add to weekly report
      - Not resolved: should already be in active incident (escalate if missed)
    - Review Datadog anomaly detection feed
      - Filter: `env:production severity:warning,error`
      - Dismiss false positives with label `fp:confirmed`
      - File tickets for true positives even if auto-resolved
  - Review deployment queue:
    - Check for any PRs merged to `main` overnight that haven't been deployed yet
      - If > 24 hours since merge: flag to Engineering Manager
      - If deploy is blocked: investigate CI/CD pipeline status
    - Verify staging environment matches production configuration
  - Check Kafka consumer lag:
    ```bash
    kubectl -n apei-core exec -it deploy/kafka-tools -- \
      kafka-consumer-groups --bootstrap-server kafka:9092 \
      --describe --all-groups | awk '$5 > 1000 {print}'
    ```
    - Lag < 100: normal
    - Lag 100–1,000: monitor, check processing rate trends
    - Lag > 1,000: investigate consumer health immediately
    - Lag > 10,000: potential incident — follow escalation procedure

- **End-of-shift handoff (within 30 min of rotation end)**
  - Complete the handoff document in Notion:
    - Active incidents (status, owner, current theory)
    - Known degradations (symptom, affected customers, ETA to fix)
    - Elevated alerts (noisy alerts being investigated or suppressed)
    - Pending deploys (what's in the queue, any concerns)
    - Items for next on-call to watch:
      - Specific metrics that were trending unusual
      - Customer-reported issues that need follow-up
      - Scheduled maintenance windows

##### 1.1.1.2 Incident Response Procedures

When an alert fires:

1. **Acknowledge** (within 5 min for SEV-1, 15 min for SEV-2)
   - Acknowledge in PagerDuty to stop escalation
   - Post in `#incidents`:
     ```
     🚨 [SEV-X] <Alert name> — Investigating
     ```

2. **Assess**
   - Determine blast radius:
     - How many users are affected?
       - Check Datadog: `apei.users.active{env:production}` — compare to baseline
       - Query affected org count: `SELECT COUNT(DISTINCT org_id) FROM executions WHERE status='failed' AND started_at > NOW() - INTERVAL '15 minutes'`
     - What features are degraded?
       - Run smoke tests: `go test ./tests/smoke/... -v`
       - Check synthetic monitors: Datadog Synthetics dashboard
     - Is data at risk (corruption, loss)?
       - Check PostgreSQL replication lag: should be < 100ms
       - Verify S3 artifact writes are succeeding
   - Determine severity:
     - SEV-1: Complete outage OR data at risk OR > 20% of users affected
     - SEV-2: Major feature broken OR 5–20% of users affected
     - SEV-3: Minor degradation OR < 5% of users affected
     - SEV-4: Cosmetic or isolated issue

3. **Mitigate** (restore service first, root cause second)
   - Common mitigations by symptom:
     - High error rate on API:
       - Check for recent deploys: `kubectl -n apei-core rollout history deployment/workflow-engine`
       - If deploy within last hour: consider rollback
       - If no recent deploy: check downstream dependencies
     - High latency (p99 > 2x baseline):
       - Check CPU/memory on pods: `kubectl -n apei-core top pods`
       - Check database connection pool: query `pg_stat_activity`
       - Check Kafka lag — may indicate processing backlog
     - Kafka consumer lag spike:
       - Check consumer pod health: `kubectl -n apei-core get pods -l app=orchestrator`
       - Restart consumers if stuck: `kubectl -n apei-core rollout restart deployment/orchestrator`
       - If partition rebalancing: wait up to 90 seconds for stabilization

4. **Communicate**
   - For SEV-1/2: Update status page within 15 min of confirmation
     - Be factual, not speculative: "We are investigating elevated error rates on workflow execution"
     - Do NOT include internal details (infra, cause theories) in public updates
   - For enterprise customers: CSM team to notify accounts with > $100K ACV within 30 min
   - Update `#incidents` every 30 min until resolved

5. **Resolve and Document**
   - Mark incident resolved in PagerDuty
   - Update status page: "Resolved — all systems normal"
   - File post-mortem ticket (required for all SEV-1; optional for SEV-2):
     - Owner: incident commander
     - Template: `https://notion.apei.io/post-mortem-template`
     - Due: within 5 business days

---

### 1.2 Alert Runbooks

#### 1.2.1 `WorkflowEngineHighErrorRate`

**Trigger condition:** `rate(apei_http_requests_total{service="workflow-engine",status=~"5.."}[5m]) / rate(apei_http_requests_total{service="workflow-engine"}[5m]) > 0.05` for 3 minutes

**Severity:** SEV-2 (auto-page primary on-call)

##### 1.2.1.1 Diagnostic Steps

```bash
# Step 1: Check pod status
kubectl -n apei-core get pods -l app=workflow-engine -o wide

# Step 2: Check recent logs for error patterns
kubectl -n apei-core logs -l app=workflow-engine --tail=200 --since=10m | \
  grep -E '"level":"error"|panic|FATAL' | \
  jq -r '. | [.timestamp, .error, .trace_id] | @tsv' | \
  sort | uniq -c | sort -rn | head -20

# Step 3: Check if error is tied to a specific workflow or org
kubectl -n apei-core exec -it deploy/workflow-engine -- \
  apei-debug top-errors --last=10m --group-by=org_id

# Step 4: Verify database connectivity
kubectl -n apei-core exec -it deploy/workflow-engine -- \
  apei-debug db-ping --all-replicas

# Step 5: Check Vault connectivity (secrets needed for workflow execution)
kubectl -n apei-core exec -it deploy/workflow-engine -- \
  vault status
```

##### 1.2.1.2 Decision Tree

```
  [Alert] High error rate detected
              │
    ┌─────────▼──────────┐
    │  Recent deploy      │
    │  within 2 hours?    │
    └────┬──────────┬─────┘
        YES          NO
         │             │
┌────────▼──────┐  ┌───▼──────────────────────┐
│ Check deploy  │  │  Errors specific to one  │
│ diff for      │  │   org or workflow?        │
│ breaking chgs │  └───────┬──────────┬────────┘
└───────┬───────┘         YES          NO
        │                  │             │
┌───────▼────────┐  ┌──────▼──────┐  ┌──▼──────────────────┐
│ Rollback if    │  │ Downgrade   │  │  Database errors in  │
│ suspect:       │  │ to SEV-3;   │  │      logs?           │
│ kubectl rollout│  │ Notify CSM  │  └──────┬──────────┬────┘
│ undo deploy/   │  └─────────────┘        YES          NO
│ workflow-engine│                           │             │
└────────────────┘              ┌────────────▼──┐  ┌───────▼────────────┐
                                │ Check         │  │ Dependency timeout  │
                                │ pg_stat_activ.│  │     errors?         │
                                │ lock contention│ └────────┬──────┬─────┘
                                │ + repl. lag;  │         YES      NO
                                │ consider      │          │        │
                                │ failover      │  ┌───────▼──┐  ┌──▼───────────┐
                                └───────────────┘  │ Identify │  │ Escalate to  │
                                                    │ timed-out│  │ engine team  │
                                                    │ service; │  │ for deep     │
                                                    │ apply    │  │ investigation│
                                                    │ circuit  │  └──────────────┘
                                                    │ breaker  │
                                                    └──────────┘
```

---

## 2. Deployment Operations

### 2.1 Release Management

#### 2.1.1 Release Versioning

We follow **Semantic Versioning 2.0.0** with extensions for pre-release:

- `MAJOR.MINOR.PATCH` — for production releases
  - `MAJOR` — breaking API changes (rare, requires migration guide + deprecation period)
    - Minimum deprecation period: 6 months with backward-compatible shim
    - Customer notification: 90 days before `MAJOR` bump
    - Migration guide required in docs before release
  - `MINOR` — new features, backward-compatible
    - Release cadence: 2 weeks (aligned with sprint boundary)
    - Requires: feature complete, tests passing, docs updated
  - `PATCH` — bug fixes, security patches
    - Release cadence: as-needed (urgent patches within 24 hours)
    - Hotfix process bypasses normal sprint cycle
- `MAJOR.MINOR.PATCH-rc.N` — release candidates
  - Deployed to staging + beta customer environment
  - Minimum soak time: 48 hours before production
  - Automated canary traffic: 5% → 25% → 100% over 24 hours
- `MAJOR.MINOR.PATCH-alpha.N` — alpha builds (internal testing only)

#### 2.1.2 Release Checklist (per sprint)

```
Pre-release (Day -3, Monday):
  □ Feature freeze — no new features merged after this point
  □ Regression test suite run against staging (automated, ~45 min)
  □ Manual QA session for high-risk changes (QA lead + feature owner)
  □ Release notes drafted (auto-generated from PR descriptions + manual review)
  □ Performance benchmark run (k6 load test against staging)
    □ p95 latency within 10% of baseline
    □ Error rate < 0.1%
    □ Memory usage within 15% of baseline

Release preparation (Day -1, Wednesday):
  □ Release candidate tagged: git tag v2.X.Y-rc.1
  □ RC deployed to staging
  □ Smoke tests passed on RC build
  □ Customer-facing changelog reviewed by Product Manager
  □ On-call engineer briefed on changes in this release

Release day (Day 0, Thursday):
  □ Deploy to production (10:00 AM EST — avoid Friday deploys)
  □ Canary traffic: 5% for 2 hours
    □ Monitor: error rate, latency, memory
    □ Roll back if any metric degrades > 20%
  □ Canary traffic: 25% for 2 hours
    □ Same monitoring thresholds
  □ Full traffic: 100%
  □ Post-deploy smoke tests
  □ Release notes published to changelog.apei.io
  □ Notify `#product-updates` Slack channel
```

---

## 3. Capacity Planning

### 3.1 Scaling Policies

#### 3.1.1 Horizontal Pod Autoscaler (HPA) Configuration

Each service has its own scaling policy tuned to its traffic pattern:

- **`workflow-engine`**
  - Min replicas: 3 (for redundancy across AZs)
  - Max replicas: 30
  - Scale-up trigger: CPU > 70% for 2 min OR memory > 80% for 2 min
    - Scale-up step: +2 replicas (not +1, to handle traffic bursts faster)
    - Scale-up cooldown: 60 seconds
  - Scale-down trigger: CPU < 30% AND memory < 40% for 10 min
    - Scale-down step: -1 replica
    - Scale-down cooldown: 5 minutes
    - Scale-down disabled during business hours (8AM–8PM EST) — prevents thrashing

- **`orchestrator`**
  - Min replicas: 2
  - Max replicas: 20
  - Scale trigger: custom metric `kafka_consumer_lag{group="apei-orchestrator"} > 5000`
    - Exposed via KEDA (Kubernetes Event-driven Autoscaler)
    - Scale formula: `ceil(lag / 5000)` replicas (1 replica per 5,000 messages of lag)
    - Max scale-up rate: +4 replicas per minute

- **`ai-inference`** (GPU nodes)
  - Min replicas: 1 (GPUs are expensive — scale to zero overnight if no traffic)
    - Scale-to-zero: if 0 requests for 10 min between 10PM–6AM EST
  - Max replicas: 8 (limited by GPU node pool)
  - Scale trigger: custom metric `inference_queue_depth > 10`
    - Queue depth per replica target: 10 concurrent requests
    - Startup probe: 90 second timeout (model loading is slow)
    - Pre-warming: automatically scale up 1 replica at 7AM EST before business hours

#### 3.1.2 Capacity Planning Calendar

| Review Cadence | Scope | Owner | Next Review |
|---------------|-------|-------|------------|
| Weekly | Kafka partition count, consumer lag trends | Platform Lead | 2026-03-30 |
| Monthly | Pod HPA bounds, node pool min/max | SRE Lead | 2026-04-07 |
| Quarterly | Total cluster size, reserved instance coverage, cost per execution | Engineering Manager + Finance | 2026-06-15 |
| Annually | Multi-region expansion, disaster recovery infrastructure | CTO + VP Engineering | 2027-01 |

<details>
<summary>Runbook History — Changes to This Document</summary>

### Changelog

| Date | Author | Change |
|------|--------|--------|
| 2026-03-21 | @james.liu | Added GPU autoscaling policy for ai-inference service |
| 2026-03-10 | @sre-team | Added WorkflowEngineHighErrorRate decision tree |
| 2026-02-28 | @james.liu | Updated incident response procedure — added Kafka lag diagnostic |
| 2026-02-15 | @morgan.rivera | Added release checklist canary thresholds after SEV-1 in January |
| 2026-01-20 | @sre-team | Initial version — migrated from Confluence |

<details>
<summary>Archived Runbooks (pre-2026, kept for reference)</summary>

#### Legacy Alert: `MonolithHighMemory` (deprecated 2025-12-01)

> **Note:** This alert was for the legacy Django monolith, which has been fully decommissioned. Kept here for historical context only.

**Trigger:** Monolith EC2 instance memory > 85% for 5 min

**Resolution (historical):**
```bash
# Restart the uWSGI workers (graceful — no downtime)
sudo systemctl reload uwsgi

# If that doesn't help, bounce the entire app process
sudo systemctl restart uwsgi

# Check for memory leak patterns
ps aux --sort=-%mem | head -20
```

This runbook is no longer applicable. The monolith was replaced by the microservices architecture in Q4 2025.

</details>
</details>
