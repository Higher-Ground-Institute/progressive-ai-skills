---
name: refine-ticket
description: Refine a single Linear issue. Fetches the full issue, picks the right template, rewrites the description, verifies acceptance criteria, re-evaluates priority, and cancels if not worth doing. Use when the user asks to refine, clean up, or fix a specific ticket.
argument-hint: "<issue-id>"
---

Refine a single Linear issue: `$ARGUMENTS`

## Steps

1. **Fetch** the full issue with `get_issue` (list results are truncated)
2. **Evaluate** using the criteria below
3. **Act** -- post the refined description as a **comment** on the issue (do NOT overwrite the existing description). If cancelling, set state to "Cancelled". Apply label/priority changes via `save_issue`.
4. **Report** -- summarise what changed and why

> **Why comment instead of overwrite?** Linear has no version history for descriptions. Posting as a comment preserves the original context. The team can then copy the refined version into the description if they approve it.

---

## Evaluation Criteria

**Cancel (state -> "Cancelled") if:**
- Already implemented in the codebase (check before assuming)
- Duplicates another open ticket (mark as "Duplicate" status instead)
- Speculative work with no clear value
- Context that created it no longer applies

**Bump priority up if:**
- Security issue -- at minimum High (2)
- Blocks other in-progress tickets
- Production bug affecting real users or live systems
- System failure causing data delivery delays or service degradation

**Drop priority if:**
- Purely cosmetic, no functional impact
- Nice-to-have with no concrete use case

**Rewrite description if:**
- Doesn't match a template (see below)
- Acceptance criteria are missing, vague, or unverifiable
- Description is a single sentence with no structure

**Suggest label if missing:**
- `NewStuff` -- new feature work
- `InternalSupport` -- support queue / internal requests
- `QualityDebt` -- bugs, tech debt, quality improvements
- `Bug` -- bug fixes
- `DevOps` -- infrastructure, CI/CD, deployment
- `Support` -- operational support tasks

---

## Templates

Choose the best fit. Tickets may span application code, data pipelines, internal tools, infrastructure, and support tasks.

**IMPORTANT: Do NOT include implementation recommendations, technical approach details, key files, or code-level suggestions.** The engineer assigned to the ticket determines how to implement it. Focus on the *what* and *why*, not the *how*.

### Feature Implementation
Use when shipping new functionality.
```
## Goal
<2-3 sentences: what and why>

## Acceptance Criteria
- [ ] <specific, verifiable outcome>
```

### Bug Fix
Use when fixing broken behaviour -- system failures, data issues, UI bugs.
```
## Problem
<What is broken -- include error text, thread links, or unexpected behaviour verbatim>

## Steps to Reproduce
1.
2.

## Expected Behavior
<What should happen>

## Acceptance Criteria
- [ ] Bug no longer reproduces following the steps above
```

### Spike
Use for time-boxed technical research that produces a recommendation, not code.
```
## Goal
<What question this spike is trying to answer>

## Background
<Context -- link to doc, prior spikes, or relevant threads>

## Questions to Address
- [ ] <specific question to answer>

## Out of Scope
<What this spike is NOT trying to answer>

## Output
* Recommendation documented in <doc link or location>
* Follow-up implementation tickets created if applicable

## Acceptance Criteria
- [ ] <specific deliverable: recommendation, doc, tickets filed>
```

### Support / Chore
Use for operational tasks: configuration changes, data fixes, support requests.
```
## Request
<What needs to happen -- include support ticket # if applicable>

## Context
<Who requested this and why>

## Steps
1. <specific action>
2. <verification step>

## Acceptance Criteria
- [ ] <specific, verifiable outcome>
```

### Refactor
Use for cleanup with no behaviour change.
```
## Goal
<What is being cleaned up and why>

## Scope
<In scope. Explicitly list what is OUT of scope.>

## Acceptance Criteria
- [ ] <specific structural outcome>
- [ ] Behaviour is identical before and after -- no functional changes
```

### Feature Planning
Use for large features broken into sub-issues.
```
## Problem
<What need or gap this addresses>

## Proposed Approach
<High-level shape of the solution -- not implementation details>

## Open Questions
- [ ] <decision needed before implementation>

## Out of Scope
<Explicitly list what this does NOT cover>

## Sub-Issues
- [ ] <child ticket identifier and title>

## Acceptance Criteria
- [ ] <high-level outcome>
```

### Discovery
Use for open-ended research that produces other tickets, not code.
```
## Goal
<What question this discovery is trying to answer>

## Background
<Context, links to relevant code, docs, or prior discussions>

## Tasks
- [ ] <specific research step>

## Out of Scope
<What this is NOT trying to answer>

## Definition of Done
This issue is complete when the following have been filed as standalone issues:
- [ ] <issue to be created>

## Notes
<Findings captured here as work progresses>
```

---

## AC Quality Bar

Acceptance criteria must be:
- **Specific** -- names exact endpoints, tables, or UI elements where relevant
- **Verifiable** -- clear pass/fail, no subjective judgment
- **Complete** -- covers the happy path and at least one edge case for bugs
- **Concise** -- consolidate related criteria into single items. Aim for 2-4 acceptance criteria for most tickets. A simple feature or bug fix should not have 6+ criteria. Boilerplate like "build succeeds" or "no regressions" should not be separate line items.

Reject: "works correctly", "looks good", "no regressions" (alone), "tests pass" without specifying which tests.

Exception: Support/Chore tickets can have simpler AC since the work is often a single operational step.

---

## Writing Style

Write like a senior engineer jotting down a ticket for a teammate -- clear, direct, human. Not a report. Not a spec. Not a wall of text.

- **Stay high-level.** Describe the goal and acceptance criteria. Do NOT include implementation recommendations, code suggestions, file paths, or technical approach. The engineer decides how to implement.
- **No filler.** Don't pad with obvious statements. If it goes without saying, don't say it.
- **Sound like a person.** Use plain language. Short sentences are fine. Fragments are fine. Avoid the stilted, over-qualified tone LLMs default to.

### Examples

**Too verbose (bad):**
> The system should ensure that when a user selects a data type that is not "Survey Responses," the "Most Recent Response" delivery type option should not be displayed in the user interface. Currently, all three delivery type options (One-Time, Most Recent Response, and Subscription) are displayed regardless of the selected data type, which may cause confusion. Additionally, unit tests should be updated to verify this conditional rendering behavior, and the build should complete successfully with no errors.

**Too terse (bad):**
> Hide "Most Recent Response" when data type != survey responses.

**Just right:**
> "Most Recent Response" only applies to survey responses, but it currently shows for all data types. Hide it when the selected data type is anything other than survey responses.

---

## Conventions

- **Point estimates** use the scale: 1, 2, 3, 5. Don't change estimates unless clearly miscalibrated.
- **Project milestones** are used to group work within projects. Don't remove or change milestone assignments.
