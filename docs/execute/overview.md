# Execute Phase Overview

The **Execute** phase is where plans become reality. This phase focuses on disciplined delivery through structured sprints, clear communication, and continuous tracking against the plan.

## Execution Framework

The APEI execution framework is built on these pillars:

| Pillar | Description | Key Practices |
|--------|-------------|--------------|
| **Rhythm** | Predictable cadence of work | Sprints, standups, reviews |
| **Visibility** | Everyone can see progress and blockers | Dashboards, standups, status updates |
| **Accountability** | Clear ownership for every task | Assignees, due dates, DoD |
| **Adaptability** | Respond to change without losing focus | Sprint adjustments, backlog grooming |

## Sprint Structure

We use two-week sprints as the standard execution unit:

```
Day 1  (Monday):    Sprint Planning (2 hours)
Day 2-9:            Execution
Day 5  (Friday):    Mid-sprint check-in (30 min)
Day 10 (Friday):    Sprint Review + Retrospective (2 hours)

Ongoing:
  - Daily standup: 15 min, same time every day
  - Backlog refinement: 1 hour mid-sprint
  - Pair programming: as needed
```

### Sprint Planning

Sprint planning follows a structured format:

1. **Review sprint goal**: What is the one sentence that describes success for this sprint?
2. **Pull from prioritized backlog**: Select stories based on capacity and priority
3. **Task breakdown**: Break stories into tasks of 1-4 hours each
4. **Assign owners**: Every task has exactly one owner
5. **Identify risks**: What could block us this sprint?
6. **Commit**: Team agrees on the sprint scope

### Definition of Done

A story is "Done" when:

- [ ] Code is written and passes all unit tests
- [ ] Code review is approved by at least one peer
- [ ] Integration tests pass in the staging environment
- [ ] Documentation is updated (API docs, README, changelog)
- [ ] Product Owner has accepted the story
- [ ] No known regressions introduced
- [ ] Feature flag is configured (if applicable)
- [ ] Monitoring and alerting are in place for new functionality

## Daily Standup

The daily standup is a 15-minute synchronization ceremony:

**Format per person (max 2 minutes):**

1. What did I complete since last standup?
2. What am I working on today?
3. Are there any blockers or risks?

**Rules:**

- Start on time, end on time
- Stand up (if in person) to keep it short
- Detailed discussions go to a "parking lot" for after standup
- Update the task board before standup, not during
- Remote team members join via video with camera on

## Tracking Execution Against Plan

### Weekly Health Check

Every Friday, the Scrum Master updates the sprint health dashboard:

| Metric | Green | Yellow | Red |
|--------|-------|--------|-----|
| Stories completed vs. planned | >80% | 60-80% | <60% |
| Blockers open | 0 | 1-2 | 3+ |
| Scope changes this sprint | 0 | 1 minor | Any major |
| Team morale (survey) | >4.0 | 3.0-4.0 | <3.0 |
| Build/deploy success rate | >95% | 85-95% | <85% |

### When Execution Drifts from Plan

If the weekly health check shows yellow or red:

1. **Diagnose**: Is it a scope problem, capacity problem, or technical problem?
2. **Communicate**: Notify stakeholders within 24 hours of identifying a risk
3. **Adjust**: Either reduce scope, extend timeline, or add resources (pick at most two)
4. **Document**: Record the deviation and decision in the sprint log
5. **Learn**: Feed the insight back to the Improve phase

## Execution Anti-Patterns

| Anti-Pattern | Symptom | Remedy |
|-------------|---------|--------|
| Hero culture | One person doing all critical work | Enforce pair programming and knowledge sharing |
| Scope creep | Sprint scope grows after planning | Require PO approval for any mid-sprint additions |
| Meeting overload | Engineers have <4 hours focus time/day | Audit meetings, establish no-meeting blocks |
| Silent blockers | Blockers not raised until sprint review | Create psychological safety to raise issues early |
| Gold plating | Over-engineering beyond requirements | Strict adherence to Definition of Done, nothing more |

> **Principle**: Execution is not about working harder; it is about working predictably. A team that delivers 80% of its plan consistently is more valuable than a team that delivers 120% one sprint and 40% the next.
