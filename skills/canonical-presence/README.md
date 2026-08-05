# Canonical Presence

**Category:** Content & Comms

Finds every place a candidate can put a statement of record after checking that the campaign
site is crawlable and snippet-eligible. Produces `campaign/presence.md` plus concrete identity
markup at `campaign/identity-markup.json`.

## Who it's for

First-time, down-ballot candidates and the volunteer doing their communications: state legislature, county commission, school board, city council. The kind of race with no press secretary, no digital consultant, and no budget. Also useful to a state party or a candidate-training program that needs a repeatable checklist to hand out.

## What it does

**Part 1 — the technical audit, and it runs first.** A site that is not crawlable and snippet-eligible cannot be cited by anything, so content work before this is wasted. The skill checks `robots.txt`, retrieval-crawler permissions, `noindex`, `noarchive`/`nocache`, `nosnippet`, `data-nosnippet`, the host's one-click "block AI scrapers" toggle, and whether the site renders without JavaScript.

Two findings this section exists to prevent:

- **`Google-Extended` does not control AI Overviews.** It controls Gemini training and grounding. AI Overviews and AI Mode are gated by `Googlebot` — so a campaign that blocks `Googlebot` to "keep AI out" has removed itself from Google Search entirely.
- **`noarchive` silently kills Copilot.** Many CMS privacy and security plugins set it by default, and nothing tells you.

**Part 2 — venue triage.** Every venue gets classified as **Open now**, **Closed this cycle; calendar it**, or **Always open**, sorted by citation value against availability. For an August 2026 start that puts Ballotpedia Candidate Connection first and the campaign's own Facebook page last, with the reasoning written out. Includes a derivation procedure for finding the state-, county-, and district-specific venues that no national list can cover.

**Part 3 — next-cycle calendar.** Every closed venue gets a verified close date, next-cycle
estimate, source, owner, and reminder.

**Part 4 — identity consistency.** One ballot name and office phrasing everywhere, plus truthful
`sameAs` links and cross-linked `ProfilePage` / `Person` / `Organization` markup written to
`campaign/identity-markup.json`. The skill hands that file to the site owner; it does not edit
or deploy the live site.

## Prerequisites

- **`campaign/positioning.md`** — the ballot name, exact office phrasing, bios, and `same_as` URLs come from there
- **A browser.** That is genuinely it for Part 1
- Access to the site's CMS and host, or the phone number of whoever has it

No AI tool is required. Search Console ownership verification is completed by a human; this
skill never requests credentials or claims an unauthenticated verification.

## How to use it

Copy `campaign-template/presence.md` to `campaign/presence.md`, then run the skill or work the SKILL.md by hand. Do Part 1 in one sitting on day one — twenty minutes — and do not start Part 2 until the audit either passes or has an owner and a date on every failure.

The output is a working document. Keep it open through the cycle, tick rows as they are submitted, and re-run the Part 1 checks monthly and after any site redesign.

Open venue rows are handed to `placement-writer` with their verified rules, deadline, cost,
source requirement, owner, and next action. This skill discovers and routes; it does not draft
the submission.

## Full manual procedure

1. Copy the presence template and approved ballot name, exact office phrasing, election date,
   and truthful `same_as` URLs from positioning.
2. Fetch `/robots.txt`. Record HTTP status, wildcard rules, the sitemap line, and whether
   retrieval crawlers are allowed. Distinguish retrieval crawlers from training crawlers.
3. View raw HTML on the home, bio, and one issue page. Search for `noindex`, `noarchive`,
   `nocache`, `nosnippet`, `max-snippet:0`, and `data-nosnippet`. Disable JavaScript and confirm
   the substantive content remains readable.
4. Have the site's human owner inspect host/CDN/CMS crawler-blocking settings and confirm the
   result. Assign every failed check an owner and date.
5. Give the human owner the Google Search Console property URL and verification instructions.
   Record only the result they confirm; do not collect credentials. Set `site_audit_passed:
   true` only when every required Part 1 check passes.
6. Work the baseline venue list, then derive state-, county-, district-, League-, endorsement-,
   forum-, and questionnaire-specific venues. Start with
   [`reference/venues.md`](../../reference/venues.md) and
   [`reference/state-voter-guides.md`](../../reference/state-voter-guides.md), then verify each
   row with the venue. Record status, real deadline, real cost, URL, contact, owner, and action.
7. Classify each venue as Open now, Closed this cycle; calendar it, or Always open. Put closed
   rows in Part 3 with reminder dates. Hand complete open rows to `placement-writer`; do not
   draft them here.
8. In Part 4, compare every known profile with the approved ballot name and office phrasing.
   Include only URLs that genuinely identify the candidate in `sameAs`.
9. Write valid JSON-LD to `campaign/identity-markup.json` with cross-linked `ProfilePage`,
   `Person`, and `Organization` nodes. Do not emit `FAQPage` or `QAPage`. Validate the JSON,
   then hand the file and intended target page to the human site owner or developer. Do not
   change the live site.
10. Show the candidate the venue list and mark irreversible rows. Wait for explicit approval.
    A human submits each placement; this skill never submits.

## Tips and edge cases

- **A blank cell is not a finding.** "$0" and "no deadline" are findings. An empty row reads as done and gets skipped forever.
- **Closed venues become calendar entries, never dead ends.** A campaign starting in August 2026 has already missed things — Washington's statement deadline was May 19, and California's were due with nomination papers. Record the date, estimate the next cycle, set a reminder.
- **Blocking training crawlers is a real choice with no visibility cost.** `GPTBot`, `ClaudeBot`, `Google-Extended`, `Applebot-Extended`, and `CCBot` do not affect whether the candidate appears in any assistant's answers. The skill tells the campaign what each choice does; it does not tell them what to pick.
- **Do not oversell the website.** Crawlability is necessary, not a promise of citation.
- **What the skill will not do:** edit Wikipedia, generate an `llms.txt`, emit `FAQPage` or `QAPage` markup, post anything anonymously, or submit anything anywhere. Every venue submission is human-reviewed and human-sent.

## Example

A school board candidate in an invented Jackson County runs Part 1 and finds three things: `robots.txt` returns 404, the SEO plugin is emitting `noarchive` sitewide, and the host's "AI scraper protection" is on. All three are fixed in an afternoon by the volunteer who built the site.

Part 2 then produces venue rows with verified status, cost, deadline, and next action. Open rows
are handed to `placement-writer`; closed rows become Part 3 reminders. Part 4 emits the candidate's
reviewable identity markup file for a human site owner to deploy.

## What it has been exercised against

Stated precisely, because a repo about not fabricating claims should not fabricate its own test history.

- **Three eval cases** in [`evals/evals.json`](evals/evals.json), runnable by `npx agent-skills-eval`: a site snapshot carrying a sitewide `noarchive`, a host-level AI-scraper toggle, and a JavaScript-only issues section, where all of the silent failures have to be found; an August venue triage where every row needs a status, deadline, cost, URL, and next action; and a request to create a Wikipedia page and an `llms.txt`, which has to be declined on both counts. They run against an invented candidate's invented site.
- **Structural validation** on every pull request via `scripts/validate_skills.py`, which enforces the agentskills.io spec plus this repo's conventions.

**Not yet done:** the eval suite has not been run against a live model, so no assertion here has
an observed pass rate, and no real campaign site has been audited with it. If you run the manual
procedure, please open an issue and say what broke.
