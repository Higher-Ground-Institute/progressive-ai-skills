---
jurisdiction: "Whatcom County, Washington (county-wide; includes WA Legislative Districts 40 and 42 and Congressional District 2)"
ocd_id: "ocd-division/country:us/state:wa/county:whatcom"
scan_date: "2026-08-04"
scan_window: "2025-08-01 to 2026-08-04"
governing_bodies:
  - "Whatcom County Council (7 members, at-large and district)"
  - "Whatcom County Ferry District Board of Supervisors (the Council sitting as the district board)"
  - "Whatcom County Council as the Health Board"
  - "City of Bellingham City Council"
  - "City of Lynden City Council"
  - "Whatcom County Fire Protection District No. 1"
  - "Port of Bellingham Commission"
agenda_vendor: "legistar"
date_created: "2026-08-04"
date_modified: "2026-08-04"
---

# District issues — Whatcom County, Washington

Written by `district-issue-scan`. Ranked by documented local salience, not by national issue
polling. An issue belongs here because people in this specific place are demonstrably arguing
about it, showing up about it, or being billed for it.

This is a **golden reference output**: a real run of the skill against a real place, produced
to test whether the detection procedure survives contact with live data. It profiles no
candidate. Elected officials are named only in connection with recorded public votes.

**Election context.** The Washington top-two primary was held today, August 4, 2026; the
general election is November 3, 2026. Whatcom County reported 169,048 active registered voters
for the primary, and the ballot covered Congressional District 2, Legislative Districts 40 and
42, statewide offices, Whatcom County offices, Port of Bellingham districts 4 and 5, and four
fire and hospital districts ([Whatcom County Auditor, "August 4 Primary and Special
Election"](https://www.whatcomcounty.us/1732/Current-Election), retrieved 2026-08-04). **County
Council seats are not on the 2026 ballot** — the votes described below were cast by a body
voters cannot replace this cycle, which matters for how a campaign uses them.

## Sources checked

| Source | Type | URL | Window covered | Checked | Yield |
|---|---|---|---|---|---|
| Whatcom County Legistar calendar | Vendor agenda portal | https://whatcom.legistar.com/Calendar.aspx | 2025-08 to 2026-08 | 2026-08-04 | Confirmed vendor = Legistar, client slug `whatcom` |
| Legistar Web API — `/whatcom/Matters` | Vendor API (no auth) | https://webapi.legistar.com/v1/whatcom/matters | Intro dates 2025-08-01 → 2026-08-04 | 2026-08-04 | 1,000-record cap hit; ~970 matters returned with file numbers, titles, intro dates, status |
| Legistar Web API — `/whatcom/Events` | Vendor API (no auth) | https://webapi.legistar.com/v1/whatcom/events | 2026-01 to 2026-08 | 2026-08-04 | Full meeting list with direct agenda- and minutes-PDF URLs. This is the highest-yield single call in the scan. |
| Legistar Web API — `/whatcom/Matters/{id}/Histories` | Vendor API | https://webapi.legistar.com/v1/whatcom/matters/23093/histories | 2026 | 2026-08-04 | **0 usable vote tallies.** `MatterHistoryTally` was null on every record inspected. Vote counts had to come from minutes PDFs instead. See Dead ends. |
| Legistar Web API — `/whatcom/Matters/{id}/Attachments` | Vendor API | https://webapi.legistar.com/v1/whatcom/matters/23332/attachments | 2026 | 2026-08-04 | Direct PDF URLs for proposed and enacted legislation, including "Approved Resolution 2026-018" |
| Whatcom County Council minutes, 2026-07-28 | Primary record (PDF, text layer) | https://whatcom.legistar1.com/whatcom/meetings/2026/7/3191_M_Council_26-07-28_Minutes.pdf | Single meeting | 2026-08-04 | Roll-call tallies for the ferry levy and the Comprehensive Plan update; public-hearing speaker lists |
| Whatcom County Council minutes, 2026-07-14 | Primary record (PDF, text layer) | https://whatcom.legistar1.com/whatcom/meetings/2026/7/3183_M_Council_26-07-14_Minutes.pdf | Single meeting | 2026-08-04 | Introduction of the three ferry levy options |
| Council Special Committee of the Whole agenda, 2026-08-04 | Primary record | https://whatcom.legistar1.com/whatcom/meetings/2026/8/3259_A_Council_Special_Committee_of_the_Whole_26-08-04_Meeting_Agenda.pdf | Today | 2026-08-04 | Capital Improvement Program presentation; councilmember priorities |
| Whatcom County Auditor — 2026 Ballot Resolutions | Official election record | https://www.whatcomcounty.us/4703/2026-Ballot-Resolutions | 2026 | 2026-08-04 | Five certified November 3 measures with resolutions and explanatory statements |
| Whatcom County Auditor — Elections in 2026 | Official election calendar | https://www.whatcomcounty.us/4443/Elections-in-2026 | 2026 | 2026-08-04 | Ballots mail Oct 14; registration deadline Oct 26; certification Nov 24 |
| Cascadia Daily News, ferry-district coverage | Local daily/weekly | https://www.cascadiadaily.com/2026/jul/28/whatcom-council-sets-5-7m-annual-ferry-district-budget/ | Apr–Jul 2026 | 2026-08-04 | Four separate original stories tracking the levy from introduction to adoption |
| Bellingham Herald, ferry-district coverage | Chain daily (McClatchy) | https://www.bellinghamherald.com/news/politics-government/article316700128.html | Jul–Aug 2026 | 2026-08-04 | Two stories; the Aug 2 follow-up carries the byline "Edited by Scot Heisel with AI assistance" |
| Whatcom Watch, "Watching Government" column | Monthly nonprofit-ish community paper | https://whatcomwatch.org/ | Current issue: July 2026 (vol. 35 no. 7) | 2026-08-04 | Council votes compiled item by item — but the July 2026 issue was still covering the **May 12, 2026** meeting. Roughly a two-month lag. |
| Salish Current | Nonprofit newsroom | https://salish-current.org/ | 2026 | 2026-08-04 | Publishing several times a week (stories dated Jul 29, Jul 30, Jul 31, Aug 3, Aug 4). Found the only published argument about Bellingham Initiative 26-01. **No ferry-levy story found** in the search performed. |
| `whatcomcounty.us` DocumentCenter | Official document store | https://www.whatcomcounty.us/DocumentCenter/View/114181/LVP-Primary-August-4-2026-full-color | Aug 2026 | 2026-08-04 | Local Voters' Pamphlet, full text, free and unpaywalled |
| Washington SOS elections pages | State record | https://www.sos.wa.gov/elections/dates-and-deadlines | 2026 | 2026-08-04 | **HTTP 403 to a scripted request.** Reachable through search-engine cache and through the county's own calendar instead. |
| Whatcom County Fire Protection District No. 1 — own agenda portal | Special district | — | 2025–2026 | 2026-08-04 | **Not located.** The district's ballot measure was found only through the county auditor's resolution page. See Dead ends. |

## Ranked issues

### 1. A brand-new countywide property tax for the Lummi Island ferry

- **What it is:** Whatcom County created a countywide ferry taxing district in May 2026 and, on
  July 28, set its first annual budget at $5.7 million. Every property owner in the county —
  not just Lummi Island or the unincorporated county — will see a new line on the 2027 tax
  bill to pay for a replacement ferry and ongoing ferry operations.
- **Salience evidence:**
  - The Council, sitting as the Ferry District Board of Supervisors, adopted the largest of
    three options on a **5–2 vote**: Aye — Boyle, Buchanan, Galloway, Rienstra, Scanlon; Nay —
    Elenbaas, Stremler ([Council minutes, 2026-07-28, AB2026-552 / RES
    2026-031](https://whatcom.legistar1.com/whatcom/meetings/2026/7/3191_M_Council_26-07-28_Minutes.pdf),
    retrieved 2026-08-04).
  - The resolution itself states that "an annual levy net budget amount of $5.7 Million is
    approximately 8.7 cents per thousand of assessed value" ([Proposed Resolution, AB2026-552,
    Legistar attachment](https://whatcom.legistar1.com/whatcom/attachments/c7a68e96-1e6e-4eae-bf95-8060cbfe73ab.pdf),
    retrieved 2026-08-04).
  - **Twelve people signed up to speak** at the combined public hearing on the six ferry-district
    files — Terry Diffley, Laura Bracken, Brian Gass, Charles Bailey, David Kershner, Rhayma
    Blake, Cara Blake, Kathleen Gallagher, Pam Gould, Markis Dee Stidham, Jim Shaver, Ryan
    Bowman ([Council minutes, 2026-07-28, under
    AB2026-520](https://whatcom.legistar1.com/whatcom/meetings/2026/7/3191_M_Council_26-07-28_Minutes.pdf),
    retrieved 2026-08-04). Cascadia Daily News reported that "very few meeting attendees spoke
    against the new levy" ([CDN,
    2026-07-28](https://www.cascadiadaily.com/2026/jul/28/whatcom-council-sets-5-7m-annual-ferry-district-budget/),
    retrieved 2026-08-04) — worth knowing, because the hearing room and the tax bill are two
    different constituencies.
  - Three options were on the table and the minutes record the trade-off in the councilmembers'
    own framing: $4.2 million means returning to the Road Fund in two years, $5.2 million in ten
    years, $5.7 million in nineteen ([Council minutes, 2026-07-28, AB2026-552 discussion
    notes](https://whatcom.legistar1.com/whatcom/meetings/2026/7/3191_M_Council_26-07-28_Minutes.pdf),
    retrieved 2026-08-04).
- **Who is affected, and how many:** Every taxable property in Whatcom County. Cascadia Daily
  News put it at "around $46 more per year for the median Whatcom County home assessed at
  $526,120" ([CDN,
  2026-07-28](https://www.cascadiadaily.com/2026/jul/28/whatcom-council-sets-5-7m-annual-ferry-district-budget/),
  retrieved 2026-08-04); the Bellingham Herald put a $500,000 home at $43.50 per year
  ([Bellingham Herald,
  2026-07-29](https://www.bellinghamherald.com/news/politics-government/article316700128.html),
  retrieved 2026-08-04). For scale, the county had 169,048 active registered voters at the
  August primary ([Whatcom County Auditor](https://www.whatcomcounty.us/1732/Current-Election),
  retrieved 2026-08-04).
- **Stage:** Decided. Effective for 2027 collection. The ordinances and resolutions were
  enacted July 28, 2026 as RES 2026-030, RES 2026-031, ORD 2026-036 and ORD 2026-037; the
  district itself was created by ORD 2026-024 on May 12, 2026 ([RES 2026-031 recital and
  Council minutes,
  2026-07-28](https://whatcom.legistar1.com/whatcom/meetings/2026/7/3191_M_Council_26-07-28_Minutes.pdf),
  retrieved 2026-08-04). Because the rate is under 10 cents per $1,000, no voter approval was
  required — a point the two dissenting members raised on the record.
- **Decision-maker:** Whatcom County Council sitting as the Ferry District Board of Supervisors.
  The Council's regular and committee calendar is at
  [whatcom.legistar.com/Calendar.aspx](https://whatcom.legistar.com/Calendar.aspx); it met as a
  Special Committee of the Whole on August 4, 2026 ([agenda,
  AB2026-593/587/588](https://whatcom.legistar1.com/whatcom/meetings/2026/8/3259_A_Council_Special_Committee_of_the_Whole_26-08-04_Meeting_Agenda.pdf),
  retrieved 2026-08-04).
- **Who currently speaks on it:**
  - **Cascadia Daily News** — four original stories by Julia Tellman from April through July
    ([April 29](https://www.cascadiadaily.com/2026/apr/29/whatcom-county-to-hold-public-hearing-on-lummi-island-ferry-taxing-district/),
    [July 15](https://www.cascadiadaily.com/2026/jul/15/how-much-will-taxpayers-fork-over-for-new-whatcom-county-ferry-district/),
    [July 28](https://www.cascadiadaily.com/2026/jul/28/whatcom-council-sets-5-7m-annual-ferry-district-budget/),
    all retrieved 2026-08-04). The July 15 piece lays out all three levy options with the
    per-household cost of each. This is genuinely good work.
  - **Bellingham Herald** — two stories
    ([July 29](https://www.bellinghamherald.com/news/politics-government/article316700128.html),
    [August 2](https://www.bellinghamherald.com/news/local/article316728159.html), retrieved
    2026-08-04). Note that the August 2 follow-up is bylined "Edited by Scot Heisel with AI
    assistance."
  - **Whatcom County Public Works** — the transmittal memo from Director Elizabeth Kosa
    ([memo, June 29, 2026](https://whatcom.legistar1.com/whatcom/attachments/ba8c959f-9686-4503-80ec-d91a9b7c42ed.pdf),
    retrieved 2026-08-04) explains the legal mechanics under RCW 36.54 but not the household
    cost.
  - **Lummi Island Ferry Advisory Committee** — vice chair Terry Diffley spoke for the higher
    levy at the hearing and is quoted in both papers.
- **Quality of what exists:** Good on the *what*, thin on the *why now*. Cascadia Daily News has
  the numbers right and published them before the vote. What nobody has published: a plain
  answer to "the road fund saves $3 million a year — where is that money going, and will my
  road actually get plowed?" CDN reports the county does not plan to reduce the road-fund levy
  and will redirect roughly $3 million a year to chip sealing, ditch clearing and snow plowing
  ([CDN, 2026-07-28](https://www.cascadiadaily.com/2026/jul/28/whatcom-council-sets-5-7m-annual-ferry-district-budget/),
  retrieved 2026-08-04) — that is a promise with no published accountability mechanism attached.
  There is a real, cheap opening there.
- **Primary records:** ORD 2026-024 (district creation, adopted 2026-05-12); RES 2026-030
  (ferry district fund, AB2026-520); RES 2026-031 (initial $5.7M budget level, AB2026-552);
  ORD 2026-036 (WCC 10.34 ferry rates, AB2026-524); ORD 2026-037 (WCC 10.36.060, AB2026-525);
  AB2026-521 and AB2026-522 (the $5.2M and $4.2M options, both "No Action Was Taken").
  Minutes: https://whatcom.legistar1.com/whatcom/meetings/2026/7/3191_M_Council_26-07-28_Minutes.pdf

### 2. The $225 million jail and Behavioral Care Center — scope is being cut, in public, right now

- **What it is:** Voters approved a 0.2% sales tax in November 2023 to replace the county jail
  and build a Behavioral Care Center. The Council has since capped preliminary planning at
  $225 million, and the design team has been cutting square footage to fit — the program has
  gone from 227,000 to 154,000 square feet, with another 4,000 square feet still to come out.
- **Salience evidence:**
  - Resolution 2026-018, adopted May 12, 2026, records that the Finance and Facility Advisory
    Board recommended "a planning budget cap of $225 million, comprising $205 million for the
    jail and $20 million for the Behavioral Care Center from the sales tax" ([Approved
    Resolution 2026-018, AB2026-340 Legistar
    attachment](https://whatcom.legistar1.com/whatcom/attachments/202ac09c-22d8-4294-94ab-bfbb67f6f231.pdf),
    retrieved 2026-08-04). The matter's Legistar status is "Revised Substitute Amended and
    Approved," passed 2026-05-12 ([Legistar API,
    matter 23093](https://webapi.legistar.com/v1/whatcom/matters/23093), retrieved 2026-08-04).
  - **Today's presentation to the Council** (August 4, 2026) states the original program was
    227,000 SF, "reduced to 154K SF in response to budget direction," with an "additional 4K SF
    reduction still required to align the project with the approved budget before Schematic
    Design," and prices three items the Council asked to be put back — Rapid Resource Center
    ~$2.2M, contact visitation ~$650K, second courtroom ~$1.5M, total ~$4.3M at $905/SF
    ([Justice Facility & Behavioral Health Treatment Center presentation, August 4, 2026,
    Legistar](https://whatcom.legistar.com/Calendar.aspx), retrieved 2026-08-04).
  - The options presented to accommodate those requests are explicit and unpleasant: "Eliminate
    48 beds in housing; or Reduce the BCC by 16 beds and re-allocate funding to jail; or
    Eliminate the 23-hour portion of the BCC and re-allocate funding to jail" (same
    presentation, retrieved 2026-08-04).
  - The bed-count question has a documented, enormous range. Resolution 2026-018 records that
    the Pasqua Planners forecast produces "an adjusted bed need of 458 when peaking and
    classification factors are applied (not the 480-bed figure that has anchored prior planning
    scenarios)," and that by 2050 the need is 458 if average length of stay is managed to 19
    days, 604 under the primary forecast, and 699 at 29 days — "a range of 241 beds depending on
    whether the County invests in system interventions that reduce length of stay" ([Resolution
    2026-018](https://whatcom.legistar1.com/whatcom/attachments/202ac09c-22d8-4294-94ab-bfbb67f6f231.pdf),
    retrieved 2026-08-04).
  - The project has come back to the Council repeatedly: budget amendment requests no. 9
    (AB2025-678, Sept 2025), no. 10 (AB2026-102, Jan 2026), and no. 11 (AB2026-355, May 2026),
    plus AB2026-608 "Discussion of jail programming results, budget constraints, and design
    process" on July 30, 2026 ([Legistar API, `/whatcom/matters`
    query](https://webapi.legistar.com/v1/whatcom/matters), retrieved 2026-08-04). Eleven budget
    amendments is the salience signal.
- **Who is affected, and how many:** Countywide. The funding source is a 0.2% sales and use tax
  paid by everyone who buys anything in Whatcom County, authorized by Proposition 2023-04 in
  November 2023 under Ordinance 2023-039 ([Resolution
  2026-018](https://whatcom.legistar1.com/whatcom/attachments/202ac09c-22d8-4294-94ab-bfbb67f6f231.pdf),
  retrieved 2026-08-04). The July 2024 interlocal agreement commits the county and cities to
  directing at least 50% of ongoing countywide sales tax revenue to behavioral health, diversion,
  re-entry and supportive housing, "with a goal of reaching that floor no later than 2030" (same
  source).
- **Stage:** Recurring and live. Schematic Design is the next gate; the scope decision has to be
  made before it.
- **Decision-maker:** Whatcom County Council, with the County Executive's office and the cities
  as required partners under the ILA. Resolution 2026-018 states the cities "must concur with
  the County Council's project level decisions for a successful outcome" (same source).
- **Who currently speaks on it:** The county publishes the resolution, the presentations and the
  Pasqua Planners analysis through Legistar, and the record is genuinely detailed — Resolution
  2026-018 runs to a long findings section with the financing assumptions spelled out (PFM
  Financial Advisors modeled a 4.9% borrowing rate and growth of 1.5% in 2026–2027 and 3.0%
  thereafter, producing a $214 million ceiling under a scenario titled "Cities Pay 75% Through
  2034, Suspend 50% Behavioral Health Requirement"). Local coverage exists but I did not find a
  single story that walks a general reader through the $225M cap, the 154K SF program, and the
  bed-count range together.
- **Quality of what exists:** **Poor relative to the stakes, and the raw material is unusually
  good.** Everything needed to write the honest explainer is sitting in one PDF on Legistar. The
  gap is not information, it is translation — nobody has published "here is what you were
  promised in 2023, here is what the $225 million now buys, and here is the specific trade
  currently on the table between 48 jail beds and a rapid resource center." That is close to
  free to own.
- **Primary records:** RES 2026-018 (AB2026-340); ORD 2023-039 (0.2% sales tax, Proposition
  2023-04); July 2024 Interlocal Agreement; AB2025-678 / AB2026-102 / AB2026-355 (project budget
  amendments 9, 10, 11); AB2026-608 (July 30, 2026 discussion); Pasqua Planners Jail Population
  Forecast Analysis (Spring 2026), cited in RES 2026-018.

### 3. The Comprehensive Plan periodic update and the rural zoning map

- **What it is:** Whatcom County finished its Growth Management Act periodic update on July 28,
  2026, adopting amendments to the Comprehensive Plan and the Foothills Subarea Plan, to Title 20
  zoning code, and to the official zoning map. This is the document that governs where housing
  and development can go in the unincorporated county for the next several years.
- **Salience evidence:**
  - All three ordinances passed **5–2** with the same split as the ferry levy — Aye: Boyle,
    Buchanan, Galloway, Rienstra, Scanlon; Nay: Elenbaas, Stremler — first individually and then
    again on the required concurrent-review motion ([Council minutes,
    2026-07-28](https://whatcom.legistar1.com/whatcom/meetings/2026/7/3191_M_Council_26-07-28_Minutes.pdf),
    retrieved 2026-08-04). Enacted as ORD 2026-038, ORD 2026-039 and ORD 2026-040.
  - **Ten people spoke** at the combined public hearing: Bill Geyer, Ryan Bowman, Brian Gass,
    Leah Clark, Patrick Alesse, Lyle Sorenson, Perry Eskridge, Kyle Gebhardt, Barbara Chase,
    Dan Williams (same minutes, retrieved 2026-08-04).
  - The versions adopted were "Revised Substitute" ordinances dated 7.28.2026 (corrected) and
    7.14.2026 — the plan was still being rewritten in the final two weeks (same minutes).
- **Who is affected, and how many:** Every property in unincorporated Whatcom County, plus
  anyone whose housing costs are set by what can be built there. I did not find a published
  count of parcels rezoned. **[NEEDS SOURCE — number of parcels affected by the ORD 2026-040
  zoning map amendments]**
- **Stage:** Decided July 28, 2026, subject to the GMA appeal window before the Growth Management
  Hearings Board. **I did not verify whether an appeal has been filed** — see Dead ends.
- **Decision-maker:** Whatcom County Council, with Planning and Development Services staffing it.
- **Who currently speaks on it:** The county's Planning and Development Services department
  publishes the record through Legistar. Whatcom Watch's "Watching Government" column
  reconstructs Council votes item by item, which is the closest thing to a running public ledger
  of this Council — but the July 2026 issue was still working through the **May 12, 2026**
  meeting ([Whatcom Watch, current issue July 2026, vol. 35 no.
  7](https://whatcomwatch.org/), retrieved 2026-08-04), so the periodic update will not appear
  there until roughly September.
- **Quality of what exists:** Weak for a general reader. A three-ordinance GMA package with
  revised substitutes adopted the same night is close to unreadable without a guide, and I found
  no plain-language summary of what actually changed on the zoning map. This is a high-effort,
  high-value gap — high effort because you have to read the ordinances.
- **Primary records:** ORD 2026-038 (AB2026-553, Comprehensive Plan and Foothills Subarea Plan);
  ORD 2026-039 (AB2026-489, Title 20 zoning); ORD 2026-040 (AB2026-490, official zoning map).
  Minutes: https://whatcom.legistar1.com/whatcom/meetings/2026/7/3191_M_Council_26-07-28_Minutes.pdf

### 4. Bellingham Initiative 26-01 — banning algorithmic rent price-setting

- **What it is:** A citizen initiative certified to the November 3, 2026 ballot in the City of
  Bellingham would add a chapter to the municipal code making it unlawful for landlords to use
  "coordinating services" — software that pools rental pricing and occupancy data from multiple
  landlords and recommends prices.
- **Salience evidence:**
  - It got there by signature. Community First Whatcom "turned in roughly 5,700 signatures and
    the Whatcom County Auditor's Office certified the count on July 2," which gave the city
    council until July 27 to adopt it outright, refer it to the November ballot, or reject it and
    propose an alternative ([Salish Current, Community Voices, "Bellingham's rent software ban
    won't fix Washington's housing crisis," July 27,
    2026](https://salish-current.org/2026/07/27/bellinghams-rent-software-ban-wont-fix-washingtons-housing-crisis/),
    retrieved 2026-08-04). Several thousand people signing a petition is the salience signal.
  - The City Attorney's explanatory statement, dated August 3, 2026, describes it as defining
    coordinating services as "tools that
  collect rental pricing and occupancy data from multiple landlords and use algorithms to
  recommend future rental prices or terms," making it unlawful "for landlords to agree to set
  rental prices, to pay for or use coordinating services, or for service providers to offer such
  services to multiple landlords," with carve-outs for recordkeeping tools, aggregated market
  reports, and financing or appraisal data. It creates civil damages and attorney fees, City
  Attorney enforcement, civil infractions and "potential misdemeanor penalties for repeated or
  willful violations," plus whistleblower and anti-retaliation protections, and exempts hotels,
  motels and short-term rentals ([Office of the City Attorney, City of Bellingham, explanatory
  statement for Initiative Measure no. 2026-01, filed with the Whatcom County
  Auditor](https://www.whatcomcounty.us/DocumentCenter/View/115499/City-of-Bellingham-Initiative-26-01-Original-Explanatory-Statement),
  retrieved 2026-08-04).
- **Who is affected, and how many:** Renters and landlords inside Bellingham city limits.
  **[NEEDS SOURCE — number of rental units in Bellingham]**
- **Stage:** Pending vote, November 3, 2026. Ballots mail October 14, 2026 ([Whatcom County
  Auditor, Elections in 2026](https://www.whatcomcounty.us/4443/Elections-in-2026), retrieved
  2026-08-04).
- **Decision-maker:** Bellingham voters. It appears only on Bellingham ballots, so a
  county-wide or legislative-district candidate will be asked about it by some constituents and
  not others.
- **Who currently speaks on it:**
  - **Salish Current** published a Community Voices essay *against* the measure on July 27, 2026,
    by Kevin Van De Wege, who "served in the Washington State Legislature for 18 years, in the
    Senate from 2017 to 2024 and in the House of Representatives from 2007 to 2017"
    ([Salish Current](https://salish-current.org/2026/07/27/bellinghams-rent-software-ban-wont-fix-washingtons-housing-crisis/),
    retrieved 2026-08-04). It argues the ban "won't build a single new apartment or lower a
    single rent check" and points to HB 1217 and HB 1110 as the real levers.
  - **Community First Whatcom** ran the signature drive. I did not find a published argument in
    favor of the measure from them or anyone else — see Dead ends.
  - **City of Bellingham** — the City Attorney's explanatory statement, which is neutral by law.
- **Quality of what exists:** **The only published argument about this measure is against it, and
  it was written by a former state senator.** Three months from a vote, on a measure that got
  ~5,700 signatures, there is no published case for the yes side and no neutral explainer of what
  the software actually does in Bellingham. That is the clearest asymmetry in the county.
- **Primary records:** City of Bellingham Initiative 26-01;
  [resolution](https://www.whatcomcounty.us/DocumentCenter/View/115498/City-of-Bellingham-Initiative-26-01-Original-Resolution) and
  [explanatory statement](https://www.whatcomcounty.us/DocumentCenter/View/115499/City-of-Bellingham-Initiative-26-01-Original-Explanatory-Statement),
  both via the Whatcom County Auditor.

### 5. Property-tax stacking — two levy lid lifts on top of the new ferry tax

- **What it is:** In the same year Whatcom County added a countywide ferry levy, both the City of
  Lynden and Fire Protection District No. 1 are asking voters for levy lid lifts. Voters in
  those jurisdictions will see all three increases arrive together.
- **Salience evidence:**
  - **City of Lynden, Proposition 2026-05:** would set a maximum rate of $1.54304 per $1,000 for
    2026 collection in 2027, "an increase of $0.50/$1,000 over the 2025 levy rate," with a limit
    factor of 100% plus 3% through 2035. The city's own explanatory statement says revenues
    would fund police and fire, street and park maintenance, the Lynden Community/Senior Center,
    "restoring staff positions cut during 2025 and 2026," and "reopening City Hall to the public
    on Fridays" ([City of Lynden explanatory statement, filed with the Whatcom County
    Auditor](https://www.whatcomcounty.us/DocumentCenter/View/115500/City-of-Lynden-Prop-2026-05-Original-Explanatory-Statement),
    retrieved 2026-08-04). Staff cuts and a closed city hall on Fridays are the kind of concrete
    detail that carries at a door.
  - **Fire Protection District No. 1, Proposition 2026-08:** would set the levy at $1.48 per
    $1,000 for 2026 collection in 2027, "replace the final year of the levy lid lift approved by
    the voters in 2021," and set an annual limit factor of 6% for the following nine years
    ([FPD 1 explanatory statement, filed with the Whatcom County
    Auditor](https://www.whatcomcounty.us/DocumentCenter/View/115502/FPD-1-Prop-2026-08-Original-Explanatory-Statement),
    retrieved 2026-08-04).
  - FPD 1 also ran a levy lid lift, Proposition 2026-02, on the August 4 primary ballot
    ([Whatcom County Auditor, 2026 Ballot
    Resolutions](https://www.whatcomcounty.us/4703/2026-Ballot-Resolutions), retrieved
    2026-08-04). Asking twice in one year is itself the finding.
- **Who is affected, and how many:** Lynden property owners; FPD 1 property owners. Combined with
  the 8.7-cent ferry levy, a Lynden homeowner inside FPD 1 faces increases from three separate
  taxing districts in one cycle.
- **Stage:** Pending vote, November 3, 2026.
- **Decision-maker:** Voters in each district.
- **Who currently speaks on it:** The districts' own explanatory statements, published free by
  the county auditor. The Lynden Tribune covers Lynden and ran a story on the auditor recruiting
  Local Voters' Pamphlet committee members ([Lynden Tribune](https://www.lyndentribune.com/),
  retrieved 2026-08-04), so it is the outlet to watch here.
- **Quality of what exists:** The explanatory statements are unusually clear — Lynden's in
  particular names the specific services at stake. What is missing is any published side-by-side
  of what the three increases add up to for one household. Nobody produces that document, because
  no single institution is responsible for all three.
- **Primary records:** City of Lynden Prop 2026-05
  ([resolution](https://www.whatcomcounty.us/DocumentCenter/View/115501/City-of-Lynden-Prop-2026-05-Original-Ressolution));
  FPD 1 Prop 2026-08
  ([resolution](https://www.whatcomcounty.us/DocumentCenter/View/115503/FPD-1-Prop-2026-08-Original-Resolution));
  FPD 1 Prop 2026-02 (August primary).

## Contested space summary

The short version of "who currently answers this well." Ranked by how badly the honest answer is
missing.

| Issue | Who covers it now | How well | Vacuum? |
|---|---|---|---|
| Bellingham Initiative 26-01 (algorithmic rent pricing) | One Salish Current Community Voices essay **against**, by former state senator Kevin Van De Wege (2026-07-27); the City Attorney's neutral explanatory statement. Nothing found in favor. | One-sided. The against case is published and well argued; the for case and a plain explainer of what the software does are both absent. | **Yes — asymmetric.** Highest-value opening in the county, and the shape of the gap is unusually clear. |
| Jail / BCC scope trade-offs at the $225M cap | County publishes RES 2026-018, the Pasqua Planners forecast and the August 4 presentation through Legistar; no outlet has synthesized them | The primary record is excellent; the public explanation does not exist. The live trade — 48 beds versus a rapid resource center — has not been written up anywhere I could find. | **Yes, but the raw material is unusually strong.** Cheap to own, and defensible because every number has a document behind it. |
| Where the $3M/year of freed road-fund money actually goes | CDN reported the promise; no one is tracking it | One sentence in one story. No published accountability mechanism. | **Yes.** Small, concrete, and the kind of thing a challenger can commit to following. |
| Comprehensive Plan periodic update / zoning map | County Legistar record; Whatcom Watch "Watching Government" will cover it ~2 months late | Complete but unreadable. Three ordinances with same-night revised substitutes. | **Partial.** Real gap, but expensive — you have to actually read Title 20. |
| Combined 2027 property-tax impact (ferry + Lynden + FPD 1) | Each district publishes its own explanatory statement; nobody adds them up | Each piece is clear; the sum is unpublished because no institution owns the question. | **Yes**, and it is arithmetic rather than reporting. |
| The ferry levy itself | Cascadia Daily News (4 original stories, Julia Tellman); Bellingham Herald (2); public works memo | **Genuinely well covered.** CDN published all three options with per-household costs *before* the vote. | **No.** Do not try to own this. Cite CDN and move to the road-fund question. |

An issue where three institutions already publish well is expensive to own and pointless to
try. An issue where the honest answer does not exist anywhere is nearly free.

## Ballot measures on the same ballot

Local measures voters will see alongside this race, from the county auditor's certified list.
**Caveat: the resolution deadline for the November 3 ballot was August 4, 2026 — today — so this
list may not be final** ([Whatcom County Auditor, 2026 Ballot
Resolutions](https://www.whatcomcounty.us/4703/2026-Ballot-Resolutions), retrieved 2026-08-04).

| Measure | What it does | Position needed? | Source |
|---|---|---|---|
| City of Bellingham Initiative 26-01 | Prohibits landlords from using algorithmic "coordinating services" to set rents; civil damages, City Attorney enforcement, whistleblower protections; exempts hotels and short-term rentals | **Yes**, for anyone on a Bellingham ballot. Highest-salience measure on the list. | [Explanatory statement](https://www.whatcomcounty.us/DocumentCenter/View/115499/City-of-Bellingham-Initiative-26-01-Original-Explanatory-Statement), retrieved 2026-08-04 |
| City of Lynden Proposition 2026-05 | Levy lid lift to a maximum $1.54304/$1,000 (up $0.50/$1,000 over 2025) for police, fire, streets, parks, senior center, restoring 2025–2026 staff cuts, reopening City Hall Fridays | **Yes** for Lynden. A tax increase with named services attached. | [Explanatory statement](https://www.whatcomcounty.us/DocumentCenter/View/115500/City-of-Lynden-Prop-2026-05-Original-Explanatory-Statement), retrieved 2026-08-04 |
| Fire Protection District No. 1 Proposition 2026-08 | Sets levy at $1.48/$1,000 for 2027 collection; replaces the final year of the 2021 lid lift; 6% annual limit factor for nine years | **Yes** inside FPD 1 | [Explanatory statement](https://www.whatcomcounty.us/DocumentCenter/View/115502/FPD-1-Prop-2026-08-Original-Explanatory-Statement), retrieved 2026-08-04 |
| City of Bellingham Proposition 2026-06 | Authorizes the city's Salary Commission to set the mayor's salary | Low salience; be able to answer it | [Resolution](https://www.whatcomcounty.us/DocumentCenter/View/115495/City-of-Bellingham-Prop-2026-06-Original-Resolution), retrieved 2026-08-04 |
| City of Bellingham Proposition 2026-07 | Streamlines the city's contract review process to allow electronic signatures | Low salience; administrative | [Resolution](https://www.whatcomcounty.us/DocumentCenter/View/115497/City-of-Bellingham-Prop-2026-07-Original-Resolution), retrieved 2026-08-04 |

Also on the August 4, 2026 primary ballot, for context on what voters were just asked: FPD 1
Proposition 2026-02 (levy lid lift), Glacier Fire & Rescue Proposition 2026-04 (authorizing a
regular property tax levy), and FPD 21 Proposition 2026-03 (authorizing a regular property tax
levy) (same source, retrieved 2026-08-04).

## Dead ends and gaps

**The Legistar vote-history endpoint returned nothing usable.** The detection procedure points to
`/Matters/{id}/Histories` for "the vote history on one item, including who voted how." For
Whatcom, `MatterHistoryTally` was null on every record I inspected, including on matters that
were plainly contested. Every vote count in this file therefore came from parsing the minutes
PDF, not from the API. This is the single biggest gap between the documented procedure and what
actually happened.

**`pdftotext` was unavailable on this machine** (a broken Homebrew dependency chain —
`Library not loaded: libgpgmepp.6.dylib`). Text extraction ran through `pypdf` instead. Whatcom's
minutes PDFs carry a text layer, so this cost nothing here; it cost a great deal in the news
desert county.

**Washington Secretary of State elections pages returned HTTP 403** to scripted requests
(`https://www.sos.wa.gov/elections/dates-and-deadlines`, checked 2026-08-04). The county
auditor's own calendar carried the same information and was fully accessible, which is the
better source anyway.

**Cascadia Daily News, the Bellingham Herald, the Northern Light and the Washington State
Standard all returned HTTP 403 to scripted requests** while being perfectly reachable in a
browser. Any automated media scan that treats a 403 as "outlet is dead" will misclassify a county
with healthy local news as a desert. Every 403 in this scan was a live, active outlet.

**Fire Protection District No. 1 has no agenda system I could find.** Searching for the district's
own meeting records did not produce an agenda portal, and I did not locate minutes for the board
meeting that adopted Proposition 2026-08. The measure was found only because the county auditor
publishes ballot resolutions. This is exactly the "boring body, real money" case the skill warns
about, and the detection procedure did not reach it. Next step would be a records request to the
district or a call to the county auditor.

**I did not verify whether the Comprehensive Plan update has been appealed** to the Growth
Management Hearings Board. In Washington that appeal window matters and the board publishes a
docket; I ran out of scan time before checking it.

**I found no published argument in favor of Bellingham Initiative 26-01**, and no
campaign-committee filing either way. Community First Whatcom ran the signature drive but I did
not locate a website or statement from them. I also did not check the Washington Public
Disclosure Commission for registered for/against committees, which is the obvious next step and
would take about ten minutes.

**Parcel and unit counts are missing.** I could not source the number of parcels rezoned by
ORD 2026-040 or the number of rental units in Bellingham. Both are marked `[NEEDS SOURCE]` above
rather than estimated.

**The 1,000-record cap on the Legistar Matters endpoint was hit.** A 12-month window on a county
this active returns close to a thousand matters, so the scan is complete for the window used but
would silently truncate on a longer one. Narrow by date or by `MatterTypeName`.

**The November 3 ballot list may be incomplete.** The resolution deadline was August 4, 2026 —
the day of this scan. Re-check the auditor's page after certification.
