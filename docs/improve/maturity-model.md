# APEI Capability Maturity Model

> **Document Owner:** Strategy & Operations | **Classification:** Internal | **Last Updated:** 2026-03-22

## Overview

The APEI Capability Maturity Model (CMM) defines five levels of organizational maturity across six capability dimensions. Teams use this model to self-assess their current state and plan structured improvement.

### How to Use This Model

1. **Self-assess** — each team rates itself on each dimension using the level descriptors
2. **Validate** — quarterly review with your manager and peers
3. **Target** — identify the highest-value capability to advance by one level
4. **Plan** — use the "advancement criteria" for your target level to create a concrete action plan

> **Key principle:** Advancing from Level 2 to Level 3 in one capability is more valuable than reaching Level 2 across all six capabilities. Depth before breadth.

---

## Maturity Levels

| Level | Name | Description |
|-------|------|-------------|
| **1** | Initial | Ad hoc, unpredictable, reactive. Success depends on individual heroics. |
| **2** | Managed | Repeatable within a team. Basic processes documented but not standardized. |
| **3** | Defined | Standardized across teams. Processes are understood, followed, and improved. |
| **4** | Quantitatively Managed | Data-driven decisions. Metrics are collected, trended, and used for planning. |
| **5** | Optimizing | Continuous improvement is systematic. The organization learns and adapts faster than competitors. |

---

## Capability Dimensions

### Dimension 1: Alignment

*How well does the team stay connected to company strategy, customer needs, and cross-team dependencies?*

#### Level 1 — Initial
- Team goals are set informally or not at all
- Strategy is communicated top-down without discussion
- Stakeholders are identified reactively (when problems arise)
- Team does not know how its work connects to company OKRs
- **Observable symptoms:**
  - "I'm not sure why we're building this"
  - Different team members have different understandings of team priorities
  - Stakeholder surprises at demos (they expected something different)

#### Level 2 — Managed
- Team has documented goals for the current quarter
- Goals are loosely connected to company OKRs but linkage is not explicit
- Stakeholders are identified at project start
  - But stakeholder list is rarely revisited
  - Engagement is irregular and reactive
- Team knows its immediate dependencies (what it needs from others)
  - Upstream dependencies: tracked in JIRA/Linear
  - Downstream dependencies: often forgotten until blocking someone
- **Advancement criteria to Level 3:**
  - [ ] Write OKRs that explicitly trace to company-level OKRs
  - [ ] Build a stakeholder map with engagement plan (not just a list)
  - [ ] Establish bi-weekly alignment check with top 3 stakeholders

#### Level 3 — Defined
- Team OKRs explicitly cascade from company OKRs with clear line-of-sight
  - Each Key Result maps to ≥ 1 company Objective
  - Impact is estimated quantitatively before committing
- Stakeholder management is proactive and structured:
  - RACI matrix maintained and reviewed quarterly
  - Regular communication cadence for each stakeholder tier:
    - **Tier 1** (High power, High interest): weekly sync or update
    - **Tier 2** (High power, Low interest): monthly briefing
    - **Tier 3** (Low power, High interest): async updates (newsletter)
    - **Tier 4** (Low power, Low interest): on-request only
  - Stakeholder feedback actively solicited, not just received
- Dependency mapping is comprehensive:
  - Dependencies documented as a formal dependency register
  - Each dependency has: owner, type (hard/soft), expected date, risk if missed
  - Blocking dependencies are escalated proactively (> 2 weeks before needed)
- **Advancement criteria to Level 4:**
  - [ ] Measure and track alignment score (stakeholder satisfaction NPS)
  - [ ] Quantify cost of misalignment (rework hours, missed OKRs)
  - [ ] Dependency health tracked as a metric (% of dependencies on track)

#### Level 4 — Quantitatively Managed
- Alignment effectiveness is measured:
  - OKR achievement rate trended quarter-over-quarter
  - Stakeholder satisfaction score (quarterly survey, target > 75 NPS)
  - Dependency on-time rate (target > 90%)
  - Rework rate attributable to misalignment (target < 5% of capacity)
- Data is used to make alignment decisions:
  - If OKR achievement < 70% for two consecutive quarters: strategy review triggered
  - If stakeholder NPS drops > 15 points: root cause analysis + action plan within 2 weeks
- Predictive signals monitored:
  - Early warning indicators for alignment drift (e.g., declining meeting attendance, increasing ad hoc requests)
- **Advancement criteria to Level 5:**
  - [ ] Alignment metrics are automated (no manual data collection)
  - [ ] Team predicts and prevents misalignment before it becomes visible
  - [ ] Benchmark against industry standards for OKR achievement rates

#### Level 5 — Optimizing
- Alignment is self-reinforcing:
  - Team continuously refines its OKR-setting process based on historical accuracy data
  - Stakeholder relationships are deep enough that stakeholders proactively include the team in planning (pull instead of push)
- Dependency management is predictive:
  - Team models dependency risk using Monte Carlo simulation of delivery dates
  - Critical path is recalculated weekly with automated alerts on deviation
- Team contributes to company-wide alignment practices:
  - Runs alignment workshops for other teams
  - Helps refine company OKR framework based on team's learnings

---

### Dimension 2: Planning

*How effectively does the team translate strategy into executable, well-estimated plans?*

#### Level 1 — Initial
- Work is planned sprint-by-sprint with no multi-sprint view
- Estimates are gut-feel with no historical calibration
- Scope is poorly defined at sprint start; refined during sprint (discovery work masking as delivery)
- No formal risk identification
- **Observable symptoms:**
  - Sprint goals change mid-sprint
  - "We'll figure it out as we go"
  - Constant firefighting leaves no time for planning

#### Level 2 — Managed
- 4-week rolling plan exists
  - Stories are written and estimated for the next sprint
  - Next sprint is partially shaped (10–20 stories in backlog)
- Estimates use story points but calibration is team-specific and informal
- High-level risks identified at sprint planning but not tracked formally
- Dependencies are listed but not tracked with rigor
- **Advancement criteria to Level 3:**
  - [ ] Maintain a 6-week rolling plan with estimates
  - [ ] Track estimation accuracy (planned vs. actual story points) each sprint
  - [ ] Implement a formal risk register with owner + mitigation for each risk

#### Level 3 — Defined
- Planning horizon extends to end of quarter (12-week view):
  - **Now (0–2 weeks):** fully specified, estimated, assigned stories
  - **Next (2–6 weeks):** well-defined epics, rough story breakdown, preliminary estimates
    - Stories are independently estimable (INVEST criteria applied)
  - **Later (6–12 weeks):** epics with rough sizing (t-shirt: S/M/L/XL/XXL)
  - **Future (> 12 weeks):** themes only, no detailed breakdown
- Estimation is calibrated:
  - Team velocity tracked over rolling 6 sprints
  - Estimation accuracy tracked: target ≤ 15% variance from planned velocity
  - Systematic biases identified (e.g., "we always underestimate API work by 30%") and corrected
- Risk management is structured:
  - Risk register maintained with: Risk, Probability (H/M/L), Impact (H/M/L), Mitigation, Owner, Status
  - Risk score = Probability × Impact (2×2 matrix)
  - Top-5 risks reviewed weekly
  - Risks converted to issues when they materialize
- **Advancement criteria to Level 4:**
  - [ ] Track and trend planning accuracy metrics over time
  - [ ] Use velocity + risk data to create probabilistic delivery forecasts (Monte Carlo)
  - [ ] Plan health score > 80% (proportion of sprint items meeting Definition of Ready)

#### Level 4 — Quantitatively Managed
- Planning quality metrics:
  - Velocity stability: `stddev(last_6_sprint_velocities) / mean < 0.15` (target)
  - Estimation accuracy by category (bug, feature, tech debt) — tracked separately
  - Scope change rate: % of sprint scope changed after sprint start (target < 10%)
  - Plan coverage: % of quarterly capacity allocated to defined work (target 85%, leaving 15% for unplanned)
- Probabilistic forecasting:
  - Monte Carlo simulation run monthly for quarterly delivery commitments
  - 85th percentile forecast used for external commitments (never P50)
  - Forecast vs. actual tracked quarterly to improve simulation parameters
- Risk metrics:
  - Mean time to identify risk after it materializes (target: catch 80% as risks before they become issues)
  - Risk mitigation effectiveness: % of mitigations that prevented the risk from materializing

#### Level 5 — Optimizing
- Planning process is continuously improved using data:
  - Root cause analysis on every major planning failure (> 25% miss)
  - A/B testing of planning techniques (e.g., test shape-up vs. scrum planning within sub-teams)
  - Planning retrospective data feeds back into team norms
- Estimation models are shared across teams:
  - Team's calibration data contributes to org-wide estimation benchmarks
  - Cross-team historical data improves individual team's planning accuracy
- Proactive capacity planning:
  - Team uses leading indicators (interview pipeline, hiring conversion rates) to plan 6+ months ahead
  - Technology choices account for future operational load, not just immediate sprint needs

---

### Dimension 3: Execution

*How reliably and efficiently does the team deliver on commitments?*

#### Level 1 — Initial
- Sprint goals missed > 50% of the time
- No consistent definition of "done" — work is "done" when the developer says so
- QA is done at the end (if at all) — bugs found late and often re-opened
- Deployments are manual, infrequent, and stressful
- No visibility into work-in-progress — no shared status tracking

#### Level 2 — Managed
- Sprint goal achievement > 60%
- Definition of done exists but is informally applied
  - "Code merged" counts as done for some items
  - Tests are written but not always at the right level
- Deployments happen bi-weekly (aligned with sprint boundary)
  - Deployment process is documented but not automated
  - Deploy takes 2–4 hours with manual steps
- Some WIP limits exist but aren't strictly enforced
- **Advancement criteria to Level 3:**
  - [ ] Define and enforce WIP limits (Kanban board or sprint WIP cap)
  - [ ] Automate the deployment process end-to-end (0 manual steps)
  - [ ] Sprint goal achievement > 80% for 3 consecutive sprints

#### Level 3 — Defined
- Delivery metrics are tracked and visible:
  - Sprint goal achievement: target > 85%
  - Cycle time: from "In Progress" to "Done" (story-level)
    - P50 cycle time target: ≤ 3 days
    - P95 cycle time target: ≤ 8 days
  - Throughput: stories completed per sprint (stable, predictable)
- Definition of Done is enforced by automation and process:
  - Code review: ≥ 2 approvals required (enforced by GitHub branch protection)
  - Tests: ≥ 80% coverage on changed code (enforced by CI)
  - Documentation: updated or PR blocked
  - Acceptance criteria: validated by PM or QA (not just developer)
  - Feature flag: controlled release via LaunchDarkly
- Deployment is automated and low-risk:
  - CI/CD pipeline fully automated (0 manual steps)
  - Deploy frequency: ≥ 2x per week
  - Feature flags enable deployment decoupled from release
  - Rollback takes < 5 minutes (automated kubectl rollout undo)
- WIP is managed:
  - Maximum WIP per engineer: 2 items (1 active, 1 in review)
  - Team WIP limit: `(team_size * 1.5)` items total in flight
  - WIP limit violations are surfaced in daily standup
- **Advancement criteria to Level 4:**
  - [ ] Measure and optimize four key metrics (DORA): lead time, deploy frequency, MTTR, change failure rate
  - [ ] P95 cycle time < 5 days (current: ~8 days)
  - [ ] Change failure rate < 5%

#### Level 4 — Quantitatively Managed

DORA metrics dashboard (updated daily):

| Metric | Current | Target | Industry Elite |
|--------|---------|--------|----------------|
| Deploy frequency | 8/month | 16/month | On-demand (multiple/day) |
| Lead time (commit → prod) | 2.1 days | 1 day | < 1 hour |
| Change failure rate | 4.2% | < 3% | < 1% |
| MTTR | 18 min | 15 min | < 1 hour |

Execution quality metrics:
- Escaped defect rate: bugs found in production / bugs found total (target < 10%)
- Technical debt ratio: tech debt items / total backlog (target < 20%)
- Interruption rate: unplanned work as % of capacity (target < 15%)

#### Level 5 — Optimizing
- Execution system is self-improving:
  - Every significant delivery failure triggers a blameless post-mortem
  - Insights from post-mortems are systematically incorporated into engineering norms
  - DORA metrics benchmarked quarterly against industry peers (via State of DevOps survey)
- Proactive quality:
  - Chaos engineering experiments run weekly to find failure modes before customers do
  - SLO error budget is actively managed — team pauses feature work to invest in reliability when error budget is below 30%

---

### Dimension 4: Measurement

*How effectively does the team collect, analyze, and act on data?*

#### Level 1 → Level 5 Summary

| Level | Key Behaviors |
|-------|--------------|
| **1** | No metrics. Decisions based on gut feel and HiPPO (Highest Paid Person's Opinion). |
| **2** | Basic metrics exist (e.g., error rate, uptime) but checked reactively — only when something breaks. |
| **3** | Metrics dashboard maintained. Weekly metric reviews. OKR progress tracked with data. Leading indicators identified. |
| **4** | Statistical process control applied. Anomaly detection automated. Experiments designed with power analysis. A/B tests run routinely. |
| **5** | Organization learns from its own data faster than it can act. Metrics influence product direction. External benchmarking. |

#### Level 3 — Defined (Detail)

A team at Level 3 maintains a coherent metrics hierarchy:

- **Strategic metrics** (quarterly review)
  - OKR achievement rate
  - Customer satisfaction (NPS, CSAT)
  - Revenue impact (ARR influenced, churn prevented)

- **Operational metrics** (weekly review)
  - Feature adoption rates for recently shipped features
    - 7-day adoption: % of eligible users who used the feature
    - 30-day retention: % of 7-day adopters still using at 30 days
  - Error rates by service (p50, p95, p99)
  - Performance metrics (latency percentiles)
  - Support ticket volume and resolution time

- **Health metrics** (daily monitoring)
  - Deployment success rate
  - CI pipeline success rate
  - On-call alert volume (alerts/week trending)
  - Test flakiness rate

- **Leading indicators** (early warning)
  - Code review turnaround time (>24h signals capacity crunch)
  - PR age histogram (PRs open > 5 days signal review bottlenecks)
  - Staging environment stability (proxy for production health)

<details>
<summary>Appendix — Team Maturity Self-Assessment Template</summary>

### Self-Assessment Worksheet

Use this template every quarter. Score each dimension 1–5 and provide evidence.

```
Team: _____________________
Quarter: Q__ 2026
Assessors: _________________

Dimension 1: ALIGNMENT
Current level: ___
Evidence: _______________________________________________
Target level (next quarter): ___
One action to advance: __________________________________

Dimension 2: PLANNING
Current level: ___
Evidence: _______________________________________________
Target level (next quarter): ___
One action to advance: __________________________________

Dimension 3: EXECUTION
Current level: ___
Evidence: _______________________________________________
Target level (next quarter): ___
One action to advance: __________________________________

Dimension 4: MEASUREMENT
Current level: ___
Evidence: _______________________________________________
Target level (next quarter): ___
One action to advance: __________________________________

Overall Maturity Score: (average of all dimensions)
Priority capability to improve: ___
```

#### Scoring Calibration Guide

To avoid grade inflation, use these calibration anchors:

- **Level 1 (Initial):** Most processes are informal and person-dependent. A key person leaving would significantly disrupt the team.
- **Level 2 (Managed):** The team can execute without its best engineer. But processes aren't consistent across similar teams.
- **Level 3 (Defined):** A new team member can understand how the team operates within their first two weeks using documented processes.
- **Level 4 (Quantitatively Managed):** The team can predict its own performance with ≥ 80% accuracy using its historical data.
- **Level 5 (Optimizing):** The team is frequently cited by other teams as a model. It actively contributes to org-wide process improvement.

<details>
<summary>Historical Assessment Records</summary>

#### Q4 2025 — Engineering Platform Team

| Dimension | Score | Notes |
|-----------|-------|-------|
| Alignment | 3 | OKRs trace to company level; stakeholder map exists but not reviewed quarterly |
| Planning | 2 | 4-week plan exists but estimation calibration not tracked |
| Execution | 3 | DORA metrics tracked; deploy frequency at 8/month (target 16/month) |
| Measurement | 2 | Basic monitoring; no leading indicators; no experiment cadence |
| **Average** | **2.5** | |

**Q1 2026 Priority:** Advance Measurement from 2 → 3 by implementing weekly metric reviews and identifying 5 leading indicators.

#### Q1 2026 — Engineering Platform Team

| Dimension | Score | Notes |
|-----------|-------|-------|
| Alignment | 3 | No change — maintained |
| Planning | 3 | Added estimation calibration tracking; velocity stability improved |
| Execution | 3 | Deploy frequency improved to 16/month; change failure rate 4.2% |
| Measurement | 3 | Weekly metric reviews established; 5 leading indicators defined and monitored |
| **Average** | **3.0** | +0.5 from Q4 2025 |

**Q2 2026 Priority:** Advance Execution from 3 → 4 by implementing DORA Level 4 metrics and achieving Elite status on deploy frequency.

</details>
</details>
