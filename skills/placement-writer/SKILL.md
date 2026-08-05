---
name: placement-writer
description: Renders a candidate-approved or published campaign answer or issue brief into a venue-compliant voter-guide response, questionnaire answer, candidate statement, op-ed body, or letter-to-the-editor body. Requires approved positioning, preserves source claims and qualifications exactly, measures the venue's actual count unit, and never submits or publishes. Use this when a campaign needs submission-ready copy fitted to a verified venue specification.
---

# Placement Writer

**Reads:** approved `campaign/positioning.md`; one `candidate-approved` or `published`
`campaign/answers/<slug>.md` or `campaign/briefs/<slug>.md`; and a verified venue spec.
**Writes:** `campaign/placements/<venue>-<topic>.md`.

This skill owns submission-ready op-ed and LTE bodies. `local-media-pitch` owns the cover email,
story tip, interview offer, or document-share email. It may consume a candidate-approved
placement for a direct op-ed/LTE submission.

## Gates

1. Confirm `campaign/positioning.md` is candidate-approved. If not, stop.
2. Confirm the source artifact has `status: candidate-approved` or `status: published`. Draft
   sources are not eligible.
3. Check the requested topic against approved positioning and `no-position-yet`.
   - For a single-topic placement, an unknown position stops the task.
   - For a multi-question form, do not draft the affected field. Insert
     `[NO POSITION YET — ask the candidate: <specific question>]` there and continue with
     unaffected fields.
4. Fill the venue spec: limit and unit, audience, tone, submission method, deadline, cost,
   opponent-reference rule, formatting, editability, and human submitter. Unverified fields stop
   drafting. Use [`reference/venues.md`](../../reference/venues.md) and
   [`reference/state-voter-guides.md`](../../reference/state-voter-guides.md), then verify
   time-sensitive mechanics with the venue.

## Output Format

Write to `campaign/placements/<venue>-<topic>.md` using
[`campaign-template/placements/_template.md`](../../campaign-template/placements/_template.md):

```markdown
---
venue: "Ballotpedia Candidate Connection"
venue_type: survey            # survey | statement | questionnaire | op-ed | letter | guide
source_artifact: "campaign/answers/stormwater-fee.md"
limit_unit: characters        # words | characters | characters_excluding_spaces | none
limit_value: 750
actual_count: 731             # measured, not estimated
deadline: "2026-09-15"
cost: "$0"
editable_after_submission: "minor corrections only"
submission_method: "web form"
candidate_name: "Jane Okonkwo"
date_created: "2026-08-04T14:00:00-05:00"
date_modified: "2026-08-04T14:00:00-05:00"
status: draft                 # draft | candidate-approved | submitted
submitted_date: ""
submitted_by: ""              # a human name — this skill never submits
---
```

Required sections: `## Venue rules`; `## Submission-ready text`, holding only the pasted text
between the `<!-- BEGIN SUBMISSION -->` and `<!-- END SUBMISSION -->` markers; the measured count
line; `## What was cut, and why`; `## Submission instructions for a human`; `## Irreversibility warning`.

## Steps

1. Record every venue rule with its source URL and verification date. Do not infer a rule from a
   similar venue.
2. Copy the approved position, evidence, qualifications, numbers, and dates into a scratch area.
   This source material is the boundary: do not introduce a new claim.
3. Render down without padding up. If the source is under the limit, keep it under; do not add
   prose merely to approach the maximum.
4. **Cut in this order, never out of order:**
   1. Throat-clearing and transitions — "as I've traveled across this district," "it's no secret
      that," "first and foremost"
   2. Adjectives and intensifiers — "critical," "commonsense," "deeply," "absolutely"
   3. Framing and narrative — the story that sets up the number, once the number can stand alone
   4. Secondary evidence — the third and fourth data points supporting the same claim
   5. Primary evidence — **never.** If the limit cannot hold one number, one date, and the
      position, the placement is not viable; report that instead of shipping adjectives.
   Log every cut and its type.
5. **Preserve source fidelity.** Compare source and placement side by side. Every number and
   date must match exactly; keep attribution, uncertainty, scope, and qualifications. A cut must
   not turn "yes, but only if" into "yes." If the limit cannot hold the position plus its primary
   evidence and qualification, report the placement as nonviable.
6. **Measure; never estimate.** Extract exactly the text between the submission markers into a
   temporary plain-text buffer. Run a real counter for the venue's unit:
   - words: `python3 -c 'import sys; print(len(sys.stdin.read().split()))'`
   - characters including spaces: `python3 -c 'import sys; print(len(sys.stdin.read()))'`
   - characters excluding spaces: `python3 -c 'import sys; print(len(sys.stdin.read().replace(" ", "")))'`
   Pipe or paste only the extracted submission text to the selected command. Remove a trailing
   newline added by the extraction method before counting if the venue would not receive it.
   Record the tool, unit, and exact result in `actual_count` and the measured-count line. Never
   use "about," "approximately," a visual estimate, or a word-to-character conversion.
7. **Enforce the venue rules against the final text.** No bullets or bold where prohibited,
   including em-dash lists that are bullets in disguise. No opponent named where prohibited,
   including "my opponent" if the rule covers references and not just names. Include any
   required disclaimer from `## Boilerplate` in `positioning.md`, inside the count.
8. Show the candidate the exact text, venue, recipient or form, deadline, and irreversible
   consequences. On explicit approval, set `status: candidate-approved` and return numbered
   submission instructions. A named human submits. This skill never sends or submits.
   Set `status: submitted`, `submitted_date`, and `submitted_by` only after that human confirms
   submission.

## Doing this without an agent

For venue research, manual counting, source-fidelity checks, and the human submission checklist,
follow the full procedure in [`README.md`](README.md).

## Tips

Answer the venue's actual question, prefer plain words under character limits, and reuse a
placement only after rechecking the new venue's rules.
