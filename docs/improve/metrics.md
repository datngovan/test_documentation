# Metrics and Measurement

Metrics are the evidence base for the Improve phase. Without measurement, improvement is guesswork. The APEI framework defines a structured approach to selecting, collecting, and acting on metrics.

## KPI Definitions

### Delivery KPIs

| KPI | Definition | Formula | Target | Collection |
|-----|-----------|---------|--------|------------|
| Sprint Velocity | Story points completed per sprint | Sum of completed story points | 35-40 pts | Automated (Linear) |
| Sprint Completion Rate | Percentage of committed stories completed | (Completed / Committed) x 100 | >85% | Automated (Linear) |
| Cycle Time | Time from "In Progress" to "Done" | Avg(Done Date - Start Date) | <5 days | Automated (Linear) |
| Lead Time | Time from request to deployment | Avg(Deploy Date - Request Date) | <10 days | Automated (Linear + CI/CD) |
| Deploy Frequency | Number of production deployments per day | Count(deploys) / working days | >1/day | Automated (CI/CD) |
| Change Failure Rate | Percentage of deployments causing incidents | (Incident Deploys / Total Deploys) x 100 | <10% | Manual (Incident log) |
| MTTR | Mean time to restore service after incident | Avg(Resolve Time - Detect Time) | <30 min | Automated (PagerDuty) |

### Quality KPIs

| KPI | Definition | Formula | Target | Collection |
|-----|-----------|---------|--------|------------|
| Defect Escape Rate | Bugs found in production vs. total bugs | (Prod Bugs / Total Bugs) x 100 | <5% | Manual (Sentry + Linear) |
| Test Coverage | Lines of code covered by automated tests | (Covered Lines / Total Lines) x 100 | >85% unit, >75% integration | Automated (Coverage tool) |
| Code Review Turnaround | Time from PR opened to approved | Avg(Approved Time - Opened Time) | <24 hours | Automated (GitHub) |
| Technical Debt Ratio | Time spent on tech debt vs. features | Tech Debt Hours / Total Hours | 15-20% | Manual (time tracking) |

### Team Health KPIs

| KPI | Definition | Collection Method | Target | Frequency |
|-----|-----------|------------------|--------|-----------|
| Team Satisfaction | Overall team happiness score | Anonymous survey (1-5 scale) | >4.0 | Bi-weekly |
| Focus Time | Hours of uninterrupted work per day | Self-reported + calendar analysis | >4 hours | Weekly |
| On-call Burden | Hours spent on unplanned work | Time tracking | <10% of capacity | Per sprint |
| Knowledge Distribution | Bus factor for critical systems | Team assessment | >2 for each system | Monthly |

## Measurement Framework

### The Four Layers

```
Layer 4: Business Outcomes
  Revenue, customer satisfaction, market share
  (Measured quarterly, owned by leadership)

Layer 3: Product Metrics
  Feature adoption, user engagement, NPS
  (Measured monthly, owned by Product)

Layer 2: Delivery Metrics
  Velocity, cycle time, quality, reliability
  (Measured per sprint, owned by Engineering)

Layer 1: Process Metrics
  Retro action completion, blocker resolution time
  (Measured per sprint, owned by Scrum Master)
```

Each layer should show a causal connection to the layer above:
- Better **process** leads to better **delivery**
- Better **delivery** leads to better **product**
- Better **product** leads to better **business outcomes**

### Selecting Metrics

When choosing what to measure, apply the KISS test:

| Criterion | Question |
|-----------|----------|
| **K**ey | Does this metric connect to a strategic objective? |
| **I**nfluenceable | Can the team actually affect this metric through their actions? |
| **S**imple | Can we explain what this metric measures in one sentence? |
| **S**ustainable | Can we collect this metric without significant manual effort? |

If any answer is "no," reconsider whether the metric is worth tracking.

## Leading vs. Lagging Indicators

Understanding the distinction between leading and lagging indicators is crucial for proactive management:

| Leading Indicators (Predictive) | Lagging Indicators (Historical) |
|--------------------------------|--------------------------------|
| Sprint confidence score (mid-sprint) | Sprint completion rate |
| PR review queue length | Average cycle time |
| Test coverage on new code | Defect escape rate |
| Blocker count at mid-sprint | Sprint carry-over points |
| Team satisfaction trend | Employee turnover |
| Design deliverable readiness | Sprint velocity |
| Dependency confirmation rate | Milestone delivery rate |

### How to Use Each Type

**Leading indicators** tell you what is likely to happen. Use them to:
- Trigger early interventions
- Adjust plans before problems become visible
- Build confidence in the team's trajectory

**Lagging indicators** tell you what already happened. Use them to:
- Validate that interventions worked
- Set baselines for future planning
- Report outcomes to stakeholders

> **Warning**: Over-indexing on lagging indicators is like driving by looking only in the rearview mirror. Balance your dashboard with both types.

## Dashboard Design

### Recommended Dashboard Layout

```
┌─────────────────────────────────────────────────────┐
│  APEI Metrics Dashboard — Sprint 14                  │
├──────────────────┬──────────────────────────────────┤
│  Sprint Health   │  Velocity Trend (6-sprint chart) │
│  ● Completion    │                                  │
│  ● Velocity      │  ████████████████░░░░            │
│  ● Quality       │  Sprint 9  10  11  12  13  14   │
├──────────────────┼──────────────────────────────────┤
│  Quality Panel   │  Team Health Panel               │
│  Coverage: 87%   │  Satisfaction: 4.2/5             │
│  Defects: 0 prod │  Focus Time: 4.5h/day           │
│  Review: 18h avg │  On-call: 8%                    │
├──────────────────┴──────────────────────────────────┤
│  Blockers: 2 open (1 High, 1 Medium)               │
│  Action Items: 1 of 3 complete from last retro      │
│  Next milestone: API v2 Release — 22 days away      │
└─────────────────────────────────────────────────────┘
```

### Dashboard Rules

1. **Refresh automatically**: No metric on the dashboard should require manual update more than once per week
2. **Show trends, not snapshots**: Every number should have a directional indicator (up/down/stable)
3. **Highlight exceptions**: Use color coding — green/yellow/red — to draw attention to items needing action
4. **Keep it focused**: Maximum 12 metrics on the main dashboard. Everything else goes in drill-down views
5. **Make it accessible**: The dashboard URL should be in the team's Slack channel topic

## Metric Anti-Patterns

| Anti-Pattern | Problem | Better Approach |
|-------------|---------|----------------|
| Measuring individual velocity | Creates competition, discourages collaboration | Measure team velocity only |
| Gaming metrics | Teams optimize for the number, not the outcome | Pair metrics (e.g., velocity + quality) |
| Too many metrics | Analysis paralysis, no clear priorities | Maximum 12 active metrics |
| Vanity metrics | Feels good but does not drive decisions | Every metric must have a target and action threshold |
| Ignoring context | Comparing velocity across teams with different work | Metrics are for trends within a team, not cross-team comparison |

> **Principle**: Metrics exist to inform decisions, not to judge people. If a metric cannot change a decision you would make, stop tracking it. If a metric is being used to punish, it will be gamed.
