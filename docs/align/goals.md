# Goals and Objectives

Effective goal-setting is the bridge between alignment and action. The APEI framework uses a structured hierarchy of goals to ensure that individual work connects directly to organizational strategy.

## SMART Goals Framework

Every goal in the APEI framework must meet the SMART criteria:

| Criterion | Definition | Example |
|-----------|-----------|---------|
| **S**pecific | Clearly defined, no ambiguity | "Reduce API response time" not "Improve performance" |
| **M**easurable | Has a quantifiable metric | "Reduce p95 latency to under 200ms" |
| **A**chievable | Realistic given constraints | Must account for team size and timeline |
| **R**elevant | Tied to strategic objectives | Must map to at least one OKR |
| **T**ime-bound | Has a clear deadline | "By end of Q2 2026" |

## OKR Structure

We use Objectives and Key Results (OKRs) as the primary goal-setting mechanism:

### Example OKRs

**Objective 1: Improve platform reliability**

| Key Result | Baseline | Target | Status |
|-----------|----------|--------|--------|
| Reduce incident count per month | 12 | 4 | On track |
| Achieve 99.95% uptime SLA | 99.8% | 99.95% | At risk |
| Reduce mean time to recovery (MTTR) | 45 min | 15 min | On track |

**Objective 2: Accelerate developer productivity**

| Key Result | Baseline | Target | Status |
|-----------|----------|--------|--------|
| Reduce CI/CD pipeline time | 18 min | 8 min | On track |
| Increase deploy frequency | 2/week | 1/day | Behind |
| Reduce onboarding time for new devs | 3 weeks | 1 week | On track |

## Goal Hierarchy

Goals flow from the organizational level down to individual contributors:

```
Company Goals (Annual)
  └── Department Goals (Quarterly)
       └── Team Goals (Quarterly)
            └── Individual Goals (Sprint/Monthly)
```

### Cascade Rules

1. **Every team goal** must map to at least one department goal
2. **Every individual goal** must map to at least one team goal
3. **No orphan goals**: If a goal does not connect upward, question its relevance
4. **Limit active goals**: Maximum 3 objectives with 3-5 key results each per team per quarter

## Goal Tracking Approach

### Weekly Check-In Format

Each week, goal owners update their goals with:

- **Confidence level**: High / Medium / Low
- **Progress percentage**: 0-100%
- **Blockers**: Any obstacles preventing progress
- **Support needed**: Specific asks from leadership or other teams

### Monthly Review

| Activity | Owner | Duration |
|----------|-------|----------|
| Goal progress review | Team Lead | 30 min |
| Risk assessment update | Project Manager | 15 min |
| Dependency check | Tech Lead | 15 min |
| Adjust targets if needed | Team Lead + Sponsor | 15 min |

## Example Goals Table

| ID | Goal | Owner | Due Date | Priority | Status |
|----|------|-------|----------|----------|--------|
| G-001 | Launch self-service onboarding portal | @sarah | 2026-03-31 | P0 | In Progress |
| G-002 | Migrate authentication to OAuth 2.1 | @mike | 2026-04-15 | P0 | Planning |
| G-003 | Reduce infrastructure costs by 20% | @devops-team | 2026-06-30 | P1 | On Track |
| G-004 | Implement automated regression testing | @qa-team | 2026-05-15 | P1 | At Risk |
| G-005 | Publish public API documentation | @docs-team | 2026-04-30 | P2 | Not Started |

## Anti-Patterns to Avoid

- **Vanity goals**: Goals that look impressive but do not drive outcomes (e.g., "Write 50 blog posts")
- **Moving goalposts**: Changing targets mid-quarter without documented justification
- **Goal overload**: More than 5 active objectives per team leads to context switching and diluted focus
- **Sandbagging**: Setting deliberately easy targets to guarantee success undermines the purpose of stretch goals

> **Remember**: Goals are a communication tool as much as a tracking tool. If the team does not know the top three goals by heart, the goals are not working.
