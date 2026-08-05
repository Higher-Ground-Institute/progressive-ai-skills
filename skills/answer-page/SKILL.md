---
name: answer-page
description: Writes one dated, sourced page answering a voter question from an approved position of record. Stops on unresolved or missing positions and routes research-first local explainers to issue-brief. Use when a campaign asks for a position page, issue-page answer, or a clear statement of where the candidate stands.
---

# Answer Page

**Reads:** `campaign/positioning.md` (required), plus `campaign/district-issues.md` for
supporting evidence.
**Writes:** `campaign/answers/<topic-slug>.md`.

One page answers one voter question from the campaign's approved message contract. Use
`campaign/positioning.md` as the only source of candidate message; do not reopen
`candidate-profile.md`.

## Routing

- Use `answer-page` when the primary need is a direct, attributable answer to where the
  candidate stands.
- Use `issue-brief` when the primary need is a neutral local reference: timeline, numbers,
  decision process, competing arguments, and public-participation instructions.
- Do not create separate answer pages for search-phrase variants of the same position. Offer
  one page covering the substantive question.

## Hard stops

Check in this order:

1. If `approved_by_candidate` is not `true`, output
   `[POSITIONING NOT APPROVED — obtain explicit candidate approval]` and stop.
2. If the topic appears under the canonical heading `## No position yet`, output
   `[NO POSITION YET — ask the candidate: <specific question from the table>]` and stop.
3. If the topic is absent from `## Positions of record`, output
   `[NO POSITION OF RECORD — run positioning-builder or obtain candidate approval]` and stop.

Never infer a position from party, biography, adjacent positions, or another candidate.

## Output Format

Write to `campaign/answers/<topic-slug>.md` using the structure in
[`campaign-template/answers/_template.md`](../../campaign-template/answers/_template.md):

Required sections, in this order: the answer paragraph (no heading), `## Why`,
`## What I would do`, `## What I don't know yet`, `## Sources`.

The first paragraph must answer the question. Source factual claims inline as
`claim ([source](url), retrieved YYYY-MM-DD)`.

## Steps

1. Confirm one concrete voter question and route to `issue-brief` if the requested product is
   primarily a factual explainer.
2. Run the three hard stops in order.
3. Pull the matching position from `## Positions of record`; do not exceed it.
4. Gather local evidence from `district-issues.md` and its primary records.
5. Draft the one-to-three-sentence answer, then `## Why`, `## What I would do`,
   `## What I don't know yet`, and `## Sources`.
6. Verify every number, quote, date, vote, bill number, and dollar amount has an inline source
   and retrieval date. Set `sources_count` to the source-table count.
7. Set `status: draft`, leave `published_url` empty, and show the full artifact to the candidate
   or authorized human.

## Lifecycle and publishing

The lifecycle is `draft` → `candidate-approved` → `published`.

- Move to `candidate-approved` only after explicit human approval of the complete page.
- Publishing is a human handoff. Give the human the approved file and destination instructions;
  do not post, submit, or upload it.
- After the human publishes, they supply the final public URL. Set `published_url` to that URL
  and then set `status: published`. Never mark published before both events occur.
- Change `date_modified` only for a substantive edit.

## Rules

- Copy factual claims and quotations exactly or use `[NEEDS SOURCE — <what to look up>]`.
- Use only the approved positioning entry and cited evidence for substantive claims.
- Attribute the page to the candidate.

## Doing this without an agent

For the full non-agent workflow and checklist, see
[`README.md`](README.md#manual-procedure).

## Tips

- If the requested page is mainly a timeline or process explainer, route to `issue-brief`.
- Keep qualifications and uncertainty exactly within the approved position of record.
