# Placement Writer

**Category:** Content & Comms
**Effort to set up:** 10 minutes to collect the venue's rules

Takes a position the campaign has already written — an answer page or an issue brief — and
renders it down to fit one specific venue's limit, tone, and rules. Output goes to
`campaign/placements/<venue>-<topic>.md`, ready for a human to submit.

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
3. **Counts the correct unit, measured.** 750 characters is about 110 words, not 750. It
   distinguishes characters including spaces from characters excluding spaces and records an
   actual count, never an estimate.
4. **Enforces venue rules** — no bullets or bold where prohibited, no opponent named where
   prohibited, required disclaimers included and counted.
5. **Returns submission instructions without submitting.** A human submits, always.

## Prerequisites

- An approved `campaign/answers/<slug>.md` or `campaign/briefs/<slug>.md`
- `campaign/positioning.md` for boilerplate, bios, and the required disclaimer
- The venue's own instructions — or twenty minutes to email them and ask

## The venue table

The `SKILL.md` carries verified mechanics for Ballotpedia Candidate Connection, Vote411/LWV,
state candidate statements (the paid / free-but-limited / unavailable branch, with California,
Washington, and Arizona worked out), endorsement questionnaires, op-eds, and letters to the
editor. Anything not in that table has to be verified before drafting — the skill will not
invent a limit. It also includes a procedure for deriving a spec for a venue that will not tell
you its rules: count three published examples and use the shortest.

## How to use it

Give it the source artifact and the venue: "render the stormwater answer for Ballotpedia." It
fills the venue rules table, cuts in order, counts, checks the rules against the final text, and
stops at an approval step that states plainly what cannot be undone.

## Tips and edge cases

- **Ballotpedia allows only minor corrections after submission.** Draft offline, sleep on it,
  and have someone who disagrees with the candidate read it first.
- **Vote411 is invitation-only** through the local League, and character limits vary by League.
  If no invitation arrives, confirm the campaign email with the League.
- **Print deadlines can precede online ones.** Ask for both.
- **A closed venue is a calendar entry, not a dead end.** Washington's 2026 statement deadline
  was May 19; California statements were due with nomination papers.

## Example

For an invented candidate — Jane Okonkwo, running for a county commission seat — the 900-word
answer page on the stormwater fee becomes `campaign/placements/ballotpedia-stormwater-fee.md`: a
731-character submission-ready block, a measured count line, and a cut log showing that four
transitions, eleven adjectives, and one secondary comparison came out while the fee increase,
the vote date, and the exemption threshold stayed in.

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
