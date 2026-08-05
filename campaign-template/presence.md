---
candidate_name: ""
jurisdiction: ""
election_date: ""
audit_date: ""               # ISO 8601
site_audit_passed: null      # true | false | null (not run)
identity_markup_file: "campaign/identity-markup.json"
date_created: ""
date_modified: ""
---

# Canonical presence — [NAME]

Written by `canonical-presence`. Every venue where this campaign can put a candidate-authored
statement of record, triaged by whether it is open, what it costs, and when it closes.

## Part 1 — Technical audit

**Run this first.** A campaign site that is not crawlable and snippet-eligible cannot be cited
by anything, and every hour spent on content before fixing it is wasted. Full procedure in
[`reference/site-ai-readiness.md`](../reference/site-ai-readiness.md).

| # | Check | Result | Fix needed |
|---|---|---|---|
| 1 | `robots.txt` returns HTTP 200 | | |
| 2 | No `Disallow: /` under `User-agent: *` | | |
| 3 | Retrieval crawlers allowed: `Googlebot`, `OAI-SearchBot`, `Claude-SearchBot`, `PerplexityBot`, `Applebot`, `bingbot` | | |
| 4 | No `noindex` on home, bio, or issue pages | | |
| 5 | No `noarchive` or `nocache` meta anywhere | | |
| 6 | No `nosnippet` / `max-snippet:0` | | |
| 7 | No `data-nosnippet` around main content | | |
| 8 | Host-level "block AI scrapers" toggle is off | | |
| 9 | Core content renders without JavaScript | | |
| 10 | `sitemap.xml` exists and is referenced in `robots.txt` | | |
| 11 | Human confirmed verification in Search Console | | |

Checks 5 and 8 are the ones that actually bite. Both are set by default by common CMS privacy
plugins and host security toggles, and both fail silently.

## Part 2 — Venue triage

Every venue gets a row. Sort by citation value × availability — a high-value venue that
closed in May is worth less this cycle than a medium-value venue open today, but it is worth
a calendar entry for next cycle.

**Status is one of three things:**

- **Open now** — submit
- **Closed this cycle; calendar it** — record the next-cycle date and move on
- **Always open** — no deadline, do it when there is time

| # | Venue | Status | Deadline | Cost | URL | Contact | Next action | Owner | Done |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Ballotpedia Candidate Connection | | | | | | | | |
| 2 | Campaign site positions of record + identity markup | | | | | | | | |
| 3 | Vote411 / local League of Women Voters | | | | | | | | |
| 4 | State candidate statement / voter pamphlet | | | | | | | | |
| 5 | Endorsement and advocacy questionnaires | | | | | | | | |
| 6 | County / municipal voter guide | | | | | | | | |
| 7 | Candidate forum video on YouTube | | | | | | | | |
| 8 | Candidate-attributed posts on the campaign's own Facebook page | | | | | | | | |

Rows 1–8 are the national baseline. Add district-specific rows below using the derivation
procedure in the skill. **Every row needs a verified URL, a real deadline, and a real cost —
including "$0" and "no deadline," which are findings, not blanks.**

### Additional venues found for this district

| # | Venue | Status | Deadline | Cost | URL | Contact | Next action | Owner | Done |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

## Part 3 — Next-cycle calendar

Venues that closed before the campaign got to them. Not dead ends — dated entries.

| Venue | Closed on | Next cycle opens (est.) | Set reminder for | Notes |
|---|---|---|---|---|
| | | | | |

## Part 4 — Identity consistency

Answer engines confuse down-ballot candidates with namesakes constantly. The fix is boring
and effective: the same name, office, and district phrasing everywhere, plus truthful
`sameAs` links tying the profiles together.

- **Name used everywhere:**
- **Office phrasing used everywhere:**
- **`sameAs` URLs:** (only pages that genuinely describe this candidate — listing a namesake's
  page is a false assertion, not an optimization)

| Venue | Name matches | Office phrasing matches | Links back to site |
|---|---|---|---|
| | | | |

**Site implementation handoff:** `campaign/identity-markup.json` is prepared for the site
owner. This workflow does not claim the markup is live until a human confirms deployment.

## Explicitly not doing

- **Wikipedia** — conflict-of-interest policy prohibits editing an article about yourself, and
  most first-time down-ballot candidates do not meet notability anyway
- **`llms.txt`** — no answer engine meaningfully consumes it
  ([Ahrefs](https://ahrefs.com/blog/llmstxt-study/))
- **`FAQPage` structured data** — the rich result was fully deprecated May 7, 2026
- **Anonymous or pseudonymous posting anywhere**
