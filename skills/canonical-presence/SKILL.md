---
name: canonical-presence
description: Audits a campaign website for crawlability and snippet eligibility, then triages every venue where a down-ballot candidate can publish a statement of record — open now, closed this cycle, or always open — recording a status, deadline, cost, verified URL, and next action for each, and finishing with identity markup that stops answer engines from confusing the candidate with a namesake. Reads campaign/positioning.md and writes campaign/presence.md. Use this when a campaign asks where it should be publishing, why it does not appear in ChatGPT or Google AI Overviews, whether AI crawlers can read its site, which voter guides or questionnaires to fill out, or what deadlines it has already missed.
---

# Canonical Presence

**Reads:** `campaign/positioning.md` (required) — the ballot name, exact office phrasing,
bios, and `same_as` URLs all come from there.
**Writes:** `campaign/presence.md`.

Two jobs in a fixed order. First, confirm the campaign site can be crawled and quoted at all.
Then find every venue where a candidate-authored statement of record can go, and put a status, a
deadline, a cost, a URL, and a next action on each one.

A page must be indexed and snippet-eligible to appear in generative AI features
([Google](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)), so
every hour spent on content before the audit passes is wasted. The order is not negotiable: the
audit takes twenty minutes and it is the only step that can invalidate all the others. If
`approved_by_candidate` is `false`, run the audit anyway — it does not depend on message — but
do not draft venue submissions on top of unapproved positioning.

## Output Format

Write to `campaign/presence.md` using
[`campaign-template/presence.md`](../../campaign-template/presence.md), which already carries
the tables: **Part 1** the eleven technical checks, each with a result and a named fix; **Part
2** one row per venue with status, deadline, cost, URL, contact, next action, owner, done;
**Part 3** the next-cycle calendar; **Part 4** identity consistency. Set
`site_audit_passed: true` only when every Part 1 check passes.

**Every venue row needs a verified URL, a real deadline, and a real cost.** "$0" and "no
deadline" are findings; a blank cell means nobody looked, and an unexamined row reads as done.

## Steps

### Part 1 — The technical audit, and it runs first

1. **Read `https://<site>/robots.txt`.** It must return HTTP 200 — not 404, not 403, not a
   soft-404 HTML page — and must not carry a stale `Disallow: /` under `User-agent: *`, the
   staging-site leak that survives launch. It must allow every retrieval crawler: `Googlebot`,
   `OAI-SearchBot`, `Claude-SearchBot`, `PerplexityBot`, `Applebot`, `bingbot`. Blocking one
   removes the candidate from that engine's answers silently, with no error and no notification
   ([OpenAI](https://developers.openai.com/api/docs/bots),
   [Anthropic](https://support.anthropic.com/en/articles/8896518),
   [Perplexity](https://docs.perplexity.ai/guides/bots)). Confirm a working `Sitemap:` line.
2. **View source on the home, bio, and issue pages** and search the HTML for four things:
   `noindex` (ineligible, full stop); `noarchive` or `nocache` — **check this one twice**,
   because Microsoft governs Copilot through page meta rather than robots.txt and `noarchive`
   means "do not link in Chat and Copilot"
   ([Bing](https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat));
   `nosnippet` or `max-snippet:0`, which breaks Google AI feature eligibility even on an indexed
   page; and `data-nosnippet` wrapping the main content.
3. **Turn the host's "Block AI Scrapers" toggle off.** Cloudflare and most managed hosts ship
   one, increasingly on by default. One click silently overrides a permissive `robots.txt`.
4. **Disable JavaScript and reload.** If the bio and issue pages come back blank, the content is
   not reliably retrievable. Fix it before writing another page.
5. **Verify the site in Google Search Console** and opt into generative AI features — the only
   free first-party measurement surface. Record every check in the Part 1 table; procedure in
   [`reference/site-ai-readiness.md`](../../reference/site-ai-readiness.md).

**Two things campaigns get wrong every single time:**

- **`Google-Extended` does not control AI Overviews.** It controls Gemini training and
  grounding, and Google states it "does not impact a site's inclusion in Google Search nor is it
  used as a ranking signal." AI Overviews and AI Mode are Google Search features gated by
  `Googlebot`; there is no separate token
  ([Google](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers)).
  A campaign that blocks `Googlebot` to "keep AI out" has removed itself from Google Search.
- **Blocking training crawlers has zero effect on visibility.** `GPTBot`, `ClaudeBot`,
  `Google-Extended`, `Applebot-Extended`, and `CCBot` collect content to train models; they do
  not build the index an assistant searches at answer time. Blocking them is a legitimate policy
  choice that costs nothing in visibility, and allowing them is equally legitimate. Tell the
  campaign what each choice does. Do not tell them what to choose. Either way, robots.txt
  changes take about 24 hours to propagate at OpenAI and Perplexity — a mistake costs a day.

### Part 2 — Venue triage

6. **Classify every venue as exactly one of three things** — no fourth status, no "maybe":
   **Open now** (submit), **Closed this cycle; calendar it** (record the next-cycle date in Part
   3 and move on), **Always open** (no deadline, do it when there is time).
7. **Work the baseline list in this order** — citation value × availability in August 2026:
   1. **Ballotpedia Candidate Connection** ([ballotpedia.org/Survey](https://ballotpedia.org/Survey))
      — free, self-serve, open at any level, and models read Ballotpedia profiles closely
      ([Higher Ground](https://highergroundlabs.com/the-first-ai-midterms-early-signals-from-california/)).
      Draft offline and pressure-test: submissions allow only minor corrections afterward.
   2. **Campaign site positions of record + identity markup** — the only surface the campaign
      controls and the thing everything else links back to. Requires a passing Part 1.
   3. **Vote411 / local League of Women Voters** — invitation-only through the local League
      ([example](https://www.lwvnd.org/elections/vote411)), so today's action is confirming the
      campaign's email with them. Non-response gets published as non-response.
   4. **State candidate statement, where one exists** — an official state or county domain, and
      Secretary of State statements were cited frequently in the 2026 California primary
      ([Higher Ground](https://highergroundlabs.com/the-first-ai-midterms-early-signals-from-california/)).
   5. **Endorsement, union, and advocacy questionnaires** — third-party mentions are the
      strongest measured correlate of AI visibility, outcorrelating backlinks roughly 3:1
      ([Ahrefs](https://ahrefs.com/blog/ai-overview-brand-correlation/)).
   6. **County and municipal voter guides** — small audience, official domain, usually free.
   7. **Forum and "why I'm running" video on YouTube** — YouTube mentions were the strongest
      single correlate tested at ~0.737, though Google-owned self-preference is a plausible
      confound ([Ahrefs](https://ahrefs.com/blog/ai-brand-visibility-correlations/)). Costs
      nothing but showing up and posting the footage.
   8. **Candidate-attributed posts on the campaign's own Facebook page** — last because it is
      owned, unranked, and easy. Under the candidate's name or not at all.
8. **Derive the state- and district-specific venues.** No national list can do this part:
   - Open the county elections office site. Search it for "candidate," "voter guide,"
     "pamphlet," and "statement." Record the deadline even when it has passed.
   - Do the same on the Secretary of State elections page. These programs are named
     inconsistently — "voters' pamphlet," "candidate statement," "voter education guide."
   - Search `"<county> League of Women Voters"` and find who administers their guide.
   - Search `"<office>" "<county>" questionnaire 2026` and `"<office>" "<county>"
     endorsement` for groups already surveying this race, and read what the other candidates
     submitted. Check the largest school district, the chamber, and neighborhood associations
     for forums and their questionnaires. Then call the county party and two organizations
     that endorse here — five minutes on the phone beats an hour of searching.

   Check [`reference/venues.md`](../../reference/venues.md) and
   [`reference/state-voter-guides.md`](../../reference/state-voter-guides.md) first, and add
   what you learn back to them.
9. **Convert every closed venue into a dated Part 3 entry.** A campaign starting in August 2026
   has already missed things — Washington's 2026 statement deadline was May 19
   ([WA SoS](https://www.sos.wa.gov/sites/default/files/2026-02/StateCandidatesGuide2026.pdf)),
   and California statements were due with nomination papers
   ([CA SoS](https://www.sos.ca.gov/elections/candidate-statements)). That is a fact, not a
   verdict. Record what closed, when, the next-cycle estimate, and a reminder sixty days ahead.

### Part 3 — Identity consistency, then approval

10. **Fix the name.** One ballot name and one office-and-district phrasing, copied verbatim from
    `## Boilerplate` in `positioning.md`, used at every venue. Answer engines confuse
    down-ballot candidates with namesakes constantly, and "Sam Ortega," "Samuel Ortega," and
    "Sam Ortega Jr." across three guides is exactly how it happens.
11. **Emit `ProfilePage` + `Person` + `Organization`, cross-linked by `@id`** — the block in
    [`reference/ai-citation-mechanics.md`](../../reference/ai-citation-mechanics.md) §2.6.
    `sameAs` takes only URLs that genuinely describe this candidate: the Ballotpedia entry, the
    state filing page, the official accounts. A namesake's page there is a false assertion, not
    an optimization. **Do not emit `FAQPage`** — the rich result was fully deprecated May 7,
    2026 ([Google](https://developers.google.com/search/updates)) — and **do not substitute
    `QAPage`**, which describes pages where users post competing answers, not single-author
    campaign content. Do not tell the campaign markup improves AI citation; Google says it is
    not required for generative AI features. Its value is disambiguation.
12. **Get human approval.** Show the candidate the venue list and name the irreversible rows:
    Ballotpedia allows only minor corrections, and a printed pamphlet statement is printed. Wait
    for a yes. **This skill never submits anything to any venue.**

## Explicitly not doing

- **No Wikipedia.** Its conflict-of-interest policy prohibits editing an article about yourself,
  most first-time candidates fail notability, and getting caught is worse than no article.
- **Skip `llms.txt`.** Across 137,000 domains, 97% of published files received zero fetches in
  May 2026 ([Ahrefs](https://ahrefs.com/blog/llmstxt-study/)), and Google states such files
  affect visibility neither way. It costs attention the campaign does not have.
- **No anonymous or pseudonymous posting anywhere.** Every venue in this file is
  candidate-attributed, human-reviewed, and human-submitted. See
  [`reference/shared-rules.md`](../../reference/shared-rules.md) Rule 3.

## Doing this without an agent

A browser, `positioning.md`, and about three hours. Do Part 1 in one sitting; nothing else
counts until it passes.

1. Type your site address in the browser bar and add `/robots.txt` to the end. If you get a 404
   page instead of plain text, that is finding number one. Read what is there and look for
   `Disallow` followed by a single `/`, and for the six crawler names in step 1 above.
2. Go to your home page, right-click, and choose **View Page Source** (Ctrl+U on Windows, Cmd+U
   on a Mac). Press Ctrl+F and search for `noindex`, `noarchive`, `nosnippet`, `nocache`, and
   `data-nosnippet`. Write down every hit, then repeat on the bio page and one issue page.
3. Log into your web host and your CMS. Search the settings for "AI," "scraper," and "search
   engine visibility," and turn off anything that blocks crawlers. In WordPress, check
   **Settings → Reading** for "Discourage search engines." Send everything you found in steps
   1–3 to whoever built the site, in one email, as a list, then re-check each fix yourself.
4. Copy `campaign-template/presence.md` to `campaign/presence.md` and fill the Part 1 table.
5. Work the eight baseline venues in order. For each, open the site, find the deadline and the
   cost, and write them down — including "$0" and "no deadline." Every row gets a next action
   that starts with a verb and names a person.
6. Run the derivation list in step 8 above for your county and state. Budget an hour; two phone
   calls will save you most of it. Anything already closed goes in the Part 3 table with a
   reminder date for next cycle, and that reminder goes in a real calendar.
7. For Part 4, write the ballot name and exact office phrasing at the top, then check every
   existing profile against it and fix the ones that differ.
8. Print the venue list and mark the irreversible rows with the candidate before anyone submits.

## Tips

**When a campaign asks why it is invisible, check `noarchive` and the host toggle first.** They
produce exactly that symptom, and no amount of content fixes either one.

**The audit is not one-and-done.** A plugin update or a host security change can re-block the
site in a week. Re-check `robots.txt` and the meta tags monthly, and after any redesign.

**Do not let the site eat the schedule.** Off-site mentions are the stronger measured correlate
([Ahrefs](https://ahrefs.com/blog/ai-overview-brand-correlation/)). A perfect site nobody
mentions loses to a plain site that Ballotpedia, the League, and two unions point at.

**A closed venue is intelligence, not failure.** The campaign that writes down "state pamphlet
closed May 19, next cycle ~May 2028, remind me March 2028" files on time next round; a shrug
misses twice.

**When the candidate has a common name**, spend an extra half hour on Part 4. Search the name
plus the office and see who else comes back — that is what a voter sees.
