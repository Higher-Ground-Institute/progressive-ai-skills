---
jurisdiction: "City of Madison and Dane County, Wisconsin"
ocd_id: "ocd-division/country:us/state:wi/place:madison"
scan_date: "2026-08-04"
scan_window: "2025-08-01 to 2026-08-04"
governing_bodies: ["Madison Common Council", "Madison Plan Commission", "Madison Transportation Commission", "Madison Board of Public Works", "Madison Water Utility Board", "Madison Police Civilian Oversight Board", "Dane County Board of Supervisors", "Madison Metropolitan Sewerage District Commission", "Madison Metropolitan School District Board of Education"]
agenda_vendor: "legistar"
date_created: "2026-08-04"
date_modified: "2026-08-04"
---

> **Real places, real records, no real candidates.** Every jurisdiction, governing body,
> meeting record, vote, dollar figure, docket number, and news outlet in this file is real and
> linked to a public source. **No candidate appears anywhere in it, and nothing in it is
> attributed to a real person running for office.** Where a real official is named, the file
> cites only something they have actually published or done in the public record, with a link.
> An AI-generated "position" attached to a real candidate's name is the exact fabrication this
> repository exists to prevent, and it would do the most damage coming from the reference
> examples. If you extend this district into candidate-attributed artifacts
> (`positioning.md`, `answers/`, `briefs/`), the candidate must be invented — see
> [`golden/README.md`](../README.md).

# District issues — City of Madison and Dane County, Wisconsin

Written as `district-issue-scan` would write it. Ranked by documented local salience, not by
national issue polling. An issue belongs here because people in this specific place are
demonstrably arguing about it, showing up about it, or being billed for it.

**Read the scope note before using this file.** This is a jurisdiction-level scan of the City
of Madison and Dane County. It is not scoped to a single alder district or county supervisory
district. A real campaign scan must be, because the district boundary determines which bodies
the voters can actually vote for — see `## Dead ends and gaps`.

**Which election.** Madison Common Council, Madison Metropolitan School District, and Dane
County Board of Supervisors seats are filled at the Wisconsin **spring election in April**, not
in November. Wis. Stat. 5.02(21) makes the spring election the one that elects "judicial,
educational, and municipal officers, and non-partisan county officers"; the next one is April
6, 2027, with a spring primary February 16, 2027 ([City of Madison
Clerk](https://www.cityofmadison.com/clerk/elections-voting), retrieved 2026-08-04). Everything
in `## Ballot measures on the same ballot` is organized around that fact.

## Sources checked

Every source actually looked at, including the ones that turned up nothing.

| Source | Type | URL | Window covered | Checked | Yield |
|---|---|---|---|---|---|
| Legistar Web API, client `madison` | Vendor API (primary records) | [`webapi.legistar.com/v1/madison/Bodies`](https://webapi.legistar.com/v1/madison/Bodies) | current | 2026-08-04 | 252 bodies, 61 flagged active. Confirms one Legistar instance covers Common Council, Plan Commission, Transportation Commission, Board of Public Works, Water Utility Board, and Police Civilian Oversight Board |
| Legistar Web API, `madison/Matters` | Vendor API (primary records) | `webapi.legistar.com/v1/madison/Matters?$filter=MatterIntroDate ge datetime'2025-08-01'` | 2025-08-01 to 2026-08-04 | 2026-08-04 | 3,772 matters across 6 date-chunked requests. **The first unchunked request silently returned exactly 1,000 records and stopped at 2025-11-06** — see `## Dead ends and gaps` |
| Legistar Web API, `madison/Events` + `/EventItems` | Vendor API (primary records) | `webapi.legistar.com/v1/madison/Events?$filter=EventBodyId eq 1 and EventDate ge datetime'2025-08-01'` | same | 2026-08-04 | 25 Common Council meetings, agenda and minutes status per meeting, item-level action names. **No vote tallies** — see `## Dead ends and gaps` |
| Legistar Web API, client `dane` | Vendor API (primary records) | [`webapi.legistar.com/v1/dane/Bodies`](https://webapi.legistar.com/v1/dane/Bodies) | current | 2026-08-04 | 166 bodies, 40 flagged active, including County Board, Zoning & Land Regulation, Public Works & Transportation, Housing Authority, Library Board. Dane County runs a **separate** Legistar instance from the city |
| Legistar Web API, client `mmsd` | Vendor API (primary records) | [`webapi.legistar.com/v1/mmsd/Events`](https://webapi.legistar.com/v1/mmsd/Events) | current | 2026-08-04 | Madison Metropolitan Sewerage District Commission, Operations Committee, Policy/Finance & Personnel Committee. Most recent Commission meeting returned: 2026-07-27. **A sewerage district with a public API is unusual and worth knowing about** |
| Legistar client slug guesses `madisonwi`, `danecounty` | Vendor API | `webapi.legistar.com/v1/madisonwi/Bodies` | — | 2026-08-04 | 0 — HTTP 500, `LegistarConnectionString setting is not set up in InSite for client`. The slug is not derivable from the jurisdiction name; it must be read off the portal hostname |
| Madison Legistar public portal | Agenda portal | [madison.legistar.com/Legislation.aspx](https://madison.legistar.com/Legislation.aspx) | current | 2026-08-04 | HTTP 200. `LegislationDetail.aspx?ID={MatterId}` resolves with the numeric ID alone, without the GUID |
| Common Council meeting minutes PDF, 2026-07-21 | Primary record | [28484_M_COMMON_COUNCIL_26-07-21_Meeting_Minutes.pdf](https://madison.legistar1.com/madison/meetings/2026/7/28484_M_COMMON_COUNCIL_26-07-21_Meeting_Minutes.pdf) | one meeting | 2026-08-04 | URL confirmed present in the API `EventMinutesFile` field. **Not parsed.** This is where vote tallies and public-comment registrations live |
| The Capital Times staff page | Local outlet | [captimes.com/staff](https://captimes.com/staff/) | current | 2026-08-04 | Named beat reporters for housing/transportation, K-12, local government, health, investigations. Also the current most-read list, used below |
| Wisconsin Watch | Nonprofit statewide newsroom | [wisconsinwatch.org](https://wisconsinwatch.org/2026/05/wisconsin-watch-local-news-collaboration-journalism-partnerships-reporting/) | 2026-05 | 2026-08-04 | Confirms an active Madison-based nonprofit newsroom and a story headlined "Madison revisits police body cameras after years of debate" |
| Wisconsin Elections Commission 2026–2027 calendar | Election record | [2026_2027 Election Calendar (PDF)](https://elections.wi.gov/sites/default/files/documents/2026_2027%20Election%20Calendar_0.pdf) | 2026–2027 | 2026-08-04 | Spring Election 2026-04-07; Partisan Primary 2026-08-11; General Election 2026-11-03 |
| Dane County certified November 3, 2026 ballot | Election record | not located | Nov 2026 | 2026-08-04 | **0 — not found.** Must be requested from the Dane County Clerk. No countywide referendum for this ballot was verified |
| Legistar API keyword search for `referend` | Vendor API | see Matters row | 2025-08-01 to 2026-08-04 | 2026-08-04 | **0 matters.** No city referendum question was introduced in the window |
| Legistar API keyword search for `F-35` | Vendor API | see Matters row | 2025-08-01 to 2026-08-04 | 2026-08-04 | **0 matters.** The Truax Field basing fight generated no Common Council legislation in this window |
| Madison Metropolitan School District board records | Primary record | not located | 2025-08 to 2026-08 | 2026-08-04 | **0 — no vendor identified.** MMSD is not in the city's Legistar instance. The district appears in city records only as a property owner and building applicant. See `## Dead ends and gaps` |
| Wisconsin Public Service Commission water rate dockets | Regulatory record | not searched | — | 2026-08-04 | **Not attempted.** Madison Water Utility rate changes are set through the PSC, and this scan did not reach them. Flagged as the highest-value remaining gap |

## Ranked issues

### 1. Police oversight: whether the Independent Monitor and the Civilian Oversight Board get real reporting power

- **What it is:** Madison created a Police Civilian Oversight Board and an Office of the
  Independent Monitor after 2020. Six years on, the Common Council is still arguing about what
  those two offices have to publish and to whom they answer. An ordinance to add public
  reporting requirements to both moved through four bodies over five months and was then
  withdrawn.
- **Salience evidence:** Ordinance file 92386, "Amending Subsections 5.19(6), (7)(i) and (8)
  and amending Subsection 5.20(9)(f) of the Madison General Ordinances to add public reporting
  requirements for the Office of the Independent Monitor and Police Civilian Oversight Board,"
  introduced 2026-03-19, referred by Common Council 2026-03-24, sent back by the Police
  Civilian Oversight Board with a recommendation to place on file 2026-03-25, re-referred
  2026-04-21, sent back by the Board again 2026-07-23, and **withdrawn at Common Council on
  2026-08-04** ([Madison Legistar file
  92386](https://madison.legistar.com/LegislationDetail.aspx?ID=100720), retrieved 2026-08-04).
  A week earlier the Council took a presentation titled "next steps regarding the Police
  Civilian Oversight Board and Office of the Independent Monitor," file 94186, 2026-07-28
  ([Legistar file 94186](https://madison.legistar.com/LegislationDetail.aspx?ID=102166),
  retrieved 2026-08-04). The Board's own annual report for 2025–2026 is file 93106, 2026-05-10,
  and its three-year action plan is file 92450, 2026-03-23. On 2026-07-15 the Council heard a
  presentation from the National Association for Civilian Oversight of Law Enforcement, file
  94063.
  An ordinance withdrawn after five months and two adverse recommendations from the very board
  it governs is the clearest documented conflict in the window.
- **Who is affected, and how many:** everyone policed in the City of Madison.
  `[NEEDS SOURCE — City of Madison 2020 census population and MPD sworn strength from the 2026
  adopted budget]`
- **Stage:** stalled, and reopening. The ordinance is withdrawn; the Council President's
  "next steps" presentation on 2026-07-28 indicates a replacement is being prepared. No
  successor ordinance had been introduced as of 2026-08-04.
- **Decision-maker:** Madison Common Council, with the Police Civilian Oversight Board as the
  referral body. Common Council meets on a roughly two-week cycle; meetings in the window ran
  2026-06-09, 06-23, 07-07, 07-21, 08-04. Next meeting date `[NEEDS SOURCE — Legistar Events
  for EventBodyId 1 after 2026-08-04; none were returned, so the fall calendar was not yet
  posted at scan time]`.
- **Who currently speaks on it:** The Common Council President put the "next steps"
  presentation on the 2026-07-28 agenda (file 94186, above); the file records that the item
  exists and who presented it, and this scan makes no claim about what was said in it. The
  Police Civilian Oversight Board publishes an annual report (file 93106). Wisconsin Watch has
  published on Madison policing, including a story headlined "Madison revisits police body
  cameras after years of debate" ([Wisconsin
  Watch](https://wisconsinwatch.org/2026/05/wisconsin-watch-local-news-collaboration-journalism-partnerships-reporting/),
  retrieved 2026-08-04). The Cap Times most-read list on 2026-08-04 carried a story headlined
  "Madison faces familiar pain, questions a week after police shooting"
  ([captimes.com](https://captimes.com/staff/), retrieved 2026-08-04) — **the headline is the
  only thing verified here. This scan did not open the story and makes no claim about the date,
  location, or circumstances of any incident.** A campaign using this file must read the
  reporting before saying anything.
- **Quality of what exists:** poor for a voter. The primary records are complete and public,
  but there is no plain-language public explanation of what the Independent Monitor can and
  cannot currently do, what file 92386 would have changed, or why it was withdrawn. Reading the
  Legistar history is the only way to find out, and almost nobody will.
- **Primary records:** MGO 5.19 and 5.20; Legistar files 92386, 94186, 94063, 93106, 92450,
  92449.

### 2. Homelessness: the permanent men's shelter's cost growth, and the Willy Street encampment

- **What it is:** Madison has been building a purpose-built permanent men's shelter — the
  Bartillon Shelter — while simultaneously managing street homelessness downtown. The shelter
  contract has generated a long series of change orders, and an encampment on Williamson
  Street is an active, unresolved fight the mayor has publicly weighed in on.
- **Salience evidence:** Change orders to Contract 9358, Bartillon Shelter, to Miron
  Construction Co., appear repeatedly across the window: No. 18 for $49,520.84 (file 90230,
  2025-10-01), No. 20 for $79,006.42 (file 90835, 2025-11-12), No. 23 for −$15,845.03 (file
  91220, 2025-12-10), No. 24 for $107,243.44 with a time extension to 2026-02-18 (file 91444,
  2026-01-07), and No. 27 for $76,891.67 (file 92068, 2026-02-19). A separate fiber-connection
  contract, No. 9673, drew change orders of $16,000.00 and $21,100.00, both marked "over
  contingency" (files 90822 and 92525). **These are the change orders returned in the window
  queried. This scan did not retrieve the full change-order series or the contract's original
  award amount, and therefore reports no total and no percentage overrun.** Anyone using this
  issue must pull the complete series first. Separately, the Common Council held a dedicated
  discussion on the purpose-built permanent men's shelter on 2025-09-30 (materials filed as
  90067), and "Men's Shelter Updates" recurs as a standing item (files 89700, 92529). A 2025
  year-end resolution transferred $2.1 million from the General Fund contingent reserve (file
  90967, 2025-11-19). The Cap Times most-read list on 2026-08-04 led with "Willy Street
  encampment remains after Madison mayor calls for an end"
  ([captimes.com](https://captimes.com/staff/), retrieved 2026-08-04).
- **Who is affected, and how many:** `[NEEDS SOURCE — Dane County Continuum of Care
  point-in-time count, and Bartillon Shelter designed bed capacity from the project file]`
- **Stage:** recurring, and on the current agenda. Change orders were still arriving in
  2026-03; the encampment was unresolved as of 2026-08-04.
- **Decision-maker:** Common Council for appropriations, Board of Public Works for change
  orders, and the Community Development Division for program contracts. On this issue the Board
  of Public Works is where the money actually moves, and almost nobody attends it.
- **Who currently speaks on it:** the mayor, per the Cap Times headline above. The Cap Times
  has a named local government reporter (Enjoyiana Nururdin) and a named housing and
  transportation reporter (Will Briggs) — see
  [`district-media-map.md`](district-media-map.md). The city publishes the change orders but no
  running total.
- **Quality of what exists:** the encampment is covered. The shelter's cost trajectory is not.
  A change order posted as a one-line Board of Public Works item is a public record that is
  technically available and practically invisible, and no outlet in this scan had aggregated
  the series. **This is the clearest vacuum in the district: a documented, uncontested,
  arithmetic story that nobody has written.**
- **Primary records:** Contract 9358 and Contract 9673 change-order files listed above;
  Legistar files 90067, 90967.

### 3. Data centers: the zoning moratorium, and what happens when it lapses

- **What it is:** In December 2025 the city introduced an ordinance creating a temporary
  moratorium on zoning certificates for data centers and telecommunications centers. It passed
  the following month. Temporary moratoria exist to buy time for a permanent rule, which means
  the real fight is the ordinance that has not been written yet.
- **Salience evidence:** Ordinance file 91135, "Creating Section 28.140 to establish a
  temporary moratorium on the consideration and/or issuance of zoning certificates for data
  centers and telecommunications centers and amending 28.061, 28.082, and 28.151 to accommodate
  the temporary moratorium," introduced 2025-12-04, referred by Common Council 2025-12-09,
  recommended for adoption by the Plan Commission after public hearing 2026-01-12, adopted
  unanimously by Common Council 2026-01-13, enacted as **ORD-26-00002** on 2026-01-24 ([Madison
  Legistar file 91135](https://madison.legistar.com/LegislationDetail.aspx?ID=99767), retrieved
  2026-08-04). A city moving from introduction to enactment in seven weeks, over the holidays,
  through a public hearing, is a city that thinks it has a timing problem.
- **Who is affected, and how many:** every ratepayer and every neighborhood adjacent to
  industrially zoned land. Wisconsin Watch has reported on AI-related infrastructure backlash
  statewide, co-publishing with Bolts on Flock surveillance cameras
  ([Wisconsin Watch](https://wisconsinwatch.org/2026/05/wisconsin-watch-local-news-collaboration-journalism-partnerships-reporting/),
  retrieved 2026-08-04). `[NEEDS SOURCE — number and location of data center applications
  pending or withdrawn in Madison, from the Zoning Administrator]`
- **Stage:** decided, with a deadline attached. The moratorium is in force. Its expiration date
  is in the text of MGO 28.140 and **was not retrieved by this scan** — the API returns the
  title, not the body. Get it: it is the single most important date on this issue.
- **Decision-maker:** Plan Commission recommends, Common Council adopts. Plan Commission is
  Legistar `BodyId` 3.
- **Who currently speaks on it:** the city, through the ordinance itself, and Wisconsin Watch
  regionally. This scan found no Madison-specific public explainer of what the moratorium
  covers or when it ends.
- **Quality of what exists:** the ordinance is findable. The answer to "can a data center be
  built near me, and for how long is that true" is not written anywhere a resident would find
  it. Cheap to own.
- **Primary records:** MGO 28.140, and amendments to 28.061, 28.082, 28.151; ORD-26-00002;
  Legistar file 91135.

### 4. North-South Bus Rapid Transit: another $6 million for design, with construction not yet let

- **What it is:** Madison built an east-west BRT line and is now designing a north-south one.
  The east-west line is still generating construction change orders; the north-south line just
  absorbed another $6 million in engineering fees before a shovel moved.
- **Salience evidence:** Resolution file 92934, "Authorizing the City to execute a contract
  with AECOM Technical Services, Inc., for continued project development and other engineering
  services associated with N-S Bus Rapid Transit and authorizing expenditure of an additional
  **$6,000,000** for the services," introduced 2026-04-29, recommended by the Finance Committee
  2026-05-11 and the Transportation Commission 2026-05-13, adopted unanimously 2026-05-19,
  enacted as **RES-26-00291** on 2026-05-22 ([Madison Legistar file
  92934](https://madison.legistar.com/LegislationDetail.aspx?ID=101095), retrieved 2026-08-04).
  On 2026-07-01 the Council took up a jurisdictional transfer agreement with the Wisconsin
  Department of Transportation for portions of S. Park Street and other streets, file 93777 — a
  transfer of state highway segments to the city is a prerequisite for the corridor and a
  transfer of long-term maintenance liability. Meanwhile the east-west line's main construction
  contract, No. 8716 to Zenith Tech Inc., drew change order No. 19 for $383,657.40 (file 92259,
  2026-03-05) and No. 20 for $0 balancing account funds (file 93462, 2026-06-04); the Mineral
  Point Road sidewalk contract, No. 8717 to Parisi Construction, drew change orders of
  $913,038.81 (file 90580, 2025-10-22) and $139,846.55 (file 92260, 2026-03-05). The Council
  also received an update on N-S BRT as file 90700, 2025-10-31.
- **Who is affected, and how many:** Metro Transit riders along the corridor and every property
  owner on the transferred street segments. `[NEEDS SOURCE — Metro Transit ridership from the
  On-Board Survey Report, Legistar file 90284, 2025-10-03]`
- **Stage:** pending. Design funded; construction not let. The jurisdictional transfer was
  before the Council as of 2026-07-01.
- **Decision-maker:** Transportation Commission (Legistar `BodyId` 1348) recommends; Common
  Council adopts; WisDOT is a required counterparty on the transfer.
- **Who currently speaks on it:** the city's project pages, and the Cap Times, which has a
  dedicated housing and transportation reporter and reported "Madison's new regional bus
  station near State Street opening this fall" ([captimes.com](https://captimes.com/staff/),
  retrieved 2026-08-04).
- **Quality of what exists:** transit is the best-covered issue in this district. Three
  institutions publish on it. **Expensive to own and largely pointless to try** — unless the
  angle is the change-order series or the maintenance liability in the jurisdictional transfer,
  neither of which anyone has written about.
- **Primary records:** RES-26-00291; Legistar files 92934, 93777, 90700, 92259, 93462, 90580,
  92260, 90284.

### 5. Flood and stormwater risk: three watershed studies landed in April 2026 and named specific streets

- **What it is:** Madison sits on an isthmus between two lakes and flooded badly in 2018. The
  city commissioned watershed studies for its most exposed basins. Three final reports were
  accepted within a week of each other in April 2026, each listing the specific alder districts
  affected. Accepting a report is not funding its recommendations.
- **Salience evidence:** Three reports accepted by the Board of Public Works: the Central
  Isthmus Watershed Study, file 92774, covering Districts 4 and 6; the East Isthmus and Yahara
  River Watershed Study, file 92775, covering Districts 2, 4, 6, 12, and 15 ([Madison Legistar
  file 92775](https://madison.legistar.com/LegislationDetail.aspx?ID=100974), retrieved
  2026-08-04); and the Warner Park and Cherokee Marsh Watershed Study, file 92776, covering
  Districts 12 and 18 — all introduced 2026-04-15, all accepted 2026-04-22. Companion
  communications accepting the final reports and recommended solutions were filed 2026-04-08 as
  92653 and 92654. Consultant contracts feeding these studies ran with Brown and Caldwell
  (amendments filed as 90812 and 91450) and MSA Professional Services (92204). On 2025-11-06 the
  Engineering Division was authorized to apply for a Wisconsin Emergency Management
  Pre-Disaster Flood Resilience Grant of **up to $250,000** (file 90756); on 2026-01-20 the City
  Engineer was authorized to apply for a WDNR Municipal Flood Control Grant for the West Towne
  Pond project (file 91576). Individual mitigation projects appear at Red Sky Drive (file 91016,
  District 9), Travis Terrace (file 91017, District 11), and Castle Creek Channel (file 92661).
  Earlier in the window the Council took an informational presentation on the potential impacts
  of the East Isthmus and Yahara study's conceptual solutions on **parkland** (file 89835,
  2025-09-04) — that is where the fight will be.
- **Who is affected, and how many:** residents and property owners in the seven named alder
  districts. `[NEEDS SOURCE — number of structures in the modeled floodplain, from the
  accepted study reports themselves]`
- **Stage:** decided as to the studies, entirely undecided as to the money. No construction
  appropriation for the recommended solutions appeared in the window.
- **Decision-maker:** Board of Public Works (Legistar `BodyId` 9) accepts and lets contracts;
  Common Council appropriates; the Board of Park Commissioners has standing on anything that
  touches parkland.
- **Who currently speaks on it:** the city's Engineering Division, in the study documents. This
  scan found no outlet coverage of the three April 2026 acceptances.
- **Quality of what exists:** the reports exist and are public. **"What did the study say about
  my street, and is the city going to pay for it" has no published answer.** A per-district
  reading of an already-public engineering report, with the parkland tradeoff named honestly,
  is close to free.
- **Primary records:** Legistar files 92774, 92775, 92776, 92653, 92654, 89835, 90756, 91576,
  91016, 91017, 92661, 90812, 91450, 92204.

### 6. Who pays for street and sewer reconstruction: 47 special assessment districts in twelve months

- **What it is:** When Madison rebuilds a street, an alley, a sewer, or a traffic signal, it
  frequently recovers part of the cost by levying a special assessment on the abutting property
  owners. This arrives as a bill. In the scan window the Common Council handled 47 separate
  assessment-district matters.
- **Salience evidence:** 47 matters whose titles contain "Assessment District" were introduced
  between 2025-08-01 and 2026-08-04 (Legistar `madison/Matters`, retrieved 2026-08-04). Named
  examples: the Lake Street Sanitary Sewer Replacement Assessment District, declared 2025-09-09
  (file 89905); Pontiac Trail, Boston Court, Rosewood Circle and Nokomis Circle Assessment
  District 2025, plans and schedule of assessments approved 2025-11-12 (file 90845, District
  10); the Pflaum Road Resurfacing Assessment District 2025, revised 2025-11-24 (file 91014,
  District 15); Virginia Terrace, Norwood Place, Rugby Row and Hillington Way Assessment
  District 2026, declared 2025-12-10 (file 91197, District 5); the Milwaukee Street & Sprecher
  Road Traffic Signal Assessment District, declared 2025-12-10 (file 91201); the South Charter
  Street Alley Assessment District 2026, schedule approved 2025-12-11 (file 91223, District 13);
  and Assessing Benefits for the Blue Harvest Lane, Feather Edge Drive & Soaring Sky Run
  Assessment District 2023, 2025-12-11 (file 91225, District 1). The city's 2026 budget resolution
  authorized a 2025 general property tax levy of **$326,666,421** for City of Madison purposes
  (file 90658, substitute adopted 2025-10-28) — the assessment is on top of that.
  The resolutions are framed as the city "declaring its intention to exercise its police
  powers," which is the statutory language and also precisely why nobody reads them.
- **Who is affected, and how many:** the abutting property owners in each district, by name, in
  the schedule of assessments attached to each resolution. The per-parcel dollar figures are in
  those attachments. **This scan did not open them, and no per-parcel figure appears in this
  file.** They contain named individuals' property information; treat them as public records to
  be read, not data to be bulk-extracted, and see
  [`reference/shared-rules.md`](../../reference/shared-rules.md) Rule 5.
- **Stage:** recurring, continuously. Districts were being declared and assessed throughout the
  window.
- **Decision-maker:** Board of Public Works approves plans and schedules; Common Council adopts.
  There is a statutory objection process at the public hearing on each district.
- **Who currently speaks on it:** nobody found. No outlet in this scan covered any individual
  assessment district. The city mails notices to affected owners.
- **Quality of what exists:** **the worst in the district, and therefore the best opportunity.**
  A resident who gets an assessment notice has no public explanation of how the amount was
  calculated, what the objection process is, or what the deadline is. This is the classic
  follow-the-money issue the skill's tips describe: a bill in the mailbox, no coverage, and no
  competing explanation.
- **Primary records:** Wis. Stat. ch. 66 special assessment provisions
  `[NEEDS SOURCE — exact statutory cite and the corresponding Madison General Ordinances
  chapter]`; Legistar files 89905, 90845, 91014, 91197, 91201, 91223, 91225, 90658.

## Contested space summary

The short version of who currently answers each issue well. Ranked by how badly the honest
answer is missing.

| Issue | Who covers it now | How well | Vacuum? |
|---|---|---|---|
| Special assessment districts (#6) | Nobody found. City mails notices to affected owners only | No public explanation of calculation, objection process, or deadline exists | **Yes — total.** Highest-value target in the district |
| Bartillon Shelter cost growth (#2) | Change orders posted individually by Board of Public Works; no aggregation anywhere | Records complete, story unwritten | **Yes.** The encampment is covered; the arithmetic is not |
| Watershed study findings by district (#5) | City Engineering, in the study PDFs | Technically complete, practically unread. Zero outlet coverage of the April 2026 acceptances found | **Yes**, and the parkland tradeoff makes it genuinely contested |
| Data center moratorium (#3) | The ordinance itself; Wisconsin Watch regionally on AI infrastructure | No Madison-specific explainer; expiration date not published anywhere findable | **Yes**, with a deadline attached |
| Police oversight (#1) | Police Civilian Oversight Board annual report; Wisconsin Watch on policing; Cap Times on incidents | Incidents covered well. The governance question — what the Monitor can actually do, why file 92386 died — is not explained | **Partly.** Covered, but only through incidents and only by the institutions involved |
| North-South BRT (#4) | Cap Times housing/transportation reporter, city project pages, Wisconsin Public Radio | Well covered | **No.** Expensive to own. Exception: change orders and the WisDOT jurisdictional transfer |

An issue where three institutions already publish well is expensive to own and pointless to
try. An issue where the honest answer does not exist anywhere is nearly free. In this district
the free issues are all at the Board of Public Works.

## Ballot measures on the same ballot

**Which ballot depends on which office, and this is where a Madison scan most easily goes
wrong.**

| Measure | What it does | Position needed? | Source |
|---|---|---|---|
| — | **No City of Madison referendum question was introduced in the scan window.** A keyword search of 3,772 matters for `referend` returned zero | n/a | Legistar `madison/Matters`, 2025-08-01 to 2026-08-04, retrieved 2026-08-04 |
| Dane County referenda, November 3, 2026 | Unknown | Unknown | **`[NEEDS SOURCE — request the certified November 3, 2026 ballot from the Dane County Clerk.]`** Not located online at scan time |
| Any April 6, 2027 school or municipal referendum | Wisconsin school districts commonly place operating and capital referenda on the April ballot | Yes, if one is filed | `[NEEDS SOURCE — MMSD Board of Education agendas; no MMSD records vendor was identified, see below]` |

**The dates that matter.** Wisconsin's spring election on April 6, 2027 is when Madison alder,
MMSD Board of Education, and nonpartisan Dane County Board seats are filled; the spring primary
is February 16, 2027 ([City of Madison
Clerk](https://www.cityofmadison.com/clerk/elections-voting), retrieved 2026-08-04). The
November 3, 2026 general election is for federal, state, and partisan county offices
([Wisconsin Elections Commission 2026–2027
calendar](https://elections.wi.gov/sites/default/files/documents/2026_2027%20Election%20Calendar_0.pdf),
retrieved 2026-08-04). A down-ballot campaign for a city or school seat that plans its media
cutoffs against November 3, 2026 is planning against the wrong election by five months.
`[NEEDS SOURCE — nomination paper circulation and filing deadlines for the April 6, 2027
spring election, from the Wisconsin Elections Commission or the City of Madison Clerk.]`

## Dead ends and gaps

Specific enough that the next person does not repeat the search.

**The Legistar API does not expose vote tallies on this instance.** This is the most important
finding in this file and it contradicts
[`reference/local-agenda-systems.md`](../../reference/local-agenda-systems.md), which lists
`/Matters/{id}/Histories` as returning "the vote history on one item, including who voted how."
On `madison`, `MatterHistoryTally` was `null` on all four matters pulled;
`/EventItems/{id}/Votes` returned an empty array with HTTP 200 for an item that had a recorded
mover, seconder, and `EventItemPassedFlagName: Pass`;
`/Events/{id}/EventItems/{id}/Votes` returned 404; and passing `?Votes=1` to the `EventItems`
collection across all 25 Common Council meetings in the window surfaced **zero** items with a
recorded dissenting vote. That is not a district where everything passes unanimously — it is a
field that is not populated. **The only dissent signal available through the API is the action
name**, and the distinction is real: across those 25 meetings the API returned "Adopt
Unanimously" 550 times, "Adopt unanimously under suspension of MGO 2.055" 22 times, and plain
"Adopt" 122 times. Those 122 are where the roll calls are. Read the tallies out of the minutes
PDF, e.g.
[`28484_M_COMMON_COUNCIL_26-07-21_Meeting_Minutes.pdf`](https://madison.legistar1.com/madison/meetings/2026/7/28484_M_COMMON_COUNCIL_26-07-21_Meeting_Minutes.pdf).
Do not report "unanimous" because the tally came back empty.

**Public-comment counts are not in the API either.** The skill ranks salience partly on
public-comment speaker counts. Nothing in `Events`, `EventItems`, or `Matters` carries a
registrant or speaker count on this instance, and 1,063 of the event items returned had a null
`EventItemActionName`. Comment registrations are in the minutes. No issue in this file is ranked
on a comment count, because no comment count was verified.

**The 1,000-record cap is silent.** A single request for all matters since 2025-08-01 returned
exactly 1,000 records and stopped at 2025-11-06 with no error, no warning, and no pagination
header. Nothing in the response indicates truncation. Six date-chunked requests returned 3,772.
A scan that issues the obvious query and trusts the result will miss nine months and conclude
the district is quiet.

**The Legistar client slug is not derivable from the jurisdiction name.** `madison` and `dane`
work; `madisonwi` and `danecounty` return HTTP 500 with
`LegistarConnectionString setting is not set up in InSite for client: {slug}`. This is a
distinctive error and it does not mean the jurisdiction has no Legistar — it means the slug is
wrong. Read it off the portal hostname. Slugs that returned this error while the jurisdiction
does have a public agenda portal: `asheville`, `cityofasheville`, `buncombecounty`, `berkeley`,
`annarbor`, `durham`. (Ann Arbor's real slug is `a2gov`.)

**Madison Metropolitan School District has no vendor identified.** MMSD is not in the city's
Legistar instance and no records system for it was located. The district appears in city
records only as a property owner or building applicant — certified survey maps at 7333 and 7341
West Towne Way (file 92397), public building filings for Sennett Middle School (file 92523) and
Cherokee Middle School (file 92524), and a "Building for the Future" discussion item (file
90350, 2025-10-09). **For a school-board race this file is inadequate and a scan must start
over from the MMSD Board of Education's own site.** School referenda in Wisconsin appear on the
April ballot and drive turnout intensity; this gap is the largest substantive hole in the scan.

**Madison Water Utility rate cases were not reached.** The Water Utility Board is inside the
city's Legistar instance (`BodyId` 36) and its 2026 operating and capital budget requests are
file 89645, but Wisconsin water rates are set by the **Public Service Commission of Wisconsin**,
not by the Council, and this scan did not search PSC dockets. A rate increase is the highest-
salience, lowest-competition issue type there is. **Start there next.** The same applies to the
Madison Metropolitan Sewerage District: its Legistar instance (`mmsd`) is reachable and its
Commission last met 2026-07-27, but no sewer rate action was pulled.

**Dane County's own record was surveyed but not scanned.** The `dane` instance was confirmed
reachable and its 40 active bodies enumerated, including Zoning & Land Regulation, Public Works
& Transportation, the Housing Authority, and the Library Board. **No Dane County matters or
events were pulled.** A county supervisory district scan must do this; the county board has
jurisdiction over the jail, the sheriff, human services, and county zoning, none of which the
city touches.

**Bodies not scanned at all:** Plan Commission (`BodyId` 3) as a body, Zoning Board of Appeals,
Landmarks Commission, Community Development Authority, Madison Public Library Board, Board of
Health for Madison and Dane County, Police and Fire Commission, and the Capital Area Regional
Planning Commission. Each was confirmed to exist and be active in the `Bodies` response; none
had its calendar pulled.

**No boundary resolution was performed.** The `ocd_id` in the frontmatter is constructed from
the Open Civic Data naming convention, not retrieved from Google Civic Information
`divisionByAddress`, and no address was resolved. For a real campaign this must be done first —
`district-issue-scan` step 1 — because the alder district, county supervisory district, and
school board seat boundaries do not coincide, and a scan of the wrong council is worse than no
scan.

**Not attempted:** the county's legal-notice newspaper of record, the clerk's press
notification list, any records request, any meeting video or auto-generated transcript. All
four are listed in [`reference/local-agenda-systems.md`](../../reference/local-agenda-systems.md)
and none was used here.

**Human approval has not happened.** `district-issue-scan` step 10 requires walking a human
through the ranked list and asking whether it matches what they hear at doors. Nobody has done
that for this file. The ranking above is defensible from the record and unvalidated against the
district.
