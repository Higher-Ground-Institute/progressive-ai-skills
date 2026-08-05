# Canonical Presence

**Category:** Content & Comms

Finds every place a candidate can put a statement of record — and first makes sure the campaign website can actually be read and quoted by search engines and AI answer engines. Produces a single triaged file with a status, deadline, cost, verified URL, and next action for every venue, plus a next-cycle calendar for the ones that already closed.

## Who it's for

First-time, down-ballot candidates and the volunteer doing their communications: state legislature, county commission, school board, city council. The kind of race with no press secretary, no digital consultant, and no budget. Also useful to a state party or a candidate-training program that needs a repeatable checklist to hand out.

## What it does

**Part 1 — the technical audit, and it runs first.** A site that is not crawlable and snippet-eligible cannot be cited by anything, so content work before this is wasted. The skill checks `robots.txt`, retrieval-crawler permissions, `noindex`, `noarchive`/`nocache`, `nosnippet`, `data-nosnippet`, the host's one-click "block AI scrapers" toggle, and whether the site renders without JavaScript.

Two findings this section exists to prevent:

- **`Google-Extended` does not control AI Overviews.** It controls Gemini training and grounding. AI Overviews and AI Mode are gated by `Googlebot` — so a campaign that blocks `Googlebot` to "keep AI out" has removed itself from Google Search entirely.
- **`noarchive` silently kills Copilot.** Many CMS privacy and security plugins set it by default, and nothing tells you.

**Part 2 — venue triage.** Every venue gets classified as **Open now**, **Closed this cycle; calendar it**, or **Always open**, sorted by citation value against availability. For an August 2026 start that puts Ballotpedia Candidate Connection first and the campaign's own Facebook page last, with the reasoning written out. Includes a derivation procedure for finding the state-, county-, and district-specific venues that no national list can cover.

**Part 3 — identity consistency.** One ballot name, one office phrasing, everywhere, plus truthful `sameAs` links and cross-linked `ProfilePage` / `Person` / `Organization` markup. Answer engines confuse down-ballot candidates with namesakes constantly; this is the fix.

## Prerequisites

- **`campaign/positioning.md`** — the ballot name, exact office phrasing, bios, and `same_as` URLs come from there
- **A browser.** That is genuinely it for Part 1
- Access to the site's CMS and host, or the phone number of whoever has it

No AI tool is required. The `## Doing this without an agent` section in the SKILL.md is the complete manual procedure, including how to view page source and read a `robots.txt`.

## How to use it

Copy `campaign-template/presence.md` to `campaign/presence.md`, then run the skill or work the SKILL.md by hand. Do Part 1 in one sitting on day one — twenty minutes — and do not start Part 2 until the audit either passes or has an owner and a date on every failure.

The output is a working document. Keep it open through the cycle, tick rows as they are submitted, and re-run the Part 1 checks monthly and after any site redesign.

## Tips and edge cases

- **A blank cell is not a finding.** "$0" and "no deadline" are findings. An empty row reads as done and gets skipped forever.
- **Closed venues become calendar entries, never dead ends.** A campaign starting in August 2026 has already missed things — Washington's statement deadline was May 19, and California's were due with nomination papers. Record the date, estimate the next cycle, set a reminder.
- **Blocking training crawlers is a real choice with no visibility cost.** `GPTBot`, `ClaudeBot`, `Google-Extended`, `Applebot-Extended`, and `CCBot` do not affect whether the candidate appears in any assistant's answers. The skill tells the campaign what each choice does; it does not tell them what to pick.
- **Do not oversell the website.** Off-site mentions correlate far more strongly with AI visibility than anything on the site does. A perfect site nobody links to loses to a plain site that Ballotpedia, the League of Women Voters, and two unions all point at.
- **What the skill will not do:** edit Wikipedia, generate an `llms.txt`, emit `FAQPage` or `QAPage` markup, post anything anonymously, or submit anything anywhere. Every venue submission is human-reviewed and human-sent.

## Example

A school board candidate in an invented Jackson County runs Part 1 and finds three things: `robots.txt` returns 404, the SEO plugin is emitting `noarchive` sitewide, and the host's "AI scraper protection" is on. All three are fixed in an afternoon by the volunteer who built the site.

Part 2 then produces fourteen rows. Ballotpedia Candidate Connection is **Open now**, $0, next action "draft answers offline this week." The state voters' pamphlet is **Closed this cycle; calendar it**, with a reminder set for March 2028. The county League of Women Voters guide is **Open now** but invitation-only, so the next action is "email the League to confirm our address." The teachers' union questionnaire arrives in September, so it gets a date rather than a shrug.

## What it has been exercised against

Stated precisely, because a repo about not fabricating claims should not fabricate its own test history.

- **Three eval cases** in [`evals/evals.json`](evals/evals.json), runnable by `npx agent-skills-eval`: a site snapshot carrying a sitewide `noarchive`, a host-level AI-scraper toggle, and a JavaScript-only issues section, where all of the silent failures have to be found; an August venue triage where every row needs a status, deadline, cost, URL, and next action; and a request to create a Wikipedia page and an `llms.txt`, which has to be declined on both counts. They run against an invented candidate's invented site.
- **Structural validation** on every pull request via `scripts/validate_skills.py`, which enforces the agentskills.io spec plus this repo's conventions.

**Not yet done:** the eval suite has not been run against a live model, so no assertion here has an observed pass rate, and no real campaign site has been audited with it. The manual procedure in `## Doing this without an agent` needs nothing but a browser, but nobody has walked it end to end. If you run it, please open an issue and say what broke.
