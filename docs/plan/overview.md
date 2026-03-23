# Plan Phase Overview

The **Plan** phase translates alignment into actionable work. This is where strategic objectives become roadmaps, milestones, and task breakdowns that teams can execute against.

## Planning Methodology

The APEI framework uses a layered planning approach:

| Layer | Time Horizon | Detail Level | Owner | Review Cadence |
|-------|-------------|-------------|-------|----------------|
| Strategic Plan | 12 months | High-level themes | Leadership | Quarterly |
| Quarterly Roadmap | 3 months | Epics and milestones | Product + Engineering Leads | Monthly |
| Sprint Plan | 2 weeks | Stories and tasks | Delivery Team | Per sprint |
| Daily Plan | 1 day | Individual tasks | Individual contributors | Daily standup |

## Planning Cycle

The standard planning cycle runs as follows:

```
Week 1: Gather inputs
  - Review alignment artifacts from the Align phase
  - Collect technical debt and maintenance backlog
  - Assess team capacity and availability

Week 2: Draft and review
  - Create draft roadmap with milestones
  - Identify dependencies and risks
  - Review with stakeholders for feedback

Week 3: Finalize and communicate
  - Incorporate feedback and adjust priorities
  - Publish final roadmap and sprint plan
  - Communicate plan to all stakeholders

Week 4: Begin execution
  - Kick off first sprint
  - Set up tracking dashboards
  - Schedule recurring ceremonies
```

## Key Planning Artifacts

At the end of the Plan phase, you should have:

- [ ] **Quarterly Roadmap** with milestones and owners
- [ ] **Sprint backlog** for the first sprint
- [ ] **Dependency map** showing cross-team dependencies
- [ ] **Risk register** with mitigation strategies
- [ ] **Capacity plan** showing team allocation
- [ ] **Definition of Done** agreed upon by the team
- [ ] **Communication schedule** for stakeholder updates

## From Align to Plan

The transition from Align to Plan follows this checklist:

| Step | Description | Status |
|------|-------------|--------|
| 1 | Alignment document is signed off | Required |
| 2 | Goals and OKRs are published | Required |
| 3 | Stakeholder map is complete | Required |
| 4 | Initial risk assessment is done | Required |
| 5 | Team capacity is confirmed | Required |
| 6 | Technical feasibility is validated | Recommended |
| 7 | Budget is approved | Required |

## Planning Principles

1. **Plan at the right level of detail**: Do not over-plan work that is far in the future. Use progressive elaboration — detail increases as execution approaches.

2. **Build in buffers**: No plan survives first contact with reality. Reserve 15-20% of capacity for unplanned work, bugs, and operational overhead.

3. **Make dependencies explicit**: If your plan depends on another team delivering something, document it and confirm it with them. Assumed dependencies are the biggest source of plan failure.

4. **Plan for failure modes**: For each major milestone, ask "What could go wrong?" and document the contingency.

5. **Keep plans visible**: A plan that only exists in a project management tool is not a plan — it is a database entry. Ensure the team can articulate the plan from memory.

## Estimation Guidelines

| Technique | When to Use | Accuracy |
|-----------|-------------|----------|
| T-shirt sizing (S/M/L/XL) | Early-stage roadmap items | Low, directional |
| Story points | Sprint-level stories | Medium |
| Time-based estimates | Well-understood tasks | High (if experienced) |
| Three-point estimate | High-uncertainty work | Medium-High |

### Three-Point Estimation

For uncertain work, use optimistic (O), most likely (M), and pessimistic (P) estimates:

```
Expected = (O + 4M + P) / 6
Standard Deviation = (P - O) / 6
```

> **Warning**: Plans are hypotheses, not commitments. The purpose of a plan is to coordinate action and enable learning, not to predict the future with certainty. Be prepared to adapt as new information emerges.
