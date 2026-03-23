# Q4 2025 Team Retrospective — Archive

> **Date:** December 19, 2025 | **Facilitator:** Jordan Park | **Status:** Archived

## Summary

Q4 2025 was a strong execution quarter. We completed the microservices migration (final 15%), launched the Kafka-based event bus replacing our old polling mechanism, and hit our revenue target ($38.5M ARR). The team grew from 14 to 18 engineers.

**Overall mood:** 4.1/5 — "Tired but proud."

---

## Key Outcomes

| Goal | Result |
|------|--------|
| Complete microservices migration | ✅ 85% → 100% |
| Kafka event bus live | ✅ All services migrated |
| Revenue: $37M ARR | ✅ $38.5M achieved |
| Zero production data loss incidents | ✅ Achieved |
| Deploy frequency: 8/month | ✅ Achieved (avg 11/month in Q4) |

---

## What Carried Into Q1 2026

The following items from Q4 retro were not resolved and were tracked into Q1:

- ⚠️ **Documentation debt** — 40% of services lacked runbooks (resolved in Q1)
- ⚠️ **p99 latency** — still above target after Kafka migration (ongoing)
- ✅ **On-call rotation equity** — fixed in January by adding 4 engineers to rotation

---

## Historical Note

This retrospective introduced the "Stop Doing Friday deploys" rule for the first time. The team voted for it with 13/18 votes but it wasn't enforced consistently. The Q1 retrospective revisited this — see `q1-2026-retro.md` for the hard-rule follow-up.
