# Answer Page

**Category:** Content & Comms

Writes one dated, sourced page answering a concrete voter question from an approved position
of record.

## When to use it

- Use `answer-page` to explain where the candidate stands on one question.
- Use [`issue-brief`](../issue-brief/SKILL.md) when the main product is a factual local
  reference with a timeline, comparisons, process, competing arguments, and participation
  instructions.
- Use one page per substantive position, not one per search phrase.

## Inputs and output

- Reads `campaign/positioning.md` and `campaign/district-issues.md`.
- Writes `campaign/answers/<topic-slug>.md` from
  [`campaign-template/answers/_template.md`](../../campaign-template/answers/_template.md).

## Manual procedure

1. Turn the request into one question a voter would ask. If the request is for a broad
   research explainer, use `issue-brief`.
2. Open `campaign/positioning.md` and check these gates in order:
   - If `approved_by_candidate` is not `true`, stop with
     `[POSITIONING NOT APPROVED — obtain explicit candidate approval]`.
   - If the topic is in `## No position yet`, stop with
     `[NO POSITION YET — ask the candidate: <specific question from the table>]`.
   - If no matching entry exists in `## Positions of record`, stop with
     `[NO POSITION OF RECORD — run positioning-builder or obtain candidate approval]`.
3. Copy the approved position entry into working notes. Do not add a position from biography,
   party, neighboring positions, or personal assumptions.
4. Create `campaign/answers/<topic-slug>.md` from the template. Set `status: draft` and leave
   `published_url` empty.
5. Write the voter question as the title and heading. Answer it in the first paragraph in one
   to three sentences, including any qualification in the position of record.
6. Follow links in `district-issues.md` to primary records. Record each source URL and retrieval
   date.
7. Write `## Why` with local evidence. Every factual claim receives an inline source:
   `claim ([source](url), retrieved YYYY-MM-DD)`.
8. Write `## What I would do` with the action, decision-making body, and mechanism stated in
   positioning.
9. Write `## What I don't know yet` from the uncertainty in the position of record.
10. Complete `## Sources`, verify every link, and set `sources_count` to the table count.
11. Run the checklist below. Then show the entire draft to the candidate or authorized human
    and ask for explicit approval.
12. After explicit approval, set `status: candidate-approved`.
13. Hand the approved file and destination instructions to a human. The human publishes it and
    returns the final public URL.
14. Put that URL in `published_url`; only then set `status: published`.

## Manual checklist

- [ ] Positioning approval was checked first.
- [ ] The topic is absent from `## No position yet`.
- [ ] A matching position of record exists.
- [ ] The question is answered in the first paragraph.
- [ ] The page does not exceed or contradict the position of record.
- [ ] Every factual claim has an inline source and retrieval date.
- [ ] `## What I would do` names the body and mechanism.
- [ ] `## What I don't know yet` states real uncertainty from positioning.
- [ ] `sources_count` matches the source table.
- [ ] `date_modified` changes only after a substantive edit.
- [ ] Publication status is set only after a human supplies `published_url`.
