# Q1 2026 Quarterly Business Review

> **Review Period:** January 1 — March 31, 2026 | **Prepared by:** Operations & Strategy | **Review Date:** 2026-03-23

## Executive Summary

Q1 2026 was a **strong quarter** marked by successful delivery of the AI Orchestration Engine beta, healthcare vertical launch, and achievement of SOC2 Type II certification. Revenue grew 11.2% QoQ to $42.8M ARR, exceeding the quarterly target by 3.1%.

### Key Wins

- Closed the largest deal in company history: HealthFirst Systems ($1.8M ACV)
- AI Orchestration Engine beta launched on schedule with 94% positive user feedback
- SOC2 Type II certification achieved — unblocked $8.2M in stalled pipeline
- Team NPS improved from 68 to 76 (target: 72)

### Key Misses

- European market entry delayed to Q3 due to GDPR legal review taking longer than expected
- Mobile app beta pushed to Q2 — React Native performance issues on Android required architecture rework
- Two SEV-1 incidents in production (target: zero) — see incident retrospectives for details
- Sales hiring fell behind: 6 of 10 planned AEs onboarded (4 offers still in negotiation)

---

## OKR Scorecard

### Company-Level OKRs

| Objective | Key Result | Target | Actual | Score | Status |
|-----------|-----------|--------|--------|-------|--------|
| **O1: Accelerate revenue growth** | Increase ARR | $41.5M | $42.8M | 1.03 | ✅ Achieved |
| | Close 3 enterprise deals >$500K ACV | 3 | 4 | 1.33 | ✅ Exceeded |
| | Reduce sales cycle length | 68 days | 72 days | 0.94 | ⚠️ Near Miss |
| **O2: Launch AI-native capabilities** | Ship AI Orchestration Engine beta | Launch by Mar 15 | Launched Mar 12 | 1.0 | ✅ Achieved |
| | Achieve 90%+ beta user satisfaction | 90% | 94% | 1.04 | ✅ Exceeded |
| | AI-generated workflows: 500 in beta period | 500 | 387 | 0.77 | ❌ Missed |
| **O3: Achieve operational excellence** | Maintain 99.95% uptime | 99.95% | 99.91% | 0.96 | ⚠️ Near Miss |
| | Reduce MTTR to 15 min | 15 min | 18 min | 0.83 | ❌ Missed |
| | Zero SEV-1 incidents | 0 | 2 | 0.0 | ❌ Missed |
| **O4: Build a world-class team** | Hire 10 AEs | 10 | 6 | 0.60 | ❌ Missed |
| | Team NPS > 72 | 72 | 76 | 1.06 | ✅ Exceeded |
| | Complete leadership training for all managers | 100% | 100% | 1.0 | ✅ Achieved |

**Overall OKR Score: 0.88** (target: 0.85 — within acceptable range)

---

## KPI Trend Analysis

| Metric | Q3 2025 | Q4 2025 | Q1 2026 | QoQ Change | Trend |
|--------|---------|---------|---------|------------|-------|
| Annual Recurring Revenue (ARR) | $34.1M | $38.5M | $42.8M | +11.2% | Accelerating |
| Monthly Active Users (MAU) | 12,400 | 14,800 | 18,200 | +23.0% | Accelerating |
| Net Revenue Retention (NRR) | 112% | 115% | 118% | +3pp | Improving |
| Gross Margin | 72.1% | 73.4% | 74.2% | +0.8pp | Stable |
| Customer Acquisition Cost (CAC) | $18,200 | $16,800 | $15,400 | -8.3% | Improving |
| CAC Payback Period | 14.2 mo | 12.8 mo | 11.5 mo | -1.3 mo | Improving |
| Logo Churn Rate | 3.2% | 2.8% | 2.4% | -0.4pp | Improving |
| Revenue Churn Rate | 1.8% | 1.5% | 1.2% | -0.3pp | Improving |
| Support Ticket Volume | 2,340 | 2,580 | 2,120 | -17.8% | Improving |
| Average Response Time (Support) | 4.2 hr | 3.8 hr | 3.1 hr | -18.4% | Improving |
| Deploy Frequency | 8/month | 12/month | 16/month | +33.3% | Accelerating |
| Mean Time to Recovery (MTTR) | 38 min | 22 min | 18 min | -18.2% | Improving |

---

## Team Velocity

### Engineering Sprint Metrics (2-week sprints)

| Sprint | Points Planned | Points Completed | Velocity | Delta | Notes |
|--------|---------------|-----------------|----------|-------|-------|
| S26-01 | 84 | 79 | 79 | -5 | Post-holiday ramp-up |
| S26-02 | 88 | 85 | 85 | -3 | Normal velocity |
| S26-03 | 92 | 91 | 91 | -1 | Strong sprint, AI engine focus |
| S26-04 | 90 | 72 | 72 | -18 | SEV-1 incident consumed 2 eng-days |
| S26-05 | 88 | 90 | 90 | +2 | Overdelivered, good flow |
| S26-06 | 94 | 88 | 88 | -6 | SOC2 audit prep pulled resources |
| **Average** | **89.3** | **84.2** | **84.2** | **-5.2** | **94.2% plan completion** |

#### Velocity Trend

```
Points |
  100  |                                            ·
   95  |           ·                                     ·
   90  |      ·         ·                     ·               ·
   85  | ·         ·         ·                     ·
   80  |                          ·
   75  |
   70  |                               ·
       +---+---+---+---+---+---+---+---+---+---+---+---
        S01 S02 S03 S04 S05 S06   ← Sprint

  · = Completed points
```

---

## Budget vs. Actual

### Q1 2026 Budget Performance by Category

| Category | Q1 Budget | Q1 Actual | Variance | Variance % | Notes |
|----------|-----------|-----------|----------|-----------|-------|
| **Engineering Salaries** | $3,200K | $3,050K | +$150K | -4.7% | Under due to 4 unfilled positions |
| **Cloud Infrastructure** | $820K | $890K | -$70K | +8.5% | AI inference GPU costs higher than modeled |
| **SaaS & Tooling** | $185K | $178K | +$7K | -3.8% | On target |
| **Sales & Marketing** | $1,400K | $1,280K | +$120K | -8.6% | Under due to delayed AE hiring |
| **Contractor & Consulting** | $320K | $410K | -$90K | +28.1% | SOC2 audit consultants + legal for EU expansion |
| **Travel & Events** | $95K | $62K | +$33K | -34.7% | Conference season starts in Q2 |
| **Office & Facilities** | $210K | $205K | +$5K | -2.4% | On target |
| **Training & Development** | $75K | $68K | +$7K | -9.3% | On target |
| **Recruiting** | $180K | $145K | +$35K | -19.4% | Under due to slower hiring pace |
| **Total** | **$6,485K** | **$6,288K** | **+$197K** | **-3.0%** | **Under budget overall** |

> **Budget Note:** While we are under budget overall (-3.0%), the cloud infrastructure overrun (+8.5%) is a concern. GPU costs for the AI inference service are trending higher than our original model assumed. We need to revisit the AI infrastructure budget for Q2-Q4 or optimize inference costs (model quantization, spot instances, batching).

---

## Action Items for Next Quarter (Q2 2026)

### P0 — Must Complete

- [ ] Ship AI Orchestration Engine to General Availability (GA) — **Owner:** Core Engine Team — **Due:** 2026-05-15
- [ ] Close remaining 4 AE hires — **Owner:** Sales + Recruiting — **Due:** 2026-04-30
- [ ] Achieve ISO 27001 certification — **Owner:** Security Team — **Due:** 2026-06-15
- [ ] Launch healthcare-specific workflow templates — **Owner:** Product Team — **Due:** 2026-05-01
- [ ] Resolve AI infrastructure cost overrun (target: bring GPU costs to within 5% of budget) — **Owner:** Platform Team — **Due:** 2026-04-30

### P1 — Should Complete

- [ ] Launch mobile app beta (Android + iOS) — **Owner:** Mobile Team — **Due:** 2026-06-01
- [ ] Implement automated capacity planning for Kubernetes clusters — **Owner:** DevOps — **Due:** 2026-05-15
- [ ] Publish updated public API documentation with interactive examples — **Owner:** Developer Relations — **Due:** 2026-05-15
- [ ] Reduce average sales cycle from 72 days to 65 days — **Owner:** Sales Ops — **Due:** 2026-06-30
- [ ] Launch customer advisory board (8-12 enterprise customers) — **Owner:** Customer Success — **Due:** 2026-05-01

### P2 — Nice to Have

- [ ] Evaluate and select European data center partner — **Owner:** Infrastructure — **Due:** 2026-06-30
- [ ] Prototype WebAssembly-based custom function runtime — **Owner:** Core Engine Team — **Due:** 2026-06-30
- [ ] Redesign onboarding flow based on Q1 user research — **Owner:** Product + Design — **Due:** 2026-06-15

---

## Lessons Learned

> **On planning accuracy:** Our revenue forecast was within 3.1% of actual — the improved bottoms-up modeling from Sales Ops is paying off. However, hiring forecasts were off by 40%. The lesson: sales pipeline forecasting has matured, but talent pipeline forecasting needs the same rigor. Recruiting should adopt similar probabilistic stage-based modeling.

> **On incident response:** Two SEV-1 incidents in a quarter is unacceptable for our uptime targets. Both incidents had avoidable root causes (memory leak in workflow engine, database connection pool exhaustion). The pattern: deploy-time validation catches syntax and logic errors but not resource-consumption regressions. We need load testing with production-scale data in the CI pipeline, not just functional tests.

> **On AI investment:** The AI Orchestration Engine beta exceeded satisfaction targets (94% vs. 90%) but fell short on adoption volume (387 vs. 500 AI-generated workflows). User interviews reveal the gap is not feature quality but discoverability — most users did not know the AI features existed. The fix is product-led: add AI suggestions inline in the workflow editor, not behind a separate menu.

> **On cross-team dependencies:** The European market entry delay (Q2 to Q3) cascaded from a single bottleneck: legal review of GDPR data processing agreements. No engineering work was blocked, but the go-to-market timeline slipped by 6 weeks. The lesson: legal and compliance reviews should start 2 quarters before the planned launch, not 1 quarter before.

---

<details>
<summary>Appendix: Raw Data & Supporting Metrics</summary>

### Revenue Breakdown by Segment

| Segment | Q4 2025 ARR | Q1 2026 ARR | Growth | % of Total |
|---------|------------|------------|--------|-----------|
| Healthcare | $6.2M | $8.1M | +30.6% | 18.9% |
| Financial Services | $5.8M | $6.4M | +10.3% | 15.0% |
| Technology | $8.4M | $9.2M | +9.5% | 21.5% |
| Manufacturing | $4.1M | $4.6M | +12.2% | 10.7% |
| Retail & E-Commerce | $3.2M | $3.8M | +18.8% | 8.9% |
| Other | $10.8M | $10.7M | -0.9% | 25.0% |
| **Total** | **$38.5M** | **$42.8M** | **+11.2%** | **100%** |

### Pipeline Metrics

| Stage | Deals | Value | Avg. Deal Size | Conversion Rate |
|-------|-------|-------|----------------|----------------|
| Qualified Lead | 142 | $28.4M | $200K | — |
| Discovery | 89 | $19.6M | $220K | 62.7% |
| Solution Design | 54 | $14.2M | $263K | 60.7% |
| Proposal | 31 | $9.8M | $316K | 57.4% |
| Negotiation | 18 | $6.2M | $344K | 58.1% |
| Closed Won | 12 | $4.3M | $358K | 66.7% |
| **Total Pipeline** | **142** | **$28.4M** | — | **8.5% (lead-to-close)** |

### Customer Health Scores

| Health Band | Customer Count | ARR in Band | % of ARR | Action |
|------------|---------------|-------------|----------|--------|
| Healthy (80-100) | 124 | $28.4M | 66.4% | Expand |
| Moderate (60-79) | 48 | $9.8M | 22.9% | Nurture |
| At Risk (40-59) | 15 | $3.6M | 8.4% | Intervene |
| Critical (<40) | 4 | $1.0M | 2.3% | Escalate |
| **Total** | **191** | **$42.8M** | **100%** | — |

### Engineering Metrics (detailed)

| Metric | January | February | March | Q1 Average |
|--------|---------|----------|-------|-----------|
| PRs Merged | 142 | 168 | 181 | 163.7/mo |
| Code Review Turnaround (p50) | 4.2 hr | 3.8 hr | 3.5 hr | 3.8 hr |
| CI Pipeline Success Rate | 94.2% | 95.1% | 96.3% | 95.2% |
| Test Coverage (backend) | 78.4% | 79.1% | 81.2% | — |
| Test Coverage (frontend) | 64.2% | 65.8% | 67.1% | — |
| Open Bug Count (end of month) | 89 | 76 | 68 | — |
| P0/P1 Bugs Fixed | 12 | 15 | 11 | 12.7/mo |

</details>
