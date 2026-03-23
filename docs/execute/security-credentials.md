# Security Runbook & Credential Management

> **Classification:** CONFIDENTIAL — Security & DevOps Only | **Document Owner:** Security Engineering | **Last Updated:** 2026-03-12

## Credential Rotation Procedures

### Rotation Schedule

All credentials follow a mandatory rotation schedule based on sensitivity level:

| Credential Type | Rotation Frequency | Last Rotated | Next Rotation | Responsible Team | Automated |
|----------------|-------------------|-------------|---------------|-----------------|-----------|
| Database master passwords | 30 days | 2026-03-01 | 2026-03-31 | Security | Yes (Vault) |
| API service account tokens | 90 days | 2026-01-15 | 2026-04-15 | Platform | Yes (Vault) |
| TLS/SSL certificates | 90 days (auto-renew) | 2026-02-28 | 2026-05-28 | Platform | Yes (cert-manager) |
| OAuth client secrets | 180 days | 2025-12-01 | 2026-06-01 | Identity | Manual |
| AWS IAM access keys | 90 days | 2026-02-15 | 2026-05-15 | DevOps | Yes (STS) |
| SSH deploy keys | 180 days | 2025-11-01 | 2026-05-01 | DevOps | Manual |
| Encryption master keys (KMS) | 365 days | 2025-06-15 | 2026-06-15 | Security | Manual |
| Third-party API keys | Per vendor policy | Varies | Varies | Engineering | Manual |

### Rotation Procedure — Database Credentials

```bash
# 1. Generate new credentials in Vault
vault write database/rotate-root/apei-production

# 2. Verify the new credentials work
vault read database/creds/apei-readonly
# Test connection with the generated credentials
psql "postgresql://${NEW_USER}:${NEW_PASS}@db-prod.internal.apei.io:5432/apei_production" -c "SELECT 1;"

# 3. Update application configuration (zero-downtime)
kubectl -n apei-core rollout restart deployment/auth-service
kubectl -n apei-core rollout restart deployment/workflow-engine
kubectl -n apei-core rollout restart deployment/orchestrator

# 4. Verify services are healthy with new credentials
kubectl -n apei-core get pods --field-selector=status.phase!=Running
curl -sf https://api.apei-platform.com/health | jq .

# 5. Revoke old credentials
vault lease revoke -prefix database/creds/apei-production/OLD_LEASE_ID
```

---

## Vault Path Structure

### Secret Engine Layout

| Vault Path | Type | Description | Access Policy |
|-----------|------|-------------|--------------|
| `secret/data/apei/production/database` | KV v2 | Production database credentials | `apei-prod-db-read` |
| `secret/data/apei/production/api-keys` | KV v2 | Third-party API keys (Stripe, SendGrid, etc.) | `apei-prod-apikeys-read` |
| `secret/data/apei/production/encryption` | KV v2 | Application-level encryption keys | `apei-prod-encryption-read` |
| `secret/data/apei/staging/database` | KV v2 | Staging database credentials | `apei-staging-read` |
| `database/creds/apei-production` | Dynamic | Dynamically generated DB credentials | `apei-prod-db-dynamic` |
| `aws/creds/apei-deploy-role` | AWS | Dynamic AWS IAM credentials for deployment | `apei-aws-deploy` |
| `pki/issue/apei-internal` | PKI | Internal TLS certificate issuance | `apei-pki-issue` |
| `transit/keys/apei-data-encryption` | Transit | Encryption-as-a-service for PII | `apei-transit-encrypt` |

### Example: Reading a Secret

```bash
# Authenticate to Vault
export VAULT_ADDR="https://vault.internal.apei.io:8200"
vault login -method=oidc role="engineer"

# Read a production secret
vault kv get -format=json secret/data/apei/production/api-keys | jq '.data.data'

# Generate dynamic database credentials (TTL: 1 hour)
vault read database/creds/apei-production
# Output:
# Key              Value
# ---              -----
# lease_id         database/creds/apei-production/abc123
# lease_duration   1h
# username         v-oidc-apei-pro-xyz789
# password         A1b2C3d4-E5f6G7h8
```

---

## Access Control Matrix

### Service-to-Service Access

| Source Service | Target Service | Protocol | Auth Method | Permissions | Network Policy |
|---------------|---------------|----------|-------------|-------------|---------------|
| API Gateway | Auth Service | gRPC/mTLS | mTLS cert | Validate tokens, refresh | `allow-gateway-to-auth` |
| API Gateway | Workflow Engine | HTTP/mTLS | mTLS cert + JWT | All workflow CRUD | `allow-gateway-to-engine` |
| Workflow Engine | Event Bus (Kafka) | TCP/TLS | SASL/SCRAM | Produce: `workflow.events` | `allow-engine-to-kafka` |
| Orchestrator | Event Bus (Kafka) | TCP/TLS | SASL/SCRAM | Consume: `workflow.events`, `task.events` | `allow-orch-to-kafka` |
| Orchestrator | Task Queue (Redis) | TCP/TLS | Password + TLS | Read/write task queues | `allow-orch-to-redis` |
| AI Inference | Object Storage (MinIO) | HTTP/TLS | Access key + Secret | Read model artifacts | `allow-ai-to-minio` |
| Notification Service | Event Bus (Kafka) | TCP/TLS | SASL/SCRAM | Consume: `notification.events` | `allow-notif-to-kafka` |
| Analytics Pipeline | Document Store (PG) | TCP/TLS | Vault dynamic creds | Read-only replica access | `allow-analytics-to-pg` |

### Human Access Levels

| Role | Production Console | Production DB | Vault Secrets | Kubernetes Admin | Incident Response |
|------|:-:|:-:|:-:|:-:|:-:|
| Junior Engineer | No | No | No | No | Observer only |
| Senior Engineer | Read-only | Read-only (via Vault) | Read (own service) | Namespace-scoped | Participant |
| Staff Engineer | Read-only | Read-only (via Vault) | Read (all services) | Namespace-scoped | Incident Commander eligible |
| Engineering Manager | Read-only | No | Read (team services) | No | Escalation contact |
| DevOps Engineer | Full access | Read/write (via Vault) | Read/write (infra) | Cluster admin | Primary responder |
| Security Engineer | Full access | Read/write (via Vault) | Full access | Cluster admin | Primary responder |
| VP Engineering | Read-only | No | Read (all) | No | Escalation contact |
| CTO | Read-only | No | Read (all) | No | Final escalation |

---

## Security Incident Response

### Response Procedures by Incident Type

#### 1. Credential Exposure (e.g., secret committed to Git)

```bash
# Step 1: Immediately rotate the exposed credential
vault write -force secret/data/apei/production/api-keys/<exposed_key>

# Step 2: Scan for unauthorized usage
aws cloudtrail lookup-events \
  --lookup-attributes AttributeKey=AccessKeyId,AttributeValue=${EXPOSED_KEY_ID} \
  --start-time $(date -d '7 days ago' --iso-8601) \
  --query 'Events[].{Time:EventTime,Event:EventName,Source:EventSource}'

# Step 3: Revoke all sessions using the old credential
vault token revoke -accessor ${ACCESSOR_ID}

# Step 4: Notify security team
curl -X POST "${SECURITY_SLACK_WEBHOOK}" \
  -d '{"text":"SECURITY INCIDENT: Credential exposure detected. Credential rotated. Investigation in progress. Incident commander: @security-oncall"}'

# Step 5: Create incident ticket
# File in Linear under "Security Incidents" project
# Severity: SEV-2 minimum for any production credential exposure
```

#### 2. Unauthorized Access Detected

1. **Contain** — Block the source IP/user immediately via WAF rule or Vault policy revocation
2. **Assess** — Determine scope: which systems were accessed, what data was exposed
3. **Investigate** — Pull audit logs from Vault, Kubernetes, AWS CloudTrail, and application logs
4. **Remediate** — Rotate all potentially compromised credentials, patch the access vector
5. **Report** — File incident report within 24 hours; notify legal if PII may have been exposed
6. **Review** — Conduct post-incident review within 72 hours

#### 3. DDoS Attack

1. Enable AWS Shield Advanced protection (already configured, auto-activates at threshold)
2. Engage CloudFront WAF rate limiting rules
3. If application-layer attack, enable geographic blocking via Kong plugin
4. Notify `#security-incidents` channel and page on-call security engineer
5. Monitor via Datadog dashboard: `https://app.datadoghq.com/dash/ddos-protection`

---

## Compliance & Audit Requirements

### Credential Audit Log Retention

| Log Type | Retention Period | Storage | Encryption | Access |
|----------|-----------------|---------|-----------|--------|
| Vault audit log | 7 years | S3 (Glacier after 90 days) | AES-256 + KMS | Security team only |
| Kubernetes audit log | 2 years | CloudWatch + S3 | AES-256 | DevOps + Security |
| AWS CloudTrail | 7 years | S3 (Glacier after 180 days) | AES-256 + KMS | Security + Finance |
| Application auth logs | 3 years | Elasticsearch + S3 | AES-256 | Engineering + Security |
| VPN access logs | 1 year | Syslog + S3 | AES-256 | IT + Security |

> **Compliance Note:** SOC2 Type II and ISO 27001 auditors require evidence of credential rotation compliance. The Vault audit log is the primary evidence source. Ensure audit logging is NEVER disabled on production Vault instances — this is a termination-level policy violation.
