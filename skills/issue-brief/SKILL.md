---
name: issue-brief
description: Writes a dated, primary-record-based reference brief on one narrow local issue. Includes timeline, comparisons, participation guidance, competing arguments, and a separately gated candidate-position section. Use when a campaign needs a factual local explainer, timeline, rate or budget analysis, development brief, or reference useful beyond the candidate's supporters.
---

# Issue Brief

**Reads:** `campaign/positioning.md` (required) and `campaign/district-issues.md` (required),
plus the primary records those files cite.
**Writes:** `campaign/briefs/<topic-slug>.md`.

One narrow local issue, documented as a public reference rather than a position page.

## Routing

- Use `issue-brief` for a timeline, numbers, process, competing arguments, and participation
  instructions.
- Use `answer-page` when the primary need is a direct explanation of where the candidate stands
  on one voter question.

## Gates

Check before drafting:

1. **Approval:** if `approved_by_candidate` is not `true`, output
   `[POSITIONING NOT APPROVED — obtain explicit candidate approval]` and stop.
2. **Scope:** if the request covers multiple decisions or decision-making bodies, narrow or
   split it before drafting.
3. **Contested space:** read the contested-space survey in `district-issues.md`. Identify the
   specific public-information gap this brief fills. If existing sources already cover the
   issue well and no concrete gap exists, stop, name those sources, and recommend
   `answer-page` if the actual need is candidate positioning.

Use `campaign/positioning.md` as the only candidate-message source. Do not reopen
`candidate-profile.md`.

## Position handling

- If the topic appears under the canonical heading `## No position yet`, continue the factual
  brief but put
  `[NO POSITION YET — ask the candidate: <specific question from the table>]`
  in `## Where [CANDIDATE] stands`. Do not state or imply a position.
- If the topic is not unresolved but has no matching `## Positions of record` entry, continue
  the factual brief but put
  `[NO POSITION OF RECORD — run positioning-builder or obtain candidate approval]`
  in the position section.
- Otherwise, keep the candidate-position section short and within the approved position of
  record.

## Finding the primary records

Follow [`reference/local-agenda-systems.md`](../../reference/local-agenda-systems.md) for agenda
portals, packets, minutes, APIs, clerks, dockets, and records requests. Count actual records,
not links or articles, in `primary_records_count`.

## Output Format

Write to `campaign/briefs/<topic-slug>.md` using
[`campaign-template/briefs/_template.md`](../../campaign-template/briefs/_template.md):

Required sections in this order: `## The short version`, `## How we got here`, `## The numbers`,
`## Who decides what happens next`, `## The arguments`, `## Where [CANDIDATE] stands`,
`## What is still unknown`, `## Sources`.

## Steps

1. Run the approval, scope, and contested-space gates.
2. Before outlining, name three real non-supporters. Record them and the value each should get
   in an HTML comment immediately after frontmatter:
   `<!-- Usefulness test: [person — concrete use]; ... -->`.
   Keep the comment through candidate approval; remove it in the human publishing pass.
3. Retrieve primary records with URLs and retrieval dates.
4. Write the sourced timeline and honest numeric comparisons.
5. Write participation instructions: body, members, next meeting, location, comment method, and
   deadline.
6. Steelman both sides with cited advocates and state shared ground.
7. Apply the position-handling rules to `## Where [CANDIDATE] stands`.
8. List pending records and unresolved facts in `## What is still unknown`. For every live
   decision, add a dated artifact follow-up:
   `[FOLLOW UP YYYY-MM-DD — verify <decision or record> and update this brief]`.
   Do not claim to create a reminder.
9. Fill the source table and counts. Source factual claims inline as
   `claim ([source](url), retrieved YYYY-MM-DD)`.
10. Delete the candidate-position section and byline as a test. The remaining document must
    still work as a useful reference for the three named non-supporters.
11. Set `status: draft`, leave `published_url` empty, and present the complete artifact for
    explicit human approval.

## Lifecycle and publishing

The lifecycle is `draft` → `candidate-approved` → `published`.

- Move to `candidate-approved` only after explicit human approval of the complete brief.
- Publishing is a human handoff. Give the human the approved file and destination instructions;
  do not post, submit, or upload it.
- After the human publishes, they supply the final public URL. Set `published_url` to that URL
  and then set `status: published`.
- Change `date_modified` only for a substantive edit.

## Doing this without an agent

For the full non-agent workflow and checklist, see
[`README.md`](README.md#manual-procedure).

## Tips

- Keep the factual brief useful when the candidate-position section is removed.
- Record pending records and live decisions with dates instead of claiming a reminder exists.
