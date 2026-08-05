---
name: placement-writer
description: Renders an existing answer page or issue brief down to fit one publication venue — Ballotpedia Candidate Connection, Vote411, a state or county candidate statement, an endorsement questionnaire, a newspaper op-ed, or a letter to the editor — by reading a venue specification (limit and unit, audience, tone, submission method, deadline, cost, rules on naming opponents, formatting, editability after submission) and cutting framing before evidence. Never inflates a source that is already under the limit, reports a measured count rather than an estimate, enforces venue rules such as no bullets or no naming the opponent, and never submits anything: it returns exact submission instructions for a human. Use this when a campaign needs to fill out a voter guide, answer a questionnaire, submit a candidate statement, or fit a position into a word or character limit.
---

# Placement Writer

**Reads:** one approved `campaign/answers/<slug>.md` or `campaign/briefs/<slug>.md`, plus a
venue spec. Falls back to `campaign/positioning.md` for boilerplate and the required disclaimer.
**Writes:** `campaign/placements/<venue>-<topic>.md`.

**Write once, render many.** Ballotpedia, Vote411, state and county candidate statements,
endorsement questionnaires, op-eds, and letters to the editor are **venue configurations, not
separate skills**. One position of record per issue, fitted through a different aperture each
time. If you find yourself writing a new position because the venue felt different, stop — that
is how a campaign ends up with six slightly different answers in six voter guides.

## The venue spec

Fill all ten fields before drafting; drafting first and cutting later produces padded text that
loses evidence in the cut. **Limit and unit** (words, characters, or characters excluding spaces
— not interchangeable); **audience** (a League guide reader is not an endorsement committee);
**tone**; **submission method**; **deadline**, including whether a print deadline precedes the
online one; **cost** ("$0" is an answer, blank is not); **rules on naming opponents**, which
some venues prohibit outright; **formatting rules**, since bullets, bold, and links are often
stripped or banned; **editability after submission**, which sets how hard the approval step has
to be; and **who submits**, always a human name. A blank field is a research task, not a default
— see **When the venue is not in the table**, below.

## Before you write anything

**No source artifact, no placement.** This skill renders; it does not originate positions. If no
approved answer page or brief covers the topic, say so and run `answer-page` or `issue-brief`
first. If the venue asks about a topic on the `no-position-yet` list in `positioning.md`, answer
that item with `[NO POSITION YET — ask the candidate: <the specific question they need to
answer>]` and keep going through the rest of the form.

**If the source is shorter than the limit, do not inflate it.** Say so and stop: *"The answer
page is 180 words and the limit is 400. Submitting it as written. Adding 220 words means adding
adjectives."* Padding replaces evidence with intensifiers: under a 200-word limit, a 90-word
answer with a dollar figure, a date, and a decision beats a 200-word answer with a mood.

## Output Format

Write to `campaign/placements/<venue>-<topic>.md` using
[`campaign-template/placements/_template.md`](../../campaign-template/placements/_template.md):

```markdown
---
venue: "Ballotpedia Candidate Connection"
venue_type: survey            # survey | statement | questionnaire | op-ed | letter | guide
source_artifact: "campaign/answers/stormwater-fee.md"
limit_unit: characters        # words | characters | none
limit_value: 750
actual_count: 731             # measured, not estimated
deadline: "2026-09-15"
cost: "$0"
editable_after_submission: "minor corrections only"
submission_method: "web form"
candidate_name: "Jane Okonkwo"
date_created: "2026-08-04T14:00:00-05:00"
date_modified: "2026-08-04T14:00:00-05:00"
status: draft                 # draft | candidate-approved | submitted
submitted_date: ""
submitted_by: ""              # a human name — this skill never submits
---
```

Required sections: `## Venue rules`; `## Submission-ready text`, holding only the pasted text
between the `<!-- BEGIN SUBMISSION -->` and `<!-- END SUBMISSION -->` markers; the measured count
line; `## What was cut, and why`; `## Submission instructions for a human`; `## Irreversibility warning`.

## Steps

1. **Fill the venue rules table** from the venue spec table below or from your own research, and
   source each row. Unverified rules get `UNVERIFIED` in the source column, not a plausible guess.
2. **Pick the source text.** One artifact, one topic. Copy the position sentence and the
   evidence out of it into a scratch area; that scratch text is your entire raw material.
3. **Render down without padding up.** Cutting a 900-word position to 100 words is the job, and
   those 100 should be the load-bearing 100, not a summary of the argument's shape. If it is
   already under the limit, do not inflate it.
4. **Cut in this order, and never out of order:**
   1. Throat-clearing and transitions — "as I've traveled across this district," "it's no secret
      that," "first and foremost"
   2. Adjectives and intensifiers — "critical," "commonsense," "deeply," "absolutely"
   3. Framing and narrative — the story that sets up the number, once the number can stand alone
   4. Secondary evidence — the third and fourth data points supporting the same claim
   5. Primary evidence — **never.** If the limit cannot hold one number, one date, and the
      position, the placement is not viable; report that instead of shipping adjectives.
   Record every cut in `## What was cut, and why` with its type. An empty cut log means the text
   was rewritten rather than rendered down, and rewritten text drifts from the position.
5. **Count the correct unit, measured.** 750 characters is 110–130 words of policy prose, not
   750 — a scoping check, never a substitute for counting. Confirm whether the venue counts
   spaces; they run about a sixth of a passage, a sentence's worth on a 750-character field. If
   it does not say, assume they count and note it. Put the **measured** number in `actual_count`
   and the count line; never write "approximately."
6. **Enforce the venue's rules against the final text.** No bullets or bold where prohibited,
   including em-dash lists that are bullets in disguise. No opponent named where prohibited,
   including "my opponent" if the rule covers references and not just names. Include any
   required disclaimer from `## Boilerplate` in `positioning.md`, inside the count.
7. **Re-read the source beside the placement.** Same position, same qualification? A cut that
   turns "yes, but only if" into "yes" is the most common and most damaging failure here.
8. **Get human approval**, then **return submission instructions** — numbered, specific, with
   the URL, the deadline, and who submits. Then stop.

## Venue specs

Verified mechanics as of 2026-08-04. Anything not listed here must be verified before drafting;
do not infer a limit or a rule from a similar venue.

| Venue | Access and cost | Limit | Editable after submission | Mechanics |
|---|---|---|---|---|
| **Ballotpedia Candidate Connection** | Self-serve at [ballotpedia.org/Survey](https://ballotpedia.org/Survey) — do not hardcode rotating form IDs. No fee. Open to candidates at any level | **750 characters per free-text field, hard-enforced with a live counter.** Five such fields on the 2026 form: three key messages, policy passions, endorsements. ⚠️ Ballotpedia's own FAQ is stale — it still describes a "Who are you?" question and a 200-word answer the live form does not have. Draft against the 750-character fields | **Minor corrections only.** A substantive change is appended as a timestamped note *above* the original, never a replacement | Around 30 minutes. Identity verification via Truepic Vision, an official filed email, or a qualifying social post. Publication up to a week **from verification, not submission** — an unverified survey is never published. Appears under "Campaign Themes" and in the Sample Ballot Lookup Tool |
| **Vote411 / League of Women Voters** | Invitation-only through the local League. Free | **Varies by League — verify before drafting**; character limits are common | Verify with the League | If no invitation arrives, confirm the campaign email with the League; non-response may be published as such; print deadlines may precede online deadlines |
| **State candidate statement** | Three-way branch: paid, free but scope-limited, or unavailable. See below | Set by statute or county rule | Assume final once filed unless the office says otherwise | See the branch notes below and [`reference/state-voter-guides.md`](../../reference/state-voter-guides.md) |
| **Endorsement / advocacy questionnaire** | By invitation from the organization. Usually free | Set by the organization, usually per question | Assume none — ask | Ask before answering: is it published verbatim, shared with other organizations, or used only internally? Answers travel |
| **Newspaper op-ed** | Free to submit; the outlet decides | Set by the outlet — ask the opinion editor | The editor edits; ask to see the final | Ask the editor: word limit, exclusivity, whether they accept candidate bylines during the election window, bio line rules, and any right-of-reply policy |
| **Letter to the editor** | Free | Set by the outlet — usually far shorter than an op-ed | None once printed | Same questions as an op-ed, plus their policy on letters from candidates and on frequency |

**The state candidate statement branch.** Determine which of the three applies before writing:

- **Paid.** California statements are county-administered and paid, with strict word counts and
  content rules ([SoS](https://www.sos.ca.gov/elections/candidate-statements),
  [Elections Code §13307](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=ELEC&sectionNum=13307.)).
  Cost and word count come from the county elections office, not from the state. Oregon is also
  paid — $750 for a legislative seat, 325 words, or 200 signatures in lieu of the fee — and is
  the one program still comfortably open for 2026, closing **2026-08-25 at 5:00 pm**
  ([manual](https://sos.oregon.gov/elections/documents/vpmanual.pdf)).
- **Free but scope-limited.** Washington uses emailed access links, strict formatting, and 100-
  or 200-word limits by office
  ([SoS guide](https://www.sos.wa.gov/sites/default/files/2026-02/StateCandidatesGuide2026.pdf),
  [RCW 29A.32](https://app.leg.wa.gov/RCW/default.aspx?cite=29A.32&full=true)). Arizona Clean
  Elections covers **every candidate on the ballot**, not only publicly financed ones, and added
  countywide offices for 2026 — but still **excludes municipal and school-board candidates**
  ([AZCCEC](https://www.azcleanelections.gov/voter-education-guide)).
- **Unavailable.** Montana, Colorado, and Massachusetts publish ballot-measure pamphlets with no
  candidate section; Nevada's is judicial-only. Look to county guides, League guides, and
  Ballotpedia instead. Do not conclude a state has no program because a web search missed it —
  check the Secretary of State's 2026 candidate manual, not the voter-facing pages. Most states
  are still unverified either way; record what you find in
  [`reference/state-voter-guides.md`](../../reference/state-voter-guides.md).

Deadlines close early — Washington's 2026 statement deadline was May 19, California statements
were due with nomination papers — and a closed venue is next cycle's calendar entry, not a dead
end.

**When the venue is not in the table.** Ask the venue, in one email, before drafting, for all
ten fields in `## The venue spec`. If they will not answer or the form does not say, **count a
published example**: count three answers other candidates have published there and use the
shortest as your limit. Note in the frontmatter that the limit is inferred and from what. Too
short costs a sentence; too long costs the submission when the form truncates it silently.

## Submission

Verbatim from [`reference/shared-rules.md`](../../reference/shared-rules.md):

> This skill never submits, posts, publishes, or sends anything. It produces a draft and the
> exact instructions for a human to submit it.
>
> End with an explicit approval step: show the human what will be published, where, and what
> is irreversible about it. Wait for them to say yes. Then hand them the submission
> instructions.

**State the irreversibility plainly, at the top of the approval conversation.** Ballotpedia
allows only minor corrections. A printed county statement is printed. A questionnaire answer
gets quoted back at a forum in October. The question is not "is this good" — it is *"is this the
sentence you want read back to you by someone who disagrees, in public, in three months?"*

## Doing this without an agent

You need the source artifact, the venue's own instructions, a word processor, and an hour.

1. Write the ten venue spec fields at the top of a blank document. Fill every one from the
   venue's instructions or by emailing them. Do not guess a limit.
2. Paste the source answer or brief below it — your only raw material; nothing new gets invented.
3. Delete throat-clearing and transitions. Then adjectives and intensifiers. Then framing and
   story. Then secondary evidence. Stop before you touch a number, a date, or a record.
4. Count it. In most word processors, `Tools > Word Count` gives words and characters both with
   and without spaces — check which one the venue means. Write the number down.
5. Still over? Return to step 3 one level up the list and cut more of that type, never numbers.
6. Re-read the venue rules with the finished text in front of you: bullets removed if banned,
   opponent unnamed if required, disclaimer included and counted. Then read the source and the
   placement side by side — same position, same qualification? — and log each cut with its type.
7. Print the exact submission text and hand it to the candidate. Say out loud what cannot be
   undone. Get a yes. Then a human submits it and fills in `submitted_by` and `submitted_date`.

## Tips

**Character limits punish long words.** "Comprehensive infrastructure modernization" is 42
characters and says nothing; "fix the Third Street culvert" is 28 and says everything. Under a
character limit, plain words are capacity.

**Answer the question the venue asked.** Voter guides print the question above the answer, and a
pivot to the campaign's preferred topic reads as evasion beside an opponent who answered it.

**One-shot venues deserve a rehearsal.** For Ballotpedia and paid statements, draft in a plain
text file, sleep on it, and have a skeptic read it before anything is pasted into a form.

**Recycle the render, not the position.** A topic already rendered to 100 words is reusable at
any venue with the same limit — re-check the venue rules, but do not re-cut from scratch.
