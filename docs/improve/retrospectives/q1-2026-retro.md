# Q1 2026 Team Retrospective

> **Date:** March 20, 2026 | **Facilitator:** Jordan Park | **Participants:** Full Engineering Team (22)

## Format: Start / Stop / Continue

---

## Start Doing

| Item | Votes | Owner | Action |
|------|-------|-------|--------|
| Load testing with production-scale data in CI | 14 | Platform Team | Add k6 scenario for 10K-node workflows to CI pipeline by Sprint 26-07 |
| Weekly metric review meeting (30 min, whole team) | 11 | Jordan Park | Starting Sprint 26-06 — Mondays 3PM |
| Pair programming for complex features (2+ SP) | 9 | Team norm | Add to Definition of Ready: stories > 8 SP require pairing plan |
| Explicit capacity planning for on-call overhead | 8 | Jordan Park | Reserve 15% capacity each sprint for unplanned/on-call work |
| "Architecture decision doc" before implementing major changes | 7 | Alice Chen | Template created; use for anything touching the engine or data model |

---

## Stop Doing

| Item | Votes | Root Cause | Fix |
|------|-------|-----------|-----|
| Deploying on Fridays | 16 | "Just one more thing" culture | Hard rule: no production deploys after 2PM Thursday |
| Skipping post-mortems for SEV-3 incidents | 12 | "Not serious enough" | Lightweight post-mortem (30 min, async doc) required for all SEV-3+ |
| Merging PRs without a description | 10 | Time pressure | PR template now enforced via GitHub Actions — blank description blocks CI |
| Adding `TODO` comments without a linked ticket | 8 | Good intentions, no follow-through | `TODO(ENG-XXXX)` format required; CI rejects bare `TODO:` comments |
| Running performance tests manually | 7 | No automated alternative | Block sprint: automate benchmark suite by end of Q2 |

---

## Continue Doing

| Item | Votes | Why it's working |
|------|-------|-----------------|
| Blameless post-mortems for SEV-1/2 | 18 | Trust has improved; engineers share information freely during incidents |
| Weekly 1:1s with skip-levels (quarterly) | 15 | Engineers feel heard; problems surface before they become attrition risks |
| Feature flags for all new features | 14 | Enables safe deployments; customer-facing issues caught in canary before full rollout |
| "No meeting Wednesdays" | 13 | Engineers report highest focus/flow state on Wednesdays |
| Public OKR progress dashboard | 11 | Everyone knows where we stand; no surprises at QBR |

---

## Top Action Items

| # | Action | Owner | Due Date | Done? |
|---|--------|-------|---------|-------|
| 1 | Add k6 10K-node load test to CI | Platform | Apr 14 (S26-07) | [ ] |
| 2 | Friday deploy hard rule — add to engineering handbook | Jordan Park | Apr 4 (S26-06) | [ ] |
| 3 | Implement PR description enforcement in GitHub Actions | Ivy Patel | Apr 4 (S26-06) | [ ] |
| 4 | Start weekly metric review meeting | Jordan Park | Mar 30 (S26-06) | [ ] |
| 5 | Architecture decision doc template — publish + announce | Alice Chen | Mar 27 | [x] Done |
| 6 | SEV-3 lightweight post-mortem template | Morgan Rivera | Apr 4 (S26-06) | [ ] |

---

## Mood Meter

*Anonymous pre-retro survey (scale 1–5)*

| Question | Avg Score | Change from Q4 |
|----------|-----------|----------------|
| How satisfied are you with team communication? | 4.1 | +0.3 |
| How confident are you in our technical direction? | 4.4 | +0.6 |
| How manageable is your workload? | 3.4 | -0.2 |
| How well does the team handle failure? | 4.2 | +0.4 |
| Would you recommend this team to a friend? | 4.5 | +0.3 |

**Notable:** Workload score declined — consistent with 2 SEV-1 incidents consuming significant eng-days. The platform stability investment in Q2 should improve this.
