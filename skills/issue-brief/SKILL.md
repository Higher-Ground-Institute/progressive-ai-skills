---
name: issue-brief
description: Writes the best available reference document on one narrow local issue — a dated, sourced brief built from primary records (the actual ordinance, the actual budget line, the actual minutes, the actual rate schedule) rather than reporting about them, with a timeline, a numbers comparison, a section on how a resident actually participates, both sides steelmanned, and a short clearly separated statement of where the candidate stands. Refuses to state a position on any topic on the no-position-yet list in positioning.md and names the open question instead. Use this when a campaign needs to explain a local fight in depth, document a rate increase, school closure, zoning decision, bond measure, or development deal, build a reference page a reporter or a non-supporter would cite, or turn district research into a public explainer.
---

# Issue Brief

**Reads:** `campaign/positioning.md` (required) and `campaign/district-issues.md` (required),
plus the primary records those files cite.
**Writes:** `campaign/briefs/<topic-slug>.md`.

One narrow local issue, documented well enough that the other side links to it. Not a position
paper — the document that should already exist about the data center, the rate hike, the school
closure, the zoning fight, and does not.

## The usefulness test

**Would someone who will never vote for this candidate still bookmark it?** If not, it is a
position paper wearing a reference document's clothes. That is a slogan until you run it:

1. **Name three real non-supporters** before you outline — not "a conservative voter" but the
   landlord who owns the fourplexes on Chestnut, the retired utility engineer in the Facebook
   group, the parent who wants the school closed because the building is failing. Ask what each
   section gives those three. "It shows the campaign cares" is not an answer; "it gives them the
   next hearing date and the sign-up deadline" is.
2. **Run the delete test.** Delete `## Where [CANDIDATE] stands` and the byline. Does the rest
   still stand as a reference document? If it collapses into advocacy, the advocacy was
   load-bearing and the brief failed. Run this after the outline, after the draft, and before
   approval — briefs fail it late, in the edit that adds adjectives.

## Before you write anything

**Read `campaign/positioning.md` first.** It is the only source of campaign message, do not
open `candidate-profile.md`, and stop if `approved_by_candidate` is `false`.

**The unknown-position rule**, verbatim from [`shared-rules.md`](../../reference/shared-rules.md):

> **Before writing, read the `no-position-yet` list in `campaign/positioning.md`.** If the
> topic you were asked to write about appears on that list, do not write a position. Output
> this instead, and then continue with the rest of the task:
>
> `[NO POSITION YET — ask the candidate: <the specific question they need to answer>]`
>
> Never infer a position from the candidate's party, from other candidates running similar
> campaigns, from their biography, or from the rest of the positioning file. If
> `positioning.md` does not state a position on the topic, the campaign does not have one
> yet, and saying so is the correct output.

Unlike `answer-page`, an unknown position does not stop this skill — the reference material is
the point. Write the brief, put the marker and the open question in the position section, go on.

## Finding the primary records

A brief built from articles summarizes someone else's work; one built from records is what
everyone else summarizes. Do all of this before drafting, and count what you get:
`primary_records_count` counts records — an ordinance PDF, a minutes page, a docket filing, a
budget line — not links. It is the one number a hostile reader checks in thirty seconds.

- **The agenda portal.** Work the vendor from the hostname: `{client}.legistar.com`,
  `{st}-{jurisdiction}.civicplus.com/AgendaCenter`, `{jurisdiction}.granicus.com`, CivicClerk,
  PrimeGov. Legistar has a public API at `https://webapi.legistar.com/v1/{Client}/{Endpoint}`,
  usually keyless ([Granicus](https://support.granicus.com/s/article/Legistar-Web-API)). Pull
  agenda, packet, minutes, roll call — the packet holds the staff report.
- **The county or municipal clerk.** Ordinances, resolutions, recorded votes, certified minutes,
  and the budget line itself, cited by page and fiscal year. Call them; clerks know which
  document you actually want.
- **The state open-records portal or a records request.** For anything unpublished — emails,
  studies, contracts, staff analyses. Response windows vary by state, days to weeks and sometimes
  months, so file the day you scope the brief.
- **The regulated entity's own filing.** A rate increase exists as a docketed filing at the
  state utility commission with testimony, exhibits, and a rate schedule attached, and that
  docket beats every article written about it.

## Output Format

Write to `campaign/briefs/<topic-slug>.md` using
[`campaign-template/briefs/_template.md`](../../campaign-template/briefs/_template.md):

```markdown
---
title: "The Verity Fields data center: what is actually happening in Pike County"
topic_slug: verity-fields-data-center
jurisdiction: "Pike County, Ohio"
candidate_name: "Marisol Reyes"
author: "Marisol Reyes"
date_created: "2026-08-04T09:00:00-04:00"
date_modified: "2026-08-04T09:00:00-04:00"
status: draft
published_url: ""
sources_count: 14
primary_records_count: 9
---
```

Required sections in this order: `## The short version`, `## How we got here`, `## The numbers`,
`## Who decides what happens next`, `## The arguments`, `## Where [CANDIDATE] stands`,
`## What is still unknown`, `## Sources`.

## Steps

1. **Narrow to one issue.** "Development" is a topic area; "the tax abatement the commission
   approved for the Verity Fields data center on June 9" is an issue. If the timeline covers
   more than one body deciding more than one thing, split the brief.
2. **Pull the primary records** using the section above, each with its URL and retrieval date,
   before drafting. Write the three non-supporters at the top of the file.
3. **Write `## How we got here`** as a dated table: date, what happened, the vote, the record.
   Vote counts come from minutes, not from coverage of the meeting.
4. **Write `## The numbers` as a comparison** — this jurisdiction against its neighbors, its own
   past five years, the state average. Comparison content measured +55.28% mean answer influence
   and how-to content +41.20%, while Q&A formatting measured −5.74%
   ([arXiv](https://arxiv.org/html/2604.25707v1)). Use the honest comparison, not a flattering one.
5. **Write `## Who decides what happens next` as a how-to** — the body, the members, the next
   meeting date and address, the comment sign-up rule and its deadline, whether written comment
   is accepted and where. Second-highest-measured genre, and the section non-supporters use.
6. **Steelman both sides.** State each case as its strongest advocate would. Where the campaign
   disagrees, quote a real person making it well — with a citation, never a straw version — and
   then write what both sides agree on.
7. **Write `## Where [CANDIDATE] stands` short** — three to six sentences from `## Positions of
   record`, clearly separated from the reference material. Longer than the rest of the document
   means the document is a mailer. Then `## What is still unknown`: outstanding records
   requests, unreleased studies, unpublished figures, and what would resolve each.
8. **Fill the source table**, set `sources_count` and `primary_records_count`, and run the
   usefulness test plus the checklist in `## Tips`.
9. **Get human approval.** Ask the candidate: *if the other side's best researcher read this,
   what would they call unfair?* Fix that, then set `status: candidate-approved`. **This skill
   never publishes anything.**

## Rules that do not bend

The candidate is the author: attributed, human-reviewed, human-published. `date_modified`
changes only after a substantive edit, never to look fresh. And **sourcing**, verbatim from
[`reference/shared-rules.md`](../../reference/shared-rules.md):

> Source every factual claim inline, with the source date. Format:
> `claim ([source name](url), retrieved 2026-08-04)`.
>
> Quotes, endorsements, statistics, bill numbers, vote counts, dollar figures, and dates are
> copied from a source or omitted. There is no third option. If you cannot find the number,
> write `[NEEDS SOURCE — <what to look up>]` and keep going. Do not approximate a figure you
> half-remember, and do not reconstruct a quote from its gist.
>
> Prefer primary records — the actual ordinance, the actual budget line, the actual meeting
> minutes — over reporting about them. When you cite reporting, cite the outlet and the
> reporter.

## Doing this without an agent

You need `positioning.md`, `district-issues.md`, a text editor, a phone, and two working days
spread across the two weeks records take to come back.

1. Pick one issue — one decision, one body — and write it as a sentence with a date in it. Tape
   up the names of three people in the district who will not vote for this candidate.
2. Open `district-issues.md`, find the issue, copy out every primary record it lists.
3. Find the body's agenda portal, search by meeting date, download the agenda, packet, and
   minutes. Then call the clerk: "I'm looking for the ordinance and the certified minutes for
   the [date] vote on [thing]." Ask what else exists on it. They will tell you.
4. For anything unpublished, file a records request through the state portal or by email to the
   agency's records officer. Ask for named documents, not "all records about." Note the filing
   date, expect days to weeks, and keep writing while you wait. For a utility issue, search the
   state utility commission's docket by company name; filings and testimony are public.
5. Build the timeline table — date, what happened, vote count, link. Then the numbers table
   with a comparison column: this county, the two next door, this county five years ago, the
   state average. Source every cell.
6. Call the clerk again for the participation section: when the body meets, where, how comment
   sign-up works, the deadline.
7. Write both cases, using a real quote from a real advocate for the side the campaign
   disagrees with — a public comment recorded in the minutes works. Then the candidate's
   position, last and under half a page.
8. Read it as one of the three people on the wall and cut every sentence that only works if you
   already agree. Give it to the candidate on paper. Have a human put it on the site.

## Tips

**The checklist before approval.** Every one must be yes:

- [ ] `primary_records_count` counts records, not articles about records
- [ ] Every number, date, vote, and dollar figure has an inline source and a retrieval date
- [ ] There is a real comparison, not just this jurisdiction's own figures
- [ ] A resident could act on `## Who decides what happens next` without calling anyone
- [ ] The opposing case would satisfy the person who holds it
- [ ] The position is shorter than the reference material, and the unknowns are named

**When the campaign's position is unpopular**, the brief is worth more, not less. Document the
issue honestly, put the strongest objection in `## The arguments`, keep the position short.
Burying an unpopular position in a fog of context is worse than stating it plainly.

**How narrow is narrow enough.** One issue, not one topic area. "Schools" is a topic area; "the
proposed closure of Kingsbury Elementary" is an issue. Test: is every timeline row the same body
deciding the same thing? If not, split it. Three narrow briefs beat one broad one, and being
genuinely different subjects they do not trip the one-page-per-phrasing rule.

**When the records are paywalled or pending.** Court records and some county portals charge per
page; ask the clerk about a free public terminal or reading-room copy. If a record is pending a
records response, publish anyway and list the request in `## What is still unknown` with the
filing date and the agency — a gap named and dated is credible, a silent gap is not.

**Keeping it current.** A brief about a live fight goes stale in weeks. Put the next decision
date in `## Who decides what happens next`, set a reminder for the day after, and when
something happens add a timeline row, update the numbers, and change `date_modified` for the
real edit. If the issue resolves, say so at the top and leave it up.
