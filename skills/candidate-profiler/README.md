# Candidate Profiler

**Category:** Research & Data

Runs a structured candidate interview and writes `campaign/candidate-profile.md`: biography,
earned standing, stated and unresolved positions, voice, committee facts, hard nos, and
candidate-named vulnerabilities.

## Who it's for

First-time down-ballot candidates and the volunteer or manager conducting intake before
`positioning-builder`.

## Prerequisites

- The candidate, alone, for about ninety minutes or two sessions
- A recorder, with permission obtained before recording
- A campaign folder copied from [`campaign-template/`](../../campaign-template/)
- Campaign frontmatter containing `election_date`
- Access to the clerk/elections office or Secretary of State record used to confirm that date

## How to use it

Ask to build or update the candidate profile. The skill asks one interview block per turn,
probes vague answers, verifies checkable facts, and drafts the profile for candidate review.
Run it before `positioning-builder`; downstream writing reads `positioning.md`, not this
internal interview record.

## Manual procedure

You need the candidate, a recorder, a notebook, the campaign frontmatter, and the template.

1. Read `election_date` from campaign frontmatter. Verify the exact office, district, election
   name, and date against the county clerk/elections office or Secretary of State. Write down
   the official URL, retrieval date, election name, and confirmed ISO date. Resolve conflicts
   before calculating or stating deadlines.
2. Print the interview blocks and leave space under every question. Meet somewhere private.
   Ask permission before recording and capture that permission on the recording.
3. Ask Blocks 1–6 in order, one block at a time. Do not skip the work-and-life block; it
   supplies the evidence for earned standing.
4. In Block 1, inspect the official committee filing and applicable disclaimer rule. Copy the
   committee legal name, committee ID, and required disclaimer exactly. Ask explicitly for
   things the campaign will never do, say, or support.
5. When an answer is abstract, ask a concrete follow-up. If needed, ask once more for an
   example with a date. After three total attempts, write the unresolved question down and
   continue.
6. Keep separate running lists for stated positions, unresolved positions and their resolving
   questions, hard nos, candidate-named vulnerabilities, and distinctive verbatim phrases.
   Do not add entries to meet a numerical target.
7. If the session reaches ninety minutes, stop and schedule another. Start the next session by
   reading back key statements and asking whether they still stand.
8. Draft `campaign/candidate-profile.md` within twenty-four hours. Transcribe quotes exactly.
   Verify proper nouns, dates, credentials, committee data, and disclaimer language; flag
   anything unresolved.
9. Apply the stopping checklist in `SKILL.md`. A short section is acceptable when it reflects
   the evidence; padding is not.
10. Give the complete draft to the candidate for review. Record corrections, preserve every
    unresolved position until its question is answered, then set `status: candidate-reviewed`.

Never put voter files, private addresses, personal phone numbers, donor financial data, or
reporter contact lists into a consumer AI chat.

## What it has been exercised against

- Two cases in [`evals/evals.json`](evals/evals.json): probing a platitude instead of recording
  it as a position, and preserving gaps in a thin transcript.
- Structural validation through `scripts/validate_skills.py`.

The eval suite has not been run against a live model, and the manual procedure has not been
validated in a real campaign interview.
