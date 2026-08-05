# Site AI readiness — the crawlability audit

**Last reviewed:** 2026-08-04
**Used by:** `canonical-presence` (Part 1)

This is the first thing a campaign should do and the thing almost no campaign does. A site
that is not crawlable and snippet-eligible cannot be cited by anything — not Google's AI
Overviews, not ChatGPT search, not Perplexity, not Claude. Every hour spent writing content
before fixing a blocked site is wasted.

The failures here are **silent**. There is no error message, no email, no dashboard warning.
The candidate simply does not appear, and nobody knows why.

Evidence and citations for everything below are in
[`ai-citation-mechanics.md`](ai-citation-mechanics.md) §1, §2, and §5. This file is the
executable procedure.

---

## The eleven checks

Run them in order. Checks 5 and 8 are the ones that actually bite in the field.

### 1. `robots.txt` returns HTTP 200

Visit `https://yourcampaignsite.org/robots.txt` in a browser.

- **Pass:** the file loads as plain text.
- **Fail:** 404, 403, a redirect to the homepage, or an HTML error page. A soft-404 that
  returns styled HTML is a fail — some crawlers will parse it as garbage directives.

A missing `robots.txt` is *not* a failure by itself; the default is "crawl everything." A
broken one is.

### 2. No stale `Disallow: /`

Read the file. Look for:

```
User-agent: *
Disallow: /
```

That blocks everything. It is the single most common catastrophic error, and it usually
arrives the same way: the site was built on a staging domain with crawling disabled, and the
`Disallow` came along when it went live. Check this on every new campaign site, every time.

Also check for a `Disallow` on the paths that matter — `/issues/`, `/about/`, `/news/`.

### 3. Retrieval crawlers are allowed

These six are the ones that determine whether a candidate appears in AI answers. **Never
block them.**

| Token | Company | What blocking it does |
|---|---|---|
| `Googlebot` | Google | Removes the site from Google Search **and** AI Overviews and AI Mode. There is no separate AI Overviews crawler. |
| `OAI-SearchBot` | OpenAI | Site "will not be shown in ChatGPT search answers" |
| `Claude-SearchBot` | Anthropic | "may reduce your site's visibility and accuracy in user search results" |
| `PerplexityBot` | Perplexity | Removes the site from Perplexity results. Perplexity explicitly recommends allowing it. |
| `Applebot` | Apple | Removes the site from Spotlight, Siri, and Safari suggestions |
| `bingbot` | Microsoft | Removes the site from Bing **and** Copilot |

Also allow the user-triggered fetchers — `ChatGPT-User`, `Claude-User`, `Perplexity-User` —
which fire because a specific person asked for the page. Blocking those breaks a request a
real voter made.

**The trap that catches campaigns:** `Google-Extended` does **not** control AI Overviews. It
controls Gemini training and Gemini grounding. Blocking it does nothing to AI Overviews, and
Google states it "does not impact a site's inclusion in Google Search nor is it used as a
ranking signal." Meanwhile a campaign that blocks `Googlebot` believing it is "keeping AI
out" has removed itself from Google entirely.

### 4. No `noindex`

View source on the homepage, the bio page, and each issue page. Search for `noindex`. Check
both:

```html
<meta name="robots" content="noindex">
```

and the `X-Robots-Tag: noindex` HTTP response header, which is invisible in view-source. In
Chrome: DevTools → Network → click the document → Headers.

`noindex` means the page cannot appear in Google Search at all, and therefore cannot appear
in any Google generative feature.

### 5. No `noarchive` and no `nocache` — the silent Copilot killer

```html
<meta name="robots" content="noarchive">
```

Microsoft governs AI usage through page-level meta directives rather than robots.txt.
`noarchive` tells Bing: "Do not link in Chat and Copilot." The site stays in Bing's index and
disappears from Copilot answers.

**This is check 5 and not check 11 because CMS privacy and "security hardening" plugins set
it by default.** A campaign that installed a WordPress security plugin in week one may have
been invisible to Copilot ever since, with nothing anywhere indicating it.

### 6. No `nosnippet` and no `max-snippet:0`

Google requires a page to be indexed **and eligible to be shown with a snippet** to appear in
generative AI features. `nosnippet` or `max-snippet:0` makes it ineligible even though it is
indexed and ranking normally.

### 7. No `data-nosnippet` around main content

```html
<div data-nosnippet>...</div>
```

Element-level snippet suppression, honored by Google and, since October 2025, by Bing. Check
that it does not wrap the actual position text. It sometimes gets applied to whole content
regions by themes trying to hide boilerplate.

### 8. Host-level crawler blocking is off

**The other one that actually bites.** Cloudflare, and increasingly other hosts and site
builders, offer a one-click "Block AI Scrapers and Crawlers" or "AI Labyrinth" toggle. It is
turned on by default in some plans. It operates at the network layer and **silently overrides
a perfectly permissive `robots.txt`.**

Where to look:
- Cloudflare dashboard → Security → Bots → "Block AI Scrapers and Crawlers"
- Squarespace, Wix, Webflow, WordPress.com: search settings for "AI", "crawler", or "block"
- Any WAF or "bot protection" feature on the hosting plan

A campaign can pass checks 1 through 7 and still be invisible because of this one.

### 9. Content renders without JavaScript

Disable JavaScript in the browser (Chrome DevTools → ⌘⇧P → "Disable JavaScript") and reload.
If the candidate's positions vanish, the site is a client-rendered SPA and its content may not
be reliably retrievable. Google can process JavaScript; other retrieval crawlers are less
consistent about it.

The fix is usually a static export or server-side rendering, which most site builders offer.

### 10. `sitemap.xml` exists and is referenced

```
Sitemap: https://yourcampaignsite.org/sitemap.xml
```

Cheap, standard, helps discovery of pages that are not linked from the homepage.

### 11. Verified in Search Console

Google states that "a site must be included in Search generative AI features in Search
Console to be eligible for display in generative AI features on Google Search." Verify the
property and check the setting. The free Generative AI performance report there is also the
only first-party measurement surface that exists.

---

## A working `robots.txt` for a campaign site

Maximum discoverability. A campaign publishes in order to be found; there is rarely a reason
to block anything.

```
# Campaign site — maximum discoverability across search and AI answer engines.
# Reviewed: 2026-08-04

# --- Search / retrieval crawlers: NEVER block these ---
User-agent: Googlebot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Applebot
Allow: /

User-agent: bingbot
Allow: /

# --- User-triggered fetchers: a person explicitly asked for this page ---
User-agent: ChatGPT-User
Allow: /

User-agent: Claude-User
Allow: /

User-agent: Perplexity-User
Allow: /

# --- Training crawlers: a separate policy decision. ---
# Blocking these has NO effect on whether the candidate appears in
# ChatGPT search, Perplexity, Claude search, Copilot, or Google AI Overviews.
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: CCBot
Allow: /

# --- Everyone else ---
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /wp-admin/
Disallow: /thank-you/

Sitemap: https://yourcampaignsite.org/sitemap.xml
```

**On the training-crawler block:** whether to allow `GPTBot`, `ClaudeBot`, `Google-Extended`,
`Applebot-Extended`, and `CCBot` is a legitimate policy choice a campaign may make on
principle. It has no effect on visibility either way. Present it that way to the candidate —
tell them what each choice does and let them decide, rather than deciding for them.

**Propagation:** OpenAI documents roughly 24 hours for a `robots.txt` change to take effect;
Perplexity says up to 24 hours. A mistake takes a day to undo. Fix this early.

---

## Structured data

Emit `ProfilePage` wrapping `Person`, plus `Organization` for the committee, cross-linked by
`@id`. A full worked example is in [`ai-citation-mechanics.md`](ai-citation-mechanics.md)
§2.6.

**Do not emit `FAQPage`.** Google fully deprecated the rich result on May 7, 2026 and removed
the documentation in June 2026. It produces nothing.

**Do not substitute `QAPage`.** Google defines it as "one question followed by its answers"
— plural, meaning forum-style pages where users submit competing answers. A campaign FAQ with
the candidate as sole voice does not fit, and marking it up as one asserts something untrue
about the page.

**Do not tell the candidate that structured data improves AI citation.** No vendor documents
that their retrieval pipeline weights JSON-LD, and Google says explicitly that structured data
"isn't required for generative AI search." The real, defensible value is different and worth
more to a down-ballot candidate anyway: **identity disambiguation.** Candidates with common
names get confused with namesakes constantly, and `sameAs` linking the candidate to their
Ballotpedia entry and official filing page is a truthful, machine-readable assertion of who
they are.

`sameAs` must contain only URLs that genuinely describe this candidate. Listing a namesake's
Wikipedia article is a false statement, not an optimization.

---

## What to skip

**`llms.txt`.** No answer engine meaningfully consumes it. Ahrefs found 97% of published
files received zero fetches in May 2026 across 137,000 domains
([study](https://ahrefs.com/blog/llmstxt-study/)); EZY logged 7 fetches from OpenAI's crawlers
against 3,990 `robots.txt` fetches over 12 weeks
([study](https://www.ezy.ai/research/do-ai-bots-read-llms-txt)). Google states such files
"won't negatively or positively impact your visibility or rankings." The one exception is
Meta's crawler, which does fetch it. Not worth a first-time candidate's attention.

**Content "chunking."** Google: "There's no requirement to break your content into tiny
pieces for AI to better understand it... There's no ideal page length."

**Rewriting content for AI.** Google: "You don't need to write in a specific way just for
generative AI search."

**A page per query variation.** Named as scaled content abuse in Google's own guidance, and
page count correlates at only r ≈ 0.194 with AI visibility.

---

## Re-audit triggers

Run the audit again after any of these, because all of them have been observed to reintroduce
a block:

- A site redesign or platform migration
- Installing or updating a security, privacy, caching, or SEO plugin
- Any change to hosting, DNS, or CDN configuration
- Turning on a "bot protection" or "AI blocking" feature for any reason
- A volunteer with dashboard access doing anything at all

Once a month during the campaign is enough otherwise.
