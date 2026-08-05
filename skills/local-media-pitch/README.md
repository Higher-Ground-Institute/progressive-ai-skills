# Local Media Pitch

**Category:** Content & Comms

Creates one attributed outreach email to one verified outlet route. Story tips, interview offers,
and document shares use a published campaign artifact; direct op-ed and LTE submissions use a
candidate-approved placement whose body was written by `placement-writer`.

## Who it's for

A first-time, down-ballot candidate or the one volunteer handling communications. Anyone who has published something substantive on a campaign site and now has to get a reporter to look at it, without a press secretary and without the relationships a consultant would already have.

## What it does

Reads approved positioning, `campaign/district-media-map.md`, and the source required for the
pitch type. It produces `campaign/pitches/<outlet>-<topic>.md`: recipient and rationale, subject
line, cover email, links or attachments, self-check, follow-up plan, and approval block.

Five pitch types, same honesty, different shape: story tip, op-ed submission, letter to the editor, interview offer, and data/document share.

The mechanics it checks before drafting are whether the outlet accepts the exact pitch type,
word limit where applicable, exclusivity, route, deadline, and election-period restriction. Any
cutoff is calculated from the verified `election_date` in positioning, never a hardcoded date.

## Prerequisites

- **`campaign/district-media-map.md`** — outlets ranked by citation value, with beat reporters and submission rules
- **Candidate-approved `campaign/positioning.md`**
- **For story tips, interview offers, and document shares:** one published answer page or issue
  brief at a live URL
- **For direct op-ed/LTE submissions:** one candidate-approved placement from
  `placement-writer`
- A named human at the campaign willing to sign it and take the phone call

Source pages follow `draft` → `candidate-approved` → `published`. Pitch files follow
`draft` → `candidate-approved` → `sent`.

## How to use it

Run it once per pitch. One source, one outlet, one route, one email. It is not a distribution
tool and it will not produce a list.

The skill drafts and instructs; a human sends. It never emails anyone, and reporter contact lists never go into a chat interface — the campaign works from contact information the outlet publishes on its own site.

## Routing table

| Pitch type | Source and approval | Outlet must accept | Deliverable |
|---|---|---|---|
| Story tip | Published answer/brief and live URL; facts only if position unresolved | Tips to the named beat reporter or listed intake | Under-200-word attributed email linking the artifact and record |
| Interview offer | Published answer/brief and live URL; approved topic | Interview pitches on that beat | Under-150-word availability email |
| Document share | Published answer/brief, live URL, and described records; facts only if position unresolved | Document tips on that beat | Under-150-word email with records |
| Op-ed submission | Candidate-approved op-ed placement; no missing-position marker | Candidate op-eds at this point in the election period | Brief cover email plus separate placement body |
| LTE submission | Candidate-approved LTE placement; no missing-position marker | Candidate letters at this point in the election period | Brief cover email plus separate placement body |

An unknown position stops op-eds, LTEs, and interview offers that would state a stance.
Factual story tips and document shares may continue without a position. Linked campaign
content requires `status: published` and a working live URL.

## Full manual procedure

1. Confirm positioning is candidate-approved and `election_date` is verified. Apply the routing
   table and reject an ineligible source before drafting.
2. Open the media map. Prefer the highest-citation-value outlet that actually covers the topic
   and district. Treat a complete outlet row checked within the last 30 days as fresh. Recheck
   only missing, unverified, or older fields, and record each new source and check date.
3. Confirm the outlet currently accepts this exact pitch type. For op-eds/LTEs verify candidate
   bylines, limit, exclusivity, editing policy, route, deadline, and election restriction. For
   tips/offers/shares verify beat fit and intake route. Calculate a blackout cutoff from the
   verified election date and the outlet's rule.
4. For reporter-routed pitches, read recent bylines and record one relevant story URL and date.
   If no recent work matches, choose another reporter or outlet.
5. For a story tip, ask whether the development would still be news if another campaign sent
   it. News requires a development, record, dated decision, or concrete consequence. If the
   answer is merely "we want coverage," stop.
6. Copy the pitch template. Write a subject under 60 characters and an attributed cover email:
   what is happening now, specific evidence and primary-record link, what the campaign can
   provide, one low-friction ask, then the named sender's role, phone, and email.
7. Keep story tips ordinarily under 200 words and interview/document emails under 150. Those
   defaults do not apply to the separately authored op-ed/LTE body, which follows the outlet's
   verified limit. Never paste the body into the cover-email field unless the outlet requires
   one combined field.
8. Compare every claim, number, date, and link with the eligible source. Open each link and
   confirm it supports the statement.
9. Show the candidate the exact email, separate body if applicable, recipient, route, and ask.
   Recheck contact data only if stale or incomplete. After explicit approval, set
   `status: candidate-approved`.
10. A named human sends from an attributed campaign account. After confirmation, set
    `status: sent`, `sent_date`, and `sent_by`. One week later, send at most one short
    follow-up, then stop.

## Tips and edge cases

- **The honest self-check is a required step, not advice.** Before drafting: is this actually news, or does the campaign just want coverage? If it's the second, the skill says so and stops. A reporter remembers who wastes their time.
- **Reading a recent story by that reporter is mandatory**, and the pitch has to name it. "You covered the rate increase in March, and here's what happened in September" is a pitch. "You cover this county" is a mailing list.
- **The document share is underrated.** Handing a reporter organized primary records with no demand attached turns the campaign into a source instead of a supplicant. It often produces nothing this month and a phone call the next three times.
- **News deserts change the plan, not the standard.** When the media map is nearly empty, the skill works outward to statewide nonprofit newsrooms, regional dailies one county over, wire services, and trade press — then says plainly that the weight has to shift to owned and borrowed surfaces instead.
- **Follow-up discipline:** one follow-up, one week later, one paragraph, then stop. Never two reporters at the same outlet.
- **What it will not do:** anonymous tips, letters ghostwritten for a supporter to sign as their own, "concerned neighbor" framing, or the same op-ed to two outlets in one market.

## Example

An invented county candidate publishes an issue brief about a stormwater billing error, sourced
to county records and committee minutes. A fresh media-map row points to the local utilities
reporter. The skill verifies that tips are accepted, drafts a short attributed email linking the
live brief and records, and offers the underlying spreadsheet.

The ask: fifteen minutes by phone this week. The campaign manager sends it, signed, with a cell number. One follow-up goes out seven days later, and then the campaign stops.

## What it has been exercised against

Stated precisely, because a repo about not fabricating claims should not fabricate its own test history.

- **Three eval cases** in [`evals/evals.json`](evals/evals.json), runnable by `npx agent-skills-eval`: a normal pitch, which has to pick the reporter who covered the beat and name her story; a request for an anonymous tip "so it doesn't look like it came from the campaign," which has to be refused with the attributed version offered instead; and an op-ed pitched to a public radio station on a topic the campaign has no position on, where both the venue and the missing position have to be caught before drafting. All three use an invented candidate, invented outlets, and `example.org` addresses.
- **Structural validation** on every pull request via `scripts/validate_skills.py`, which enforces the agentskills.io spec plus this repo's conventions.

**Not yet done:** the eval suite has not been run against a live model, so no assertion here has
an observed pass rate, and no pitch produced by this skill has been sent to a real reporter. The
manual procedure has not been walked end to end. If you run it, please open an issue and say
what broke.
