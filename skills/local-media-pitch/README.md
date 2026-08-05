# Local Media Pitch

**Category:** Content & Comms

Turns one published campaign answer page or issue brief into one pitch, to one named reporter, at one outlet — with that outlet's word limit, exclusivity terms, election-period restrictions, and deadline verified before a word is drafted. Writes *to* journalists, never as them.

## Who it's for

A first-time, down-ballot candidate or the one volunteer handling communications. Anyone who has published something substantive on a campaign site and now has to get a reporter to look at it, without a press secretary and without the relationships a consultant would already have.

## What it does

Reads `campaign/district-media-map.md` and one artifact from `campaign/answers/` or `campaign/briefs/`, then produces `campaign/pitches/<outlet>-<topic>.md`: the recipient and the reason, a subject line, an email under 200 words, the linked primary records, a recorded self-check, and an approval block.

Five pitch types, same honesty, different shape: story tip, op-ed submission, letter to the editor, interview offer, and data/document share.

The mechanics it checks before drafting: word limit, exclusivity, submission address, deadline, and — the one campaigns get caught by — the outlet's election-period restriction on candidate copy. Many outlets stop running candidate letters and op-eds several weeks before an election. The skill finds the exact rule and the exact cutoff date, or records who at the newsroom confirmed there isn't one.

## Prerequisites

- **`campaign/district-media-map.md`** — outlets ranked by citation value, with beat reporters and submission rules
- **One published answer page or issue brief**, live on the campaign site. No artifact, no pitch
- A named human at the campaign willing to sign it and take the phone call

No AI tool is required. The `## Doing this without an agent` section is the full manual procedure.

## How to use it

Run it once per pitch. One artifact, one outlet, one reporter, one email. It is not a distribution tool and it will not produce a list.

The skill drafts and instructs; a human sends. It never emails anyone, and reporter contact lists never go into a chat interface — the campaign works from contact information the outlet publishes on its own site.

## Tips and edge cases

- **The honest self-check is a required step, not advice.** Before drafting: is this actually news, or does the campaign just want coverage? If it's the second, the skill says so and stops. A reporter remembers who wastes their time.
- **Reading a recent story by that reporter is mandatory**, and the pitch has to name it. "You covered the rate increase in March, and here's what happened in September" is a pitch. "You cover this county" is a mailing list.
- **The document share is underrated.** Handing a reporter organized primary records with no demand attached turns the campaign into a source instead of a supplicant. It often produces nothing this month and a phone call the next three times.
- **News deserts change the plan, not the standard.** When the media map is nearly empty, the skill works outward to statewide nonprofit newsrooms, regional dailies one county over, wire services, and trade press — then says plainly that the weight has to shift to owned and borrowed surfaces instead.
- **Follow-up discipline:** one follow-up, one week later, one paragraph, then stop. Never two reporters at the same outlet.
- **What it will not do:** anonymous tips, letters ghostwritten for a supporter to sign as their own, "concerned neighbor" framing, or the same op-ed to two outlets in one market.

## Example

An invented candidate for the Jackson County Board publishes an issue brief showing that a stormwater billing error double-charged 340 households across two years, sourced to county billing records and the September utility committee minutes.

The media map ranks the Jackson County Ledger — a nonprofit newsroom, high citation value, no paywall — above the regional daily that runs wire copy. The skill picks its utilities reporter, notes her March story on the rate increase, checks the submission page (letters 250 words; op-eds exclusive, 650 words; no candidate op-eds after October 20), and drafts a 160-word story tip that links the billing records directly and offers the underlying spreadsheet.

The ask: fifteen minutes by phone this week. The campaign manager sends it, signed, with a cell number. One follow-up goes out seven days later, and then the campaign stops.

## What it has been exercised against

Stated precisely, because a repo about not fabricating claims should not fabricate its own test history.

- **Three eval cases** in [`evals/evals.json`](evals/evals.json), runnable by `npx agent-skills-eval`: a normal pitch, which has to pick the reporter who covered the beat and name her story; a request for an anonymous tip "so it doesn't look like it came from the campaign," which has to be refused with the attributed version offered instead; and an op-ed pitched to a public radio station on a topic the campaign has no position on, where both the venue and the missing position have to be caught before drafting. All three use an invented candidate, invented outlets, and `example.org` addresses.
- **Structural validation** on every pull request via `scripts/validate_skills.py`, which enforces the agentskills.io spec plus this repo's conventions.

**Not yet done:** the eval suite has not been run against a live model, so no assertion here has an observed pass rate, and no pitch produced by this skill has been sent to a real reporter. The manual procedure in `## Doing this without an agent` is written to be followable without any AI tool, but nobody has walked it end to end. If you run it, please open an issue and say what broke.
