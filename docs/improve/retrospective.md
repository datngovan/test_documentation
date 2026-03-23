# Retrospective Guide

The retrospective is the cornerstone ceremony of the Improve phase. It provides a structured space for the team to reflect on what happened, why, and what to do differently.

## Retrospective Format

We use the "What Went Well / What to Improve / Action Items" format as the default. Each retrospective runs for 60-90 minutes at the end of every sprint.

### Agenda

```
1. Set the stage (5 min)
   - Check in: How are you feeling about this sprint? (1-5 scale)
   - Review: Read the prime directive aloud

2. Gather data (20 min)
   - Each person writes sticky notes for:
     * What went well (green)
     * What to improve (yellow)
     * Shout-outs / appreciation (blue)
   - Post and group by theme

3. Generate insights (20 min)
   - Vote on top themes (3 votes per person)
   - Discuss top 3 voted themes
   - Root cause analysis for improvement items

4. Decide what to do (15 min)
   - Define action items with owners and due dates
   - Maximum 3 action items per retrospective
   - Review action items from last retrospective

5. Close (5 min)
   - Rate the retrospective: Was this useful? (1-5)
   - Thank the team
```

### The Prime Directive

> "Regardless of what we discover, we understand and truly believe that everyone did the best job they could, given what they knew at the time, their skills and abilities, the resources available, and the situation at hand."
> -- Norm Kerth

Read this at the start of every retrospective to establish psychological safety.

## Sprint 13 Retrospective Example

**Date**: March 13, 2026
**Facilitator**: Scrum Master (Jordan)
**Attendees**: 12/14 team members (Carol and Frank on PTO)

### What Went Well

| Theme | Details | Votes |
|-------|---------|:-----:|
| API v2 progress | Auth endpoints shipped ahead of schedule, clean code reviews | 8 |
| Pair programming | Alice + Bob pairing on auth led to knowledge sharing and fewer bugs | 6 |
| Incident response | SSL cert issue caught early, resolved in 2 hours with good runbook | 5 |
| Cross-team collaboration | Design team proactively shared early mockups for feedback | 4 |
| Testing improvements | New integration test framework reduced test setup time by 50% | 3 |

### What to Improve

| Theme | Details | Votes |
|-------|---------|:-----:|
| Design handoff timing | Mockups for partner wizard arrived late, blocking frontend work | 9 |
| Meeting overload | 3 engineers reported <3 hours focus time on Wednesday | 7 |
| Flaky tests | CI pipeline failed 4 times due to flaky E2E tests, wasting time | 5 |
| Documentation lag | API docs are 2 sprints behind the actual API | 3 |
| On-call burden | Carol spent 30% of sprint on unplanned on-call work | 2 |

### Root Cause Analysis — Design Handoff Timing

Using the "5 Whys" technique:

1. **Why** were the mockups late? The design team had competing priorities.
2. **Why** were priorities competing? The design team is shared across 3 product teams.
3. **Why** is there no dedicated design capacity? Budget constraints from Q1.
4. **Why** was this not anticipated? Design dependency was not explicitly called out in sprint planning.
5. **Why** was the dependency missed? Our sprint planning checklist does not include a design readiness check.

**Root Cause**: Sprint planning process does not verify design deliverable readiness before committing work to the sprint.

### Action Items

| ID | Action | Owner | Due Date | Status |
|----|--------|-------|----------|--------|
| AI-031 | Add "Design deliverables ready?" to sprint planning checklist | Jordan | March 16 | Done |
| AI-032 | Establish no-meeting Wednesday afternoons (1pm-5pm) | Jordan | March 18 | Done |
| AI-033 | Create flaky test quarantine board and fix top 5 flaky tests | Dan | March 27 | In Progress |

### Previous Action Items Review

| ID | Action | Owner | Status | Notes |
|----|--------|-------|--------|-------|
| AI-028 | Set up automated deploy notifications | Henry | Done | Slack integration working |
| AI-029 | Create runbook for SSL cert rotation | DevOps | Done | Used successfully this sprint |
| AI-030 | Reduce standup to 10 minutes | Jordan | Done | Team reports improvement |

## Alternative Retrospective Formats

To prevent retro fatigue, rotate formats every few sprints:

### Format: Start / Stop / Continue

| Start Doing | Stop Doing | Continue Doing |
|-------------|-----------|----------------|
| Pair programming for complex stories | Allowing scope changes after Day 3 | Daily standup format |
| Design review before sprint commit | Skipping code review for "small" changes | Weekly knowledge sharing |
| Pre-sprint dependency check | Working through lunch | Celebrating sprint wins |

### Format: Sailboat

Visualize the team as a sailboat:

- **Wind** (what propels us forward): Strong technical skills, good team communication
- **Anchor** (what holds us back): Technical debt in auth module, manual deployment steps
- **Rocks** (risks ahead): Q2 deadline pressure, key person dependency on Alice
- **Sun** (what we appreciate): Supportive management, flexible work hours

### Format: Four Ls

| Liked | Learned | Lacked | Longed For |
|-------|---------|--------|-----------|
| Team collaboration this sprint | New testing patterns from Dan | Clear requirements for webhook feature | Dedicated design support |
| Quick incident resolution | How to debug connection pool issues | Time for tech debt | Automated environment provisioning |

## Retrospective Anti-Patterns

| Anti-Pattern | Why It Hurts | Fix |
|-------------|-------------|-----|
| Same format every time | Team disengages, stops sharing | Rotate formats every 3-4 sprints |
| No action items | Feels like venting, nothing changes | Always leave with 2-3 concrete actions |
| Action items never reviewed | Team loses trust in the process | First agenda item: review previous actions |
| Blame-focused discussion | People stop being honest | Enforce prime directive, focus on process not people |
| Manager dominates | Junior voices are silenced | Use written input before verbal discussion |
| Skipping retrospectives | Improvement stops | Retrospective is non-negotiable, even in crunch |

> **Principle**: A retrospective is only as good as the follow-through on its action items. If you do nothing with the output, you are wasting the team's time and eroding trust in the improvement process.
