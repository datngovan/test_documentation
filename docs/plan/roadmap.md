# Roadmap

The roadmap is the primary artifact of the Plan phase. It provides a time-based view of what the team intends to deliver, organized by milestones and themes.

## Quarterly Roadmap — Q2 2026

| Month | Theme | Milestone | Owner | Dependencies | Status |
|-------|-------|-----------|-------|-------------|--------|
| April | Foundation | Core API v2 release | @backend-team | Auth service migration | Planned |
| April | Foundation | Database schema migration | @data-team | None | Planned |
| April | UX Overhaul | Design system v3 launch | @design-team | Component audit complete | In Progress |
| May | Integration | Third-party payment gateway | @payments-team | Legal review, API v2 | Planned |
| May | Integration | Partner API onboarding flow | @platform-team | API v2, docs published | Planned |
| May | Quality | Automated E2E test suite | @qa-team | Staging environment ready | Planned |
| June | Scale | Horizontal scaling for ingest pipeline | @infra-team | Monitoring dashboards | Planned |
| June | Scale | CDN rollout for static assets | @infra-team | DNS migration | Planned |
| June | Launch | Public beta for self-service portal | @product-team | All integration milestones | Planned |

## Milestone Definitions

### M1: Core API v2 Release (April 15)

**Scope:**
- RESTful API with OpenAPI 3.1 specification
- Rate limiting and authentication via OAuth 2.1
- Backward-compatible with v1 endpoints (deprecation notices included)
- Comprehensive API documentation with interactive examples

**Acceptance Criteria:**
- [ ] All v2 endpoints pass integration tests
- [ ] Performance benchmarks meet SLA (p95 < 200ms)
- [ ] Security audit completed with no critical findings
- [ ] API documentation published and reviewed by partner team

### M2: Design System v3 (April 30)

**Scope:**
- Updated component library with accessibility improvements
- Dark mode support across all components
- Figma-to-code pipeline automated
- Migration guide for v2 to v3

**Acceptance Criteria:**
- [ ] All components pass WCAG 2.1 AA audit
- [ ] Storybook documentation covers all components
- [ ] Bundle size does not increase by more than 10%
- [ ] Three pilot teams have migrated successfully

### M3: Public Beta (June 30)

**Scope:**
- Self-service portal with onboarding wizard
- Billing integration with usage-based pricing
- Support ticket system integration
- Analytics dashboard for customers

**Acceptance Criteria:**
- [ ] 50 beta customers onboarded successfully
- [ ] NPS score of beta cohort is above 40
- [ ] Zero P0/P1 bugs in production for 2 consecutive weeks
- [ ] Documentation covers all customer-facing features

## Dependency Map

Understanding dependencies is critical for realistic planning:

```
Auth Migration ──────┐
                     ├──→ API v2 Release ──────┐
Schema Migration ────┘                         │
                                               ├──→ Partner API ──→ Public Beta
Design System v3 ──→ Self-Service Portal ──────┘        │
                                                        │
Legal Review ──→ Payment Gateway ───────────────────────┘

Staging Env ──→ E2E Test Suite ──→ Public Beta

Monitoring ──→ Horizontal Scaling ──→ Public Beta
```

### Critical Path

The critical path runs through:

1. Auth Migration → API v2 → Partner API → Public Beta

Any delay in these items directly impacts the beta launch date. These tasks have zero float and must be prioritized above all other work.

## Roadmap Review Cadence

| Review Type | Frequency | Attendees | Purpose |
|------------|-----------|-----------|---------|
| Sprint Review | Bi-weekly | Delivery team + stakeholders | Demo progress, gather feedback |
| Roadmap Check-in | Monthly | Product + Engineering leads | Assess timeline, adjust priorities |
| Quarterly Planning | Quarterly | All leads + sponsors | Set next quarter roadmap |
| Ad-hoc Replanning | As needed | Affected teams + PM | Respond to significant changes |

### When to Replan

Trigger a roadmap revision when:

- A critical-path milestone slips by more than one week
- A new P0 priority emerges that was not on the roadmap
- A key team member leaves or a dependency team's capacity changes significantly
- External factors change (market, regulatory, competitive)

> **Principle**: The roadmap is a living document. Update it as reality changes, and communicate changes to all stakeholders within 24 hours of the decision.
