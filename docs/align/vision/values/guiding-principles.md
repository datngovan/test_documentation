# Engineering Guiding Principles

> **Owner:** CTO Office | **Last Updated:** 2026-02-01

## How We Build

These principles guide day-to-day engineering decisions. When facing a tradeoff, reference these before escalating.

---

### P1 — Boring Technology Wins

Choose the technology you understand deeply over the technology that's exciting. PostgreSQL over NewDB. Kafka over custom queues. HTTP over custom protocols. Boring technology has documentation, battle-tested failure modes, and a hiring market.

> **Exception:** When boring technology is demonstrably inadequate (performance, scale, correctness), we explore alternatives with a time-boxed proof of concept before committing.

---

### P2 — Observability Is Not Optional

Every service must be observable from day one:
- **Logs:** structured JSON, every request, every error
- **Metrics:** RED pattern (Rate, Errors, Duration) at minimum
- **Traces:** distributed trace IDs propagated through every service call

If you can't debug it in production without `kubectl exec`, it's not ready to ship.

---

### P3 — Design for Failure

Assume every external call will fail. Assume every disk will fill up. Assume every service will restart mid-request.

| Pattern | When to apply |
|---------|--------------|
| Circuit breaker | Any outbound HTTP call to a non-critical dependency |
| Retry with backoff | Transient errors (network, rate limits) |
| Idempotency keys | Any write operation that may be retried |
| Graceful degradation | Features that can function (with less data) without a dependency |
| Dead letter queue | Any message queue consumer |

---

### P4 — Explicit Over Implicit

Configuration is explicit. Defaults are documented. Magic is avoided.

- No hidden environment-specific behavior
- No `if ENV == 'production'` in business logic
- No implicit type coercions in API inputs
- Config values that affect production behavior require a code review, not just a dashboard click

---

### P5 — Ownership Is Clear

Every system, service, table, and API endpoint has a named owner. Ownerless things rot. When something breaks at 3 AM, someone knows it's their problem to fix.

Ownership register is maintained in `CODEOWNERS` and the service catalog at `https://catalog.internal.apei.io`.

---

### P6 — Security Is a Feature

Security is not a phase or a team — it's a property of everything we build.

- Secrets never appear in logs, URLs, or error messages
- Every user input is validated and sanitized before processing
- Least-privilege is the default for IAM roles, DB credentials, and API scopes
- New endpoints require a threat model in the PR description for any data-mutating operations

---

### P7 — Automate the Second Time

The first time you do something manually, that's fine. The second time, document it. The third time, automate it. Manual processes that happen more than monthly should have an automation ticket in the backlog.

---

### When Principles Conflict

Principles are heuristics, not laws. When two principles pull in opposite directions, use this decision framework:

1. What is the blast radius if we get this wrong?
2. Is this decision reversible in < 1 day?
3. What would we tell a new engineer joining the team this decision teaches them about how we work?

The answer to (3) is usually the right call.
