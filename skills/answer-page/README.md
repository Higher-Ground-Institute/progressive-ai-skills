# Answer Page

**Category:** Content & Comms

Writes one dated, sourced position-of-record page that answers a single question a voter
would actually ask. The page a reporter links to, a voter reads, and an answer engine quotes.

## Who it's for

A first-time candidate for state legislature, county commission, school board, or city
council who has no comms staff and needs an issues section that says something. Also for the
volunteer who got handed "can you write up where she stands on the water thing" and has never
written a position page before.

Frequency: a handful of times at the start of a campaign, then once whenever a new issue
becomes real. Three to five substantive pages is a complete issues section. Eighty is a spam
problem.

## What it does

Reads `campaign/positioning.md` — the campaign's approved message file — and writes
`campaign/answers/<topic-slug>.md`.

The output is structured as an answer, not a blog post:

1. **The answer, in the first paragraph.** No windup, no "as I've traveled across this
   district." A voter who reads three sentences knows where the candidate stands.
2. **Why** — two to four paragraphs of dollar figures, dates, vote counts, and comparisons,
   each sourced inline with a URL and a retrieval date.
3. **What I would do** — the specific action, at the specific body, through the specific
   mechanism.
4. **What I don't know yet** — real uncertainty, and what would change the candidate's mind.
5. **Sources** — a numbered table where every link has been checked.

## The two things it refuses to do

This is most of the value, so it is worth stating plainly.

**It will not invent a position.** Before writing, the skill reads the `no-position-yet` list
in `positioning.md`. If the requested topic is on it, the skill outputs
`[NO POSITION YET — ask the candidate: <the specific question>]` and stops. It will not infer
a stance from the candidate's party, from similar candidates, or from the rest of the file. A
model asked what a candidate thinks about anything will produce a confident answer, and that
answer, published in a voter guide under the candidate's name, is a fabrication.

**It will not generate a page per search phrasing.** Asked for separate pages for "housing,"
"rent," "zoning," and "affordable housing," it declines and offers one page instead. Google
names that pattern as scaled content abuse, and page count correlates at only r ≈ 0.194 with
AI visibility — it is a spam risk that does not work.

## Prerequisites

- `campaign/positioning.md`, written by `positioning-builder`, with
  `approved_by_candidate: true`
- `campaign/district-issues.md`, written by `district-issue-scan`, for the underlying evidence
- A human who will read the page before it goes on the site

No AI tool required. The `## Doing this without an agent` section in `SKILL.md` is a complete
manual procedure — about ninety minutes with a text editor.

## How to use it

Ask for a specific question, not a topic:

> "Write my answer page on whether the county should roll back the stormwater fee increase."

If you ask for "something about housing," the skill will push back and make you name the
question first. That is deliberate. A topic is not a question, and pages that answer topics
answer nothing.

## Tips and edge cases

- **"Yes, but" beats "yes."** A qualified position with a stated threshold sounds like
  someone who read the ordinance. An unqualified one sounds like someone who did not.
- **The generic-content test:** swap in a different district's name. If the page still reads
  fine, it is national boilerplate and it fails. Local evidence is the entire value.
- **Unpopular positions get written anyway**, with the strongest objection stated fairly in
  `## Why`. The page exists so voters find the candidate's real reasoning instead of the
  opponent's version of it.
- **`## What I don't know yet` is not optional and not false modesty.** It is the section
  that separates a position from a slogan.
- **Dates mean something.** `date_modified` changes only after a substantive edit. Never bump
  it to look fresh.

## Example

Given a `positioning.md` containing a settled position on a county stormwater fee, the skill
produces `campaign/answers/stormwater-fee.md` opening:

> **Should the county roll back the 2026 stormwater fee increase?**
>
> No — but the county should exempt households under 200% of the federal poverty line, which
> the ordinance as written does not do.
>
> ## Why
>
> The fee went from $4.50 to $11.25 a month in January
> ([Ordinance 2026-14](https://example.gov/ord-2026-14), adopted 2026-01-14) — a 150%
> increase applied at a flat rate regardless of household income or lot size...

Given the same request for a topic listed under `no position yet`, it produces:

> `[NO POSITION YET — ask the candidate: should the exemption threshold be tied to the
> federal poverty line, to the county median income, or to assessed property value?]`

## What it has been exercised against

Being specific about this, because a repo about not fabricating claims should not fabricate
its own test history.

- **Three eval cases** in [`evals/evals.json`](evals/evals.json), runnable by
  `npx agent-skills-eval`: the `no-position-yet` refusal, the query-variant refusal, and a
  normal page with a full source table. They run against an invented campaign in an invented
  county, so no real candidate's unreviewed positions are involved.
- **Structural validation** on every pull request via `scripts/validate_skills.py`.

- **Real district research** in [`golden/`](../../golden/), for checking the invented fixtures
  against how real places actually behave. It covers *places*, not candidates — no position is
  attributed to a real person anywhere in it.

**Not yet done:** no real campaign has used this on a live race, and the eval suite has not
been run against a model to see which assertions the no-skill baseline also passes. Several
probably do, and those should be deleted when we find out. The manual procedure above is
written to be followable without any AI tool, but nobody has walked it end to end. If you run
this on a real campaign, please open an issue and say what broke.
