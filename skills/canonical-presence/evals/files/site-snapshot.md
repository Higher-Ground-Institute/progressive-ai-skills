# Site snapshot — ellisonforashfield.example.org

> Fixture for skill evaluation. Everything below is invented. It is a snapshot of what a
> person would see if they ran the technical audit by hand on 2026-08-04, transcribed here so
> the audit can be evaluated without a live site.
>
> Four things are wrong with this site. Three of them are silent.

---

## `https://ellisonforashfield.example.org/robots.txt`

HTTP 200, `content-type: text/plain`

```
User-agent: *
Disallow: /admin/
Disallow: /thank-you/

User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: Google-Extended
Disallow: /

Sitemap: https://ellisonforashfield.example.org/sitemap.xml
```

> Note from the volunteer who set this up: "Blocked the AI bots so ChatGPT can't scrape Maya's
> positions and put words in her mouth."

---

## `https://ellisonforashfield.example.org/` — `<head>` excerpt

```html
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Maya Ellison for Ashfield County Commission</title>
<meta name="description" content="Maya Ellison is running for Ashfield County Commission, District 3.">
<meta name="robots" content="index, follow, noarchive">
<link rel="canonical" href="https://ellisonforashfield.example.org/">
```

Response headers:

```
HTTP/2 200
content-type: text/html; charset=UTF-8
x-powered-by: WordPress
```

---

## `https://ellisonforashfield.example.org/issues/permits/` — `<head>` excerpt

```html
<title>Permitting — Maya Ellison for Ashfield County</title>
<meta name="robots" content="index, follow, noarchive">
```

Body renders fully with JavaScript disabled. Content is server-rendered HTML.

---

## `https://ellisonforashfield.example.org/about/` — `<head>` excerpt

```html
<title>About Maya — Maya Ellison for Ashfield County</title>
<meta name="robots" content="index, follow, noarchive, max-snippet:0">
```

---

## Host configuration

Cloudflare dashboard → Security → Bots:

| Setting | State |
|---|---|
| Bot Fight Mode | Off |
| **Block AI Scrapers and Crawlers** | **On** |
| AI Labyrinth | Off |

WordPress → Settings → Reading:

| Setting | State |
|---|---|
| Discourage search engines from indexing this site | Unchecked |

Active plugins: Akismet, Wordfence Security, WP Super Cache, **SEO Guard Pro** (adds the
`noarchive` directive site-wide; enabled by default on install).

---

## Structured data

`https://ellisonforashfield.example.org/about/` contains one JSON-LD block:

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Who is Maya Ellison?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Maya Ellison is a candidate for Ashfield County Commission, District 3."
      }
    }
  ]
}
```

No `ProfilePage`, no `Person`, no `Organization`, no `sameAs`.

---

## Search Console

Property not verified. Nobody at the campaign has an account.

---

## `https://ellisonforashfield.example.org/sitemap.xml`

HTTP 200, lists 9 URLs, last modified 2026-07-30.
