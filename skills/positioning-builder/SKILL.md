---
name: positioning-builder
description: Builds campaign/positioning.md from the candidate profile, district issue scan, and media map. Selects evidence-backed topics to own, records settled positions, preserves unresolved questions, and prepares the campaign's message contract for explicit candidate approval. Use when a campaign needs its message, issue priorities, positions of record, or the required handoff before writing content.
---

# Positioning Builder

**Reads:** `campaign/candidate-profile.md`, `campaign/district-issues.md`,
`campaign/district-media-map.md` — all three required.
**Writes:** `campaign/positioning.md`, using
[`campaign-template/positioning.md`](../../campaign-template/positioning.md).

`campaign/positioning.md` is the only campaign-message source downstream writing skills use.
Do not make downstream skills reopen `candidate-profile.md`.

## Output Format

Follow [`campaign-template/positioning.md`](../../campaign-template/positioning.md), including
frontmatter and the canonical sections `## Message`, `## Topics to own`,
`## Positions of record`, `## No position yet`, `## Voice`, `## Boilerplate`, and
`## Hard nos`.

## Topic selection

Select three to five topics to own. Each requires cited evidence for:

1. **Salience:** a local record showing people care, such as a vote, hearing, cost change, or
   participation count.
2. **Earned standing:** a specific fact from `candidate-profile.md` connecting the candidate to
   the topic.
3. **Contested space:** a documented information or representation gap, checked against
   `district-issues.md` and `district-media-map.md`.

Record the strongest case against each selected topic. Put rejected topics and reasons in
`### Topics considered and rejected`. If fewer than three topics clear all bars, keep the
smaller set and document why.

## Position contract

Use the canonical heading `## No position yet`.

- Copy every existing row into that section unchanged. You may add a row with a specific open
  question. Never remove or resolve a row by inference.
- An owned topic may remain in `## No position yet`. Ownership governs research and publishing
  priority; it does not imply a settled position.
- For every owned topic **not** in `## No position yet`, require a matching entry in
  `## Positions of record`.
- Add positions of record for necessary, non-owned topics when the campaign needs a defensible
  answer. `## Positions of record` may therefore contain more topics than `topics_to_own`.
- Resolve a row only after the candidate explicitly answers its question. Move the answer to
  `## Positions of record` and remove the row only on that basis.

Downstream handling is skill-specific: `answer-page` stops on an unresolved topic;
`issue-brief` may publish factual reference sections while withholding the candidate position.
Do not claim that all writing skills stop.

## Hard stops

- Missing any required input: stop and name the missing file.
- Unsupported topic bar: do not list that topic in `topics_to_own`.
- Inferred candidate position: stop and add or preserve a `## No position yet` row.

## Steps

1. Read all three inputs completely.
2. List plausible topics and evaluate each against the three bars with citations.
3. Record the case against each viable topic; select up to five and record all rejections.
4. Copy `## No position yet` forward unchanged, then add newly surfaced open questions.
5. Write `## Positions of record` for settled owned topics and necessary non-owned topics.
   Include the position, action, sourced evidence and retrieval dates, uncertainty, strongest
   objection and response, conviction, and approval state.
6. Fill `## Message`, `## Voice`, `## Boilerplate`, and `## Hard nos`.
7. Verify:
   - every `topics_to_own` slug has a matching topic section;
   - every owned topic absent from `## No position yet` has a position of record;
   - every original unresolved row remains intact unless explicitly answered by the candidate;
   - ballot name, office, disclaimer, committee legal name, truthful `same_as` URLs,
     pronunciation, 25/50/100-word bios, voice, and hard nos are present.
8. Use `[NEEDS SOURCE — <what to look up>]` for a known sourcing gap; do not omit the field.

## Candidate approval

Set `approved_by_candidate: false` by default. An agent may set it to `true` and fill
`approved_date` only after the candidate or authorized human explicitly confirms approval in
the current interaction. Approval from a prior file, inference, or silence is insufficient.
Until then, leave it `false`.

## Doing this without an agent

For the full non-agent workflow, see [`README.md`](README.md#manual-procedure).

## Tips

- Keep positions of record for necessary non-owned topics.
- Treat an owned unresolved topic as valid; research can proceed without inventing a stance.
