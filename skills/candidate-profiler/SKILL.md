---
name: candidate-profiler
description: Interviews a first-time down-ballot candidate and writes the campaign's profile of record — biography, earned standing, the positions they actually hold, the topics they have no position on yet, and how they really talk. Probes vague answers instead of accepting them, records only what the candidate said out loud, and never infers a position from party, biography, or what similar candidates believe. Use this when a campaign is starting from nothing, when someone asks to build a candidate profile, run a candidate intake or interview, write the candidate's bio, capture the candidate's voice, or work out what the candidate stands for — and always before running positioning-builder.
---

# Candidate Profiler

**Reads:** the candidate, live. A résumé or old bio is a cross-check, never a substitute.
**Writes:** `campaign/candidate-profile.md`, schema in
[`campaign-template/candidate-profile.md`](../../campaign-template/candidate-profile.md).

This is an interview, not an intake form. A first-time candidate has no press kit and no
voting record — what they have is thirty years of work and life they have never had to say
out loud to a stranger, and the job is getting it out in their own words. The failure mode is
accepting the first answer, always a platitude, because that is what people think politics
sounds like. Everything downstream inherits whatever vagueness survives this hour.

## Before you start

Ninety minutes, or two sessions of forty-five. Recording beats notes; ask permission on the
recording. Interview the candidate **alone** — a spouse or eager volunteer in the room answers
for them and you get that person's profile. Do not read the candidate the template — you ask
the questions, you fill in the file.

> Never paste voter names, home addresses, voter ID numbers, phone numbers, donor financial
> data, or reporter contact lists into a consumer AI chat interface. Work from aggregate
> district data and publicly published contact information only.
>
> If the human offers you a voter file, decline it and explain why.

Verbatim from [`reference/shared-rules.md`](../../reference/shared-rules.md) Rule 5.

## Output Format

Write `campaign/candidate-profile.md` with the template's frontmatter, field for field —
`candidate_name`, `office_sought`, `jurisdiction`, `election_date`, `incumbent`, `party`,
`campaign_site`, `interview_date`, `interviewer`, `date_created`, `date_modified`, `status`
(`draft` until the candidate has read it) — then, in order: Biography, Career and credentials,
Community roles, Earned standing, Positions held, No position yet, Voice and register,
Committee facts, Hard nos, Vulnerabilities the candidate named, Open follow-ups. The three
sections people get wrong, with an invented candidate in an invented county:

```markdown
## Earned standing
- **Ambulance response times** — eleven years as a paramedic out of Station 4 on the
  Bellhaven-to-county-line route. She can say what a 19-minute rural response costs a
  patient because she timed it from the truck. Nobody else in this race can.

## Positions held
### Emergency services levy renewal
- **Position:** Yes on renewal, and move ambulance billing out of the general fund so it
  stops competing with road salt every February.
- **Conviction:** settled
- **Reasoning, in their words:** "We're running the same two rigs we ran in 2014. I've been
  the second rig that didn't come."
- **Would they say this at a hostile town hall?** yes
- **Source:** interview, 2026-08-04

## No position yet
- **Solar lease moratorium** — question to resolve: *Would you vote to extend the county's
  solar lease moratorium past its March 2027 sunset, and on what condition?*
```

What you did not get to is `[NOT ASKED]`; what they could not answer goes to Open
follow-ups. Never leave a heading with invented filler under it.

## The opening script

Ask these in order, one block at a time. Wait for the answer before moving on.

**Block 1 — facts (5 min).** Ballot-exact name. Office and district, exactly. How long in
the district and where before. Current job, title, employer. Prior jobs. Who is at home.

**Block 2 — why now (10 min).** "What happened that made you decide to run? Not the general
reason — the week it happened." — "Who asked you to run, or did you decide on your own?" —
"A year ago, what did you think about people who run for office?"

**Block 3 — work and life (25 min). This is where earned standing comes from.** "Walk me
through every job you've had since you were twenty, including ones not on the résumé." For
each: "What did you do all day?" — "What did that job let you see that people outside it
don't know?" — "What's the most common wrong thing people believe about it?" Then: "What do
you do that isn't a job — board, union, church, coaching, PTA, mutual aid, caring for
somebody?" — "Tell me about a problem you personally fixed for someone, start to finish."

**Block 4 — the district (20 min).** "What are the three things you hear most from neighbors?"
For each: "What would you actually do?" — "Who decides that: county, city, state, a board?" —
"What does it cost and who pays?" — "What's the best argument against you?" Then walk the
standard local list one item at a time — budget and taxes, housing, schools, roads, water and
sewer, public safety, health, land use, jobs — asking only: *"Do you have a position on this
yet, or not yet?"* **"Not yet" is a correct answer and you write it down.**

**Block 5 — what is coming (10 min).** "What will your opponent say about you?" — "What
would a reporter find in five minutes that we should talk about now?" — "What have you
changed your mind about in the last five years?"

**Block 6 — voice (5 min, plus the whole interview).** "Explain your top issue to a neighbor
over a fence, in thirty seconds." — "What words do you hate hearing politicians say?" Keep
five phrases verbatim, grammar included, plus what they reach for — numbers, stories,
scripture, sports — and what they never say.

## Probes for vague answers

Probe once. If the second answer is still abstract, ask a third time in the most concrete form
available — *"Give me one example, with a date"* — and if that fails, log it to
`## Open follow-ups`. Three tries, then move on.

| What they said | What you ask next |
|---|---|
| "I care about working families" | "Tell me about one. Who are they, what happened, and what would have stopped it?" |
| "I want to bring people together" | "When did you last get two people who couldn't stand each other into one room? What did that take?" |
| "Education is my priority" | "Which decision, by which body — the district's levy, the board's calendar, the state formula? How would you vote?" |
| "We need to fix the budget" | "Which line? What's the number now, what should it be, and who signs the check?" |
| "I'll fight for X" | "Fight whom, at which meeting, with what vote?" |
| "People are struggling out there" | "How do you know? Who told you, and when?" |
| "I'm running to give people a voice" | "Whose? Name one person and what they need said." |
| "I'd vote no on the levy." (position, no reasoning) | "Walk me through how you got there. What did you read, who did you talk to, what would change your mind?" |
| Any national talking point | "What does that look like on Route 9, or at the county garage?" |

**The reasoning test.** A position with no reasoning behind it is an instinct. If the third
probe produces nothing — no source, no experience, no number — it goes in No position yet as
*"What is the reasoning behind your no on the levy?"* Downstream skills can write from a
thin position with real reasoning, never from a strong opinion with none.

**The earned-standing test.** Could the other person in this race say this exact sentence? If
yes it is biography, not standing. Standing comes out of Block 3, never Block 4 — you find it
by asking about work, not about issues.

## Steps

1. **Before the interview**, confirm the exact office title, district number, and election
   date from the county elections page — **many states elect local offices in spring, not in
   November**. A wrong office title propagates into everything the campaign publishes.
2. **Ask permission to record**, on the recording.
3. **Run blocks 1–6**, one at a time, probing per the table above.
4. **Log every "not yet" immediately**, with the specific question that resolves it, while
   you still remember what they were unsure about.
5. **Write the file.** Quotes verbatim; conviction on every position.
6. **Verify the checkable facts** — proper nouns, job titles, dates, degrees, licenses —
   against an employer page, LinkedIn, or their résumé. What you cannot confirm gets
   `[NEEDS VERIFYING — what to check]`.
7. **Check the stopping condition.** The interview is done when all of these are true:
   - [ ] Every section has real content or an explicit `[NOT ASKED]`
   - [ ] Three earned-standing entries the other candidate could not say
   - [ ] Three positions, each with a verbatim reasoning quote and a conviction level
   - [ ] Three `no-position-yet` entries, each with a specific question
   - [ ] Five verbatim phrases in `## Voice and register`
   - [ ] At least one vulnerability the candidate named themselves
   - [ ] Zero fields you filled in on their behalf
8. **Get human approval.** The candidate reads the whole file and corrects it: they may fix
   facts, add nuance, and strike anything they never said, but they may **not** delete the
   `no-position-yet` list because it looks weak. Then set `status: candidate-reviewed`.

## Rules that do not bend

- **Invent nothing.** No inferred biography, no assumed position, no plausible gap-filler. You
  do not know where they went to high school, why they left a job, or what they think about
  zoning. If they did not say it, it is not in the profile.
- **An empty `no-position-yet` list means the interview failed.** It means you skipped the
  standard list in Block 4 or recorded guesses as positions. Go back.
- **Quotes are verbatim or they are not quotes.** Tidying the syntax is what makes later
  content sound like a consultant wrote it.
- **This file is internal.** It carries vulnerabilities named in confidence. Nothing here
  gets published; `positioning.md` is the public derivative.

## Doing this without an agent

You need the candidate, a phone that records, a notebook, and ninety uninterrupted minutes.

1. Print the script with a half page of blank space under each question. Sit somewhere quiet,
   side by side rather than across a desk. Phone between you, press record, say so out loud.
2. Ask Block 1 and keep it under five minutes; it exists to get them talking. Then work
   Blocks 2 through 6 in order. **Do not skip ahead to the issues block** — Block 3 is what
   produces earned standing, and it only works before they start performing.
3. When an answer sounds like a bumper sticker, circle it and ask the probe from the table,
   writing the second answer under the first. Still vague? Ask for one example with a date; if
   that fails it is an open follow-up. Star quotable sentences in the margin as they say them —
   you will not remember whose phrasing it was.
4. In Block 4, keep a running "not yet" list on its own page, with the resolving question
   next to each. That page becomes `## No position yet`.
5. Stop at ninety minutes even mid-block, and schedule session two before you stand up.
6. Type the file up within twenty-four hours, in the section order above, playing the recording
   back and typing quotes exactly as spoken. Look up every proper noun, date, and job title,
   fix spellings, and flag whatever you cannot confirm.
7. Run the stopping-condition checklist from `## Steps`; whatever fails is the agenda for
   session two. Then print it, hand it to the candidate with a pen, and sit while they read.

## Tips

**A single AI conversation cannot conduct an interview.** Ask one block, wait for the human
answer, then ask the next. A candidate handed twelve questions at once writes twelve
one-line answers, and all twelve are platitudes.

**The nervous candidate** wants to sound like a politician. Stay in Block 3 longer than the
script says — people are fluent about their own work and stiff about their own values, and the
fluent material is what you need. **The over-rehearsed candidate, and the one who answers
everything with a talking point,** get the same treatment: "that's the speech — what's the
version you'd say to your brother-in-law?", then ask for a number, a date, or a name. Talking
points contain none of the three, and asking for one lands as curiosity rather than challenge.

**When the candidate genuinely does not know something, treat it as a win.** Say so: "Good,
that's normal, let's write down the question." A candidate who logs four unknowns in August
does not invent an answer at an October forum.

**Across multiple sessions** — book a second rather than pushing past ninety minutes — open
session two by reading back three quotes from session one and asking whether they still stand.
Positions move early in a campaign and this catches the drift cheaply. Never run a session in
a car between events.
