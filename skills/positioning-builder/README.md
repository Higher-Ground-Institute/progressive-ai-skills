# Positioning Builder

**Category:** Content & Comms

Turns a candidate interview and district research into `campaign/positioning.md` — the single file every writing skill in this repo reads for campaign message. It picks the three to five topics the campaign will own, writes the positions of record, carries the unresolved questions forward untouched, and stops until the candidate signs off.

## Who it's for

First-time, down-ballot candidates who have done the research and now have to decide what they actually run on. Also the volunteer who has been handed a profile, an issue scan, and a media map and told to "put together the message."

## What it does

Reads `candidate-profile.md`, `district-issues.md`, and `district-media-map.md`, then applies **three bars to every candidate topic — each requiring cited evidence, not assertion:**

1. **Salience** — people here demonstrably care, cited to the issue scan and the primary record underneath it. A public-comment count, a contested vote, a rate increase with a dollar figure.
2. **Candidate fit / earned standing** — the topic sits on this person's actual background. A nurse owns emergency-room wait times. A former code-enforcement officer owns slumlords. This is the one bar an opponent cannot copy, which makes it the campaign's real defense.
3. **Contested space** — nobody currently publishes a good answer. Owning a topic three institutions already cover well is expensive and pointless. Owning one where the honest answer does not exist is nearly free.

A topic clearing two bars is something the campaign talks about, not something it owns.

The skill then **argues against every surviving topic** and records that argument in the file. Anything that does not survive lands in a `## Topics considered and rejected` table with the reason. Three to five topics, not fifteen — and it pushes back when the campaign wants more.

It also runs a completeness check, because the whole point of the contract is that no downstream skill ever has to open the profile: voice, bios at three lengths, ballot name, office phrasing, disclaimer text, committee legal name, `sameAs` URLs, hard nos.

## Prerequisites

- `campaign/candidate-profile.md` from `candidate-profiler`
- `campaign/district-issues.md` from `district-issue-scan`
- `campaign/district-media-map.md` from `district-media-map`
- The candidate available for roughly an hour to argue with the result

All three inputs are required. Positioning built without the issue scan is a guess, and positioning built without the media map misjudges contested space.

## How to use it

Ask it to build positioning once the three inputs exist. It drafts the file with `approved_by_candidate: false`.

Then sit down with the candidate and read it out loud, topic by topic. The useful question on each one is *would you still be saying this in October, at a forum, badly outspent?* When they agree to the whole file, a human flips `approved_by_candidate` to `true`.

**Nothing downstream runs until that flag is true.** `answer-page`, `issue-brief`, `placement-writer`, `canonical-presence`, and `local-media-pitch` all check it.

## Tips and edge cases

- **The `no-position-yet` list is never resolved here.** This skill may add rows. It may never fill one in by inference — not from party, not from biography, not from adjacent positions. Only the candidate answering the question resolves an entry. That rule is the single mechanism stopping every downstream skill from fabricating a position under the candidate's name.
- **When fit and salience do not overlap** — the district is arguing about sewer rates and the candidate is a nurse — take a position on the salient issue but keep it out of `topics_to_own`, and look for a documentable seam. An invented seam is worse than no topic.
- **Two viable topics is a valid answer.** Small districts may have exactly two live fights. Two owned completely beat five covered adequately.
- **Positions of record can outnumber topics to own.** The campaign needs a defensible answer on the school levy whether or not it owns education. Owning is about where the writing time goes.
- **When the candidate's honest position is unpopular**, record it as settled with the strongest objection answered fairly. Softening it in positioning guarantees forty pieces of hedged content downstream.

## Example

Marisol Vega, running for the Cordwell County Commission, comes out of the process with three topics: emergency-response times (standing from fifteen years on night shift, salience from a contested 4–3 vote on the ambulance contract, contested space empty), utility affordability, and the county's deferred bridge maintenance. Six other topics — including two the campaign badly wanted — sit in the rejected table with a sentence each. Two rows stay in `## No position yet`, unanswered, because she has not decided yet and nobody gets to decide for her.

## What it has been exercised against

Stated precisely, because a repo about not fabricating claims should not fabricate its own test history.

- **Three eval cases** in [`evals/evals.json`](evals/evals.json), runnable by `npx agent-skills-eval`: a clean build from all three inputs, where a topic has to be owned while still sitting on the `no-position-yet` list; a seven-topic interview that has to come out at three to five with everything cut recorded in the rejected table; and the campaign asking for nine topics, which has to be argued with rather than filled. All three use an invented candidate and county.
- **Structural validation** on every pull request via `scripts/validate_skills.py`, which enforces the agentskills.io spec plus this repo's conventions.

**Not yet done:** the eval suite has not been run against a live model, so no assertion here has an observed pass rate, and no real campaign has built positioning with it. The manual path in `## Doing this without an agent` is written for printouts and index cards, but nobody has walked it end to end. If you run it, please open an issue and say what broke.
