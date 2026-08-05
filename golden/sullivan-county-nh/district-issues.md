---
jurisdiction: "Sullivan County, New Hampshire (Claremont, Newport, Charlestown, Cornish, Croydon, Unity, Plainfield, Grantham, Sunapee, Springfield, Goshen, Lempster, Acworth, Langdon, Washington)"
ocd_id: "ocd-division/country:us/state:nh/county:sullivan"
scan_date: "2026-08-04"
scan_window: "2025-08-01 to 2026-08-04"
governing_bodies:
  - "Sullivan County Board of Commissioners (3 members)"
  - "Sullivan County Delegation / County Convention (the county's NH House members, sitting as the county legislature)"
  - "Sullivan County Executive Finance Committee (a subcommittee of the Delegation)"
  - "Claremont City Council (9 members)"
  - "Claremont School Board / SAU 6"
  - "Sullivan County Criminal Justice Coordinating Committee (SCCJCC)"
agenda_vendor: "none-found"
date_created: "2026-08-04"
date_modified: "2026-08-04"
---

# District issues — Sullivan County, New Hampshire

Written by `district-issue-scan`. Ranked by documented local salience, not by national issue
polling.

This is a **golden reference output** and the harder of the two cases: Sullivan County is a
documented news desert. It profiles no candidate. Elected officials are named only in connection
with recorded roll-call votes, which is what county minutes are.

**Why this county is the hard case.** Northwestern University's 2025 State of Local News Report
classed Sullivan County as one of the places "without any local news source," and neighboring
Cheshire County as a one-source county — "the only two counties in New Hampshire where residents
have fewer than three local papers based within them" ([Keene Sentinel, "Twin State Valley
reflects on life without local news," by Abigail
Ham](https://www.keenesentinel.com/news/local/twin-state-valley-nh-vt-reflects-on-life-without-local-news/article_a516c6ec-1e12-417b-a511-f71958d9d06d.html),
retrieved 2026-08-04). The Claremont-based *Eagle Times* suspended operations in July 2025 after
192 years, following a staff walkout over unpaid wages ([Union Leader,
2025-07-01](https://www.unionleader.com/news/business/eagle-times-of-claremont-suspends-operations/article_4110d3b3-d2e2-408c-b147-d1a071095a02.html);
[NHPR,
2025-07-30](https://www.nhpr.org/nh-news/2025-07-30/he-bought-the-local-paper-to-help-his-hometown-now-hes-being-blamed-for-its-demise),
both retrieved 2026-08-04). Every issue below is therefore reconstructed from primary records
rather than from reporting — which is exactly what the skill is supposed to be able to do.

**Election context.** The New Hampshire state primary is September 8, 2026, and the general
election is November 3, 2026; the filing period ran June 3–12, 2026 ([NH Secretary of State,
Running for Office](https://www.sos.nh.gov/elections/running-office), retrieved 2026-08-04).
**The connection a campaign needs to understand here:** in New Hampshire the county convention
*is* the county's delegation of state representatives. The Sullivan County Executive Finance
Committee's own budget presentation lists every member as "Rep." with a House district number
([Sullivan County EFC Presentation to Delegation, FY2027 Budget, July 2,
2026](https://sullivancountynh.sharepoint.com/:f:/s/SullivanCountyAgendaMeetingNotes/IgCEk4ic7o9YT6Ffvz_0sZK1Ad1Ev8KzPJ4TZAfhGZkYPnM?e=rYkTU2),
retrieved 2026-08-04). A vote for a state representative in Sullivan County on November 3 is also
a vote on who sets the county budget and who decided the TRAILS question below.

## Sources checked

| Source | Type | URL | Window covered | Checked | Yield |
|---|---|---|---|---|---|
| `sullivancountynh.gov` — vendor detection | County website | https://www.sullivancountynh.gov/ | 2026 | 2026-08-04 | Site footer reads "Government Websites by CivicPlus®". **But `/AgendaCenter` and `/agendacenter` both return HTTP 404** — the standard CivicPlus agenda module is not deployed. `/ArchiveCenter` and `/DocumentCenter` return 200. |
| Sullivan County "Budgets, Minutes & Annual Reports" hub | County website | https://www.sullivancountynh.gov/129/Agendas-Minutes | 2026 | 2026-08-04 | **The actual answer.** Nine links, all pointing off-domain to Microsoft SharePoint folders. No vendor system at all. |
| Commissioners Meeting Agenda and Minutes (SharePoint) | Primary records | https://sullivancountynh.sharepoint.com/:f:/s/SullivanCountyAgendaMeetingNotes/IgBUB_S1_lEzS7wn3zkcFzt6AQBC2wWu74X_aU_eCLDz4kI?e=tI3Gm9 | 2025–2026 | 2026-08-04 | Draft and ratified minutes as PDFs. Reachable in a browser; a scripted `curl` gets a login redirect or a JavaScript stub. |
| Delegation Meeting Agendas, Materials, and Minutes (SharePoint) | Primary records | https://sullivancountynh.sharepoint.com/:f:/s/SullivanCountyAgendaMeetingNotes/IgCEk4ic7o9YT6Ffvz_0sZK1Ad1Ev8KzPJ4TZAfhGZkYPnM?e=rYkTU2 | 2025–2026 | 2026-08-04 | FY2027 budget convention minutes, EFC presentation, roll-call votes |
| Budget, Taxes & Audit Documents (SharePoint) | Primary records | https://sullivancountynh.sharepoint.com/:f:/s/SullivanCountyAgendaMeetingNotes/IgDgylHZS1koSq2v1wLdsq3nAWF5n3URA7BGhZBMQQMC6j4?e=HYbOxp | FY2027 | 2026-08-04 | County-by-county tax comparison showing Sullivan's FY2027 increase |
| Criminal Justice Coordinating Committee Minutes (SharePoint) | Primary records | https://sullivancountynh.sharepoint.com/:f:/s/SullivanCountyAgendaMeetingNotes/IgC1_rfDE8e4QaPi2cR7-iPpAT8oyb58rXI6prJqVlrAxhE?e=nwG1gx | 2025–2026 | 2026-08-04 | Folder exists and is the venue where the TRAILS-versus-Drug-Court question is being worked. **Not read in this scan** — flagged as the highest-value unexamined source. |
| Sullivan County Delegation Convention minutes, 2026-07-02 (DRAFT) | Primary record, PDF **with** text layer | via the Delegation SharePoint folder above | Single meeting | 2026-08-04 | Complete roll calls on the TRAILS cut and the FY2027 budget. **The ratified version of the same minutes is an image-only scan with no text layer; only the draft is searchable.** |
| Sullivan County Board of Commissioners minutes, 2026-07-20 (DRAFT) | Primary record, PDF with text layer | via the Commissioners SharePoint folder above | Single meeting | 2026-08-04 | The TRAILS follow-up work plan; attendance list; next steps for 2026-08-17. **The ratified version is again an image-only scan.** |
| `claremontnh.com` — vendor detection | City website | https://www.claremontnh.com/council-minutes | 2026 | 2026-08-04 | **No vendor.** Bespoke CMS with a JavaScript "Select Year / Select Month" document picker. Not crawlable; documents must be pulled through a browser. |
| Claremont City Council agenda, 2026-06-10 | Primary record | via claremontnh.com council documents | Single meeting | 2026-08-04 | Ordinance 645 (water rates) and 646 (sewer rates), first readings |
| Claremont City Council agenda + packet, 2026-06-24 | Primary record, **206-page image-only scan** | via claremontnh.com council documents | Single meeting | 2026-08-04 | Full text of Ordinances 645 and 646 with rate tables, plus the June 10 minutes. **Zero text layer — recovered by OCR.** See Dead ends. |
| Claremont posted minutes for 2026-06-24 and 2026-07-22 | Primary record | claremontnh.com | Jun–Jul 2026 | 2026-08-04 | **Not found.** The June 10 minutes were obtainable only because they were bound into the June 24 packet. |
| Claremont Community Media Center (CCTV) video-on-demand API | Public meeting video | https://reflect-claremont.cablecast.tv/cablecastapi/v1/shows | 2026 | 2026-08-04 | **6,676 shows.** Government meetings on demand: School Board 7/21/26, Conservation Commission 7/16/26, Planning Board 7/13/26, Sullivan County Commissioners 6/15/26, City Council 6/10/26. The single best-functioning public-records channel in this county. |
| MeetingWatch — Claremont City Council | **Third-party AI meeting-transcription service, not a newsroom** | https://meetingwatch.org/nh/claremont/city-council/ | Feb–Jul 2026 | 2026-08-04 | **Found last, and it changes the picture.** 13 council meetings transcribed and indexed since February 2026, with per-meeting reports, vote counts, quoted statements and timestamps into the CCTV video. Also covers Newport, Plainfield, Springfield and Sunapee. Its analysis is AI-generated and it says so; treat it as an index, not a source. See the media map. |
| `eagletimes.com` | Former daily | https://www.eagletimes.com/ | 2026 | 2026-08-04 | HTTP 200, but the page reads "A new website coming soon! — BigScoots.com … is parked at BigScoots." **A parked domain.** |
| Valley News | Regional daily | https://vnews.com/ | 2025–2026 | 2026-08-04 | Covers Claremont, Newport, Charlestown, Cornish, Croydon, Plainfield, Springfield, Sunapee and Unity per its own published coverage-area list. Multiple Claremont school-crisis stories. |
| New Hampshire Bulletin | Statewide nonprofit (States Newsroom) | https://newhampshirebulletin.com/ | 2025–2026 | 2026-08-04 | Sustained coverage of the Claremont school deficit and HB 292. HTTP 403 to a scripted request; readable in a browser. |
| The Vermont Journal & The Shopper / The Message of the Week | Weekly, Ludlow VT | https://vermontjournal.com/ | 2025–2026 | 2026-08-04 | **Covers Claremont City Council meeting by meeting.** The single most surprising finding in this scan — see the media map. |
| NH Secretary of State — 2026 election calendar | State record | https://www.sos.nh.gov/elections/running-office | 2026 | 2026-08-04 | Primary Sept 8; general Nov 3; filing June 3–12; per-office fees and petition counts; nomination-paper deadlines. HTTP 403 to a scripted request; readable in a browser. |
| Sullivan County local ballot measures for Nov 3, 2026 | Election record | — | 2026 | 2026-08-04 | **None found, and structurally there should be none** — NH town, city and school money questions are decided at March town meeting / SB2 ballots, not on the November state ballot. See Ballot measures. |

## Ranked issues

### 1. The Delegation cut $500,000 from TRAILS — the jail's substance-use treatment program — on a 7–5 vote, and the county is now trying to work out what that means

- **What it is:** TRAILS is a residential substance-use treatment program run inside the Sullivan
  County Department of Corrections, operating since 2010. On July 2, 2026, at the county budget
  convention, the Delegation adopted an amendment cutting $500,000 aimed specifically at that
  program. County staff are now assembling the analysis that was not available before the vote.
- **Salience evidence:**
  - **The roll call.** "A roll call vote was taken on Rep. Girard's amendment. Those voting 'No'
    were Rep's M. Aron, Cloutier, Damon, Palmer, and Sullivan; those voting 'Yes' were Rep's
    J. Aron, Drye, Girard, Grant, Heminway, Rollins, and Smith. The vote carried 7 Yes, and 5 No.
    Amendment adopted." ([Sullivan County Delegation Convention of FY27 Budget, 7/02/2026 Minutes
    — DRAFT, p. 6, via the county's Delegation SharePoint
    folder](https://sullivancountynh.sharepoint.com/:f:/s/SullivanCountyAgendaMeetingNotes/IgCEk4ic7o9YT6Ffvz_0sZK1Ad1Ev8KzPJ4TZAfhGZkYPnM?e=rYkTU2),
    retrieved 2026-08-04.) A 7–5 vote on a single program line is the strongest salience signal
    in this county.
  - **The debate is in the record, at length.** The mover framed it as a sunset: the program costs
    about $750,000 a year to run, so a $500,000 cut "allows them $250K to sunset the program out."
    Rep. Sullivan objected that "this reduction topic was not brought up with the EFC — it could
    have and should have been discussed but wasn't," and said he "can't support an abrupt
    elimination of this nature." Rep. Palmer "noted he did not have enough info to vote in favor
    of the amendment." Rep. Damon asked whether the commissioners would have flexibility to cut
    elsewhere; "Chair Smith explained this motion is targeted at TRAILS." (Same minutes, pp. 4–6,
    retrieved 2026-08-04.)
  - **The operating numbers, from the superintendent, on the record.** DOC Superintendent Coughlan
    told the convention there were **five people enrolled in TRAILS that day, with one having just
    graduated**; that TRAILS runs in 90-day sessions averaging **5–7 inmates per session**; that
    there is a female unit holding eight, all for TRAILS; and that since TRAILS opened in 2010 it
    is estimated to have **saved the county approximately $6 million**. He also noted that even if
    TRAILS were cut, the county "would still need Clinicians and Case Managers" (same minutes,
    retrieved 2026-08-04).
  - **It did not end with the vote.** Eighteen days later, County Manager Ferland told the
    commissioners that "following the Delegation's decision at Convention to cut the TRAILS
    program, and after a conversation with Delegation Chair Smith," he had asked the HR director
    to lead a cross-department effort to "compile numbers and provide clarity on the populations
    served by TRAILS compared with Drug Court," gather "statistics on recidivism rates and cost
    avoidance related to DOC bed usage," and "determine what services would need to be outsourced,
    and at what cost, if staff positions are eliminated." The County Attorney was on the call "to
    better understand perspectives from local police departments, judges, and probation and
    parole," and noted that "although clinicians are housed under the TRAILS budget, they provide
    essential services for the criminal justice system beyond that program." The county manager
    discussed "the need to determine when to convene the Delegation and present a funding outline,
    including potential offsets and a possible 4-month funding approach for active cases already
    in the adjudication process." ([Sullivan County Board of Commissioners, 7/20/2026 Regular
    Business Meeting Minutes — DRAFT, pp. 1–2, via the Commissioners SharePoint
    folder](https://sullivancountynh.sharepoint.com/:f:/s/SullivanCountyAgendaMeetingNotes/IgBUB_S1_lEzS7wn3zkcFzt6AQBC2wWu74X_aU_eCLDz4kI?e=tI3Gm9),
    retrieved 2026-08-04.)
- **Who is affected, and how many:** Directly, a small number — 5–7 people per 90-day session, so
  roughly 20–28 people a year, plus the clinical staff whose positions sit in that budget line.
  Indirectly, everyone: Sullivan County has about 43,000 residents ([Keene
  Sentinel](https://www.keenesentinel.com/news/local/twin-state-valley-nh-vt-reflects-on-life-without-local-news/article_a516c6ec-1e12-417b-a511-f71958d9d06d.html),
  retrieved 2026-08-04), and the county's own analysis is about whether treatment or incarceration
  is cheaper. **The smallness of the number is itself the argument on both sides** and is
  documented rather than asserted.
- **Stage:** **Decided but actively being reopened.** The cut is in the adopted FY2027 budget. The
  commissioners scheduled follow-up for **August 17, 2026 at 2:00 p.m.** (same commissioners
  minutes, retrieved 2026-08-04), and the county manager is weighing when to reconvene the
  Delegation.
- **Decision-maker:** The Sullivan County Delegation, with the Board of Commissioners
  administering and the Executive Finance Committee as the gatekeeping subcommittee. **All twelve
  Delegation members are state representatives whose seats are on the November 3, 2026 ballot.**
- **Who currently speaks on it:** **Almost nobody.** I found no news coverage of the TRAILS vote
  in any outlet during this scan. The only public account is the draft minutes themselves, posted
  to a SharePoint folder linked from a county web page, and the CCTV video record. The Sullivan
  County Criminal Justice Coordinating Committee is discussing it — the commissioners' minutes
  name it as where the topic originated — and its minutes folder is public, but I did not read
  it.
- **Quality of what exists:** **The record is genuinely good and completely unread.** The draft
  minutes contain the full debate, the roll call, the cost figures and the enrollment numbers.
  Nobody has turned any of that into something a resident could read in five minutes. This is the
  clearest issue-vacuum I found in either county in this exercise.
- **Primary records:** Sullivan County Delegation Convention of FY27 Budget, 7/02/2026, DRAFT
  minutes; Sullivan County BOC Regular Business Meeting, 7/20/2026, DRAFT minutes; Sullivan County
  EFC Presentation to Delegation, FY2027 Budget, 7/02/2026. All in the county's SharePoint folders
  linked from https://www.sullivancountynh.gov/129/Agendas-Minutes.

### 2. The FY2027 county budget raises $21,009,303 in property taxes, up 6.45%

- **What it is:** Sullivan County adopted a $44,094,238 budget for FY2027 that raises just over
  $21 million from county property taxes — a 6.45% increase. The number moved three times in one
  evening as the Delegation amended it on the floor.
- **Salience evidence:**
  - **The arithmetic is on the record, line by line.** The Executive Finance Committee recommended
    a $44,519,738 budget with $21,434,803 to be raised by taxes, an 8.60% increase, "Approx $50
    per year for home valued at $250,000" — and noted "EFC voted 3-2 in support of this proposal"
    ([Sullivan County EFC Presentation to Delegation, FY2027 Budget, July 2,
    2026](https://sullivancountynh.sharepoint.com/:f:/s/SullivanCountyAgendaMeetingNotes/IgCEk4ic7o9YT6Ffvz_0sZK1Ad1Ev8KzPJ4TZAfhGZkYPnM?e=rYkTU2),
    retrieved 2026-08-04). The EFC had already cut the commissioners' request, reducing the
    increase "from 9.89% to 8.60%."
  - The floor then amended it again: the $500,000 TRAILS cut, plus **$25,000 restored to Discover
    Sugar River Region** (amendment adopted 10 yes, 1 no, 1 abstention) and **$49,500 restored to
    County Grants** (adopted 7–5). Chair Smith asked for the running total and the clerk recorded
    it: "Amendments change the budget to $44,094,238 ($44,519,738.00-$500,000+$25,000+$49,500),
    with taxes to be raised of $21,009,303 ($21,434,803-$425,500)" ([Delegation Convention
    7/02/2026 DRAFT minutes, p.
    8](https://sullivancountynh.sharepoint.com/:f:/s/SullivanCountyAgendaMeetingNotes/IgCEk4ic7o9YT6Ffvz_0sZK1Ad1Ev8KzPJ4TZAfhGZkYPnM?e=rYkTU2),
    retrieved 2026-08-04).
  - **Final adoption, 9–3.** "Those voting 'Yes' were Rep's J. Aron, M. Aron, Cloutier, Drye,
    Girard, Grant, Hemingway, Rollins, and Smith; those voting 'No' was Damon, Palmer, and
    Sullivan. 9-Yes and 3-No. Motion adopted." (Same minutes, p. 9, retrieved 2026-08-04.)
  - **The county confirms the final number independently.** Sullivan's own FY2027 tax comparison
    lists "Sullivan | FY2027 | $21,009,303 | 6.45% | Increase over 2026," ranking it 9th of ten
    responding New Hampshire counties by dollars raised, against an average reported increase of
    6.6% ([Sullivan County, County Taxes to Be Raised — Responding Counties, in the Budget, Taxes
    & Audit Documents SharePoint
    folder](https://sullivancountynh.sharepoint.com/:f:/s/SullivanCountyAgendaMeetingNotes/IgDgylHZS1koSq2v1wLdsq3nAWF5n3URA7BGhZBMQQMC6j4?e=HYbOxp),
    retrieved 2026-08-04). That document's own footer states: "Table, Graph and format of this
    report was created using AI."
  - **The drivers are stated plainly by the EFC:** nursing-home census down because of
    construction ("Lower census = less revenue"), the "Final $5M bond for project" with a bond
    payment of about $400K in FY27, a **7.7% increase to healthcare costs** and a **3.1% cost of
    living adjustment**, against a Sullivan County Health Care reserve fund with a "current
    balance: $0," a capital reserve of about $800K, and an unassigned fund balance of about $4.0M
    ([EFC presentation, slides 3–4](https://sullivancountynh.sharepoint.com/:f:/s/SullivanCountyAgendaMeetingNotes/IgCEk4ic7o9YT6Ffvz_0sZK1Ad1Ev8KzPJ4TZAfhGZkYPnM?e=rYkTU2),
    retrieved 2026-08-04).
- **Who is affected, and how many:** Every property taxpayer in the county's fifteen towns and
  the city of Claremont. On the EFC's own arithmetic, roughly $50 a year on a $250,000 home at the
  8.60% figure — the adopted 6.45% figure is lower, but I did not find a published per-household
  restatement at the final number. **[NEEDS SOURCE — per-household impact at the adopted 6.45%
  increase]**
- **Stage:** Decided July 2, 2026, in effect for FY2027 (July 1, 2026 – June 30, 2027).
- **Decision-maker:** Sullivan County Delegation, on recommendation from the Executive Finance
  Committee. Both are made up of the county's state representatives.
- **Who currently speaks on it:** The county publishes the EFC presentation and the minutes. I
  found no news story about the Sullivan County FY2027 budget in any outlet. The county's own tax
  comparison — the document that puts Sullivan's increase next to the other nine counties — is
  the single most useful public artifact and is buried three clicks into a SharePoint folder.
- **Quality of what exists:** The primary record is unusually complete for a county this size,
  and the EFC presentation is clear. The public explanation does not exist. A one-page "your
  county tax bill went up 6.45%; here is where the money went and here is the roll call" would be
  the first such document in the county.
- **Primary records:** Sullivan County Delegation Convention of FY27 Budget, 7/02/2026 DRAFT
  minutes (budget adoption and all three floor amendments); Sullivan County EFC Presentation to
  Delegation, FY2027 Budget; Sullivan County FY2027 County Taxes to Be Raised comparison. The
  Delegation also adopted the standard RSA 24:14/24:15 transfer authorization (12–0) and
  unanticipated-funds authorization at the same meeting.

### 3. The Claremont School District's $5 million hole, and what the city is still paying for it

- **What it is:** In August 2025 an audit revealed the Claremont School District had budgeted $5
  million it did not have. A year later the district has closed a school, realigned the rest,
  taken a private bank loan, been the subject of two state bills, and declined the state's rescue
  fund.
- **Salience evidence:**
  - "Claremont descended into chaos last August after the discovery of a $5 million financial hole
    in its current budget, a shortfall caused by an improper assumption about federal funding by
    district officials. After securing a private loan from the Claremont Savings Bank to allow it
    operate through April 2026, the district had asked lawmakers in the fall to consider providing
    state financial assistance" ([New Hampshire Bulletin, "As state mulls school district bailout
    fund, Claremont says no thank you,"
    2026-02-04](https://newhampshirebulletin.com/2026/02/04/as-state-mulls-school-district-bailout-fund-claremont-says-no-thank-you/);
    same reporting at [Valley News,
    2026-02-04](https://vnews.com/2026/02/04/claremont-rejects-state-aid/), both retrieved
    2026-08-04). The loan was **$4 million** ([New Hampshire Bulletin,
    2025-11-19](https://newhampshirebulletin.com/2025/11/19/senators-move-forward-claremont-loan-fund-plan-with-strings-attached/),
    retrieved 2026-08-04).
  - **The budget the board adopted was $865,000 short and it papered the gap with a $1
    line item.** "The budget proposal approved Jan. 21 is still $865,000 short. For now, the board
    has taken that $865,000 out of its sports funding and recommended funding athletics, for now,
    at $1" ([New Hampshire Bulletin,
    2026-02-04](https://newhampshirebulletin.com/2026/02/04/as-state-mulls-school-district-bailout-fund-claremont-says-no-thank-you/),
    retrieved 2026-08-04). Athletics funded at one dollar is the kind of fact that carries at a
    door without any interpretation.
  - **Real options with real tax numbers were on the table.** A grade-specific realignment of the
    two elementary schools came to "$44.8 million, or 3.9% above the current $43.1 million budget,
    and would add $1.35 per $1,000 of assessed valuation to the school tax rate"; keeping both at
    K–5 came to $46.2 million, "a 7% increase from this year, with a $2.46 tax increase from the
    current overall rate of $17.45"; a three-school model came to $43.4 million with "no tax
    impact" ([Valley News, "Claremont School Board rejects three-school proposal,"
    2026-01-08](https://vnews.com/2026/01/08/claremont-school-board-budgets/), retrieved
    2026-08-04). The board rejected the three-school option.
  - **The board then amended below all of those.** On a 4–3 vote it adopted an amended aligned
    model at roughly $42,957,713 ([The Vermont Journal & The Shopper, "Claremont School Board
    rejects proposed budget increase, approves aligned
    model"](https://vermontjournal.com/featured-articles/claremont-school-board-rejects-proposed-budget-increase-approves-aligned-model/),
    retrieved 2026-08-04). The same story records the business administrator saying "these budget
    models that we proposed tonight [do] not include funding any of the deficit."
  - **Bluff Elementary School closed in October 2025** ([Union Leader, "Lawmakers OK bills tied to
    Claremont school
    crisis"](https://www.unionleader.com/news/education/lawmakers-ok-bills-tied-to-claremont-school-crisis/article_65897126-14b3-4f1f-9820-335c4a05bc7f.html),
    retrieved 2026-08-04).
  - **It reached the legislature.** HB 292 created a revolving loan fund for districts in fiscal
    distress, amended in the Senate to cap access at three consecutive school years, bar
    districts that already hold a line of credit, and require a Legislative Budget Assistant
    audit; HB 121 would let the State Board of Education place a district on probation and
    ultimately name an independent administrator ([NH Bulletin,
    2025-11-19](https://newhampshirebulletin.com/2025/11/19/senators-move-forward-claremont-loan-fund-plan-with-strings-attached/);
    [Union
    Leader](https://www.unionleader.com/news/education/lawmakers-ok-bills-tied-to-claremont-school-crisis/article_65897126-14b3-4f1f-9820-335c4a05bc7f.html),
    both retrieved 2026-08-04). Democrats objected that HB 292 carried "a 'poison pill' amendment
    to automatically grant any affected parent a taxpayer-subsidized Education Freedom Account"
    (Union Leader, same). **Claremont said it would not use the fund even if enacted** (NH
    Bulletin, 2026-02-04).
  - **Right-to-know costs are being borne by the district.** In March 2026 the school board chair
    reported the district was receiving numerous right-to-know requests and that "just last month,
    the legal cost for these requests was over $12,400" ([The Vermont Journal & The Shopper,
    "Claremont City Council hears school update, Acuity
    opposition"](https://vermontjournal.com/featured-articles/claremont-city-council-hears-school-update-acuity-opposition/),
    retrieved 2026-08-04).
- **Who is affected, and how many:** Every household in Claremont, through both the school tax
  rate and the schools themselves. Half the children in nearby Newport's public schools qualify
  for free lunch, "more than twice the statewide rate" ([NHPR,
  2025-07-30](https://www.nhpr.org/nh-news/2025-07-30/he-bought-the-local-paper-to-help-his-hometown-now-hes-being-blamed-for-its-demise),
  retrieved 2026-08-04) — the regional context for why a school budget fight here is not abstract.
- **Stage:** Recurring. The FY2027 school year begins with athletics nominally funded at $1 and
  the deficit not yet retired.
- **Decision-maker:** Claremont School Board / SAU 6, with the NH legislature and Department of
  Education in a supervisory role under the new statutes. **Claremont school board seats are
  filled at the March city election, not in November** — candidate filing for the March 10, 2026
  ballot ran January 21–30, 2026 (Vermont Journal, same source). A November candidate cannot run
  on this, but will be asked about it constantly.
- **Who currently speaks on it:** **This is the exception in Sullivan County — it is actually
  covered.** Valley News (Claremont is in its published coverage area), New Hampshire Bulletin,
  NHPR, WMUR, the Union Leader and the Vermont Journal have all reported on it. Steve Taylor told
  the Keene Sentinel that "the county's top stories, like Claremont's fiscal problems, have been
  picked up by outlets like WMUR, N.H. Public Radio and The Valley News, but 'nobody's doing the
  day to day reports'" ([Keene
  Sentinel](https://www.keenesentinel.com/news/local/twin-state-valley-nh-vt-reflects-on-life-without-local-news/article_a516c6ec-1e12-417b-a511-f71958d9d06d.html),
  retrieved 2026-08-04). That is exactly the pattern: the crisis is covered, the follow-through is
  not.
- **Quality of what exists:** Good on the crisis, thin on the present tense. The most recent
  detailed coverage I found is from February 2026. What is unpublished: where the $865,000 landed,
  whether athletics got its money back, and what the FY2027 school tax rate actually turned out to
  be.
- **Primary records:** Claremont School District FY2027 budget; HB 292 and HB 121 (NH General
  Court); Claremont School Board minutes of 2026-01-07, 2026-01-20 (public hearing) and
  2026-01-21. School Board meetings are recorded and streamed by CCTV — School Board 7/21/26 is
  the most recent on demand ([CCTV video
  archive](https://reflect-claremont.cablecast.tv/cablecastapi/v1/shows), retrieved 2026-08-04).

### 4. Claremont locked in five-year water and sewer rate schedules — and the vote split twice

- **What it is:** Claremont adopted two ordinances setting water and sewer rates for FY2027
  through FY2031. They were argued over in a way almost nothing else on that agenda was, and the
  council split 5–4 on the water side.
- **Salience evidence:**
  - **Ordinance 645 (water) and Ordinance 646 (sewer)** had first readings on June 10, 2026 and
    second readings with public hearings on June 24, 2026 ([Claremont City Council agendas for
    2026-06-10 and 2026-06-24, via claremontnh.com council documents], retrieved 2026-08-04).
  - **The water vote failed once before it passed.** Staff presented a "level increase" model and
    a "minimum increase" model. A motion to advance the **level** option failed **2–7**; a motion
    to advance the **minimum** option then carried **5–4** ([Claremont City Council minutes,
    June 10, 2026, as bound into the June 24, 2026 council packet, pp. 13–15], retrieved
    2026-08-04, **text recovered by OCR from an image-only scan**).
  - **The sewer vote split too.** The **level** option for Ordinance 646 carried **6–3** at first
    reading. Staff explained on the record that "the level increase option would implement a 2%
    increase annually for all five years, while the minimum increase option would hold rates flat
    in the first year followed by 2% increases in years two through five" (same minutes, p. 15,
    retrieved 2026-08-04).
  - **The council also changed the ordinance language from discretionary to mandatory review.**
    Every successful motion carried the amendment "may review annually" to "shall review
    annually." One councillor argued on the record that this was "a substantial change"; the
    assistant mayor "disagrees and stated Ordinances have multiple readings to make changes if
    needed" (same minutes, p. 14, retrieved 2026-08-04). Small, and exactly the kind of thing that
    determines whether these rates get revisited.
  - **The adopted schedules, from the ordinance text in the packet.** Ordinance 645 revises the
    schedule adopted by Ordinance #586 on or about July 14, 2021. The FY2027→FY2031 water volume
    charge for the first tier (0–1,000 cu. ft. per quarter) runs **$2.91, $3.03, $3.09, $3.15,
    $3.21 per 100 cu. ft.**; the quarterly fixed charge for the smallest meter runs **$20.96,
    $21.79, $22.23, $22.67, $23.13**. Ordinance 646 revises the schedule adopted by Ordinance #588
    on the same 2021 date; the quarterly sewer fixed fee runs **$55.39, $56.49, $57.62, $58.78,
    $59.95**, and the volume charge under 200,000 cu. ft./month runs **$6.83, $6.97, $7.11, $7.25,
    $7.40 per 100 cu. ft.** ([Ordinance 645 and Ordinance 646 text, City Council packet,
    2026-06-24, pp. 27–29 and 37–39], retrieved 2026-08-04).
  - **Sourcing caveat, stated plainly:** the June 24 packet is a 206-page scanned PDF with no text
    layer. Every figure above was recovered by optical character recognition. The new-rate columns
    were legible and internally consistent — the sewer figures check out to exactly 2% per year,
    matching what staff described — but **the struck-through prior-rate columns were not reliably
    readable, so this file does not state the FY2026 baseline.** Verify against the signed
    ordinance before quoting a dollar figure publicly.
  - **The 5–4 reading is independently corroborated.** MeetingWatch, a third-party service that
    transcribes the meeting video, describes the same meeting as "split 5-4 on the water rate
    ordinance," with the council opting for the "minimum" increase model ([MeetingWatch, Claremont
    City Council, June 10,
    2026](https://meetingwatch.org/nh/claremont/city-council/2026-06-10/), retrieved 2026-08-04).
    Two independent derivations — OCR of the scanned minutes and transcription of the video —
    landing on the same tally is the strongest confirmation available here. **Both are machine
    output. Neither is the signed record.**
- **Who is affected, and how many:** Every metered water and sewer customer in Claremont, plus
  unmetered flat-rate customers. **[NEEDS SOURCE — number of Claremont water and sewer accounts]**
- **Stage:** Second reading and public hearing held June 24, 2026. **I could not confirm the final
  adoption vote** — see Dead ends.
- **Decision-maker:** Claremont City Council, which meets the 2nd and 4th Wednesday of each month
  at 6:30 p.m. in Council Chambers at City Hall ([City of Claremont, City
  Council](https://www.claremontnh.com/council-minutes), retrieved 2026-08-04).
- **Who currently speaks on it:** The Vermont Journal covered the June 24 meeting, but its account
  focuses on the budget, library funding and outside-agency appropriations rather than the rate
  ordinances ([The Vermont Journal & The Shopper, "Claremont City Council discusses
  budget"](https://vermontjournal.com/featured-articles/claremont-city-council-discusses-budget/),
  retrieved 2026-08-04). No journalist has written about the rate ordinances. **The only published
  account of the June 10 debate is machine-generated**: MeetingWatch's report summarizes the split,
  quotes the "pay me now, pay me later" exchange, and timestamps it into the video
  ([MeetingWatch](https://meetingwatch.org/nh/claremont/city-council/2026-06-10/), retrieved
  2026-08-04). The city publishes the ordinance text — inside a 206-page unsearchable scan.
- **Quality of what exists:** **Effectively nothing that a resident would find.** A five-year rate
  schedule that reaches every household in the city, adopted after a failed motion and a 5–4 vote,
  has no human-written public explanation at all. What exists is an AI summary on a site most
  Claremont residents have never heard of, whose own footer says the analysis "may contain errors"
  and whose member index misspells half the council. This is precisely the case the skill flags:
  "a rate increase adopted at a sparsely-attended meeting shows up on every household's bill and
  has usually never been explained to anyone." **It also raises the bar slightly: the explainer a
  campaign writes now has to be better than a machine's, and correctly spelled.**
- **Primary records:** Claremont Ordinance 645 "Water Rates"; Ordinance 646 "Sewer Rates";
  City Council minutes 2026-06-10 (bound into the 2026-06-24 packet); City Council agendas
  2026-06-10 and 2026-06-24; predecessor Ordinances #586 and #588 (2021). Video of the June 10
  meeting is on demand at CCTV ("City Council - 6/10/26",
  [reflect-claremont.cablecast.tv](https://reflect-claremont.cablecast.tv/), retrieved
  2026-08-04).

## Contested space summary

| Issue | Who covers it now | How well | Vacuum? |
|---|---|---|---|
| Claremont water and sewer rates, FY2027–FY2031 (Ord. 645/646) | **No journalist.** The Vermont Journal covered the June 24 meeting but not the rate ordinances. The only published account of the June 10 debate is [MeetingWatch's AI-generated report](https://meetingwatch.org/nh/claremont/city-council/2026-06-10/). | Near-nonexistent. The ordinance text is inside a 206-page unsearchable scan; the one summary that exists is machine-written, self-labeled as possibly erroneous, and misspells councillors' names. | **Yes — total.** Cheapest thing to own in either county in this exercise. Reaches every household. The bar is now "better than a machine," which is still a low bar and worth clearing. |
| The TRAILS cut and its reversal fight | **Nobody.** Only the county's own draft minutes, in SharePoint, and the CCTV video. | Nonexistent as public explanation; the underlying record is excellent. | **Yes — total**, and the record is rich enough to write from confidently. Also live: the commissioners take it up again August 17. |
| The FY2027 county budget and the 6.45% tax increase | **Nobody.** The county's own EFC presentation and tax-comparison document. | Nonexistent as public explanation. The county even produced the cross-county comparison and then buried it. | **Yes — total.** And the delegation members who voted on it are the ones on the November ballot. |
| Claremont School District deficit | Valley News (Patrick O'Grady, part-time contributor), NH Bulletin, NHPR, WMUR, Union Leader, Vermont Journal | **Genuinely well covered at the crisis points**, and the reporting is accurate and detailed. | **No, on the 2025–2026 crisis.** **Yes, on the present tense** — where the $865,000 landed, whether athletics got funded, what the FY2027 rate is. Cheap follow-up, expensive to re-litigate. |
| Sullivan County commissioner / sheriff / county attorney races | Not found | — | Unknown. Not scanned; see Dead ends. |

The honest summary for this county: **three of four issues have no published answer at all, and
the fourth has good coverage of last year and nothing about this year.** In Whatcom the question
was which gaps are worth the effort. Here it is which gaps a campaign has the capacity to fill,
because they are all open.

## Ballot measures on the same ballot

**I found no local ballot measures for November 3, 2026 in Sullivan County, and this appears to
be structural rather than a gap in the search.** New Hampshire towns, cities and school districts
decide budget and bond questions at March town meeting or on an SB2 ballot, not on the November
state ballot — Claremont's school board seats and budget articles were on the **March 10, 2026**
ballot, with candidate filing January 21–30, 2026 ([The Vermont Journal & The Shopper, on the
January 21 school board
meeting](https://vermontjournal.com/featured-articles/claremont-school-board-rejects-proposed-budget-increase-approves-aligned-model/),
retrieved 2026-08-04).

| Measure | What it does | Position needed? | Source |
|---|---|---|---|
| *(none found for Nov 3, 2026)* | New Hampshire local money questions are decided in March, not November | n/a | See note above |
| **Statewide constitutional amendment questions (CACRs)** | The NH General Court may place constitutional amendments on the November ballot | **UNVERIFIED — check** | Not checked in this scan. NH Secretary of State, https://www.sos.nh.gov/2026-election-details |

**What is on the November 3 ballot in Sullivan County instead** is the set of offices: county
commissioners, sheriff, county attorney, treasurer, register of deeds, register of probate, state
senate, and the state representative seats that collectively *are* the county delegation ([NH
Secretary of State, Running for Office](https://www.sos.nh.gov/elections/running-office),
retrieved 2026-08-04). For county office the filing fee was $10 or 50 primary petitions; for state
representative, $2 or 5 petitions (same source). A campaign here should treat "who voted 7–5 to
cut TRAILS" as the ballot question, because functionally it is one.

**One live deadline as of the date of this scan.** The major-party filing period closed June 12,
but candidates running from a political organization or by nomination papers are still on the
clock: **August 5, 2026 at 5:00 p.m. is the last day to submit signed nomination papers to the
Supervisors of the Checklist** in each town or city, with certification due August 26 and
certified papers due to the Secretary of State by September 2 ([NH Secretary of State, Running
for Office](https://www.sos.nh.gov/elections/running-office), retrieved 2026-08-04). County
office requires 150 nomination papers from the county; state representative, 150 from the
district. That is tomorrow.

## Dead ends and gaps

**The vendor-detection procedure produced a false positive, then a dead end, then the real
answer.** Sullivan County's site footer says "Government Websites by CivicPlus®", which by the
documented procedure means `civic-scraper` against `/AgendaCenter`. **`/AgendaCenter` returns
HTTP 404** (checked 2026-08-04). `/ArchiveCenter` and `/DocumentCenter` return 200 but are not
where the minutes live. The records are in **nine Microsoft SharePoint folders**, linked out from
`/129/Agendas-Minutes` — a case the procedure does not describe at all. Detecting the CMS vendor
turned out to say nothing about where the records are.

**SharePoint defeats scripted retrieval.** `curl` and standard fetch tools against those
SharePoint folder URLs return a login redirect or a JavaScript stub. The documents are genuinely
public and open fine in a browser. Every Sullivan County document cited in this file was
retrieved through a browser session, not a script. Any automated scan will report this county as
having no accessible records, which is false.

**Ratified minutes are image-only scans; draft minutes have a text layer.** For both the
Delegation convention and the Board of Commissioners, the *ratified* PDF is a scan of a signed
paper copy with no searchable text, while the *draft* posted earlier is a native PDF. Every quote
and roll call in this file therefore comes from the **draft**. This is worth stating twice: the
authoritative version of the record is less usable than the provisional one. Before publishing
any of these vote counts, check them against the ratified scan by eye.

**`pdftotext` was unavailable** (broken Homebrew dependency: `Library not loaded:
libgpgmepp.6.dylib`), and Ghostscript was not installed, so ImageMagick could not rasterize PDFs
either. The workaround that finally worked was: `pypdf` to pull the embedded page images out of
the scanned PDF, macOS `sips` to convert them from JPEG 2000 to PNG, then `tesseract` for OCR.
That chain is not in any skill documentation and took several attempts to assemble. **In a news
desert this is not an incidental tooling problem — it is the difference between having the record
and not having it.**

**OCR figures carry OCR risk.** In the Claremont rate tables the new-rate columns were clean and
internally consistent, but strikethrough formatting on the superseded columns produced garbage,
and OCR rendered "Irish" as "Trish" in the roll calls. Councillor surnames in issue 4 are
therefore reported as tallies rather than as name-by-name attributions. Do not quote an
OCR-derived name.

**Claremont posts agendas and packets but not recent minutes.** As of 2026-08-04 I could not find
posted minutes for the June 24, 2026 or July 22, 2026 council meetings. The June 10 minutes exist
publicly only because they were bound into the June 24 packet for approval. The city's document
picker is a JavaScript "Select Year / Select Month" control on a bespoke CMS, so there is no
listing page to check this against — which is itself part of the problem.

**I could not confirm the final adoption vote on Ordinances 645 and 646, and three independent
records stop at exactly the same place.** The second reading and public hearing were scheduled for
June 24, 2026 and the agenda confirms they were on it. But the city has not posted June 24
minutes; CCTV's video-on-demand archive stops at the **June 10** council meeting; and MeetingWatch,
which builds its reports from the video, lists **June 9, June 10, June 30 and July 8 — and no
June 24 or July 22 at all** ([MeetingWatch, Claremont City
Council](https://meetingwatch.org/nh/claremont/city-council/), retrieved 2026-08-04). Three
separate systems missing the same two meetings points at one cause: **the video for those meetings
appears never to have been posted**, and everything downstream of the video is therefore missing
too. The only account of the June 24 and July 22 meetings that exists anywhere is the one written
by a reporter who was in the room, for a weekly newspaper published in Vermont. Next step: request
the June 24 and July 22 minutes from the Claremont city clerk under RSA 91-A.

**MeetingWatch was found by accident, and the detection procedure would never have found it.** It
turned up in a search-engine result while I was re-checking whether `claremontnh.com` was
reachable, after both the issue scan and the media map were otherwise complete. Nothing in
`local-agenda-systems.md` or `district-media-map`'s source list points at third-party civic-tech
meeting aggregators — they are not press-association members, not on findyournews.org, not on
LION's member list, and not linked from the city's own site. In a county with no newspaper it was
the single largest secondary index of the public record available, covering **five Sullivan County
towns**. **The procedure should add a step: search `"<town name>" council meeting transcript` and
`"<town name>" site:meetingwatch.org` or equivalent, and check whether someone else is already
indexing these meetings.** See the media map for what it is and the substantial reasons not to
cite it.

**The Criminal Justice Coordinating Committee minutes folder was not read.** It is public, it is
linked from the county's own page, and the commissioners' minutes identify it as where the
TRAILS-versus-Drug-Court question originated. This is the highest-value unexamined source in the
county and it is one browser session away.

**Newport, Charlestown, Cornish, Unity and the eleven other towns were not scanned at all.** This
file covers the county government and Claremont. Patrick O'Grady, the last reporter covering
Sullivan County, told the Keene Sentinel that for the smaller towns "there's almost no news out of
those towns" ([Keene
Sentinel](https://www.keenesentinel.com/news/local/twin-state-valley-nh-vt-reflects-on-life-without-local-news/article_a516c6ec-1e12-417b-a511-f71958d9d06d.html),
retrieved 2026-08-04). Assume the same is true of their records until checked.

**An unexamined lead: the Acuity Management construction-and-demolition waste proposal in
Claremont.** Residents raised objections at the March 25, 2026 council meeting, including
statements about tonnage of C&D waste being brought into the city ([The Vermont Journal & The
Shopper](https://vermontjournal.com/featured-articles/claremont-city-council-hears-school-update-acuity-opposition/),
retrieved 2026-08-04). I could not reach a primary record for it in this scan and have therefore
not ranked it as an issue, but organized opposition to a waste facility is normally high-salience
and this deserves a proper look at the Planning Board and NH Department of Environmental Services
records.

**I did not check the NH General Court site for CACRs** (constitutional amendment questions) that
would appear on the statewide November ballot, and I did not enumerate the Sullivan County
candidates who filed by the June 12 deadline. Both are quick and both were out of scope for a
place-focused scan.

**No news-archive search was possible for 2025–2026 Sullivan County local government**, because
the archive does not exist. The *Eagle Times* domain is a parked page at a hosting provider
(`eagletimes.com`, checked 2026-08-04) and 192 years of its coverage is not online. The Fiske Free
Library in Claremont holds newspaper archives on microfilm going back to 1834 (Keene Sentinel,
same source) — for anything historical, that library is the search engine.
