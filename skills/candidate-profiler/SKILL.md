---
name: candidate-profiler
description: Interviews a first-time down-ballot candidate and writes the campaign's profile of record — biography, earned standing, stated and unresolved positions, voice, committee facts, hard nos, and candidate-named vulnerabilities. Probes vague answers, records only what the candidate said or a source verifies, and never infers a position. Use for candidate intake, biography, voice, or positions, and before positioning-builder.
---

# Candidate Profiler

**Reads:** the candidate, live; the campaign's existing frontmatter for `election_date`; and
public records used to verify checkable facts. A résumé or old bio is a cross-check, not a
substitute for the interview.
**Writes:** `campaign/candidate-profile.md`, using
[`campaign-template/candidate-profile.md`](../../campaign-template/candidate-profile.md).

## Before you start

Plan for ninety minutes or two sessions. Ask permission before recording. Interview the
candidate alone, ask one interview block per turn, and never send the full question set at once.

Read `election_date` from the campaign's existing frontmatter; never assume or derive it.
Confirm the election name and date against the county clerk/elections office or Secretary of
State before using it. If official sources conflict, stop date-dependent work and log the
conflict in `## Open follow-ups`.

> Never paste voter names, home addresses, voter ID numbers, phone numbers, donor financial
> data, or reporter contact lists into a consumer AI chat interface. Work from aggregate
> district data and publicly published work-contact information only.
>
> If the human offers a voter file, decline it and explain why.

## Output Format

Write `campaign/candidate-profile.md` with the template's frontmatter field for field:
`candidate_name`, `office_sought`, `jurisdiction`, confirmed `election_date`, `incumbent`,
`party`, `campaign_site`, `interview_date`, `interviewer`, `date_created`, `date_modified`, and
`status` (`draft` until candidate review).

Keep the template's section order. Under `## Biography`, record:

`Election date verified: [election name], [ISO date] ([official source], retrieved [date]).`

For the sections most often mishandled:

- **Earned standing:** record a specific experience that the other candidate could not claim.
- **Positions held:** include concrete action, conviction, verbatim reasoning, whether they
  would say it at a hostile town hall, and source.
- **No position yet:** include the topic and the specific question needed to resolve it.
- **Committee facts:** copy the committee legal name, committee ID, required disclaimer
  verbatim, and verification source. Flag, never guess, missing details.
- **Hard nos:** record only explicit refusals, verbatim where possible.

What was not reached is `[NOT ASKED]`. An asked question with no usable answer goes in
`## Open follow-ups`. Never add filler to make a section look complete.

## Interview blocks

Ask these in order. In an agent conversation, ask **one block per turn**, wait for the full
answer, run needed probes, and only then offer the next block.

**Block 1 — facts.** Ballot-exact name; exact office and district; time in the district;
current and prior work; household. Ask for the committee's exact legal name and ID as filed,
the required disclaimer text, and the filing or official rule that verifies each. Ask: "What
will this campaign never do, say, or support?" Record those answers as hard nos.

**Block 2 — why now.** "What happened that made you decide to run? Not the general reason —
the week it happened." "Who asked you to run, or did you decide on your own?" "A year ago,
what did you think about people who run for office?"

**Block 3 — work and life.** Walk through jobs, including those not on the résumé. For each:
what did you do, what did it let you see, and what do outsiders get wrong? Ask about boards,
unions, congregations, coaching, PTA, mutual aid, and caregiving. Ask for a problem they
personally fixed, start to finish. Earned standing comes from this evidence, not issue claims.

**Block 4 — the district.** Ask what they hear from neighbors. For each topic: what would you
do, which body decides, what does it cost and who pays, and what is the best argument against
you? Walk budget and taxes, housing, schools, roads, water and sewer, public safety, health,
land use, and jobs one at a time, asking whether they have a position yet. "Not yet" is valid.

**Block 5 — what is coming.** "What will your opponent say about you?" "What would a reporter
find in five minutes that we should discuss now?" "What have you changed your mind about in
the last five years?"

**Block 6 — voice.** "Explain your top issue to a neighbor over a fence, in thirty seconds."
"What words do you hate hearing politicians say?" Preserve any distinctive phrases verbatim
and note whether they reach for numbers, stories, scripture, sports, or humor. Do not pad to a
phrase count.

## Probes and classification

Probe an abstract answer once, then ask for one concrete example with a date. After three total
attempts, log the unresolved question and move on. Useful forms include:

- "Who specifically, what happened, and what would have prevented it?"
- "Which decision, by which body, and how would you vote?"
- "Which line, what is the number now, what should it be, and who signs the check?"
- "What does that look like on this district's road, school, or public counter?"
- For a position without reasoning: "What did you read, who did you ask, and what could change
  your mind?"

A position without source, experience, number, or other real reasoning is not usable. Put the
resolving question in `No position yet`. Earned standing passes only if the opponent could not
truthfully make the same claim.

## Steps

1. Read `election_date` from campaign frontmatter. Verify the exact office, district, election
   name, and date with the clerk/elections office or Secretary of State; record what was used.
2. Ask permission to record.
3. Run Blocks 1–6 one block per turn, using the probes above.
4. Log unknowns and resolving questions as they arise.
5. Draft the file with verbatim quotes and a conviction level for every stated position.
6. Verify proper nouns, dates, credentials, committee facts, and disclaimer text against
   authoritative records. Mark unresolved claims `[NEEDS VERIFYING — what to check]`.
7. Stop only when:
   - [ ] Every section has evidence, `[NOT ASKED]`, `[NONE NAMED]`, or a specific follow-up
   - [ ] Every experience raised was tested for earned standing; unsupported entries were cut
   - [ ] Every position raised has reasoning and conviction or is listed as unresolved
   - [ ] Every unknown raised has a specific resolving question
   - [ ] Voice contains observed language only, with no quota-driven filler
   - [ ] Committee legal name, ID, and disclaimer are verified or explicitly flagged
   - [ ] Election name, confirmed date, official source, and retrieval date are recorded
   - [ ] Zero facts or positions were supplied on the candidate's behalf
8. Have the candidate review the whole file. They may correct facts, add nuance, and remove
   words they did not say. An unresolved position may be removed only after they answer its
   resolving question. Then set `status: candidate-reviewed`.

## Rules that do not bend

- **Invent nothing.** Do not infer biography, motivation, position, committee data, or
  disclaimer language.
- **Do not force a nonempty section.** Empty earned-standing, position, unknown-position,
  hard-no, voice, or vulnerability sections are valid only when the relevant questions were
  asked and the result is explicit. Never pad to a quota.
- **Quotes are verbatim or are not quotes.**
- **This file is internal.** It may contain vulnerabilities named in confidence.
  `positioning-builder` carries approved material, committee facts, hard nos, and every
  unresolved position into `campaign/positioning.md`. Downstream writing skills read
  `positioning.md`, never `candidate-profile.md`.

## Doing this without an agent

For the complete no-agent procedure, see [`README.md`](README.md#manual-procedure). The safety
rules, output contract, interview blocks, probes, and stopping condition above still apply.

## Tips

When an interview spans sessions, begin the resumed session by reading back the prior
positions and asking whether they still stand. Record changes rather than silently replacing
the earlier answer.
