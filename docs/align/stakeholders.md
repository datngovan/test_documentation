# Stakeholder Management

Stakeholder management ensures the right people are informed, consulted, and empowered throughout the APEI lifecycle. Poor stakeholder management is the leading cause of project misalignment and late-stage surprises.

## Stakeholder Map

Stakeholders are categorized by their level of influence and interest:

```
            High Influence
                 |
    Manage       |      Collaborate
    Closely      |      Closely
                 |
  ───────────────┼─────────────────
                 |
    Monitor      |      Keep
    (Minimal)    |      Informed
                 |
            Low Influence

   Low Interest ←──────→ High Interest
```

### Stakeholder Categories

| Category | Influence | Interest | Strategy |
|----------|-----------|----------|----------|
| **Key Players** | High | High | Collaborate closely, involve in decisions |
| **Context Setters** | High | Low | Keep satisfied, manage expectations |
| **Subjects** | Low | High | Keep informed, leverage their enthusiasm |
| **Crowd** | Low | Low | Monitor, minimal communication |

## RACI Matrix

The RACI matrix defines who is Responsible, Accountable, Consulted, and Informed for each major activity:

| Activity | Product Owner | Tech Lead | Engineering | Design | QA | Stakeholders |
|----------|:---:|:---:|:---:|:---:|:---:|:---:|
| Define requirements | A | C | C | C | I | R |
| Architecture decisions | I | A | R | I | C | I |
| Sprint planning | A | R | R | C | C | I |
| UI/UX design | C | I | I | A/R | C | C |
| Code implementation | I | R | A/R | I | I | I |
| Testing & QA | I | C | C | I | A/R | I |
| Release approval | A | R | I | I | R | C |
| Retrospective | R | R | R | R | R | I |
| Budget decisions | C | I | I | I | I | A |

**Legend:**
- **R** = Responsible (does the work)
- **A** = Accountable (final decision maker)
- **C** = Consulted (provides input before decision)
- **I** = Informed (notified after decision)

## Communication Plan

### Communication Cadence

| Audience | Channel | Frequency | Content | Owner |
|----------|---------|-----------|---------|-------|
| Executive sponsors | Email summary | Weekly | Progress, risks, decisions needed | Project Manager |
| Key stakeholders | Steering committee | Bi-weekly | Status review, roadmap updates | Product Owner |
| Development team | Standup | Daily | Blockers, progress, handoffs | Scrum Master |
| All stakeholders | Newsletter | Monthly | Highlights, wins, upcoming changes | Communications Lead |
| External partners | Quarterly review | Quarterly | Roadmap, integration updates | Partnership Manager |

### Communication Templates

**Weekly Status Update:**

```markdown
## Weekly Status: [Project Name]
**Period**: [Date Range]
**Overall Status**: 🟢 On Track / 🟡 At Risk / 🔴 Off Track

### Highlights
- [Key accomplishment 1]
- [Key accomplishment 2]

### Risks & Issues
| Risk | Impact | Mitigation | Owner |
|------|--------|------------|-------|

### Decisions Needed
- [ ] [Decision 1 — needed by DATE]

### Next Week Focus
- [Priority 1]
- [Priority 2]
```

## Stakeholder Engagement Levels

Track each stakeholder's engagement level over time:

| Stakeholder | Role | Current Engagement | Target Engagement | Action Required |
|------------|------|:---:|:---:|-----------------|
| VP Engineering | Sponsor | Supportive | Champion | Invite to demo sessions |
| Product Director | Context Setter | Neutral | Supportive | Schedule 1:1 alignment |
| Platform Team Lead | Dependency Owner | Resistant | Supportive | Address integration concerns |
| Design Lead | Collaborator | Supportive | Supportive | Maintain current cadence |
| Security Team | Reviewer | Unaware | Informed | Send architecture overview |
| Customer Success | Advocate | Champion | Champion | Leverage for user feedback |

### Engagement Scale

1. **Unaware** — Does not know the project exists
2. **Resistant** — Aware but opposed or concerned
3. **Neutral** — Aware but not engaged
4. **Supportive** — Positive and willing to help when asked
5. **Champion** — Actively advocates and removes obstacles

## Managing Difficult Stakeholders

When encountering resistance:

1. **Listen first**: Understand the root cause of resistance before responding
2. **Find common ground**: Identify shared objectives between your project and their concerns
3. **Provide data**: Use metrics and evidence rather than opinions to make your case
4. **Offer involvement**: Give resistant stakeholders a meaningful role to increase ownership
5. **Escalate constructively**: If alignment is impossible, escalate with documented context to a shared authority

> **Principle**: Every stakeholder interaction is an opportunity to reinforce alignment. Treat communication as a strategic activity, not an administrative chore.
