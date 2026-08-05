# Golden districts

> **Real places, real records, no real candidates.** Every jurisdiction, governing body,
> meeting record, vote, dollar figure, docket number, and news outlet in this directory is
> real and linked to a public source. **No candidate appears anywhere in it, and nothing in it
> is attributed to a real person running for office.** Where a real official is named, the
> file cites only something they have actually published or done in the public record, with a
> link. An AI-generated "position" attached to a real candidate's name is the exact
> fabrication this repository exists to prevent, and it would do the most damage coming from
> the reference examples.

**Research window:** all four districts were scanned on **2026-08-04**, against records covering
roughly 2025-08 through 2026-08. Every "retrieved" date in every file is that day. The general
election these were written against is **November 3, 2026** — with the caveat, below, that it is
the wrong election for local office in three of the four places.

**Not human-verified.** These are AI-assisted research outputs. Every claim carries a source link
and a retrieval date, and unconfirmed claims are marked `UNVERIFIED` in place, but no person has
independently checked them line by line. Read [the section on this](#these-have-not-been-verified-by-a-human-line-by-line)
before citing anything here.

**Validator:** `python3 scripts/validate_skills.py` does not read this directory; it was run
before and after these files were added and reported the same result both times.

---

## What a golden district is

The nine campaign skills have eval fixtures under `skills/*/evals/`. Those fixtures use
invented places and invented people on purpose, because their job is to test *refusal* — does
the skill decline to write a position that is not in `positioning.md`, does it mark an
unsourced number, does it refuse to draft an anonymous community post. A fixture that used a
real district would put real unreviewed claims in a public repository.

Fixtures cannot tell you what good output looks like against a real place. That is what this
directory is for. Each golden district is the output two research skills would produce if run
carefully against a real US jurisdiction, using only public records, with every claim linked:

- [`district-issue-scan`](../skills/district-issue-scan/SKILL.md) →
  `district-issues.md`
- [`district-media-map`](../skills/district-media-map/SKILL.md) →
  `district-media-map.md`

Plus a written record, per district, of what could and could not be found — a separate
`NOTES.md` in two of them, and the sources-checked table plus `## Dead ends and gaps` sections
in the other two. **The failure log is the most useful thing here.** A clean output teaches you
the schema; the failure log teaches you what actually happens when you try. The sources-checked
tables deliberately include the rows that yielded nothing, because in a news desert "searched
the county agenda center for 2025–2026, found image-only PDFs, no vendor system" is not an
absence of a finding. It is the finding.

## The districts

Three districts, produced by two separate runs of the same two skills on 2026-08-04. Whatcom
and Sullivan are a matched pair — one place with working local news, one news desert — because
the contrast is the thing being demonstrated. Madison is a third, deeper scan of a large
jurisdiction with three separate Legistar instances. Read the pair on its own; read Madison
across it to see how much of the output is the procedure and how much is the place.

> **A fourth district, Alexander County, Illinois, was planned and never produced** — the run
> that was writing it ended before it got there. Earlier drafts of this file described it, and
> those references have been removed. Nothing in this directory depends on it. It remains the
> obvious next contribution: a Medill-identified news desert in a state neither pair covers.

### The pair — Washington and New Hampshire

| | [`whatcom-county-wa/`](whatcom-county-wa/) | [`sullivan-county-nh/`](sullivan-county-nh/) |
|---|---|---|
| **Place** | Whatcom County, Washington (Bellingham, Ferndale, Lynden, Blaine, Point Roberts) | Sullivan County, New Hampshire (Claremont, Newport, Charlestown and twelve more towns) |
| **Why chosen** | A locally owned startup daily, an independent nonprofit newsroom, a 34-year-old volunteer community monthly and a McClatchy paper all covering the same county; plus a live citizen initiative, a contested county ferry tax, and a Legistar instance with a working public API | The *Eagle Times* closed in July 2025 after 192 years of publishing from Claremont. Northwestern's 2025 State of Local News Report codes Sullivan as a **zero-source county** — one of only two in New Hampshire with fewer than three locally based papers, and the only one with none ([Keene Sentinel](https://www.keenesentinel.com/news/local/twin-state-valley-nh-vt-reflects-on-life-without-local-news/article_a516c6ec-1e12-417b-a511-f71958d9d06d.html), retrieved 2026-08-04) |
| **Media assessment** | `healthy` | `thin` — see below; this is a deliberate departure from the Medill classification |
| **Agenda vendor** | Legistar (`whatcom.legistar.com`), public API working and high-yield; one special district's portal could not be located at all | `none-found` — the county publishes to a **public SharePoint document library**, a vendor class the detection procedure does not currently name |
| **Outlets found** | 8 | 10, of which exactly **one** is based in the county — and it is a public-access TV station, not a newsroom. One more is software. |
| **What the pair demonstrates** | What "contested space" looks like when several outlets have already published good answers, so the campaign's job is to find the gap rather than fill the void | That a county-of-publication news-desert count misses the out-of-state weekly that actually covers the city, the PEG channel that holds the video record, and the unsigned AI service that has quietly become the largest published index of both |

The desert cases are the point of both pairs. `district-media-map` is supposed to treat a
two-row map as a finding rather than a failure, and `canonical-presence` is supposed to carry
more weight where there is no reporter to pitch. Neither claim means anything until you can
see it done.

**One difference in form.** The Wisconsin and Illinois districts record their failures in a
separate `NOTES.md`. The Washington and New Hampshire districts record theirs inline, in the
`## Dead ends and gaps` section that `district-issues.md` already provides, and in the
sources-checked table above it — including the rows that returned nothing. Either placement
works; the requirement is that the failures are written down somewhere a reader will find them.

## The rule: real district data, invented candidates

**Use real district data. Never attach a profile, a position, or a quote to a real person
running for office.**

Real, and used freely here: jurisdictions, governing bodies, ordinance and resolution numbers,
meeting dates, enactment dates, regulatory docket numbers, dollar figures, news outlets, their
owners, their published submission rules, their staff pages, and the published work of named
reporters.

Invented, always: candidates. There is no candidate in these files at all, which is possible
because `district-issues.md` and `district-media-map.md` are the only two artifacts in the
campaign folder that carry no candidate content by design — neither template has a candidate
field. That is exactly why they were chosen as the golden set.

**If you extend a golden district into a candidate-attributed artifact** —
`candidate-profile.md`, `positioning.md`, `answers/`, `briefs/`, `placements/`, `pitches/` —
the candidate must be invented, and must be obviously invented. Use a name that cannot be
mistaken for a real person and label it in the frontmatter, for example
`candidate: "EXAMPLE — Rosalind Thackeray (invented, not a real candidate)"`. Do not use the
name of anyone who has ever filed for office anywhere.

### Why the line is here and not somewhere more convenient

It would be more useful, in the narrow sense, to show a complete campaign folder for a real
race. It is not worth it. The failure mode this repository exists to prevent is a language
model producing a confident, plausible, fabricated position and that position ending up in a
voter guide under a real candidate's name. Reference examples get copied, adapted, quoted, and
scraped more than any other file in a repository. A fabricated position seeded from
`golden/` would travel further and be trusted more than the same error made by a campaign
volunteer at 11pm.

Naming real *officials* is different, and it is required by the schema:
`district-issues.md` has a **who currently speaks on it** field, and filling it means saying
which officials, outlets, and organizations have published a position. Everything of that kind
in these files is a link to something the person actually did or published, described in the
narrowest terms the record supports. Where the record shows only that a person put an item on
an agenda, that is all the file says.

### Personal data

No private individual's personal contact details appear here. A newsroom tips line, an opinion
desk address, a reporter's published work email, and a government office's main phone number
are public record and are included. A personal mobile number, a home address, or an email
address inferred from a `first.last@` pattern is not, and none appears. The Cap Times staff
page does not publish individual reporter emails; that file records the desk address it
publishes and says so, rather than guessing the pattern. The Sullivan County map does the same
thing in a harder case: it names the county's only dedicated reporter, because he is quoted
about his own beat in a published news story, and then leaves his email as
`[not published on the pages I checked]` rather than deriving it from a colleague's address —
even though the colleague's address is right there and the pattern is obvious. A guessed address
that happens to be correct is still a guess, and the next one will not be. See
[`reference/shared-rules.md`](../reference/shared-rules.md) Rule 5.

## How to use these

**As a reference.** Read
[`sullivan-county-nh/district-media-map.md`](sullivan-county-nh/district-media-map.md) before
you write a media map for a rural county, so you know what a legitimate short answer looks
like. Read
[`madison-dane-county-wi/district-issues.md`](madison-dane-county-wi/district-issues.md) to see
what "salience evidence" means in practice:
an enactment number, a withdrawal date, a change-order amount, not an adjective. Read
[`whatcom-county-wa/district-issues.md`](whatcom-county-wa/district-issues.md) for the
**contested-space** field done at length — the section that asks who already publishes a good
answer on each issue, and which is the field runs skip most often. Read
[`sullivan-county-nh/district-issues.md`](sullivan-county-nh/district-issues.md) for what a scan
looks like when the records are public but nothing indexes them, and
[`sullivan-county-nh/district-media-map.md`](sullivan-county-nh/district-media-map.md) for a
real published cost of earned media: the one weekly that reaches Claremont charges **$75 for a
200-word political letter and $0.50 a word after that**, and the regional daily forbids
reproducing its work in political material at all. Those two rules change a plan more than any
reporter's name in the file.

**As a benchmark.** Run `district-issue-scan` against one of these jurisdictions and compare.
Useful questions: did the run detect the right vendor for each body, or assume one? Did it
invent a vote tally that the API does not actually expose? Did it check the county's *own*
site or trust a same-named county in another state? Did it log the dead ends, or silently drop
them? Did it assume the local election is in November?

**As a caution.** Everything here decays. Election cutoffs, reporter beats, staff pages, and
portal URLs are the fields most likely to be wrong first, and a media map is only as good as
its last recheck. The Madison map already contains one outlet that shut down in April 2026 and
would have been listed as live by any scan built from a 2025 source. Treat every date in these
files as the date it was checked, which is what it is.

**As a starting point for a fifth district.** The most useful thing anyone could add here is a
golden district with a vendor none of these four hit. Between them they cover Legistar (three
instances), Granicus, a WordPress PDF dump and a public SharePoint library. Still unrepresented:
**CivicClerk**, **CivicPlus Agenda Center**, a county whose record exists only as a YouTube
livestream with no written minutes at all, and any jurisdiction where the working language of
the public record is not English. See [`CONTRIBUTING.md`](../CONTRIBUTING.md).

**And read the next section before you cite any of it.**

## These have not been verified by a human, line by line

Say this plainly, because the rest of this README is about how carefully these were built and
that can leave the wrong impression.

**Every file in this directory is AI-assisted research output. A person has not independently
checked it claim by claim against the underlying documents.** What was done: each URL was
fetched and its status recorded, every factual sentence carries a source link and the date it
was retrieved, and things that could not be confirmed are marked `UNVERIFIED` in place rather
than dropped or smoothed over. What was not done: a second reader opening each source and
confirming that it says what the file says it says.

Specific things most likely to be wrong, in rough order:

- **Numbers read out of OCR.** Several rate figures in the Sullivan County file were recovered
  from rasterized scans. OCR misreads digits. The file flags where this applies. **Re-read those
  tables against the original PDF before quoting a dollar amount in public.**
- **Vote tallies transcribed from minutes.** Read by machine from a PDF, not confirmed against
  video.
- **Draft versus ratified minutes.** At least one significant vote in the Sullivan County file is
  sourced to *draft* minutes, because the ratified version is an unsearchable scan. Draft minutes
  get corrected.
- **Anything about a person.** Reporter beats and desk addresses move. Every one here was copied
  from a page the outlet publishes, and none was inferred from a `first.last@` pattern, but they
  go stale within a cycle.
- **Submission rules and election cutoffs**, which outlets change without announcing.

The rule that follows from this: **these are a model of the format and a demonstration of the
method, not a citable source.** If a campaign wants to use a fact from one of these files, the
file gives it the link and the date — go read the link. That is what the links are for.

## Findings that apply beyond these districts

These surfaced while building these files. Each is recorded in full in the district's own
`NOTES.md` or `## Dead ends and gaps` section, but they generalize far enough to belong here.

**1. The Legistar public API does not return vote tallies on every instance.**
[`reference/local-agenda-systems.md`](../reference/local-agenda-systems.md) lists
`/Matters/{id}/Histories` as returning "the vote history on one item, including who voted
how." On Madison's instance it does not: `MatterHistoryTally` was null on every matter
checked, `/EventItems/{id}/Votes` returned an empty array, and across 25 Common Council
meetings the API surfaced no recorded dissenting vote. The tallies exist — in the minutes PDF.
A scan that trusts the field name and reports "unanimous" because the tally came back empty
will be confidently wrong. Details and the exact requests are in
[`madison-dane-county-wi/NOTES.md`](madison-dane-county-wi/NOTES.md).

**Confirmed independently on a second instance.** The Whatcom County run hit exactly the same
thing: `MatterHistoryTally` was null on every matter checked on `whatcom.legistar.com`, and the
7–0 and 4–3 roll calls reported in
[`whatcom-county-wa/district-issues.md`](whatcom-county-wa/district-issues.md) had to be read
out of the minutes PDFs. Two unrelated instances in two states behaving the same way is enough
to treat this as the default rather than a Madison quirk. **The reference document should say
so, and should say "get tallies from the minutes" as the primary method rather than the
fallback.**

**2. "Convert it against Nov 3, 2026" is the wrong election in three of these four places.**
`district-media-map` step 7 says to convert election-period cutoffs against November 3, 2026.
For the offices a first-time down-ballot candidate actually runs for, that date is wrong in
three of the four golden districts. Wisconsin elects municipal, school district, and nonpartisan county
officers at the **spring election in April**
([Wis. Stat. 5.02(21)](https://www.cityofmadison.com/clerk/elections-voting)); the next one is
April 6, 2027, with a February 16, 2027 primary. Illinois elects its local offices at the
**consolidated election in April of odd years**; Alexander County's last one was April 1, 2025
([Ballotpedia](https://ballotpedia.org/Alexander_County,_Illinois,_elections,_2025)). A
campaign that computed its media cutoffs against November 3, 2026 would have them wrong by
five months in Madison and by seventeen in Cairo.

Washington makes the same point from the other direction. Whatcom County elects its council at
the **odd-year general election**, so **no Whatcom County Council seat is on the November 3,
2026 ballot** ([Whatcom County Auditor, Current
Election](https://www.whatcomcounty.us/1732/Current-Election), retrieved 2026-08-04). Every
county vote described in that district's issue scan was cast by a body voters cannot replace
this cycle — which does not make those votes useless to a campaign, but does change completely
what they are useful *for*. **`district-issue-scan` should require the run to state which of the
bodies it scanned are actually on the ballot in the cycle being planned for.** It currently does
not, and it is an easy thing to get silently wrong.

**3. "Agenda vendor" has a fourth category the procedure does not name: the document library.**
`reference/local-agenda-systems.md` teaches hostname detection for Legistar, CivicPlus,
Granicus, PrimeGov and CivicClerk, then falls back to "PDFs on the county website." Sullivan
County, New Hampshire is none of those. It publishes its Board of Commissioners and County Delegation
records into a **public Microsoft SharePoint document library** reached from
[`sullivancountynh.gov`](https://www.sullivancountynh.gov/166/County-Commissioners). There is no
vendor hostname to match, no calendar page to scrape, and an ordinary HTTP fetch gets a login
redirect or an empty JavaScript shell — the records are fully public, and every naive detection
method reports that they do not exist. They were retrieved by driving a browser session against
SharePoint's own REST endpoints. **A scan that stops at "no vendor found, PDFs only" will
conclude a county with a complete public record has none.** SharePoint, Google Drive and Dropbox
folders are common in small counties and belong in the detection list with an explicit note that
they require a browser.

**4. Scanned PDFs with no text layer are the most dangerous kind of dead end, because they look
like an empty result.** The ratified minutes of the Sullivan County Delegation and Claremont's
206-page June 24 council packet are image-only scans. Text extraction returns zero characters.
Searching them returns nothing. Nothing in the pipeline reports an *error* — the honest-looking
output is "no records found." The June 24 water and sewer ordinance rate tables in
[`sullivan-county-nh/district-issues.md`](sullivan-county-nh/district-issues.md) exist only
because the pages were rasterized and run through OCR, and the July 2 TRAILS roll call was
recovered only because a *draft* version of the minutes, unlike the ratified one, still had a
text layer. **The procedure should say: if a PDF extracts to under roughly 100 characters per
page, it is a scan, not an empty document. Say so in the sources-checked table and OCR it or
mark it unread.** Silently treating it as empty is how a scan misses the thing it was run to
find.

**5. A dead newspaper's website can return HTTP 200.** `eagletimes.com` — the *Eagle Times* of
Claremont, 192 years old, closed July 2025 — resolves today and serves a hosting-provider
placeholder. Any link checker scores it live. Any media map built by crawling a 2024 outlet
directory will list it as an active outlet with a working site. **Check the front page for a
story with a date on it, not the status code.**

**6. Counting outlets by county of publication misses real coverage and real infrastructure.**
Sullivan County is a zero-source county in the national count, and yet the *Claremont City
Council is covered meeting by meeting* — by a free weekly published across the state line in
Ludlow, Vermont, which launched a Claremont edition specifically to do it. Meanwhile the
county's entire video record of council, school board, planning, zoning and county commission
meetings sits in a 6,676-item public archive maintained by a PEG access nonprofit that produces
no written journalism and therefore counts as nothing. The county-level assessment in that file
is `thin` rather than `desert` for this reason, and the file says plainly why it diverges from
the national classification. **But the split matters more than the label: Claremont city
government is thinly covered and Sullivan County government is not covered at all.**
`district-media-map`'s three-way healthy/thin/desert scale assumes one governing body per
jurisdiction. **It should be assessed per body, because that is where the actual gap is.**

**7. Something else has already moved into the vacuum, and it is a language model.** The largest
secondary index of Claremont's public record is
[MeetingWatch](https://meetingwatch.org/nh/claremont/) — an automated service that pulls the
meeting video off the town's own streaming platform, transcribes it, runs a fixed question set
over the transcript, and publishes a report within a day. In Claremont it has covered **38
meetings across 5 boards since February 2026**; it covers four more Sullivan County towns; and in
a county whose newspaper closed last July, it is the only published account of most of those
meetings (retrieved 2026-08-04). It is free, fast, timestamped into the video, and genuinely
useful as a finding aid.

It is also unsigned — no named editor, publisher or funder — and its own footer says the analysis
"may contain errors." That warning is earned: its Claremont council roster lists `gerard` and
`girard` as two different people (there is one Mayor Dale Girard), renders Councilor **Koloski**
as "Kowalski" and Assistant Mayor **Matteau** as "Mattel," and attributes quotes to constructions
like "Speaker S31 (Councilor Kowalski)." Those are transcript artifacts hardening into a public
record of who said what.

Three things follow, and they matter well beyond this county:

- **The detection procedure has no step that would find this.** MeetingWatch is not a press
  association member, not on findyournews.org, not on LION's member list, and not linked from the
  city's site. It turned up in a search-engine result by accident, after both files were
  otherwise finished. **Add a step: search for `"<town>" council meeting transcript` and check
  whether a third party is already indexing these meetings.** Where one exists it is the fastest
  route into the record; either way, knowing it exists is part of knowing the information
  environment.
- **It belongs on the map, and it belongs there labeled.** The Sullivan map lists it under the
  heading "a machine, not a newsroom," with citation value zero as an earned-media target and an
  explicit rule: use it to find the minute of video, then cite the video and the minutes. **Never
  quote it, and never attribute a statement to a named official on its authority.** A campaign
  that repeats a misspelled AI attribution under its own name has committed exactly the error
  this repository exists to prevent — and would have done it while trying to be diligent.
- **It resets what "nobody has explained this" means.** In Claremont the honest finding is no
  longer that nothing exists, but that what exists is machine-written, unsigned, and wrong about
  the councillors' names. That is still an enormous opening. It is just a slightly different one,
  and a scan that reported "no coverage" would have described the county as it was six months ago.
