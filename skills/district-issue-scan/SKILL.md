---
name: district-issue-scan
description: Builds a ranked, evidence-backed inventory of what people in one specific jurisdiction actually argue about. Detects the local agenda-software vendor from the hostname, pulls meeting records through its API or a supported scraper, reads local coverage, catalogs local ballot measures, and surveys who already publishes a good answer on each issue. Ranks by documented salience — public-comment counts, contested votes, rate increases with dollar figures, petitions — never by national issue polling. Use this when a campaign needs to find the real local issues in a district, research a city council or county commission or school board record, identify the ballot measures voters will see alongside the race, or work out which issues are worth writing about because nobody has answered them well yet.
---

# District Issue Scan

**Reads:** nothing required. Takes a jurisdiction name and a street address inside the district.
**Writes:** `campaign/district-issues.md`, using
[`campaign-template/district-issues.md`](../../campaign-template/district-issues.md).

"Housing" is not a district issue. "The 5–2 vote to approve the Cutler Road annexation after
forty-one people signed up for public comment" is. Most issue research fails the same way —
national talking points with a place name dropped in — and the defense is mechanical: every
issue in the output carries a primary record with a URL and a retrieval date, or it stays out.

## Find the sources before you look for issues

There is no national registry of local agenda systems, and any skill that ships a fixed list is
wrong in most of the 3,000-plus US counties. Detect the vendor instead. This procedure is the
skill; the rest is bookkeeping.

**1. Find the jurisdiction's official agenda page.** Search `"<jurisdiction> council agenda"`,
then `"<jurisdiction> board of commissioners minutes"`. Start from the `.gov` or `.us` site.
Many official sites link out or iframe to a vendor, so follow the link and watch the URL bar.

**2. Read the hostname.** The vendor is almost always in it.

| Hostname pattern | Vendor | How to pull |
|---|---|---|
| `{client}.legistar.com` | Legistar (Granicus) | Public web API — see below |
| `{st}-{jurisdiction}.civicplus.com/AgendaCenter` | CivicPlus | `civic-scraper` |
| `{jurisdiction}.granicus.com` | Granicus | `civic-scraper` |
| `*primegov.com` | PrimeGov | `civic-scraper` |
| `*civicclerk.com` / `*.portal.civicclerk.com` | CivicClerk | `civic-scraper` |
| PDFs on the jurisdiction's own site | none | Manual extraction |

**3. Use the vendor API or a supported scraper.** Legistar exposes a public API at
`https://webapi.legistar.com/v1/{Client}/{Endpoint}`, commonly without authentication. Useful
endpoints: `/Events`, `/Matters`, `/Matters/{id}/Histories`, `/Bodies`, `/Persons`. Responses
cap at 1,000 records and support OData filtering
([Granicus](https://support.granicus.com/s/article/Legistar-Web-API),
[examples](https://webapi.legistar.com/Home/Examples), retrieved 2026-08-04).
[`civic-scraper`](https://github.com/biglocalnews/civic-scraper) supports CivicClerk, CivicPlus,
Granicus, Legistar, and PrimeGov.

⚠️ **Do not read vote tallies out of the API.** On Madison's instance `MatterHistoryTally` was
null on every matter checked and `/EventItems/{id}/Votes` returned empty, across 25 meetings
with no recorded dissent — the tallies are in the minutes PDF only
([`golden/madison-dane-county-wi/NOTES.md`](../../golden/madison-dane-county-wi/NOTES.md)). The
failure is silent and it inverts the finding: an empty tally read as consensus turns a contested
12–7 vote into "unanimous," when the split was the whole story. Take tallies from the minutes,
or record the vote as unretrieved and name the meeting to open.

**4. Fall back to official documents and manual extraction.** No vendor is normal for water
districts, library boards, and small townships. Download the last twelve months of agenda and
minutes PDFs and read them. This is slow and it works.

**Three traps before you conclude "no records exist"** — all three were hit in real scans
([`golden/`](../../golden/)), and all three look identical to an empty county:

- **The CMS is not the agenda system.** A "Government Websites by CivicPlus®" footer does not
  mean `/AgendaCenter` exists. Sullivan County, NH's returns 404 while the records sit in nine
  public SharePoint folders. Follow the site's own "Agendas & Minutes" link and see where it
  lands; do not infer the portal from the footer.
- **Public document libraries defeat scrapers, not browsers.** SharePoint, Google Drive, and
  Dropbox links return a login redirect or a JS stub to `curl` while opening fine for a human.
  Retrieve them in a browser. A complete public record can look like none at all.
- **Image-only PDFs extract to nothing and raise no error.** Under ~100 characters per page
  means it is a scan — rasterize and OCR. Check the draft minutes too; in Sullivan the draft had
  a text layer and the ratified version did not. Re-verify any OCR'd number before publishing it.

### Worked example — Cordwell County, Ohio (invented)

Searched `Cordwell County commissioners agenda`. Top result is
`cordwellcountyoh.gov/government/agendas`, a page of links; clicking "Meeting Calendar" lands on
`cordwellcounty.legistar.com/Calendar.aspx`. Hostname says Legistar, client slug
`cordwellcounty`. Therefore:

```
https://webapi.legistar.com/v1/cordwellcounty/Events?$top=100
  &$filter=EventDate gt datetime'2025-08-01'
https://webapi.legistar.com/v1/cordwellcounty/Matters?$filter=MatterTypeName eq 'Ordinance'
```

Then searched `Halstead Falls school board agenda`, landing on
`oh-halsteadfalls.civicplus.com/AgendaCenter`: CivicPlus, no public API, so `civic-scraper` with
that URL. Cordwell Regional Water District posts board packets as PDFs on a WordPress site, no
vendor at all — twelve months of PDFs, read by hand. That is where the sewer-rate fight was.

## Which bodies to scan

City or village council, county commission, school board, water and sewer district, planning and
zoning, library board, transit authority — plus any special district that levies a tax or rate.

**The boring bodies carry the most locally salient fights.** Nobody covers the water district,
which is exactly why a double-digit rate increase there produces angrier voters than anything
the county commission did all year, and why no other candidate in the race will have read the
packet. It arrives on every household's bill and has usually never been explained to anyone.

## Which jurisdictions

Get the district boundary right first, or you will research a council the voters cannot vote for.

- Google Civic Information API's `divisionByAddress` still returns Open Civic Data IDs for an
  address even though the Representatives API is closed
  ([announcement](https://groups.google.com/g/google-civicinfo-api/c/9fwFn-dhktA), retrieved
  2026-08-04). Record the OCD-ID in the output frontmatter.
- Open States API v3 `/people.geo` maps a point to state legislators. It needs an `X-API-KEY`;
  plan for about 10 requests per minute and 500 per day
  ([docs](https://docs.openstates.org/api-v3/), retrieved 2026-08-04). For statewide work pull
  the bulk CSV at `https://data.openstates.org/people/current/{state}.csv` instead.
- **Open States barely covers local offices.** For school boards, county commissions, and
  special districts, use the official county or municipal site and the county board of elections.

**Then ask which of these bodies is actually on the ballot this cycle, and mark each one.** In
the Whatcom County scan this got skipped, and the run produced well-sourced council fights for a
council with **no seat on the November 2026 ballot** ([`golden/whatcom-county-wa/NOTES.md`](../../golden/whatcom-county-wa/NOTES.md)).
Those issues are still worth knowing — they are context — but they are not the race, and a
candidate who cannot tell the difference builds a platform for an office nobody is electing.
Confirm against the county auditor or elections office, and remember that
[many states elect local offices in spring, not November](../../reference/shared-rules.md).

**When a special district has no findable portal, work backwards from the ballot.** Whatcom Fire
Protection District No. 1 has no locatable agenda system at all; its levy measure surfaced only
through the **county auditor's ballot-resolution page**, which lists what each district
certified. The auditor knows what a district put on the ballot even when the district publishes
nothing.

## Output Format

Write `campaign/district-issues.md` following the template field for field: frontmatter
(`jurisdiction`, `ocd_id`, `scan_date`, `scan_window`, `governing_bodies`, `agenda_vendor`,
`date_created`, `date_modified`), then `## Sources checked`, `## Ranked issues`,
`## Contested space summary`, `## Ballot measures on the same ballot`, `## Dead ends and gaps`.
Each ranked issue carries: what it is, salience evidence, who is affected and how many, stage,
decision-maker, who currently speaks on it, quality of what exists, primary records. Three to
eight issues. Fifteen issues means you did not rank; you listed.

## Steps

1. **Fix the boundary.** Resolve the district to an OCD-ID and write down every governing body
   whose seats or levies appear on this ballot. Set `scan_window` to at least twelve months.
2. **Run the detection procedure** above, once per body. Record the vendor for each in the
   sources table even when the answer is `none-found`.
3. **Pull the record.** Agendas, minutes, and vote tallies for the window. Minutes matter more
   than agendas — agendas say what was scheduled, minutes say who showed up and shouted.
4. **Search local news archives** on the outlet's own site, not just Google: `site:` the local
   paper, the nonprofit statewide newsroom, the county's legal-notices page. Note the paywall
   status of anything you cite.
5. **When there is no local news**, substitute primary records plus what people say in public:
   public-comment sign-in sheets, letters read into the record, board correspondence packets,
   the county auditor's rate and levy filings. Say plainly in `## Dead ends and gaps` that no
   outlet covers this body. That is a finding, not a gap in your effort.
6. **Catalog local ballot measures** on the same ballot, from the county board of elections
   certified ballot. Levies, bond issues, charter amendments, and zoning referenda come up at
   every door, and a candidate without a position on the school levy looks unprepared.
7. **Rank by documented salience.** Each rank rests on evidence: a public-comment count from the
   minutes, a contested vote with the tally, a rate increase with its dollar figure and
   effective date, a petition's signature count, repeated local coverage. Neither assumption nor
   national polling ranks. If the only support is "people care about this everywhere," cut it.
8. **Run the contested-space survey.** For each issue, find who currently publishes an answer —
   incumbents, the county itself, advocacy groups, the paper — and judge how good it is. Fill
   the `## Contested space summary` table. **This is the field every scan skips and the one that
   decides whether writing about the issue is worth the campaign's time.** Three institutions
   covering an issue well makes it expensive to own and pointless to try. An issue where the
   honest answer does not exist anywhere is nearly free.
9. **Fill `## Sources checked` completely**, including the dead ends.
10. **Get human approval.** Walk a human through the ranked list and ask: *does this match what
    you hear at doors?* Where it does not, find the record or drop the issue. Do not reorder on
    vibes alone — record what changed and why.

## Rules that do not bend

Sourcing, copied from [`reference/shared-rules.md`](../../reference/shared-rules.md) Rule 2:

> Source every factual claim inline, with the source date. Format:
> `claim ([source name](url), retrieved 2026-08-04)`.
>
> Quotes, endorsements, statistics, bill numbers, vote counts, dollar figures, and dates are
> copied from a source or omitted. There is no third option. If you cannot find the number,
> write `[NEEDS SOURCE — <what to look up>]` and keep going. Do not approximate a figure you
> half-remember, and do not reconstruct a quote from its gist.
>
> Prefer primary records — the actual ordinance, the actual budget line, the actual meeting
> minutes — over reporting about them. When you cite reporting, cite the outlet and the
> reporter.

**Log every dead end and every empty result in the sources table.** A source you checked that
yielded nothing is a real finding: it stops the next person re-running your search, and it is
the difference between an honest map of a news desert and a padded one. The Yield column reads
`0 — no coverage of this body since 2024`, never blank.

## Doing this without an agent

A library computer, a notebook, and roughly two working days. Do it in this order.

1. Write down every body that appears on this ballot: council, commission, school board, water
   district, planning and zoning, library, transit. One page in the notebook per body.
2. For each body, search `"<body name> agenda"` and click through to the calendar. Write the URL
   down. If the address says `legistar.com`, `civicplus.com`, `granicus.com`, `primegov.com`, or
   `civicclerk.com`, write the vendor too. If it is just PDFs, write "PDFs."
3. If it says `legistar.com`, note the word before `.legistar.com` — that is the client name.
   Type `https://webapi.legistar.com/v1/<client>/Events` into the address bar. A wall of text
   means you have the whole meeting list; save the page. An error means go back to the calendar.
4. Download the last twelve months of minutes for each body. Minutes, not agendas.
5. Read them with a highlighter. Mark three things: any vote that was not unanimous, any item
   with more than five public-comment speakers, and any rate, fee, or levy change with a dollar
   figure. Those three marks are your issue list.
6. Search the local paper's own website for each marked item. Save what you find, and write down
   what you searched and got nothing on — you will need that list.
7. Ask the county board of elections for the certified November 3, 2026 ballot; list every measure.
8. For each issue, spend fifteen minutes on who already explains it well. If a neighbor googled
   this tonight, would they find a straight answer? Write yes or no, and who from.
9. Rank the issues by the evidence you highlighted — comment counts, vote splits, dollar
   figures — not by which one feels biggest.
10. Type it into the template, one section per issue, every claim with a link and today's date.
11. Show it to someone who knocks doors. Fix what does not match, but only by finding a record.

## Tips

**Minutes over agendas, always.** An agenda tells you what somebody scheduled. Minutes tell you
who came, who spoke, and how the vote split. Salience lives in the minutes.

**The place-swap test.** Replace the jurisdiction name in your issue list with a different
county. If the list still reads fine, you have written national issues and the scan failed.

**A non-unanimous vote is a gift.** Almost everything passes local bodies unanimously, so a 4–3
vote means somebody's constituents were angry enough to move a member — and there is a recorded
reason why. Start there.

**Follow the money.** Rate increases, levy renewals, and bond issues put a bill in every mailbox
in the district — salience that arrives whether or not anyone is talking about it. And an issue
that has returned to the same board four times in two years beats one loud meeting.

**Do not let the contested-space survey drift into "nobody covers this."** Check the incumbent's
site, the county's own explainer pages, pinned posts in the local Facebook group, and advocacy
organizations. The honest finding is often "covered, but only by the people who caused the
problem" — which is the best possible opening.
