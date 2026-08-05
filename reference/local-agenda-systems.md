# Local agenda systems — finding the records

**Last reviewed:** 2026-08-04
**Used by:** `district-issue-scan`, `issue-brief`

There are over 3,000 counties and roughly 19,000 municipalities in the United States. No
fixed directory of their meeting-records systems will stay accurate, and shipping one would
mean shipping something that is wrong in most places on day one.

So this is a **detection procedure** instead. It works anywhere, and it degrades gracefully to
"call the clerk," which is a real answer and often the fastest one.

---

## The procedure

### 1. Find the jurisdiction's official agenda page

Search for the exact name of the body plus a records word:

```
"Rockbridge County Board of Supervisors" agenda minutes
"Rockbridge County" "board of supervisors" site:.gov
```

Start from the official county or city `.gov` site and look for **Agendas**, **Meetings**,
**Minutes**, **Public Notices**, or **Legislative Information** in the navigation. Ignore
third-party aggregators until you have found the official source — you want the record, not
somebody's copy of it.

### 2. Identify the hostname and the vendor

Look at the URL of the agenda page. Five vendors cover most of the country, and each has a
recognizable pattern:

| Vendor | URL pattern | Notes |
|---|---|---|
| **Legistar** (Granicus) | `{client}.legistar.com` | Has a public API. The best case by a wide margin. |
| **Granicus** | `{jurisdiction}.granicus.com` | Often video plus documents |
| **CivicPlus** | `{st}-{jurisdiction}.civicplus.com/AgendaCenter` | e.g. `oh-columbus.civicplus.com` |
| **PrimeGov** | `{jurisdiction}.primegov.com` | |
| **CivicClerk** | `{jurisdiction}.civicclerk.com` | |

If none match, the jurisdiction is probably posting PDFs to its own web server. That is
common in small places and it is fine — go to step 4.

### 3. Use the vendor API or a supported scraper

**Legistar** exposes a public web API, commonly without authentication:

```
https://webapi.legistar.com/v1/{Client}/{Endpoint}
```

The `{Client}` is the subdomain from step 2. Useful endpoints:

| Endpoint | Returns |
|---|---|
| `/Events` | Meetings, with dates and agenda links |
| `/Matters` | Legislative items — ordinances, resolutions, contracts |
| `/Matters/{id}/Histories` | The action history on one item. ⚠️ **Often not the vote tally — see below** |
| `/Bodies` | Committees and boards |
| `/Persons` | Current and former members |

### ⚠️ Do not trust the API for vote tallies

**Verified 2026-08-04 on two unrelated instances in two states** — Madison, WI and Whatcom
County, WA, scanned independently. `MatterHistoryTally` came back null on every matter checked
in both. On Madison, `/EventItems/{id}/Votes` also returned an empty array, and across 25 Common
Council meetings the API surfaced no recorded dissenting vote — for a body that certainly had
some. The tallies exist, but only in the minutes PDF.

Two instances is enough to treat this as the default rather than a quirk. **Reading the tally
from the minutes is the primary method; the API is the thing that will not have it.**

The failure is silent and it inverts the finding. A scan that trusts the field name reads an
empty tally as consensus and reports a contested 12–7 vote as unanimous, which is the opposite
of what a candidate needs to know — a split vote is the story. **Never infer a vote from an
empty or null tally field.** Either pull the number from the minutes document, or record the
vote as unretrieved and say which meeting's minutes to open.

### ⚠️ `/Matters` silently truncates at 1,000 records

A twelve-month window on a mid-size county hits the cap. You get a truncated result set, **no
error, and no indication anything is missing** — the worst available failure mode. Page the
results or narrow the date range, and never conclude a body was quiet because the list came
back short.

---

## The CMS is not the agenda system

**Detect these separately.** Sullivan County, NH's site footer reads *"Government Websites by
CivicPlus®,"* which by the procedure above means running `civic-scraper` against
`/AgendaCenter`. That path returns **404**. The actual records live in nine Microsoft SharePoint
folders linked from `/129/Agendas-Minutes`.

Who built the website and where the agendas live are unrelated questions. Answer the second one
by following the site's own "Agendas & Minutes" link and seeing where it lands, not by reading
the footer.

### Public document libraries — the missing category

SharePoint, Google Drive, and Dropbox folders are common in small counties and **they defeat
scripted retrieval while being fully public.** `curl` gets a login redirect or a JavaScript stub
for a document anyone can open in a browser.

| Signal | What it means |
|---|---|
| URL contains `sharepoint.com`, `drive.google.com`, `dropbox.com` | Document library, not a vendor portal |
| `curl` returns a login page or JS stub, browser opens it fine | Library, not a permissions problem |
| Agenda link leaves the county domain entirely | Follow it; the records are there |

Retrieve these with a browser session, not a scraper. **A scan that stops at "no vendor found"
concludes that a county with a complete public record has none** — which is the difference
between a candidate who can cite the actual vote and one who believes no record exists.

### Image-only PDFs look exactly like empty documents

Scanned minutes have no text layer. Extraction returns zero characters, search returns nothing,
and **nothing raises an error.**

**Heuristic: under roughly 100 characters extracted per page means it is a scan, not an empty
document.** Rasterize and OCR it. Non-obvious corollary from Sullivan County — the *draft*
minutes of a meeting had a text layer and the *ratified* version did not. Check both, and note
which one you read, because drafts get corrected.

Anything read by OCR should be re-verified against the original before a campaign publishes a
number from it.

Responses cap at 1,000 records and support OData filtering, so narrow by date:

```
https://webapi.legistar.com/v1/{Client}/Events?$filter=EventDate gt datetime'2025-08-01'
```

Docs: [Legistar Web API](https://support.granicus.com/s/article/Legistar-Web-API) ·
[examples](https://webapi.legistar.com/Home/Examples)

**For the other four vendors**, [`civic-scraper`](https://github.com/biglocalnews/civic-scraper)
from Big Local News supports CivicClerk, CivicPlus, Granicus, Legistar, and PrimeGov. It is a
Python package maintained for newsroom use.

Neither of these is required. A person clicking through the agenda portal and reading minutes
gets the same information more slowly, and reads them more carefully.

### 4. Fall back to official documents and manual extraction

When there is no vendor and no API:

1. **The clerk.** Every jurisdiction has one, the email is public, and clerks answer. Ask for
   minutes for a date range. This is frequently faster than any scraping.
2. **The legal notice publisher of record.** Every county designates a newspaper for legal
   notices — rate changes, hearings, bond issues, zoning applications. It is a complete,
   legally-mandated record of pending public decisions, and almost nobody in politics reads
   it. Find it by searching `"{county}" "legal notices" newspaper` or by asking the clerk.
3. **State open-records portals.** Many states aggregate local budget filings, audits, and
   utility rate cases.
4. **The body's own YouTube or Vimeo channel.** Many small jurisdictions stream meetings but
   never post minutes. Auto-generated transcripts are searchable.
5. **A records request.** Slow — days to weeks — but it works, and it is free or nearly free
   in most states. Start it early and keep working while you wait.

---

## Which bodies to scan

The interesting fights are usually not at city council.

| Body | Why it matters |
|---|---|
| City / town council | Most visible, most covered, most crowded |
| County commission / board of supervisors | Budget, sheriff, jail, roads, land use |
| School board | Closures, boundaries, budget, curriculum. High turnout intensity. |
| **Water / sewer / utility district** | Rate increases with dollar figures attached. Almost never covered. |
| **Planning and zoning** | Where housing and development fights actually get decided |
| Library board | Small budget, disproportionate salience in recent cycles |
| Transit authority | Service cuts are intensely felt and rarely explained well |
| Hospital or health district | Where they exist, they are major local employers |

Water and planning are the highest-yield and lowest-competition sources in this list. A rate
increase adopted at a sparsely-attended utility board meeting shows up on every household's
bill and has usually never been explained to anyone.

---

## District and representative boundaries

Figuring out which jurisdictions a legislative district actually contains is its own problem.

**Google Civic Information `divisionByAddress`** still returns Open Civic Data identifiers,
even though the Representatives API was shut down in April 2025
([announcement](https://groups.google.com/g/google-civicinfo-api/c/9fwFn-dhktA)). The chain
that works:

```
divisionByAddress → OCD-ID → Open States /people.geo (state legislators)
                           → official county/municipal sites (everything below that)
```

**Open States API v3** requires an `X-API-KEY`. Plan for roughly 10 requests per minute and
500 per day ([docs](https://docs.openstates.org/api-v3/),
[limits](https://github.com/openstates/issues/discussions/205)). For statewide work, skip the
API and use the bulk CSV:

```
https://data.openstates.org/people/current/{state}.csv
```

**Coverage limits worth knowing before you rely on any of this:**

- The Open States `people` repository covers **current officeholders, not candidates**
  ([schema](https://raw.githubusercontent.com/openstates/people/main/schema.md)). It is not a
  candidate-submission channel and should not be treated as one.
- **OpenFEC is federal-only** ([API](https://api.open.fec.gov/developers)). For state and
  local campaign finance, use the state disclosure portal. Every state has one; they vary
  enormously in quality.
- **Ballotpedia's and Democracy Works' APIs are gated.** Use the public Ballotpedia pages and
  official county election records instead.
- Local-office coverage in Open States is limited. Below the state legislature, the official
  county or municipal site is the authority.

---

## What "checked and found nothing" looks like

Log the empty results in the sources table in `district-issues.md`. An honest record of where
you looked and found nothing is worth real time to the next person, and in a news-desert
district it is most of what the scan produces.

Write it as: source, URL, window covered, date checked, and "no relevant items." Not a blank
row.
