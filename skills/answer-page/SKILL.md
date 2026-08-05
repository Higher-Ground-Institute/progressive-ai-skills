---
name: answer-page
description: Writes one dated, sourced position-of-record page answering a single question a voter would actually ask, using the campaign's positioning file as the only source of message. Refuses to write a position on any topic listed as no-position-yet, and refuses to generate near-duplicate pages for search-phrasing variations. Use this when a campaign needs to publish where a candidate stands on an issue, write a position page, answer a voter question in writing, or build out the issues section of a campaign site.
---

# Answer Page

**Reads:** `campaign/positioning.md` (required), plus `campaign/district-issues.md` for
supporting evidence.
**Writes:** `campaign/answers/<topic-slug>.md`.

One page, one question, one substantive position. This is the campaign's source of record on
an issue — the page a reporter links to, a voter reads, and an answer engine quotes.

The unit is an **answer**, not a blog post. A blog post is about a topic. An answer resolves a
question in its first paragraph and then proves it.

## Before you write anything

**Read `campaign/positioning.md` first.** It is the only source of campaign message. Do not
open `candidate-profile.md` — if positioning does not carry what you need, the fix is to add
it to positioning, not to re-derive the message from the profile.

Two hard stops, checked in this order:

**1. The unknown-position rule.** Read the `## No position yet` table. If the requested topic
appears there, do not write a position. Output this and stop:

```
[NO POSITION YET — ask the candidate: <the specific question from the table>]
```

Never infer a position from the candidate's party, from other candidates running similar
campaigns, from their biography, or from adjacent positions in the file. If positioning does
not state a position, the campaign does not have one, and saying so is the correct output.
Offer to draft the page as soon as the candidate answers the question.

**2. The one-page-per-position rule.** If asked for a page per search phrasing — "one for
*housing*, one for *rent*, one for *zoning*, one for *affordable housing*" — decline and
explain. Google names that pattern as scaled content abuse
([Google](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)), and
page count correlates at only r ≈ 0.194 with AI visibility
([Ahrefs](https://ahrefs.com/blog/ai-brand-visibility-correlations/)). It is a spam risk that
does not work. Offer one strong page covering the position instead.

Also stop if `approved_by_candidate` is `false` in the positioning frontmatter. Say that the
candidate has not signed off on positioning yet and that writing content on top of unapproved
positioning wastes the work.

## Output Format

Write to `campaign/answers/<topic-slug>.md` using the structure in
[`campaign-template/answers/_template.md`](../../campaign-template/answers/_template.md):

```markdown
---
title: "Where does Jane Doe stand on the stormwater fee increase?"
topic_slug: stormwater-fee
question: "Should the county roll back the 2026 stormwater fee increase?"
candidate_name: "Jane Doe"
author: "Jane Doe"
date_created: "2026-08-04T11:30:00-04:00"
date_modified: "2026-08-04T11:30:00-04:00"
status: draft
sources_count: 6
---

# Should the county roll back the 2026 stormwater fee increase?

No — but the county should exempt households under 200% of the federal poverty
line, which the ordinance as written does not do.

## Why
...
## What I would do
...
## What I don't know yet
...
## Sources
```

Required sections, in this order: the answer paragraph (no heading), `## Why`,
`## What I would do`, `## What I don't know yet`, `## Sources`.

**The first paragraph answers the question.** Not background, not a story about knocking
doors, not "as I've traveled across this district." A voter who reads three sentences and
stops should know exactly where the candidate stands.

## Steps

1. **Confirm the question.** Write it as a single sentence a real voter would say out loud.
   If the request was "write something about housing," push back and get to a question:
   *Should the city allow duplexes on the east side?* A topic is not a question.
2. **Check `positioning.md`** for the two hard stops above. Stop if either fires.
3. **Pull the position of record** for this topic slug from `## Positions of record`. That
   text is your source. Do not invent supporting arguments that are not in it.
4. **Gather evidence** from `district-issues.md` and the primary records it cites. Prefer the
   actual ordinance, budget line, or minutes over reporting about them. Every number needs a
   URL and a retrieval date.
5. **Write the answer paragraph.** One to three sentences. Include the qualification if there
   is one — "yes, but only if" is a real position and voters trust it more than a clean yes.
6. **Write `## Why`** — two to four paragraphs, dense with specifics. Dollar figures, dates,
   vote counts, comparisons to neighboring jurisdictions. Source each inline as
   `claim ([source](url), retrieved YYYY-MM-DD)`.
7. **Write `## What I would do`** — the specific action, at the specific body, through the
   specific mechanism. "Fight for working families" is not an action.
8. **Write `## What I don't know yet`** — real uncertainty, what would change their mind.
   Do not skip this and do not make it fake-humble. It is the section that earns trust.
9. **Fill the source table** and set `sources_count` to match.
10. **Run the self-check** in `## Tips` below.
11. **Get human approval.** Show the candidate the full page. Ask explicitly: *is every
    sentence here something you would say at a hostile town hall?* Wait for a yes. Only then
    set `status: candidate-approved`. **This skill never publishes anything.**

## Rules that do not bend

- **Source every factual claim inline, with the date.** Quotes, endorsements, statistics,
  bill numbers, vote counts, dollar figures, and dates are copied from a source or omitted.
  If you cannot find a number, write `[NEEDS SOURCE — what to look up]` and keep going. Never
  approximate a figure or reconstruct a quote from its gist.
- **No claim that is not in `positioning.md` or a cited source.** The candidate has to defend
  every sentence on this page in public.
- **`date_modified` changes only after a substantive edit.** Never bump a date to look fresh.
- **The candidate is the author.** Attributed, human-reviewed, human-published. See
  [`reference/shared-rules.md`](../../reference/shared-rules.md).

## Doing this without an agent

You need `positioning.md`, `district-issues.md`, a text editor, and about ninety minutes.

1. Open `positioning.md`. Find the `## No position yet` table. **If your topic is in it, stop
   here** and go ask the candidate the question in that row. Do not write the page.
2. Still in `positioning.md`, find your topic under `## Positions of record`. Copy that entry
   into a new file. This is your raw material — everything on the finished page has to trace
   back to it or to a source you are about to look up.
3. Write the question at the top as one sentence, the way a neighbor would ask it.
4. Under it, write the answer in one to three sentences. If you find yourself writing a
   paragraph of setup first, delete the setup. It goes in `## Why`.
5. Open `district-issues.md` and find the issue. Follow its links to the primary records — the
   ordinance PDF, the budget page, the meeting minutes. Write down each number you use along
   with the URL and today's date.
6. Write `## Why` using those numbers. Rule of thumb: if a sentence has no number, no date,
   and no name in it, it is probably an adjective wearing a suit. Cut it or replace it.
7. Write `## What I would do`. Name the body that decides, the vote or action, and when it
   happens.
8. Write `## What I don't know yet`. Ask the candidate directly: "what would change your mind
   about this?" Use their answer.
9. Build the source table. Number every source and check every link opens.
10. Read the page out loud. Anything you stumble over, rewrite.
11. Give it to the candidate on paper. Ask: *would you say every sentence of this at a town
    hall where half the room disagrees with you?* Fix whatever they hesitate on.
12. Have a human — not a tool — put it on the site.

## Tips

**The self-check before approval.** Every one of these must be yes:

- [ ] The question is answered in the first paragraph
- [ ] Every factual claim has an inline source with a date
- [ ] No quote, statistic, bill number, vote, or date appears without a source
- [ ] Nothing on the page contradicts or exceeds `positioning.md`
- [ ] The evidence is local and specific, not national talking points with a place name
      dropped in
- [ ] `## What I don't know yet` says something real
- [ ] A reader who disagrees with the candidate would still call the page honest
- [ ] Reading level around 8th–10th grade; sentences short enough to say out loud

**The generic-content test.** Swap the district name for a different one. If the page still
reads fine, it is national boilerplate and it fails. Local evidence is not decoration; it is
the entire value of the page.

**Write density, not length.** Controlled measurement found comparison content at +55% and
how-to content at +41% mean answer influence, while Q&A formatting measured −5.7%
([arXiv](https://arxiv.org/html/2604.25707v1)). Compare this jurisdiction to its neighbors or
to its own past. Explain how a resident actually participates. Do not reformat the page as a
FAQ — that is the one structural move the evidence says is slightly negative.

**"Yes, but" is a stronger position than "yes."** A qualified answer with a stated threshold
sounds like someone who has thought about the tradeoff. An unqualified answer sounds like
someone who has not read the ordinance.

**When the candidate's position is unpopular**, write it anyway and put the strongest
objection in `## Why`, answered fairly. The page exists so that voters find the candidate's
real reasoning instead of the opponent's characterization of it.

**One page per position.** If the campaign has twelve genuine positions, twelve pages is
correct. Eighty pages for eighty phrasings of four positions is scaled content abuse and it
does not work anyway.
