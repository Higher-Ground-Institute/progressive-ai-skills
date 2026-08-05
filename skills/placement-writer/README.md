# Placement Writer

**Category:** Content & Comms
**Effort to set up:** 10 minutes to collect the venue's rules

Takes a candidate-approved or published answer page or issue brief and renders it down to fit
one verified venue. Output goes to `campaign/placements/<venue>-<topic>.md` for candidate review
and human submission.

## Who it's for

Down-ballot candidates filling out the pile of voter guides, questionnaires, and statements that
arrive in the last ninety days: Ballotpedia, Vote411, the county statement, four endorsement
questionnaires, the paper's op-ed page. Nobody has a communications director. Everybody has a
deadline.

## What it does

The core idea is **write once, render many**. Ballotpedia, Vote411, state and county candidate
statements, endorsement questionnaires, op-eds, and letters to the editor are venue
configurations, not separate skills. One position of record goes in; a differently shaped
version of the same position comes out each time.

The skill reads a **venue spec** — limit and unit, audience, tone, submission method, deadline,
cost, rules on naming opponents, formatting rules, editability after submission, and who submits
— and then does five things:

1. **Renders down without padding up.** Cutting 900 words to 100 is the job. If the source is
   already shorter than the limit, it says so and stops rather than inflating it.
2. **Preserves evidence before framing.** Fixed cut order: throat-clearing, then adjectives, then
   framing and narrative, then secondary evidence. Primary evidence is never cut. Every cut is
   logged with its type.
3. **Counts the correct unit with a real tool.** It distinguishes words, characters including
   spaces, and characters excluding spaces, and records the command and exact result.
4. **Enforces venue rules** — no bullets or bold where prohibited, no opponent named where
   prohibited, required disclaimers included and counted.
5. **Returns submission instructions without submitting.** A human submits, always.

## Prerequisites

- Candidate-approved `campaign/positioning.md`
- A `candidate-approved` or `published` `campaign/answers/<slug>.md` or
  `campaign/briefs/<slug>.md`
- The venue's own instructions — or twenty minutes to email them and ask

The artifact lifecycle is `draft` → `candidate-approved` → `published`.

## Ownership boundary

This skill writes the submission-ready body of an op-ed or letter to the editor.
`local-media-pitch` writes the cover email and may attach or paste a candidate-approved
placement for direct submission. Story tips, interview offers, and document shares remain
`local-media-pitch` outputs.

## How to use it

Give it the source artifact and venue: "render the stormwater answer for Ballotpedia." It
verifies eligibility, fills the venue rules, cuts in order, runs a measured count, checks source
fidelity, and stops for candidate approval.

For a single-topic request, an unknown position stops the task. For a multi-question form, only
the affected field is blocked and receives
`[NO POSITION YET — ask the candidate: <specific question>]`.

## Full manual procedure

1. Confirm positioning is candidate-approved and the source artifact is `candidate-approved` or
   `published`. Do not render from a draft.
2. Check the topic against approved positioning and `no-position-yet`. Stop a single-topic task
   if the position is unknown; on a multi-question form, mark only the affected field with the
   missing-position marker.
3. Build the ten-field venue spec: limit and unit, audience, tone, submission method, deadline,
   cost, opponent-reference rule, formatting, editability, and named human submitter. Start with
   [`reference/venues.md`](../../reference/venues.md) and
   [`reference/state-voter-guides.md`](../../reference/state-voter-guides.md), then verify
   time-sensitive fields on the venue's own page or with a named venue contact. Record the URL,
   contact, and verification date. A blank or unverified field stops drafting.
4. Copy the position sentence, primary evidence, qualifications, exact numbers, exact dates,
   and required disclaimer into a scratch document. This is the full source boundary.
5. If the source is under the venue maximum, do not pad it. If it is over, cut in this order:
   throat-clearing and transitions; adjectives and intensifiers; framing and narrative;
   secondary evidence. Never cut primary evidence. Log each cut by type.
6. Put only submission text between the template's submission markers. Extract that exact text
   to a plain-text buffer and run the counter matching the venue:

   ```sh
   python3 -c 'import sys; print(len(sys.stdin.read().split()))'              # words
   python3 -c 'import sys; print(len(sys.stdin.read()))'                      # characters with spaces
   python3 -c 'import sys; print(len(sys.stdin.read().replace(" ", "")))'       # characters without spaces
   ```

   Pipe or paste only the submission buffer into one command. Remove an extraction-added
   trailing newline if it will not be submitted. Record the command, unit, and exact result.
7. Compare the final copy to the source side by side. Every number and date must be identical.
   Confirm attribution, uncertainty, scope, and every qualification survived. If the maximum
   cannot hold the position plus primary evidence and qualification, mark the placement
   nonviable instead of distorting it.
8. Recheck formatting, opponent references, disclaimers, cost, deadline, and submission route.
9. Show the candidate the exact copy, venue, deadline, and irreversible consequences. After an
   explicit yes, set `status: candidate-approved` and hand numbered instructions to the named
   human submitter. The skill never submits. Set `submitted`, `submitted_date`, and
   `submitted_by` only after the human confirms submission.

## Venue research notes

- Candidate-guide and statement mechanics change by jurisdiction and cycle. Treat the two
  reference tables as leads, not substitutes for current venue verification.
- For Vote411, verify the local League's invitation and field limits.
- For state and county statements, verify eligibility, cost, limit, deadline, formatting, and
  finality with the administering election office.
- For questionnaires, ask whether responses are public, shared, or internal.
- For op-eds and LTEs, verify candidate-bylines policy, limit, exclusivity, election cutoff,
  bio rules, editing rights, and submission route.
- If a venue will not state a limit, do not invent one. Ask a named contact and record the
  answer. Published examples can inform planning but are not a verified rule.

## Tips and edge cases

- **Ballotpedia allows only minor corrections after submission.** Draft offline, sleep on it,
  and have someone who disagrees with the candidate read it first.
- **Vote411 is invitation-only** through the local League, and character limits vary by League.
  If no invitation arrives, confirm the campaign email with the League.
- **Print deadlines can precede online ones.** Ask for both.
- **A closed venue is a calendar entry, not a dead end.** Record the verified close date and a
  next-cycle reminder.

## Example

For an invented county-commission candidate, a long stormwater answer becomes a short
Ballotpedia placement. The output records the exact counter result and a cut log while preserving
the source's fee amount, vote date, qualification, and exemption threshold.

## What it has been exercised against

Stated precisely, because a repo about not fabricating claims should not fabricate its own
test history.

- **Three eval cases** in [`evals/evals.json`](evals/evals.json), runnable by
  `npx agent-skills-eval`: a Washington candidate statement, where the output has to come in
  under 100 words with the source's numbers intact; a Vote411 answer at 750 *characters*,
  where the skill has to demonstrate it understood the unit by reporting a measured character
  count; and "fill these out and submit them for me," where it must draft, warn that
  Ballotpedia allows only minor corrections afterward, and submit nothing. They run against an
  invented campaign in an invented county.
- **Structural validation** on every pull request via `scripts/validate_skills.py`, which
  enforces the agentskills.io spec plus this repo's conventions.

**Not yet done:** the eval suite has not been run against a live model, so no assertion here
has an observed pass rate — including the word and character limits, which are the obvious
candidates for a mechanical verification script and do not have one yet. No real campaign has
submitted anything produced this way, and the manual path has not been walked end to end
either. If you run it, please open an issue and say what broke.

## Related

- [`answer-page`](../answer-page/SKILL.md) and [`issue-brief`](../issue-brief/SKILL.md) — the
  source artifacts this skill renders from
- [`reference/state-voter-guides.md`](../../reference/state-voter-guides.md) — the expanding
  state-by-state table
- [`reference/shared-rules.md`](../../reference/shared-rules.md) — the rules every skill enforces
