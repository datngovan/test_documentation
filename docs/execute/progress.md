# Progress Tracking

Effective progress tracking provides visibility into sprint execution without creating overhead. The goal is to surface problems early and celebrate wins along the way.

## Sprint Progress Dashboard

### Current Sprint: Sprint 14 (March 16-27, 2026)

**Sprint Goal:** Complete API v2 authentication endpoints and begin partner onboarding flow.

| Story | Points | Assignee | Status | Notes |
|-------|:---:|---------|--------|-------|
| APEI-401: OAuth 2.1 token endpoint | 8 | Alice | Done | Merged March 19 |
| APEI-402: Refresh token rotation | 5 | Alice | Done | Merged March 20 |
| APEI-403: API key management UI | 8 | Frank | In Review | PR #847 open |
| APEI-404: Rate limiting middleware | 5 | Bob | In Progress | 60% complete |
| APEI-405: Partner signup wizard - Step 1 | 5 | Eve | In Progress | Blocked by design |
| APEI-406: Webhook delivery system | 8 | Dan | In Progress | On track |
| APEI-407: API usage analytics endpoint | 3 | Henry | To Do | Starting March 24 |
| APEI-408: Update API documentation | 2 | Ivy | To Do | Depends on APEI-401,402 |

**Total points committed: 44 | Completed: 13 | In Progress: 26 | To Do: 5**

## Velocity Tracking

### Rolling 6-Sprint Velocity

| Sprint | Committed | Completed | Carry-over | Velocity |
|--------|:---------:|:---------:|:----------:|:--------:|
| Sprint 9 | 40 | 35 | 5 | 35 |
| Sprint 10 | 38 | 38 | 0 | 38 |
| Sprint 11 | 42 | 36 | 6 | 36 |
| Sprint 12 | 40 | 40 | 0 | 40 |
| Sprint 13 | 45 | 39 | 6 | 39 |
| Sprint 14 | 44 | 13* | — | — |

*Sprint 14 is in progress.

**Average velocity (last 5 sprints): 37.6 points**
**Standard deviation: 2.1 points**
**Recommended commitment range: 35-40 points**

### Velocity Trend Analysis

The team's velocity has been stable over the last five sprints, ranging from 35 to 40 points. Key observations:

- Sprints with zero carry-over (10, 12) correlate with fewer mid-sprint scope changes
- Sprint 11 had a carry-over of 6 due to an unplanned production incident consuming 2 engineer-days
- The team should not commit above 42 points until average velocity sustainably exceeds 40

## KPI Dashboard

### Delivery Metrics

| KPI | Target | Current | Trend | Status |
|-----|--------|---------|:-----:|--------|
| Sprint completion rate | >85% | 87% | Up | On Track |
| Average cycle time | <5 days | 4.2 days | Stable | On Track |
| Defect escape rate | <5% | 3.1% | Down | On Track |
| Code review turnaround | <24 hours | 18 hours | Stable | On Track |
| Deploy frequency | 1/day | 0.8/day | Up | At Risk |
| Change failure rate | <10% | 7% | Down | On Track |
| MTTR (mean time to recovery) | <30 min | 22 min | Down | On Track |

### Quality Metrics

| Metric | Sprint 12 | Sprint 13 | Sprint 14* | Target |
|--------|:---------:|:---------:|:----------:|:------:|
| Unit test coverage | 84% | 86% | 87% | 85% |
| Integration test coverage | 72% | 74% | 74% | 80% |
| Bugs found in QA | 8 | 5 | 3 | <8 |
| Bugs found in production | 2 | 1 | 0 | 0 |
| Technical debt items added | 4 | 3 | 2 | <5 |
| Technical debt items resolved | 6 | 4 | 1 | >3 |

## Burn-Down Approach

### Sprint 14 Burn-Down

We track remaining story points daily:

| Day | Ideal Remaining | Actual Remaining | Deviation |
|-----|:---:|:---:|:---:|
| Day 1 (Mon) | 44 | 44 | 0 |
| Day 2 (Tue) | 40 | 42 | +2 |
| Day 3 (Wed) | 35 | 38 | +3 |
| Day 4 (Thu) | 31 | 33 | +2 |
| Day 5 (Fri) | 27 | 31 | +4 |
| Day 6 (Mon) | 22 | 26 | +4 |
| Day 7 (Tue) | 18 | — | — |
| Day 8 (Wed) | 13 | — | — |
| Day 9 (Thu) | 9 | — | — |
| Day 10 (Fri) | 0 | — | — |

**Burn-down Status**: Slightly behind ideal pace. The team is 4 points behind at mid-sprint. The deviation is primarily due to the design blocker on APEI-405. If the blocker is resolved by Day 7, the team should recover.

### Interpreting Burn-Down Deviations

| Pattern | Cause | Action |
|---------|-------|--------|
| Consistent deviation growing | Scope too large or unexpected complexity | Consider descoping lowest-priority story |
| Flat line (no progress) | Blockers or context switching | Escalate blockers immediately |
| Steep drop at end | Stories completed in batches | Break stories into smaller pieces |
| Below ideal line | Team over-committed and delivering fast | Verify quality is not being sacrificed |

> **Tip**: The burn-down chart is a conversation starter, not a judgment tool. Use it to ask "What do we need to do differently?" not "Why are we behind?"
