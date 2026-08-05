# Positioning Builder

**Category:** Content & Comms

Builds `campaign/positioning.md`, the campaign-message contract used by downstream writing
skills. It selects evidence-backed topics to own, records settled positions, and preserves
unresolved questions without inference.

## Inputs and output

- Reads `campaign/candidate-profile.md`, `campaign/district-issues.md`, and
  `campaign/district-media-map.md`.
- Writes `campaign/positioning.md` from
  [`campaign-template/positioning.md`](../../campaign-template/positioning.md).
- Requires explicit candidate or authorized-human approval before
  `approved_by_candidate` may become `true`.

## Core contract

- The canonical unresolved-position heading is `## No position yet`.
- Existing unresolved rows are copied unchanged. They are resolved only by an explicit candidate
  answer, never by inference.
- An owned topic may remain unresolved.
- Every owned topic not in `## No position yet` needs a position of record.
- Necessary positions of record may be included even when the campaign does not own the topic.
- `answer-page` stops on an unresolved position; `issue-brief` may still publish factual
  reference material while withholding the position.

## Manual procedure

1. Print or open all three input files and the positioning template. Read them completely before
   evaluating topics.
2. Make one card or working-note block for each plausible topic.
3. On each card, record:
   - **Salience:** the strongest local record, including a date, count, cost, or vote and its
     citation.
   - **Earned standing:** the specific candidate experience that supports speaking on the topic,
     cited to the profile.
   - **Contested space:** who already covers the topic and the specific gap left open, cited to
     the issue scan or media map.
4. Exclude any topic missing a supported bar. If fewer than three qualify, keep the smaller set
   and record the limitation.
5. For each remaining topic, write the strongest honest argument for excluding it. Select no
   more than five. Add every excluded topic to `### Topics considered and rejected` with its
   reason.
6. Copy the profile's unresolved-position table under the exact heading
   `## No position yet`. Preserve every row and question word for word. Add rows for new open
   questions discovered during review.
7. For each owned topic:
   - if it appears in `## No position yet`, leave it unresolved and do not invent a position;
   - otherwise, write a matching `## Positions of record` entry.
8. Add positions of record for non-owned topics the campaign still must answer. Each entry
   includes the one-sentence position, specific action and decision-making body, cited evidence
   with retrieval dates, uncertainty, strongest objection and response, conviction, and
   approval state.
9. Fill the message, voice, boilerplate, and hard-nos sections. Verify ballot name, exact office
   phrasing, required disclaimer, committee legal name, truthful `same_as` URLs, pronunciation,
   and 25/50/100-word bios.
10. Use `[NEEDS SOURCE — <what to look up>]` for a known source gap. Do not omit required fields.
11. Review the complete file with the candidate topic by topic. Ask for an explicit approval or
    requested changes.
12. Set `approved_by_candidate: true` and `approved_date` only when that approval is explicitly
    given in the current interaction. Otherwise leave `approved_by_candidate: false`.

## Manual verification

- [ ] Every owned topic has all three bars and a recorded case against it.
- [ ] Every rejected topic has a reason.
- [ ] Every original unresolved row remains unless the candidate explicitly answered it.
- [ ] Every owned topic absent from `## No position yet` has a position of record.
- [ ] Necessary non-owned positions are included.
- [ ] All downstream identity, voice, legal, and boilerplate fields are complete.
- [ ] Approval is `false` unless explicitly confirmed in the current interaction.
