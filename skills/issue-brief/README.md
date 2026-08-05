# Issue Brief

**Category:** Content & Comms
**Effort to set up:** none beyond an existing `campaign/` folder

Writes the best available public reference on one narrow local issue — the data center, the
rate hike, the school closure, the zoning fight — built from primary records rather than from
reporting about them. Output goes to `campaign/briefs/<topic-slug>.md`.

## Who it's for

First-time, down-ballot candidates with no staff: state legislature, county commission, school
board. It is also the skill a volunteer can run without any AI tool, which is the point — the
`SKILL.md` contains the complete manual procedure, including how to file a records request and
how long to expect it to take.

## What it does

The brief is not a position paper. It is the document that should already exist about the issue
and does not. Every section is built around one test: **would someone who will never vote for
this candidate still bookmark it?**

The skill produces a document with:

1. **A dated timeline** of how the decision happened — ordinance numbers, meeting dates, roll-call
   votes, each linked to the record rather than to coverage of the record
2. **A numbers table built as a comparison** — this jurisdiction against its neighbors, against
   its own past, against the state average
3. **A participation section** — the body, the next meeting, the address, how public comment
   sign-up works and when it closes
4. **Both sides steelmanned**, with the opposing case quoted from a real advocate
5. **The candidate's position, short and clearly separated** from the reference material
6. **What is still unknown** — pending records requests, unreleased studies, unpublished figures

Frontmatter carries `sources_count` and `primary_records_count`. The second number counts actual
records — an ordinance PDF, a minutes page, a docket filing, a budget line — not articles about
them.

## Prerequisites

- `campaign/positioning.md` with `approved_by_candidate: true`
- `campaign/district-issues.md` from `district-issue-scan`
- Access to the jurisdiction's agenda portal, a phone for the clerk, and patience for records
  requests

## How to use it

Point the skill at one issue: "write the brief on the June 9 tax abatement vote." It reads
positioning, pulls the primary records, drafts the brief, and stops at a human approval step.
It never publishes.

If the topic is on the `no-position-yet` list, the brief still gets written — the position
section carries `[NO POSITION YET — ask the candidate: ...]` and names the open question. That
is a passing result, not a failure.

## Tips and edge cases

- **Narrow beats broad.** "Schools" is a topic area. "The proposed closure of Kingsbury
  Elementary" is an issue. If the timeline covers more than one body deciding more than one
  thing, write two briefs.
- **Unpopular positions make the brief more valuable, not less.** Document honestly, put the
  strongest objection where it belongs, keep the position short.
- **Records take time.** File the request the day you scope the brief and keep writing. Publish
  with the outstanding request named and dated in `## What is still unknown`.
- **It goes stale.** Put the next decision date in the participation section and set a reminder
  for the day after.

## Example

For an invented candidate — Marisol Reyes, running for the Pike County Commission — the brief
`campaign/briefs/verity-fields-data-center.md` opens with what the commission approved on
June 9, a timeline table linking each vote to the minutes, a table comparing the county's
abatement terms to the two counties next door, the date and sign-up rule for the next
commission meeting, the developer's case and the opponents' case each stated at full strength,
and six sentences on where Reyes stands.

## What it has been exercised against

Stated precisely, because a repo about not fabricating claims should not fabricate its own
test history.

- **Three eval cases** in [`evals/evals.json`](evals/evals.json), runnable by
  `npx agent-skills-eval`: a full brief built from primary records; a request for a brief on
  "housing," which has to be narrowed to one decision before anything is written; and a
  request for a brief on an issue the contested-space survey already rates as well covered,
  where saying so is the passing result. They run against an invented campaign in an invented
  county.
- **Structural validation** on every pull request via `scripts/validate_skills.py`, which
  enforces the agentskills.io spec plus this repo's conventions.

**Not yet done:** the eval suite has not been run against a live model, so no assertion here
has an observed pass rate, and no real campaign has published a brief written this way. The
manual procedure in `SKILL.md` — including how to file a records request — is written to be
followable with a text editor and a phone, but nobody has walked it end to end. If you run it,
please open an issue and say what broke.

## Related

- [`answer-page`](../answer-page/SKILL.md) — the campaign's position of record on a question
- [`placement-writer`](../placement-writer/SKILL.md) — renders a brief down to fit a venue
- [`reference/shared-rules.md`](../../reference/shared-rules.md) — the rules every skill enforces
