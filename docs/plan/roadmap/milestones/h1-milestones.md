# H1 2026 Milestone Tracker

> **Period:** Jan 1 — Jun 30, 2026 | **Owner:** Engineering Leadership | **Updated:** 2026-03-23

## Status Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Complete |
| 🔄 | In Progress |
| ⚠️ | At Risk |
| ❌ | Missed |
| 📅 | Scheduled |

---

## Q1 Milestones

| Milestone | Owner | Due | Status | Notes |
|-----------|-------|-----|--------|-------|
| SOC2 Type II certification | Security | Mar 15 | ✅ | Achieved Mar 12 |
| AI Engine beta launch | Core Engine | Mar 15 | ✅ | Launched Mar 12, 94% satisfaction |
| HealthFirst deal close ($1.8M ACV) | Sales | Mar 31 | ✅ | Closed Mar 18 |
| Hire 10 AEs | Sales | Mar 31 | ⚠️ | 6 of 10 hired; 4 in negotiation |
| MTTR < 15 min | SRE | Mar 31 | ❌ | Achieved 18 min; 2 SEV-1s set back progress |
| Zero SEV-1 incidents | SRE | Mar 31 | ❌ | 2 SEV-1s in Q1 |

**Q1 Summary:** 4/6 milestones met (67%). Revenue target exceeded; reliability targets missed.

---

## Q2 Milestones

| Milestone | Owner | Due | Status | Notes |
|-----------|-------|-----|--------|-------|
| AI Engine GA | Core Engine | May 15 | 🔄 | On track; enterprise SSO in progress |
| ISO 27001 cert | Security | Jun 15 | 🔄 | Pre-audit gap assessment Apr 1 |
| Mobile beta launch | Mobile | Jun 1 | 🔄 | Architecture rework complete |
| Healthcare templates v1 (20 templates) | Product | May 1 | 📅 | Research phase |
| Complete AE hiring (4 remaining) | Recruiting | Apr 30 | ⚠️ | 2 offers pending; 2 not yet made |
| EU entity incorporation | Legal | May 31 | 📅 | Solicitor engaged |
| Reduce cloud infra cost by 15% | Platform | Jun 30 | 🔄 | Reserved instance review underway |
| Team NPS > 78 | HR | Jun 30 | 📅 | Q1 was 76 |

---

## Key Dependencies

```
AI Engine GA (May 15)
  └─ requires: Enterprise SSO (Okta/SAML) ←── Engineering (Apr 15)
  └─ requires: Load test at 10K concurrent executions ←── QA (May 1)

ISO 27001 (Jun 15)
  └─ requires: Pre-audit gap remediation ←── Security (Apr 30)
  └─ requires: Vendor assessments complete ←── Security (Apr 20)
  └─ requires: Employee security training 100% ←── HR (Apr 15)

EU Entity (May 31)
  └─ requires: Solicitor engagement ←── Legal ✅
  └─ requires: Registered address in Dublin ←── Operations (Apr 30)
  └─ requires: Director appointment ←── CEO (May 1)
```
