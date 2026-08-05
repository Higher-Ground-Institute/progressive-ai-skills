---
name: canonical-presence
description: Audits a campaign website for crawlability and snippet eligibility, triages candidate-statement venues as open, closed, or always open, and writes identity markup for human deployment. Reads campaign/positioning.md and writes campaign/presence.md plus campaign/identity-markup.json. Use this when a campaign asks where to publish, why it is absent from search or AI answers, which venue deadlines it missed, or how to disambiguate the candidate from namesakes.
---

# Canonical Presence

**Reads:** `campaign/positioning.md` (required) — the ballot name, exact office phrasing,
bios, and `same_as` URLs all come from there.
**Writes:** `campaign/presence.md` and `campaign/identity-markup.json`.

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
5. **Hand Google Search Console verification to a human.** Provide the property URL and
   verification instructions, then record the human-confirmed result. Do not claim verification
   from an unauthenticated crawl and do not request or handle credentials. Record every check in
   the Part 1 table; procedure in
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
7. **Work the baseline list in this order:**
   1. **Ballotpedia Candidate Connection** ([ballotpedia.org/Survey](https://ballotpedia.org/Survey))
      — verify current eligibility, mechanics, and editability.
   2. **Campaign site positions of record + identity markup** — requires a passing Part 1.
   3. **Vote411 / local League of Women Voters** — invitation-only through the local League
      ([example](https://www.lwvnd.org/elections/vote411)); confirm the campaign email.
   4. **State candidate statement, where one exists.**
   5. **Endorsement, union, and advocacy questionnaires.**
   6. **County and municipal voter guides.**
   7. **Forum and candidate video on YouTube.**
   8. **Candidate-attributed posts on the campaign's own Facebook page.**
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
9. **Hand open venue rows to `placement-writer`.** Each handoff includes the venue URL, verified
   rules, deadline, cost, source artifact needed, owner, and next action. Do not draft the venue
   response in this skill.

### Part 3 — Next-cycle calendar

10. **Convert every closed venue into a dated Part 3 entry.** Record the verified close date,
    next-cycle estimate, source, owner, and a reminder sixty days ahead.

### Part 4 — Identity consistency, then approval

11. **Fix the name.** One ballot name and one office-and-district phrasing, copied verbatim from
    `## Boilerplate` in `positioning.md`, used at every venue. Answer engines confuse
    down-ballot candidates with namesakes constantly, and "Sam Ortega," "Samuel Ortega," and
    "Sam Ortega Jr." across three guides is exactly how it happens.
12. **Write `campaign/identity-markup.json`** with `ProfilePage`, `Person`, and `Organization`
    cross-linked by `@id` — the structure in
    [`reference/ai-citation-mechanics.md`](../../reference/ai-citation-mechanics.md) §2.6.
    `sameAs` takes only URLs that genuinely describe this candidate: the Ballotpedia entry, the
    state filing page, the official accounts. A namesake's page there is a false assertion, not
    an optimization. **Do not emit `FAQPage`** — the rich result was fully deprecated May 7,
    2026 ([Google](https://developers.google.com/search/updates)) — and **do not substitute
    `QAPage`**, which describes pages where users post competing answers, not single-author
    campaign content. Do not tell the campaign markup improves AI citation; Google says it is
    not required for generative AI features. Its value is disambiguation. **This skill writes
    the JSON file but does not edit or deploy the live site.** Hand the file and target page to
    the site's human owner or developer.
13. **Get human approval.** Show the candidate the venue list and name the irreversible rows:
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

For browser checks, venue derivation, Search Console handoff, identity-markup validation, and
human approval, follow the full procedure in [`README.md`](README.md).

## Tips

Recheck the technical audit monthly and after redesigns. Treat closed venues as calendar inputs,
and spend extra identity-review time when the candidate has a common name.
