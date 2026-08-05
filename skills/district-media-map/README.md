# District Media Map

**Category:** Research & Data

Builds a working contact map of every outlet, beat reporter, community platform, and candidate forum that reaches one district, and writes `campaign/district-media-map.md`. Every row is meant to be actionable today: who to email, at what address, about what, by when, under what rules.

## Who it's for

First-time, down-ballot candidates and the volunteer who has been told to "get us some press" and discovered that the county's daily paper closed its bureau in 2016. Also anyone who needs a media list before running `local-media-pitch`.

## What it does

Outlets do not organize themselves by legislative district, so the skill starts with geography — every municipality, township, school district, and county the district touches — and searches on those names.

It then builds the candidate list from eight public sources rather than a prebuilt national database: the state press association directory, the Institute for Nonprofit News directory, LION Publishers members, public radio by ZIP, university journalism outlets, the county's legal-notice publisher of record, the clerk's press notification list, and three months of council and commission minutes. The union is always larger than what the campaign named from memory.

Each outlet then gets **tested rather than assumed**. Read the last fourteen days of the local section and count: a story is original if a named local reporter wrote it and a local body, meeting, or person is in the lede. Wire tags, syndicated columns, and press releases run verbatim do not count. Fewer than three original local stories in fourteen days is low citation value no matter how large the outlet.

Ranking is by **citation value, not circulation** — five tests scored 0, 1, or 2, none of which is audience size. A 4,000-subscriber nonprofit newsroom that sends someone to the commission meeting outranks a 60,000-circulation daily running the same wire copy as forty other papers, because only one of them will ever produce an original sentence about this candidate.

For every outlet it records the submission mechanics — letters and op-ed limits, addresses, exclusivity, questionnaires, paywall — and it converts the election-period rule into a **specific date**. Campaigns usually learn that rule in late October, three weeks too late to use it.

## Prerequisites

- The district's geography, from the county elections or state legislature site
- Web access, a phone for the newsrooms that never published their policy, and three to four hours

No paid media database. The skill will not buy, scrape, or import one, and it never guesses an email address pattern.

## How to use it

Ask for a media map and name the district. Then check the two fields that go stale fastest — the beat reporter and the election cutoff — about every thirty days.

Output goes to `campaign/district-media-map.md`, which `positioning-builder` reads for contested space and `local-media-pitch` reads for everything.

## Tips and edge cases

- **A news desert is a finding, not a failed scan.** No outlet has covered a governing body of this district in 90 days means the map is two rows long and the plan changes: statewide nonprofit newsroom, public radio statehouse desk, legal-notice weekly, and much more weight on Ballotpedia, Vote411, forum video, and the campaign's own pages. Padding the list with regional outlets that do not cover the district is the failure mode.
- **The staff page is stale; the bylines are not.** Pitch whoever wrote three county stories this month, whatever their title says.
- **Chain-owned papers need one extra question.** One reporter across four counties is normal. Ask which four.
- **Letters and op-eds are different pipelines** with different editors, limits, and sometimes different cutoffs. An 800-word op-ed sent to the letters address gets deleted, not forwarded.
- **This file is a real contact list for real journalists.** It stays in the campaign folder. It does not get pasted into a chat window for cleanup, and the skill contacts no one — a human sends every email.

## Example

Ashfield County District 3 comes out thin: a 5,200-circulation independent weekly whose one reporter attends the commission meeting, a one-person public radio bureau that runs no candidate copy at all, a 38,000-circulation regional daily that produced zero stories about an Ashfield governing body in two weeks, and a chamber newsletter that reprints whatever it is sent. The weekly and the radio bureau rank first and second. The daily, despite being seven times larger than everything else combined, ranks below both — and the map records the weekly's real deadline as a date: nothing candidate-written after the October 7 issue.

## What it has been exercised against

Stated precisely, because a repo about not fabricating claims should not fabricate its own test history.

- **Three eval cases** in [`evals/evals.json`](evals/evals.json), runnable by `npx agent-skills-eval`: the circulation argument, where a 38,000-daily has to rank below a 5,200 weekly and the scores have to be shown; the masthead claim, where "we serve four counties" has to be tested against fourteen days of bylines rather than accepted; and a news-desert district, where the correct output is a two-row map with the desert section filled in rather than a padded list. All three run against invented outlets in an invented county, with `example.org` addresses.
- **Structural validation** on every pull request via `scripts/validate_skills.py`, which enforces the agentskills.io spec plus this repo's conventions.

**Not yet done:** the eval suite has not been run against a live model, so no assertion here has an observed pass rate, and no real campaign has built a map with it. The manual procedure in `## Doing this without an agent` is written for a notebook and a library computer, but nobody has walked it end to end. If you run it, please open an issue and say what broke.
