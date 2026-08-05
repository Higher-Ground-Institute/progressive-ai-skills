# NOTES — City of Madison and Dane County, Wisconsin

> **Real places, real records, no real candidates.** Every jurisdiction, governing body,
> meeting record, vote, dollar figure, docket number, and news outlet in this file is real and
> linked to a public source. **No candidate appears anywhere in it, and nothing in it is
> attributed to a real person running for office.** Where a real official or reporter is named,
> the file cites only something they have actually published or done in the public record, with
> a link. An AI-generated "position" attached to a real candidate's name is the exact
> fabrication this repository exists to prevent, and it would do the most damage coming from
> the reference examples. See [`golden/README.md`](../README.md).

**Scan date:** 2026-08-04 · **Window:** 2025-08-01 to 2026-08-04 · **Time spent:** roughly one
working session, agent-assisted, network access only, no API keys, no paid tools.

This is the failure log for
[`district-issues.md`](district-issues.md) and
[`district-media-map.md`](district-media-map.md). It exists because the failure modes are what a
campaign actually needs to know, and because a clean output file hides all of them.

---

## Why this district was chosen

The brief for the golden set asked for a place with (a) an active local newspaper or nonprofit
newsroom, (b) an online agenda portal reachable in practice, and (c) a genuine documented local
controversy in the public record. Madison satisfies all three unusually well, which is both the
reason to pick it and the reason to be careful about generalizing from it.

Candidates considered and rejected, in the order they were tested, with the reason:

| Considered | Legistar slug tried | Result | Why rejected |
|---|---|---|---|
| Asheville / Buncombe County, NC | `asheville`, `cityofasheville`, `buncombecounty` | HTTP 500 on all three | Attractive on media grounds — Asheville Watchdog is a nonprofit newsroom and post-Helene water is a heavily documented controversy — but no API-reachable agenda records, so it could not demonstrate a working vendor pull |
| Berkeley, CA | `berkeley` | HTTP 500 | Same |
| Durham, NC | `durham` | HTTP 500 | Same |
| Ann Arbor, MI | `annarbor`, then `a2gov` | **`a2gov` works** | A viable alternative. Madison was chosen over it because Madison has three separate API-reachable instances, including a sewerage district, which lets the golden file demonstrate the skill's "the boring bodies carry the salient fights" claim rather than assert it |

Madison should be read as the **ceiling**, not the median. Three Legistar instances with a
working public API, five outlets with named beat reporters, three of them nonprofits, and a
League of Women Voters chapter that co-produces candidate video with the city's own municipal
channel is not what most districts look like. The paired news-desert district exists so the
golden set is not only this.

---

## The most useful failure modes

Ordered by how much time they would cost someone who did not know about them, and by how
plausible the wrong answer looks.

### 1. The Legistar API says it returns vote tallies. On this instance it does not.

**This is the one that produces a confidently false output**, and it is the failure mode most
worth fixing in the repo itself.

[`reference/local-agenda-systems.md`](../../reference/local-agenda-systems.md) documents
`/Matters/{id}/Histories` as returning "The vote history on one item, including who voted how."
`district-issue-scan` builds its whole ranking method on non-unanimous votes — "A non-unanimous
vote is a gift ... a 4–3 vote means somebody's constituents were angry enough to move a member."
On `madison`, the API will not give you that.

What was actually run, and what came back:

| Request | Result |
|---|---|
| `GET /v1/madison/Matters/{id}/Histories` on matters 99767, 100720, 101095, 99627 | 200. Full referral chain with body names, action names, dates, mover and seconder IDs. **`MatterHistoryTally` was `null` on every row of all four.** `MatterHistoryRollCallFlag` present but unhelpful |
| `GET /v1/madison/EventItems/881013/Votes` — an item with a recorded mover, a recorded seconder, and `EventItemPassedFlagName: Pass` | **200 with an empty array `[]`** |
| `GET /v1/madison/Events/28485/EventItems/881013/Votes` | **404** |
| `GET /v1/madison/Events/{id}/EventItems?AgendaNote=1&MinutesNote=1&Votes=1` across all 25 Common Council meetings in the window | 200. Items returned. **Zero items with any recorded dissenting vote.** 1,063 of the items had a null `EventItemActionName` |

An empty array is the dangerous shape. A 404 or a 500 tells you to look elsewhere; `[]` with a
200 reads as "there were no dissenting votes," and a scan that reports "adopted unanimously"
on that basis has fabricated a vote count from a null field. The correct inference is that the
field is not populated on this client.

**The workaround, which is genuinely good enough.** The distinction lives in
`EventItemActionName` instead. Across those 25 meetings:

| Action name | Count |
|---|---|
| *(null)* | 1,063 |
| Adopt Unanimously | 550 |
| Refer | 398 |
| Referred | 279 |
| Grant | 208 |
| Disallow | 125 |
| **Adopt** | **122** |
| Refer For Public Hearing | 105 |
| Adopt unanimously under suspension of MGO 2.055 | 22 |
| Adopt Substitute | 10 |

Madison's clerk records unanimous voice votes as **"Adopt Unanimously"** and roll calls as plain
**"Adopt."** So the 122 plain-"Adopt" items are the entire set of contested Council votes in
twelve months, and that list is derivable from the API in one pass. **The tally itself is only in
the minutes PDF**, whose URL the API does hand you in `EventMinutesFile`, e.g.
[`28484_M_COMMON_COUNCIL_26-07-21_Meeting_Minutes.pdf`](https://madison.legistar1.com/madison/meetings/2026/7/28484_M_COMMON_COUNCIL_26-07-21_Meeting_Minutes.pdf).
Those PDFs were **not parsed** for this scan, which is why no vote tally appears anywhere in
`district-issues.md`.

**By hand:** identical. The action name is printed in the online agenda and minutes; the tally is
in the minutes. Reading 122 items is an afternoon.

**Caveat on scope.** This was tested on one client, `madison`. Other Legistar clients may
populate `Votes` correctly. **Do not generalize the failure — generalize the check.** Before
trusting a tally field, pull one matter you know was contested and confirm the field is
populated. If it comes back empty, assume it is empty everywhere on that client.

### 2. The 1,000-record cap truncates silently, with no error and no pagination hint

The obvious first query — every matter introduced since the start of the window — returned
**exactly 1,000 records** and stopped at **2025-11-06**. No error, no warning, no `nextLink`, no
total count, nothing in the response indicating truncation. A keyword scan of that response
found nothing at all for `referend`, `oversight`, or `rezon`, and would have supported the
conclusion that Madison had a quiet year.

The same window in six date-chunked requests returned **3,772 matters**, and the police
oversight fight, the data center moratorium, the three watershed studies, and the $6 million BRT
engineering contract are all in the nine months the first query dropped.

```
# silently truncated at 1,000, ends 2025-11-06
/v1/madison/Matters?$filter=MatterIntroDate gt datetime'2025-08-01'

# correct: chunk by month or quarter and concatenate
/v1/madison/Matters?$filter=MatterIntroDate ge datetime'2026-01-01' and MatterIntroDate lt datetime'2026-03-01'
```

The cap is documented in `reference/local-agenda-systems.md` and in Granicus's own docs. Knowing
it exists and knowing what truncation *looks like* are different things. **Rule of thumb: if a
Legistar response contains exactly 1,000 records, it is truncated. Treat 1,000 as an error
code.** Madison introduces roughly 250–350 matters a month, so monthly or quarterly chunks are
safe; a large city could need weekly.

### 3. The Legistar client slug is not derivable from the jurisdiction name, and the error is misleading

Wrong slugs return **HTTP 500** with a distinctive message:

```
{"Message":"An error has occurred.",
 "ExceptionMessage":"LegistarConnectionString setting is not set up in InSite for client: madisonwi", ...}
```

That is a 500 and it reads like the API is broken. It is not — it means the client does not
exist under that name. Observed:

| Slug tried | Result |
|---|---|
| `madison` | **works** — City of Madison |
| `dane` | **works** — Dane County |
| `mmsd` | **works** — Madison Metropolitan Sewerage District |
| `madisonwi`, `danecounty` | 500, slug not set up |
| `annarbor` | 500 · `a2gov` works instead |
| `asheville`, `cityofasheville`, `buncombecounty`, `berkeley`, `durham` | 500 |

There is no way to enumerate valid clients. **Read the slug off the portal hostname** — the word
before `.legistar.com` — exactly as `district-issue-scan` step 2 says. Guessing from the
jurisdiction name failed more often than it worked here, and the 500 is easy to misread as "this
jurisdiction has no Legistar," which for Asheville and Berkeley is a different and also wrong
conclusion: both have public agenda portals, just not API-enabled Legistar clients under the
slugs tried.

### 4. One city can be three separate Legistar instances, and the interesting one is the sewer district

Madison, Dane County, and the Madison Metropolitan Sewerage District each run their **own**
Legistar client. A scan that finds `madison` and stops has not looked at the county board — which
holds the jail, the sheriff, human services, and county zoning — or at the body that sets sewer
rates.

`mmsd` was reachable and returned `Commission`, `Operations Committee`,
`Policy, Finance & Personnel Committee`, and two ad hoc committees including one on green
infrastructure implementation policy; its most recent Commission meeting was **2026-07-27**. This
is precisely the body `district-issue-scan` singles out: "Water and planning are the
highest-yield and lowest-competition sources in this list. A rate increase adopted at a
sparsely-attended utility board meeting shows up on every household's bill and has usually never
been explained to anyone." **It is reachable by public API, and this scan still did not pull a
single rate action from it.** That is the largest self-inflicted gap in the Madison files, and it
is the first thing the next person should do.

Meanwhile the Madison **Water** Utility Board is *inside* the city instance as `BodyId` 36 — a
different pattern from the sewerage district, in the same city, for the same category of
decision. Do not assume a consistent structure even within one municipality.

### 5. Meeting records exist; the two things the skill ranks on do not

`district-issue-scan` ranks salience on, among other things, **public-comment speaker counts**
and **contested vote tallies**. On this instance, through the API, neither is available. Nothing
in `Events`, `EventItems`, or `Matters` carries a registrant or speaker count. Both live in the
minutes PDF.

The practical consequence for `district-issues.md`: **no issue in it is ranked on a
public-comment count, because no public-comment count was verified.** The ranking rests instead
on dollar figures, enactment numbers, referral chains, procedural outcomes such as a withdrawal,
and counts of recurring matters — all of which the API does give. That is a weaker basis than the
skill's ideal and it is stated in the file rather than papered over. A scan that wants comment
counts must read minutes, and there is no shortcut.

### 6. A media map goes stale faster than anything else in the campaign folder, and it fails silently

Tone Madison, an independent Madison politics and culture outlet, **stopped publishing in April
2026** ([tonemadison.com](https://tonemadison.com/articles/tone-madison-is-saying-goodbye/),
retrieved 2026-08-04). Any Madison media list assembled from a 2025 source still lists it. A
pitch sent there gets no bounce and no reply — it is not an error state, it is silence, which is
indistinguishable from being ignored.

That single row justifies the skill's "recheck the whole map every thirty days" tip better than
the tip does. There is a second-order point worth recording: **the archive is still live and
still citable.** For `canonical-presence` purposes a dead outlet's archive can still be what an
answer engine retrieves, so "closed" and "irrelevant" are not the same status.

### 7. The most important field in the media map is the one nobody publishes

`district-media-map` step 7: find the election-period rule and turn it into a date. **It is not
published by any of the five outlets profiled.** Not on the Wisconsin State Journal's letters
page, not on its submission form, not on the Cap Times submission form, and not in the Cap Times
opinion policy — which discusses letters, op-eds, word limits, and editorial standards at length
and never mentions candidates or elections.

So the skill's fallback is the only path: a human calls the newsroom in the morning and asks. The
map records it as `[UNVERIFIED]` for all five outlets, which is the honest state, and flags it as
priority one in the closing checklist. **A campaign cannot resolve this field from the web.** Any
scan that returns a confident cutoff date for these outlets invented it.

### 8. "Convert it against Nov 3, 2026" is the wrong election

`district-media-map` step 7 hardcodes November 3, 2026 as the conversion date, and the same
assumption runs through `district-issue-scan` step 7 ("Ask the county board of elections for the
certified November 3, 2026 ballot"). For the offices this playbook is aimed at, that date is
wrong in Wisconsin.

Wis. Stat. 5.02(21) makes the **spring election**, held the first Tuesday in April, the one that
elects "judicial, educational, and municipal officers, and non-partisan county officers." Madison
alder seats, Madison Metropolitan School District Board of Education seats, and nonpartisan Dane
County Board of Supervisors seats are all filled then. Next spring election: **April 6, 2027**.
Spring primary: **February 16, 2027** ([City of Madison
Clerk](https://www.cityofmadison.com/clerk/elections-voting), retrieved 2026-08-04). November 3,
2026 is the partisan general for federal, state, and partisan county offices ([Wisconsin
Elections Commission 2026–2027
calendar](https://elections.wi.gov/sites/default/files/documents/2026_2027%20Election%20Calendar_0.pdf),
retrieved 2026-08-04).

A campaign for a Madison alder seat that computed a 14-day media cutoff against November 3, 2026
would be off by five months. **The generalizable fix is to resolve the election date for the
specific office before computing any cutoff, and never to carry a date forward from the skill
text.** This is now stated as a rule in
[`reference/shared-rules.md`](../../reference/shared-rules.md) Rule 7.

### 9. The voter-guide deadline had already passed at scan time

LWV Dane County's Candidates' Answers guide for the November 3, 2026 ballot closed on **June 22,
2026**, extended to **9:00 pm on July 14, 2026**
([lwvdanecounty.org](https://www.lwvdanecounty.org/be-a-voter), retrieved 2026-08-04). The scan
ran on August 4, 2026. For a candidate on that ballot, the single most important nonpartisan
voter-guide surface in the district was three weeks gone before the media map existed.

This is not a research failure; it is the finding. It argues for something the skill sequence
implies but does not state: **the deadline inventory should be built first, before the outlet
profiles**, because outlet profiles keep and deadlines expire.

### 10. Same-name and same-building confusions

Two small ones worth recording because both produce plausible wrong answers:

- **The Cap Times publishes two different letters addresses.** Its staff page gives
  `tctvoice@captimes.com`; the standing footer on published letters gives
  `tctvoice@madison.com`. Both are the outlet's own published text. The map records both and says
  which to prefer. A scan that finds one and reports it as the address is right by luck.
- **The Cap Times and the Wisconsin State Journal share a street address**, 1901 Fish Hatchery
  Road, Madison, WI 53713, and a print distribution relationship, while being editorially
  separate with separate opinion pipelines and separate word limits (250 versus 200). Treating
  them as one outlet, or assuming a submission to one reaches the other, is an easy and
  consequential error.

---

## What was verified, and what was not

### Verified from primary records

- Three Legistar clients reachable without authentication: `madison` (252 bodies, 61 active),
  `dane` (166 bodies, 40 active), `mmsd`.
- 3,772 Madison matters introduced 2025-08-01 to 2026-08-04, retrieved in six date-chunked
  requests.
- 25 Madison Common Council meetings in the window, with per-meeting agenda and minutes status
  and item-level action names.
- **ORD-26-00002**, data center and telecommunications moratorium creating MGO 28.140. Introduced
  2025-12-04, Plan Commission recommendation after public hearing 2026-01-12, adopted unanimously
  2026-01-13, enacted 2026-01-24. Legistar file 91135.
- **Ordinance file 92386**, public reporting requirements for the Office of the Independent
  Monitor and Police Civilian Oversight Board. Full five-month referral chain, two adverse
  recommendations from the Oversight Board (2026-03-25, 2026-07-23), **withdrawn at Common
  Council 2026-08-04**.
- **RES-26-00291**, additional **$6,000,000** to AECOM Technical Services for North-South BRT
  project development. Adopted 2026-05-19, enacted 2026-05-22. Legistar file 92934.
- **RES-25-00649**, up to **$13,963,000** from the Affordable Housing Fund for four projects,
  approximately 425 rental units of which 263 affordable. Adopted 2025-12-09, enacted 2025-12-16.
- 2026 City Budget resolution authorizing a 2025 general property tax levy of **$326,666,421**
  for City of Madison purposes. Substitute adopted 2025-10-28, Legistar file 90658.
- Three watershed study final reports — Central Isthmus (92774), East Isthmus and Yahara River
  (92775), Warner Park and Cherokee Marsh (92776) — all introduced 2026-04-15 and accepted
  2026-04-22, each listing affected alder districts.
- Individual Bartillon Shelter change orders, by number and exact amount, as listed in
  `district-issues.md`.
- **47** matters containing "Assessment District" introduced in the window.
- **Zero** matters containing `referend` or `F-35` introduced in the window.
- Wisconsin spring election 2027 dates and the statutory basis for which offices are filled then.
- Submission mechanics: Wisconsin State Journal 200-word letters, `wsjopine@madison.com`, online
  form, P.O. Box 8058, once-per-month cap; Cap Times 250-word letters and ~700-word op-eds,
  `tctvoice@captimes.com`, opinion desk staffing.
- Cap Times beat structure: eleven named editorial staff with published beats.
- Cap Times endorses in Madison Common Council races, and did so in at least one cycle without
  interviewing candidates — confirmed in the outlet's own published letter quoting its opinion
  editor.
- Isthmus is a 501(c)(3) nonprofit, founded 1976, fifty years in print as of April 2026, editor
  Judith Davidoff, publisher Jason Joyce.
- Madison365 is operated by 365 Media Foundation, a 501(c)(3); editor in chief A. David Dahmer,
  executive editor Robert Chappell.
- Tone Madison ceased publishing April 2026.
- LWV Dane County deadlines for the November 2026 guide; Know Your Candidates as a joint LWV
  Dane County / Madison City Channel video series with existing Alder, Dane County Board, and
  Madison School Board episodes.

### Not verified, and what it would take

| Gap | What it would take |
|---|---|
| **Any vote tally** | Parse the 122 plain-"Adopt" items' minutes PDFs. Half a day |
| **Any public-comment count** | Same PDFs. Same half day |
| **MMSD Board of Education records** | No vendor identified. Start from the district's own site. **This is disqualifying for a school-board race** and is the largest substantive hole |
| **Madison Water Utility rate cases** | Wisconsin **Public Service Commission** dockets. Not searched at all. Highest-value remaining target |
| **Madison Metropolitan Sewerage District rate actions** | `mmsd` Legistar is reachable; no matters pulled. Second-highest-value target |
| **Dane County matters and events** | `dane` confirmed reachable, 40 active bodies enumerated, **nothing pulled**. Mandatory for a county supervisory race |
| **Fourteen-day original-reporting test on any outlet** | Read fourteen days of five local sections, tally local bylines against wire and press-release reprints. Roughly five minutes per outlet per the skill; realistically an hour |
| **Election-period cutoffs** | Phone calls. Cannot be resolved from the web |
| **Individual reporter emails** | Read bylines, or ask the desk. **Do not guess the pattern** |
| **Isthmus submission rules** | Read isthmus.com's own submissions page. The values in the map came from a search summary |
| **Paywall status for WSJ and Cap Times** | Test in a clean browser session |
| **Community platforms** | Identify neighborhood associations and their groups from the city's neighborhood association list; read each group's pinned political-posting rules. Member counts for private groups cannot be verified without joining |
| **Certified November 3, 2026 Dane County ballot** | Request from the Dane County Clerk |
| **April 6, 2027 nomination paper deadlines** | Wisconsin Elections Commission or City of Madison Clerk |
| **OCD-ID resolution** | The `ocd_id` in the frontmatter is constructed from the Open Civic Data naming convention, **not** retrieved from Google Civic Information `divisionByAddress`. No address was resolved and no district boundary was fixed |
| **Ownership of the Wisconsin State Journal** | Cited to Wikipedia in the map and flagged as secondary. Confirm from an SEC filing or the outlets' own about pages |
| **Bodies never scanned** | Plan Commission, Zoning Board of Appeals, Landmarks Commission, Community Development Authority, Library Board, Board of Health, Police and Fire Commission, Capital Area Regional Planning Commission. All confirmed active in the `Bodies` response; none had a calendar pulled |
| **Human approval** | `district-issue-scan` step 10 and `district-media-map` step 11. Has not happened for either file |

### Deliberately not done

- **No minutes PDFs were parsed.** Their URLs are recorded; the extraction is the next person's
  work and is called out in both files.
- **No per-parcel special assessment amounts were extracted.** They are in the schedule-of-
  assessments attachments to each resolution, and they are named individuals' property records.
  They are public records to be read in context, not data to be bulk-extracted into a campaign
  file. See [`reference/shared-rules.md`](../../reference/shared-rules.md) Rule 5.
- **No community platform rows were invented.** The table in the media map is empty with an
  explanation, which is the correct output when member counts and moderators cannot be verified.
- **No claim was made about the police shooting referenced in a Cap Times headline.** The
  headline was verified as appearing in the outlet's most-read list on 2026-08-04. The story was
  not opened, and `district-issues.md` says so explicitly at the point of use.
- **No total was computed for the Bartillon Shelter change orders.** The individual amounts
  retrieved are listed; the full series and the original contract award were not retrieved, so a
  total or a percentage overrun would be an unsupported number. This is the single most tempting
  place in the file to produce a satisfying figure that is not in a source.

---

## Suggested changes to the repo

These came out of building the file rather than reading it, and each names a specific line.

1. **`reference/local-agenda-systems.md`** describes `/Matters/{id}/Histories` as returning "the
   vote history on one item, including who voted how." Qualify it: the field exists, is not
   populated on every client, and returns an empty array rather than an error when it is not.
   Add the check — pull one known-contested matter and confirm the field is populated before
   relying on it.
2. **Same file, same table.** Note that a response of exactly 1,000 records is a truncation
   signal, not a result, and that no field in the response indicates it.
3. **`district-issue-scan` step 2** could say that one municipality may have several Legistar
   clients, and that utility and sewer districts sometimes have their own — which is where the
   skill's own "follow the money" tip points.
4. **`district-media-map` step 7 and `district-issue-scan` step 7** hardcode November 3, 2026.
   Replace with an instruction to resolve the election date for the specific office first.
   Wisconsin and Illinois both hold their local elections in April, and between them that covers
   both golden districts.
5. **`district-media-map`** might add a step ordering: build the deadline inventory — voter
   guides, questionnaires, forum conveners, election cutoffs — **before** profiling outlets.
   Outlet profiles keep; deadlines expire, and one had already expired here.
6. **Both skills** would benefit from an explicit instruction that a null or empty field is not
   evidence of absence. That is the single behavior that separated a correct output from a
   plausible false one at three different points in this scan.
