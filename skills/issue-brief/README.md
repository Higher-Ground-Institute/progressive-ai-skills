# Issue Brief

**Category:** Content & Comms

Writes a dated public reference on one narrow local issue from primary records. Output goes to
`campaign/briefs/<topic-slug>.md`.

## When to use it

- Use `issue-brief` when readers need a timeline, numeric comparisons, the decision process,
  both sides, and instructions for participating.
- Use [`answer-page`](../answer-page/SKILL.md) when the primary need is where the candidate
  stands on one voter question.

## Inputs and output

- Reads `campaign/positioning.md`, `campaign/district-issues.md`, and cited primary records.
- Uses [`reference/local-agenda-systems.md`](../../reference/local-agenda-systems.md) for record
  retrieval.
- Writes from
  [`campaign-template/briefs/_template.md`](../../campaign-template/briefs/_template.md).

## Manual procedure

1. Open `campaign/positioning.md`. If `approved_by_candidate` is not `true`, stop with
   `[POSITIONING NOT APPROVED — obtain explicit candidate approval]`.
2. Narrow the issue to one decision and one decision-making body. Split broader requests.
3. Check the contested-space survey in `district-issues.md`. Write down the specific
   information gap the brief will fill. If existing sources already cover the issue well and no
   concrete gap remains, stop and name those sources. Use `answer-page` if the underlying need
   is candidate positioning.
4. Name three real people or organizations unlikely to support the candidate and the concrete
   use each should get from the brief.
5. Create the brief from the template. Immediately after frontmatter, record:
   `<!-- Usefulness test: [person — concrete use]; [person — concrete use]; [person — concrete use] -->`
   Keep this comment through approval and remove it during the human publishing pass.
6. Follow [`reference/local-agenda-systems.md`](../../reference/local-agenda-systems.md) to
   retrieve the agenda, packet, minutes, roll call, ordinance or resolution, budget records,
   relevant docket filings, and any needed public-records response. Record URL and retrieval
   date for each.
7. If records are missing, file a request for named documents and record the agency and filing
   date in `## What is still unknown`.
8. Write `## The short version` with what happened, who decides, the material cost or scale,
   and the next known event.
9. Build `## How we got here` as a chronological table. Take votes and dates from primary
   records.
10. Build `## The numbers` as an honest comparison with neighboring jurisdictions, prior years,
    or a relevant state benchmark. Source each cell.
11. Write `## Who decides what happens next` with the body, members, next meeting date and
    location, public-comment method, and deadline.
12. Write each side's strongest case in `## The arguments`. Use a cited real advocate where
    possible and include shared ground.
13. Handle `## Where [CANDIDATE] stands`:
    - If the topic appears in `## No position yet`, use
      `[NO POSITION YET — ask the candidate: <specific question from the table>]`.
    - If no position of record exists, use
      `[NO POSITION OF RECORD — run positioning-builder or obtain candidate approval]`.
    - Otherwise, summarize only the approved position of record and keep it shorter than the
      factual reference sections.
14. In `## What is still unknown`, list pending records and unresolved facts. For each live
    decision, add
    `[FOLLOW UP YYYY-MM-DD — verify <decision or record> and update this brief]`.
    This dated artifact entry replaces an unsupported claim that a reminder was created.
15. Complete `## Sources`. Set `sources_count` to all sources and
    `primary_records_count` only to actual records, not reporting about them.
16. Source factual claims inline as
    `claim ([source](url), retrieved YYYY-MM-DD)`.
17. Temporarily remove the byline and candidate-position section. Confirm the remaining brief
    is still useful to each of the three named non-supporters.
18. Set `status: draft`, leave `published_url` empty, and show the complete artifact to the
    candidate or authorized human.
19. After explicit approval, set `status: candidate-approved`.
20. Hand the approved file and destination instructions to a human. The human publishes it and
    returns the final public URL.
21. Remove the internal usefulness-test comment, put the URL in `published_url`, and only then
    set `status: published`.

## Manual checklist

- [ ] Positioning approval, narrow scope, and contested-space gap were checked.
- [ ] Three non-supporters and their concrete uses are recorded in the specified comment.
- [ ] Timeline events, comparisons, participation details, and arguments are sourced.
- [ ] Every factual claim has an inline source and retrieval date.
- [ ] `primary_records_count` counts records rather than articles.
- [ ] The position section uses the approved position or the required marker.
- [ ] Every live decision has a dated `[FOLLOW UP ...]` entry.
- [ ] The brief passes the delete test without its byline and position section.
- [ ] `date_modified` changes only after substantive edits.
- [ ] A human supplied `published_url` before status became `published`.
