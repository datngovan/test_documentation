# Resources and Capacity

Resource planning ensures that the team has the people, budget, and tools needed to execute the roadmap. Under-resourcing is the most common reason plans fail.

## Team Roles and Responsibilities

| Role | Count | Responsibilities | Reports To |
|------|-------|-----------------|------------|
| Product Owner | 1 | Prioritization, stakeholder management, requirements | VP Product |
| Engineering Manager | 1 | Team health, hiring, process improvement | Director of Engineering |
| Tech Lead | 1 | Architecture, code quality, technical decisions | Engineering Manager |
| Senior Engineers | 3 | Feature development, mentoring, code review | Tech Lead |
| Mid-level Engineers | 4 | Feature development, bug fixes | Tech Lead |
| Junior Engineers | 2 | Feature development, testing, documentation | Senior Engineers |
| UX Designer | 1 | User research, wireframes, prototypes | Design Lead |
| QA Engineer | 2 | Test planning, automation, regression testing | QA Lead |
| DevOps Engineer | 1 | CI/CD, infrastructure, monitoring | Tech Lead |
| Scrum Master | 1 | Ceremonies, impediment removal, process | Engineering Manager |

**Total team size: 17**

## Budget Allocation

### Q2 2026 Budget Breakdown

| Category | Allocated | Spent to Date | Remaining | % Used |
|----------|-----------|--------------|-----------|--------|
| Personnel (salaries) | $850,000 | $283,000 | $567,000 | 33% |
| Cloud infrastructure | $120,000 | $38,000 | $82,000 | 32% |
| Software licenses | $45,000 | $44,500 | $500 | 99% |
| Training & development | $15,000 | $3,200 | $11,800 | 21% |
| Contractor support | $60,000 | $0 | $60,000 | 0% |
| Contingency (10%) | $109,000 | $0 | $109,000 | 0% |
| **Total** | **$1,199,000** | **$368,700** | **$830,300** | **31%** |

### Cost Optimization Opportunities

- **Reserved instances**: Switch from on-demand to reserved for predictable workloads (estimated savings: $18,000/quarter)
- **License consolidation**: Eliminate redundant tools — three teams use different monitoring solutions
- **Contractor timing**: Delay contractor engagement until M2 completion to focus budget on critical-path items

## Tools and Technology Stack

### Development Tools

| Category | Tool | Purpose | License Cost |
|----------|------|---------|-------------|
| IDE | VS Code / JetBrains | Code editing | $0 / $15/mo per seat |
| Version Control | GitHub Enterprise | Source code management | $21/user/mo |
| CI/CD | GitHub Actions | Build, test, deploy | Included with GH Enterprise |
| Project Management | Linear | Issue tracking, sprints | $8/user/mo |
| Documentation | Notion | Internal docs, wikis | $10/user/mo |
| Design | Figma | UI/UX design | $15/editor/mo |
| Communication | Slack | Team messaging | $12.50/user/mo |
| Monitoring | Datadog | APM, logs, metrics | $23/host/mo |
| Error Tracking | Sentry | Exception monitoring | $26/mo (team plan) |
| Feature Flags | LaunchDarkly | Feature management | $12/seat/mo |

### Technology Stack

```yaml
Frontend:
  framework: React 19
  language: TypeScript 5.4
  styling: Tailwind CSS 4.0
  state: Zustand
  testing: Vitest + Playwright

Backend:
  runtime: Node.js 22 LTS
  framework: Fastify 5
  language: TypeScript 5.4
  database: PostgreSQL 16
  cache: Redis 7
  search: Elasticsearch 8

Infrastructure:
  cloud: AWS
  containers: ECS Fargate
  cdn: CloudFront
  dns: Route 53
  iac: Terraform
  monitoring: Datadog + PagerDuty
```

## Capacity Planning

### Team Capacity — Q2 2026

| Team Member | Role | Availability | Planned Vacation | Effective Capacity |
|------------|------|:---:|:---:|:---:|
| Alice Chen | Tech Lead | 100% | 5 days (May) | 92% |
| Bob Kumar | Senior Eng | 100% | 10 days (June) | 85% |
| Carol Park | Senior Eng | 80% (20% on-call) | 0 days | 80% |
| Dan Olsen | Senior Eng | 100% | 5 days (April) | 92% |
| Eve Martinez | Mid Eng | 100% | 0 days | 100% |
| Frank Liu | Mid Eng | 100% | 10 days (May) | 85% |
| Grace Kim | Mid Eng | 50% (50% other project) | 0 days | 50% |
| Henry Wu | Mid Eng | 100% | 5 days (June) | 92% |
| Ivy Singh | Junior Eng | 100% | 0 days | 100% |
| Jack Brown | Junior Eng | 100% | 5 days (April) | 92% |

### Capacity Risks

| Risk | Impact | Likelihood | Mitigation |
|------|--------|:---:|-----------|
| Grace pulled fully to other project | Lose 50% of one engineer | High | Pre-assign her work to Eve as backup |
| Hiring for open Senior Eng role delayed | Reduced senior capacity all quarter | Medium | Prioritize contractor for M1 tasks |
| Unplanned on-call burden increases | 10-20% capacity loss for on-call engineers | Medium | Invest in reducing alert noise this sprint |
| Key person dependency on Alice for auth | Single point of failure | High | Pair programming sessions to share knowledge |

> **Rule of thumb**: Plan for 70-80% utilization, not 100%. The remaining capacity absorbs unplanned work, meetings, and context-switching overhead. Teams that plan at 100% utilization consistently miss deadlines.
