# Sprint 26-06 — Planning & Progress

> **Sprint:** March 23 – April 4, 2026 | **Team:** Core Engineering | **Capacity:** 88 points

## Sprint Goal

> *Complete AI Engine enterprise SSO integration and ship healthcare workflow template v1 set so the team is unblocked for GA.*

---

## Committed Stories

| ID | Title | Points | Assignee | Status |
|----|-------|--------|---------|--------|
| ENG-1241 | Implement Okta SAML integration for AI Engine | 8 | Alice Chen | 🔄 In Progress |
| ENG-1242 | Add SCIM provisioning for enterprise SSO | 5 | Alice Chen | 📅 Scheduled |
| ENG-1243 | Healthcare: patient intake workflow template | 3 | Dan Okafor | 📅 Scheduled |
| ENG-1244 | Healthcare: appointment scheduling template | 3 | Dan Okafor | 📅 Scheduled |
| ENG-1245 | Healthcare: lab result notification template | 3 | Dan Okafor | 📅 Scheduled |
| ENG-1246 | Fix memory leak in Flink analytics pipeline | 5 | Bob Martinez | 🔄 In Progress |
| ENG-1247 | Upgrade Kafka to 3.7.1 (security patch) | 3 | James Liu | ✅ Done |
| ENG-1248 | Add p99 latency SLO alert for workflow engine | 2 | Karen Singh | ✅ Done |
| ENG-1249 | Refactor step handler plugin registry (tech debt) | 8 | Carol Washington | 🔄 In Progress |
| ENG-1250 | Write load test for 10K concurrent executions | 5 | Emily Zhao | 📅 Scheduled |
| ENG-1251 | Mobile: fix Android WebSocket reconnection bug | 5 | Henry Nakamura | 🔄 In Progress |
| ENG-1252 | Add workflow import/export (JSON) | 5 | Grace Kim | 📅 Scheduled |
| ENG-1253 | Update API docs with AI endpoints | 2 | Ivy Patel | 📅 Scheduled |
| ENG-1254 | Dependency audit + update (Q1 cleanup) | 3 | Karen Singh | 📅 Scheduled |
| **Total** | | **60** | | |

*Remaining 28 points reserved for unplanned work (support, bugs, on-call)*

---

## Daily Standup Log

### Day 1 — March 23

- **Alice:** Started SAML integration; IdP metadata parsing works; assertion validation in progress
- **Bob:** Reproduced Flink memory leak in staging; heap dump shows unbounded accumulation in window operator
- **James:** Kafka upgrade complete in staging; monitoring 24h before prod promotion
- **Blockers:** None

### Day 2 — March 24

- **Alice:** SAML working end-to-end with Okta sandbox; now hardening error paths
- **Bob:** Root cause confirmed: window state not evicted when watermark advances past window; fix in PR #1891
- **James:** Kafka 3.7.1 promoted to production; consumer lag nominal
- **Karen:** p99 SLO alert deployed; test-firing confirmed
- **Blockers:** ENG-1249 blocked on design review — Carol needs 30 min sync with Bob
