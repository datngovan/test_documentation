# Blockers and Escalation

Blockers are impediments that prevent a team member from making progress on their assigned work. The APEI framework treats blocker management as a first-class process, not an afterthought.

## Current Blockers

| ID | Blocker | Raised | Owner | Blocked Work | Severity | Status | ETA |
|----|---------|--------|-------|-------------|:--------:|--------|-----|
| B-042 | Design mockups for partner signup wizard not delivered | March 17 | @design-lead | APEI-405 | High | In Progress | March 24 |
| B-043 | Staging environment SSL certificate expired | March 19 | @devops | E2E test suite | Critical | Resolved | Resolved March 20 |
| B-044 | Legal review of partner ToS pending | March 14 | @legal-team | Partner onboarding flow | Medium | Waiting | Unknown |
| B-045 | Third-party payment API sandbox is down | March 21 | @payments-vendor | Payment integration testing | High | Escalated | March 25 (vendor ETA) |
| B-046 | Database connection pool exhaustion under load | March 22 | @carol | Load testing | Medium | Investigating | TBD |

## Blocker Classification

| Severity | Definition | Response Time | Escalation Path |
|----------|-----------|:---:|----------------|
| **Critical** | Blocks entire team or production is affected | 1 hour | Immediately to Engineering Manager + VP |
| **High** | Blocks 2+ engineers or a critical-path item | 4 hours | Scrum Master → Engineering Manager |
| **Medium** | Blocks 1 engineer on a non-critical item | 24 hours | Scrum Master → Tech Lead |
| **Low** | Slows progress but workaround exists | 48 hours | Noted in standup, tracked on board |

## Escalation Process

When a blocker is identified, follow this escalation ladder:

```
Step 1: Self-resolve (0-2 hours)
  └─ Can you unblock yourself? Ask a teammate? Find a workaround?

Step 2: Team-level escalation (2-4 hours)
  └─ Raise in standup or Slack. Tech Lead or Scrum Master assists.

Step 3: Management escalation (4-8 hours)
  └─ Engineering Manager engages. Cross-team coordination if needed.

Step 4: Executive escalation (8-24 hours)
  └─ VP or Director intervenes. Vendor or partner escalation.

Step 5: War room (24+ hours, Critical only)
  └─ Dedicated team assigned. Hourly status updates. All-hands if needed.
```

### Escalation Template

When escalating a blocker, use this format:

```markdown
**Blocker ID**: B-XXX
**Summary**: [One-line description]
**Impact**: [What is blocked and how many people are affected]
**Root Cause**: [Known or suspected]
**What has been tried**: [List attempts to resolve]
**What is needed**: [Specific ask — decision, resource, access, etc.]
**Deadline**: [When this becomes critical if not resolved]
```

## Blocker Resolution SLA

| Severity | Target Resolution Time | Max Acceptable Time | Escalation Trigger |
|----------|:---:|:---:|---------------------|
| Critical | 4 hours | 8 hours | Immediately if not resolved in 4h |
| High | 24 hours | 48 hours | Auto-escalate at 24h |
| Medium | 3 business days | 5 business days | Review in weekly check-in |
| Low | 5 business days | 10 business days | Review in sprint retro |

### SLA Compliance Tracking

| Month | Critical SLA Met | High SLA Met | Medium SLA Met | Overall |
|-------|:---:|:---:|:---:|:---:|
| January 2026 | 100% (1/1) | 75% (3/4) | 90% (9/10) | 87% |
| February 2026 | 100% (2/2) | 100% (5/5) | 83% (5/6) | 92% |
| March 2026* | 100% (1/1) | 50% (1/2) | 100% (2/2) | 80% |

*March is in progress.

## Common Blocker Patterns

Understanding recurring blockers helps prevent them:

| Pattern | Frequency | Root Cause | Prevention |
|---------|:---------:|-----------|------------|
| Cross-team dependency delays | 3-4 per quarter | Misaligned sprint timelines | Sync sprint planning across dependent teams |
| Environment/infrastructure issues | 2-3 per quarter | Manual provisioning, config drift | Invest in infrastructure-as-code, automated environment health checks |
| Waiting for design | 2 per quarter | Design team capacity | Include design in sprint planning, create design sprint buffer |
| External vendor/API issues | 1-2 per quarter | Vendor reliability | Build mock/stub layers for vendor dependencies, establish vendor SLAs |
| Unclear requirements | 1-2 per quarter | Insufficient refinement | Enforce "ready" criteria before stories enter sprint |

## Blocker Prevention Checklist

Before each sprint, review:

- [ ] Are all dependencies from other teams confirmed and scheduled?
- [ ] Are all environments provisioned and verified?
- [ ] Are all design deliverables for this sprint complete or in final review?
- [ ] Are all third-party services and APIs available and tested?
- [ ] Are all access permissions and credentials in place?
- [ ] Does every story meet the Definition of Ready?

> **Principle**: The best blocker is one that never happens. Invest more time in prevention during planning than in resolution during execution. Every blocker that could have been predicted is a failure of the planning process, not the execution process.
