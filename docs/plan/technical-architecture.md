# Technical Architecture & System Design

> **Document Owner:** Platform Engineering | **Last Updated:** 2026-03-10 | **Classification:** Internal

## Architecture Overview

The APEI platform is built on a **microservices architecture** deployed on Kubernetes, with an event-driven backbone for asynchronous communication between services. The system is designed for horizontal scalability, fault isolation, and independent deployment of individual components.

### Design Principles

1. **API-first** — every capability is exposed through a versioned REST or gRPC API before any UI is built
2. **Event-driven** — services communicate asynchronously via an event bus; synchronous calls are used only when consistency requires it
3. **Infrastructure as Code** — all infrastructure is defined in Terraform and deployed through CI/CD pipelines
4. **Zero-trust networking** — service-to-service communication requires mutual TLS and JWT-based authorization
5. **Observability by default** — every service emits structured logs, metrics, and traces from day one

---

## System Components

| Component | Type | Technology | Owner | Status | SLA (Uptime) |
|-----------|------|-----------|-------|--------|--------------|
| API Gateway | Infrastructure | Kong + custom plugins | Platform Team | Production | 99.99% |
| Auth Service | Core Service | Go 1.22, PostgreSQL | Identity Team | Production | 99.99% |
| Workflow Engine | Core Service | Rust, RocksDB | Core Engine Team | Production | 99.95% |
| Orchestrator | Core Service | Go 1.22, NATS JetStream | Core Engine Team | Production | 99.95% |
| Event Bus | Infrastructure | Apache Kafka 3.7 | Platform Team | Production | 99.99% |
| Task Queue | Infrastructure | Redis 7.2 Cluster | Platform Team | Production | 99.95% |
| Document Store | Data Layer | PostgreSQL 16 + Citus | Data Team | Production | 99.95% |
| Search Index | Data Layer | Elasticsearch 8.12 | Data Team | Production | 99.9% |
| Object Storage | Data Layer | MinIO (S3-compatible) | Platform Team | Production | 99.95% |
| AI Inference Service | ML Service | Python 3.12, vLLM, CUDA | ML Team | Beta | 99.5% |
| Notification Service | Support Service | Node.js 20, Bull MQ | Product Team | Production | 99.9% |
| Analytics Pipeline | Data Layer | Apache Flink, ClickHouse | Data Team | Production | 99.5% |
| Web Dashboard | Frontend | React 18, TypeScript, Vite | Frontend Team | Production | 99.9% |
| Mobile App | Frontend | React Native 0.73 | Mobile Team | Beta | 99.0% |

---

## System Architecture Diagram

```mermaid
flowchart TD
    WebApp["Web App"] --> GW["API Gateway\nKong"]
    Mobile["Mobile App"] --> GW
    CLI["CLI Tool"] --> GW
    ExtAPI["Third-Party APIs"] --> GW

    GW --> AuthSvc["Auth Service\nGo + PostgreSQL"]
    GW --> Engine["Workflow Engine\nRust + RocksDB"]
    GW --> Orch["Orchestrator\nGo + NATS JetStream"]

    Engine --> Kafka["Event Bus\nApache Kafka"]
    Orch --> Kafka

    Kafka --> AI["AI Inference\nPython + vLLM"]
    Kafka --> Notif["Notification Service\nNode.js + BullMQ"]
    Kafka --> Analytics["Analytics Pipeline\nFlink + ClickHouse"]

    AuthSvc --> PG[("PostgreSQL + Citus")]
    Engine --> PG
    Notif --> PG
    Analytics --> ES[("Elasticsearch 8.12")]
    Engine --> S3[("MinIO / S3")]
```

---

## Technology Decision Log

| Decision | Options Considered | Chosen | Rationale | Date |
|----------|-------------------|--------|-----------|------|
| Primary language for core services | Go, Rust, Java, C# | Go (general), Rust (engine) | Go for rapid development and strong concurrency; Rust for the hot-path workflow engine where memory safety and performance are critical | 2024-06-15 |
| Event bus | Kafka, NATS, RabbitMQ, Pulsar | Apache Kafka | Battle-tested at scale, strong ecosystem, exactly-once semantics, team familiarity | 2024-07-01 |
| Primary database | PostgreSQL, CockroachDB, MySQL | PostgreSQL + Citus | Citus provides horizontal sharding while preserving PostgreSQL compatibility; avoids CockroachDB licensing concerns | 2024-07-10 |
| API Gateway | Kong, Envoy, AWS API Gateway, Traefik | Kong | Plugin ecosystem, Lua extensibility, strong Kubernetes integration, community support | 2024-08-01 |
| ML inference runtime | TensorFlow Serving, Triton, vLLM, Ollama | vLLM | Best throughput for LLM serving, PagedAttention, active community, easy horizontal scaling | 2025-09-15 |
| Frontend framework | React, Vue, Svelte, Angular | React 18 | Largest talent pool, mature ecosystem, team expertise, strong TypeScript support | 2024-06-01 |
| Search engine | Elasticsearch, Meilisearch, Typesense | Elasticsearch | Full-text search + analytics in one system, mature aggregation framework, handles our scale (500M+ docs) | 2024-08-20 |
| Container orchestration | Kubernetes, Nomad, ECS | Kubernetes | Industry standard, portability across clouds, GitOps with ArgoCD | 2024-06-01 |

---

## API Specification

### Core Endpoints

| Method | Endpoint | Auth | Description | Rate Limit |
|--------|----------|------|-------------|------------|
| `POST` | `/api/v2/workflows` | Bearer JWT | Create a new workflow definition | 100 req/min |
| `GET` | `/api/v2/workflows/{id}` | Bearer JWT | Retrieve a workflow by ID | 500 req/min |
| `PUT` | `/api/v2/workflows/{id}` | Bearer JWT | Update an existing workflow | 100 req/min |
| `DELETE` | `/api/v2/workflows/{id}` | Bearer JWT | Soft-delete a workflow | 50 req/min |
| `POST` | `/api/v2/workflows/{id}/execute` | Bearer JWT | Trigger a workflow execution | 200 req/min |
| `GET` | `/api/v2/executions/{id}` | Bearer JWT | Get execution status and results | 500 req/min |
| `GET` | `/api/v2/executions/{id}/logs` | Bearer JWT | Stream execution logs (SSE) | 100 req/min |
| `POST` | `/api/v2/workflows/{id}/schedule` | Bearer JWT | Create a cron-based schedule | 50 req/min |
| `GET` | `/api/v2/analytics/workflows` | Bearer JWT | Workflow analytics and metrics | 30 req/min |
| `POST` | `/api/v2/ai/generate` | Bearer JWT + AI scope | Generate workflow from natural language | 20 req/min |

### Authentication Flow

All API requests require a valid JWT obtained through OAuth 2.0 / OIDC:

```
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
```

#### API Usage Examples

**HTML** — Embed a workflow status widget:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Workflow Status</title>
  <style>
    body { font-family: system-ui, sans-serif; padding: 24px; background: #f8fafc; }
    .card { background: #fff; border-radius: 10px; padding: 20px 24px; border: 1px solid #e2e8f0; max-width: 420px; }
    .status { display: flex; align-items: center; gap: 10px; margin-top: 12px; }
    .dot { width: 10px; height: 10px; border-radius: 50%; background: #22c55e; animation: pulse 1.5s infinite; }
    .label { font-size: 14px; font-weight: 600; color: #1D1F2A; }
    .meta { font-size: 12px; color: #64748b; margin-top: 4px; }
    @keyframes pulse { 0%,100% { opacity: 1; } 50% { opacity: 0.4; } }
  </style>
</head>
<body>
  <div class="card">
    <strong>daily-data-sync</strong>
    <div class="status">
      <div class="dot"></div>
      <div>
        <div class="label">Running</div>
        <div class="meta">Started 2 minutes ago &middot; Step 2 of 3</div>
      </div>
    </div>
  </div>
</body>
</html>
```

**Python** — Create and execute a workflow:

```python
import requests

API_BASE = "https://api.apei-platform.com/v2"
TOKEN = "your-jwt-token"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}

# Create a workflow
workflow_payload = {
    "name": "daily-data-sync",
    "description": "Sync CRM data to warehouse every 24h",
    "steps": [
        {
            "id": "extract",
            "type": "http_request",
            "config": {
                "url": "https://crm.example.com/api/contacts",
                "method": "GET",
                "headers": {"Authorization": "Bearer ${secrets.CRM_TOKEN}"}
            }
        },
        {
            "id": "transform",
            "type": "jq_transform",
            "config": {"expression": ".data[] | {id, email, updated_at}"},
            "depends_on": ["extract"]
        },
        {
            "id": "load",
            "type": "database_insert",
            "config": {
                "connection": "${connections.warehouse}",
                "table": "contacts_staging",
                "mode": "upsert",
                "conflict_key": "id"
            },
            "depends_on": ["transform"]
        }
    ],
    "error_handler": {
        "type": "retry",
        "max_retries": 3,
        "backoff": "exponential"
    }
}

resp = requests.post(f"{API_BASE}/workflows", json=workflow_payload, headers=headers)
workflow = resp.json()
print(f"Created workflow: {workflow['id']}")

# Execute the workflow
exec_resp = requests.post(
    f"{API_BASE}/workflows/{workflow['id']}/execute",
    json={"params": {"full_sync": True}},
    headers=headers,
)
execution = exec_resp.json()
print(f"Execution started: {execution['execution_id']}")
```

**JavaScript** — Monitor execution with Server-Sent Events:

```javascript
const API_BASE = "https://api.apei-platform.com/v2";
const TOKEN = "your-jwt-token";

// Create workflow
const workflow = await fetch(`${API_BASE}/workflows`, {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${TOKEN}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    name: "realtime-alert-pipeline",
    steps: [
      {
        id: "listen",
        type: "webhook_trigger",
        config: { path: "/alerts/incoming", method: "POST" },
      },
      {
        id: "classify",
        type: "ai_classify",
        config: {
          model: "apei-classifier-v2",
          labels: ["critical", "warning", "info"],
        },
        depends_on: ["listen"],
      },
      {
        id: "route",
        type: "conditional_branch",
        config: {
          conditions: [
            { when: "classify.output.label == 'critical'", then: "page_oncall" },
            { when: "classify.output.label == 'warning'", then: "slack_notify" },
          ],
          default: "log_only",
        },
        depends_on: ["classify"],
      },
    ],
  }),
}).then(r => r.json());

// Stream execution logs via SSE
const evtSource = new EventSource(
  `${API_BASE}/executions/${workflow.last_execution_id}/logs?token=${TOKEN}`
);

evtSource.addEventListener("step_complete", (event) => {
  const data = JSON.parse(event.data);
  console.log(`Step ${data.step_id} completed in ${data.duration_ms}ms`);
});

evtSource.addEventListener("execution_complete", (event) => {
  const data = JSON.parse(event.data);
  console.log(`Workflow finished: ${data.status} (${data.total_duration_ms}ms)`);
  evtSource.close();
});

evtSource.addEventListener("error", () => {
  console.error("SSE connection lost, reconnecting...");
});
```

**Go** — Bulk workflow management:

```go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"time"
)

const apiBase = "https://api.apei-platform.com/v2"

type Workflow struct {
	ID          string    `json:"id"`
	Name        string    `json:"name"`
	Status      string    `json:"status"`
	CreatedAt   time.Time `json:"created_at"`
	LastRunAt   time.Time `json:"last_run_at,omitempty"`
	SuccessRate float64   `json:"success_rate"`
}

type WorkflowList struct {
	Data       []Workflow `json:"data"`
	TotalCount int       `json:"total_count"`
	NextCursor string    `json:"next_cursor,omitempty"`
}

func listWorkflows(token string, cursor string) (*WorkflowList, error) {
	url := fmt.Sprintf("%s/workflows?limit=50&status=active", apiBase)
	if cursor != "" {
		url += "&cursor=" + cursor
	}

	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return nil, fmt.Errorf("creating request: %w", err)
	}
	req.Header.Set("Authorization", "Bearer "+token)

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return nil, fmt.Errorf("executing request: %w", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		body, _ := io.ReadAll(resp.Body)
		return nil, fmt.Errorf("API error %d: %s", resp.StatusCode, string(body))
	}

	var result WorkflowList
	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		return nil, fmt.Errorf("decoding response: %w", err)
	}
	return &result, nil
}

func executeWorkflow(token, workflowID string, params map[string]interface{}) (string, error) {
	body, _ := json.Marshal(map[string]interface{}{"params": params})
	url := fmt.Sprintf("%s/workflows/%s/execute", apiBase, workflowID)

	req, _ := http.NewRequest("POST", url, bytes.NewReader(body))
	req.Header.Set("Authorization", "Bearer "+token)
	req.Header.Set("Content-Type", "application/json")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	var result struct {
		ExecutionID string `json:"execution_id"`
	}
	json.NewDecoder(resp.Body).Decode(&result)
	return result.ExecutionID, nil
}

func main() {
	token := "your-jwt-token"

	workflows, err := listWorkflows(token, "")
	if err != nil {
		fmt.Printf("Error listing workflows: %v\n", err)
		return
	}

	fmt.Printf("Found %d active workflows\n", workflows.TotalCount)
	for _, wf := range workflows.Data {
		fmt.Printf("  [%s] %s — success rate: %.1f%%\n", wf.ID, wf.Name, wf.SuccessRate*100)
	}
}
```

---

## Non-Functional Requirements

| Requirement | Category | Target | Current | Measurement |
|------------|----------|--------|---------|-------------|
| API response time (p95) | Performance | < 200ms | 180ms | Datadog APM |
| API response time (p99) | Performance | < 500ms | 420ms | Datadog APM |
| Workflow execution throughput | Performance | 10,000 exec/sec | 7,200 exec/sec | Load test (k6) |
| System availability | Reliability | 99.95% | 99.97% | Uptime calculation |
| Recovery Time Objective (RTO) | Reliability | 15 minutes | 22 minutes | Incident retrospectives |
| Recovery Point Objective (RPO) | Reliability | 1 minute | 30 seconds | Backup verification |
| Time to deploy (commit to prod) | Velocity | < 30 minutes | 24 minutes | CI/CD metrics |
| Concurrent users | Scalability | 50,000 | 32,000 (tested) | Load test (k6) |
| Data encryption at rest | Security | AES-256 | AES-256 | Compliance audit |
| Data encryption in transit | Security | TLS 1.3 | TLS 1.3 | SSL Labs scan |
| Audit log retention | Compliance | 7 years | 7 years | Policy enforcement |

---

<details>
<summary>Legacy System Migration Notes</summary>

### Migration from v1 Monolith

The original APEI platform (v1) was a Django monolith deployed on EC2 instances. Migration to the current microservices architecture began in Q3 2024 and is **85% complete** as of March 2026.

#### Remaining Migration Items

- [ ] Migrate legacy reporting engine to ClickHouse-based analytics pipeline (target: Q2 2026)
- [ ] Decommission legacy PostgreSQL 12 instance after data verification (target: Q2 2026)
- [ ] Port remaining 12 custom workflow actions from Python to Go (target: Q3 2026)
- [ ] Sunset v1 API endpoints (currently serving ~3% of traffic) (target: Q4 2026)

#### Migration Lessons Learned

1. **Strangler fig pattern worked well** — we routed traffic incrementally to new services behind the API gateway, avoiding a big-bang cutover
2. **Data migration was the hardest part** — schema differences between the monolith ORM models and the new normalized schema required 47 custom migration scripts
3. **Feature parity took longer than expected** — the monolith had accumulated undocumented features over 3 years; discovering and replicating them added 2 months to the timeline
4. **Dual-write period was essential** — running both systems in parallel for 6 weeks caught 23 data consistency bugs before the full cutover

#### v1 API Compatibility Layer

A compatibility shim exists at `/api/v1/*` that translates v1 API calls to v2 format. This shim will be removed in Q4 2026. Clients still using v1 endpoints:

| Client | v1 Calls/Day | Migration Status | Contact |
|--------|-------------|-----------------|---------|
| Legacy Mobile App (iOS 14) | 12,400 | In progress — targeting v2 by April 2026 | @mobile-team |
| Partner: AcmeCorp Integration | 3,200 | Notified — migration guide sent | @partnerships |
| Internal: Legacy Admin Panel | 890 | Scheduled for rebuild in Q3 2026 | @frontend-team |

</details>
