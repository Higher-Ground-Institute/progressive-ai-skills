# Candidate Profiler

**Category:** Research & Data

Runs a structured interview with a candidate and turns it into `campaign/candidate-profile.md` — the profile of record every other campaign skill builds on. It is an interview skill, not a document-ingestion skill: the input is a person talking, and the core competence is asking the follow-up question that turns "I care about working families" into something a campaign can actually publish.

## Who it's for

A first-time, down-ballot candidate — state legislature, county commission, school board — with no staff, no consultant, and no press kit. In practice the person running the skill is the candidate's most organized volunteer, a spouse, or a part-time manager who has never conducted an interview before. Anyone at a campaign, party committee, or candidate-training program who needs to get a new candidate's biography, standing, positions, and voice out of their head and onto paper can use it.

## What it does

The input is a ninety-minute conversation. The output is one Markdown file with nine sections: biography, career and credentials, community roles, earned standing, positions held, no position yet, voice and register, vulnerabilities the candidate named, and open follow-ups.

Three parts of that output carry most of the value:

1. **Earned standing** — what this person's actual work and life have earned them the right to talk about. A paramedic can talk about ambulance response times because she has timed them from the truck. This section comes out of questions about jobs and volunteering, never out of questions about issues, and the test for every entry is whether the other candidate in the race could say the same sentence.
2. **The `no-position-yet` list** — every topic where the candidate does not have a settled position, each paired with the specific question that would resolve it. Every downstream skill reads this list and refuses to write a position on anything in it. An empty list means the interview failed.
3. **Voice** — verbatim phrases, words the candidate avoids, register. Without it, later content defaults to a national-consultant voice no local voter has ever heard a neighbor use.

The skill ships a real opening script — six blocks of actual questions in order — and a probe table mapping the platitudes candidates reach for to the follow-up that breaks them open. It refuses the first vague answer, probes up to three times, and logs what it cannot resolve instead of inventing it.

## Prerequisites

- **The candidate, alone, for ninety minutes.** Two forty-five minute sessions also work. A spouse or volunteer in the room will answer for them.
- **A recorder** — a phone voice memo is fine. Ask permission on the recording.
- **A campaign folder.** Copy [`campaign-template/`](../../campaign-template/) to start one.
- **No AI tool required.** `## Doing this without an agent` in the SKILL.md is the complete manual procedure: what to print, how to take notes, how to run the probes on paper.

## How to use it

Run it once at campaign kickoff, before `positioning-builder` and before anyone writes a word of public content. Say something like "interview me for my candidate profile" or "help me figure out what I actually stand for" and the skill takes over.

**Drive it turn by turn.** A single AI conversation cannot conduct an interview. The skill asks one block, waits for the real answer, probes if the answer is vague, and only then moves on. A candidate handed twelve questions at once writes twelve one-line answers, all of them platitudes.

Revisit the file when positions move — realistically once or twice more before Election Day, plus whenever the `no-position-yet` list gets resolved.

## Tips and edge cases

- **The over-rehearsed candidate** answers everything with the stump speech. The fix in the skill: "That's the speech. What's the version you'd say to your brother-in-law?" followed by a request for a number, a date, or a name.
- **The nervous candidate** stiffens on values questions and relaxes on work questions. Stay in the work-and-life block longer; that block is where earned standing lives anyway.
- **"I don't know" is a passing answer.** The skill treats it as a win, logs it with the resolving question, and moves on. A candidate who names four unknowns in August does not invent one at an October forum.
- **The skill invents nothing.** No inferred biography, no assumed position, no filled-in gap. Unverifiable facts get marked `[NEEDS VERIFYING]` rather than smoothed over.
- **No voter data goes near a chat tool.** The skill declines a voter file and says why.
- **The file is internal.** It records vulnerabilities the candidate named in confidence. `positioning.md` is the artifact that faces the public.

## Example

Delia Fenn is running for the Marrow County Commission. Asked about her priorities, she says she cares about public safety. The skill does not record a position. It asks what she did all day as a paramedic, what that job let her see that outsiders do not, and what people get wrong about it — and comes back with an earned-standing entry about rural ambulance response times she has personally timed, a settled position on the emergency services levy with a verbatim quote behind it, and a `no-position-yet` entry on the solar lease moratorium reading: *Would you vote to extend the moratorium past its March 2027 sunset, and on what condition?*

She reads the draft with a pen, corrects two job dates, and marks it `candidate-reviewed`.

## What it has been exercised against

Stated precisely, because a repo about not fabricating claims should not fabricate its own test history.

- **Two eval cases** in [`evals/evals.json`](evals/evals.json), runnable by `npx agent-skills-eval`: the platitude case, where "I care about working families" has to produce a follow-up question rather than a recorded position, and a thin-transcript case, where the profile has to show how little the interview actually got instead of filling the gaps. Both run against an invented candidate in an invented county.
- **Structural validation** on every pull request via `scripts/validate_skills.py`, which enforces the agentskills.io spec plus this repo's conventions.

**Not yet done:** the eval suite has not been run against a live model, so no assertion here has an observed pass rate, and no real campaign has used this in an interview. The manual procedure in `## Doing this without an agent` is written to be followable with a printed script and a notebook, but nobody has walked it end to end. If you run this on a real candidate, please open an issue and say what broke.
