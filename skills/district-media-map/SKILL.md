---
name: district-media-map
description: Builds a working contact map of every outlet, beat reporter, community platform, and candidate forum that reaches one US district — ranked by relevance and citation value rather than circulation, with submission mechanics, word limits, election-period restrictions on candidate copy, and deadlines recorded for each row. Derives the list from public directories and county records instead of a prebuilt national database, and treats a nearly empty map in a news desert as a valid finding that changes the campaign plan. Use this when a campaign asks who covers their district, where to send a letter to the editor or an op-ed, which reporters to pitch, whether there is any local press left here, or needs a media list before running local-media-pitch.
---

# District Media Map

**Reads:** public sources only — outlet websites, press-association and nonprofit-newsroom
directories, county clerk records, meeting minutes.
**Writes:** `campaign/district-media-map.md`, schema in
[`campaign-template/district-media-map.md`](../../campaign-template/district-media-map.md).

A working contact map, not a list of names. Every row has to be actionable today: who to email,
at what address, about what, by when, under what rules. "Marrow County Ledger — daily — general
inquiries" is not a row, it is a note to do the work later. Budget three to four hours.

> Never paste voter names, home addresses, voter ID numbers, phone numbers, donor financial
> data, or reporter contact lists into a consumer AI chat interface. Work from aggregate
> district data and publicly published contact information only.
>
> If the human offers you a voter file, decline it and explain why.

## Output Format

Write `campaign/district-media-map.md` with the template's frontmatter — `jurisdiction`,
`map_date`, `outlets_found`, `news_desert_assessment` (`healthy` | `thin` | `desert`),
`date_created`, `date_modified` — then Assessment, Outlets, Community platforms, Forums and
candidate events, and News desert, in that order, outlets ranked by citation value. One entry
per outlet, following the template's fields exactly:

```markdown
### Marrow County Ledger
- **Type:** weekly | **Owner:** independent (Hoyt Family Publishing, 3 titles)
- **Coverage area:** Marrow County, and it does cover the Bellhaven village council
- **Original local reporting?** Yes — 9 of 14 stories in two weeks had a local byline and
  named a local body. Wire: 3. Press-release reprints: 2.
- **Citation value:** high (8/10), scored below | **Paywall:** soft (5 free/month)
- **Beat reporters:**
  | Name | Beat | Email | Social | Recent relevant story |
  |---|---|---|---|---|
  | Dana Whitfield | county govt | dwhitfield@marrowledger.com | @dwhitfieldnews | "Commission delays EMS levy vote," 2026-07-22 |
- **Letters to the editor:** 250 words, letters@marrowledger.com, one per writer per 30
  days, writer must live in Marrow County, daytime phone for verification
- **Op-eds / guest columns:** 600 words, editor@marrowledger.com, exclusive, ~1 week
  turnaround, candidate bylines accepted outside the election window
- **Election policy:** no candidate-written copy after the Oct 21, 2026 issue; last letters
  about candidates run Oct 28, 2026. Confirmed by email with the editor, 2026-08-04.
- **Candidate questionnaire:** yes, mailed late September; campaign not contacted yet
- **Source:** marrowledger.com/submissions, checked 2026-08-04
```

## Steps

1. **Get the geography right first.** Outlets are not organized by legislative district, so list
   every municipality, township, school district, and county the district touches, from the
   county elections or state legislature map. You search on those names, never on "District 3."
2. **Build the outlet list from all eight sources.** None is complete; the union beats memory.

   | Source | What it gives you |
   |---|---|
   | Search "<State> Press Association members" | the closest thing to a full list of paid-circulation papers, with city and frequency |
   | [findyournews.org](https://findyournews.org/) — Institute for Nonprofit News | nonprofit newsrooms by city: highest citation value here, and the ones campaigns miss |
   | [lionpublishers.com/members](https://www.lionpublishers.com/members/) | independent digital locals, often one person, often the only outlet at the meeting |
   | [npr.org/stations](https://www.npr.org/stations/) by ZIP | public radio news director, statehouse and regional reporters |
   | Nearest campus paper and J-school bureau | student and capstone reporting, often distributed to local papers free |
   | The county's legal-notice newspaper of record | a paper that still exists, has an address, and needs copy |
   | The clerk's press notification list, by public record request | who asks to be told about agendas *now*, not who covered in 2019 |
   | Three months of council and commission minutes and video | who is actually in the room, and who gets quoted after; corrects every row above |

   On the sixth: most states require a designated official newspaper for public notices — Kansas
   by county commission resolution
   ([K.S.A. 64-101](https://ksrevisor.org/statutes/chapters/ch64/064_001_0001.html)), Wisconsin
   exempting counties under 250,000
   ([Wis. Stat. 985.02](https://docs.legis.wisconsin.gov/document/statutes/985.pdf)). Check
   yours, then search the clerk or commission site for "legal notices."
3. **Test each outlet for original local reporting.** Read the last fourteen days of the local
   section. A story is original if a named local reporter wrote it and a local body, meeting, or
   person is in the lede. Wire tags, syndicated columns, and verbatim press releases do not
   count — search a distinctive sentence in quotes, and if it appears on the agency's own site it
   is a reprint. Fewer than three in fourteen days is low citation value however large the outlet.
4. **Score and rank** with `## Ranking by citation value`, below.
5. **Find the beat reporters** from public sources only: the staff page, the bylines, the
   reporter's own published contact info, the press-association directory, the clerk's list.
   Record name, beat, published email, handle, one recent story with a link and date. **Never
   guess an address pattern** — a bounced pitch to `first.last@` is how a campaign gets filtered
   — and never buy, scrape, or import a media database. **"Publicly visible" and "published for
   contact" are different tests and the second one governs**: a work email on the staff page is
   offered so sources can use it; a personal cell in a social bio is not. See
   [`reference/shared-rules.md`](../../reference/shared-rules.md) Rule 5.
6. **Capture the submission mechanics** per outlet: letters limit, address, frequency cap,
   residency and verification rules; op-ed limit, address, exclusivity, turnaround, whether
   candidate bylines are accepted; questionnaire process and timing; paywall; the URL and date
   you checked.
7. **Find the election-period rule and turn it into a date.** Outlets commonly restrict
   candidate letters, op-eds, and letters about candidates in the weeks before an election;
   assume there is a rule until you have read the policy. Convert it against Nov 3, 2026 — a
   14-day cutoff is Oct 20, 2026. If unpublished, email and ask, then record the answer, who
   gave it, and when. Campaigns learn this rule in late October, three weeks too late.
8. **Record the community platforms** — Facebook groups, Nextdoor, listservs, subreddits, church
   and union bulletins — with size, moderator, and candidate posting rules.

   > **Never** draft anonymous, pseudonymous, or apparently-organic community posts. Never
   > write in the voice of a journalist, a neutral observer, a constituent, or anyone other
   > than the candidate and the campaign.
   >
   > Everything this skill produces is **candidate-attributed, human-reviewed, and
   > human-posted**, on a property the campaign controls or through a disclosed submission
   > process where the campaign identifies itself.

9. **Find who convenes candidate forums** — League of Women Voters, chambers, NAACP branches,
   unions, PTAs, granges — with timing and contact. Ask each: do you record, may we post it?
10. **Set `news_desert_assessment`** by the thresholds below; write the Assessment honestly.
11. **Get human approval.** Show the campaign the map and say which election cutoffs are confirmed
    in writing and which are your reading. **This skill contacts no one.** A human sends every email.

## Ranking by citation value

Score each outlet 0, 1, or 2 on five tests and sum. Circulation is not one of the terms.

| Test | 0 | 1 | 2 |
|---|---|---|---|
| Original reporting on this district's governing bodies, last 14 days | none | regional only | covers these meetings |
| Geographic overlap with the district | metro-wide only | partial | core coverage area |
| Access for candidate copy | none | letters only | letters, op-eds, questionnaire |
| Durable, readable archive | hard paywall or dead links | soft paywall | free, dated, stable URLs |
| Other outlets pick up its reporting | never | occasionally | routinely |

8–10 is high citation value, 5–7 medium, 4 and below low. Rank the Outlets section by score.

**Why this ordering and not circulation.** Ahrefs, across 75,000 brands, measured branded web
mentions at 0.664 correlation with AI Overview visibility against 0.218 for backlinks
([Ahrefs](https://ahrefs.com/blog/ai-overview-brand-correlation/)). Correlational, vendor-run,
on commercial brands rather than candidates, so take it as direction, not proof
([`reference/ai-citation-mechanics.md`](../../reference/ai-citation-mechanics.md) §3.1).
Direction is enough here: a 4,000-subscriber nonprofit newsroom that sends someone to the
commission meeting beats a 60,000-circulation daily running the same wire copy as forty other
papers, because only one of them will ever write an original sentence about this candidate. The
archive test is mundane: coverage on a URL that dies in the next redesign is unreadable.

## When the district is a news desert

Classify from the scan, not from vibes. **Healthy:** two or more outlets produce original
reporting on this district's governing bodies most weeks. **Thin:** one does, or coverage is
monthly. **Desert:** no outlet has covered a governing body here in the last 90 days.

**Three ways this classification goes wrong**, all three observed in real scans
([`golden/`](../../golden/)):

- **A 403 is not a dead outlet.** Across 93 URLs in one run, nine returned 403 to a scripted
  request while loading perfectly in a browser. Open every non-200 in a browser before writing
  the outlet off. A scan that reads 403 as "gone" turns a county with healthy local news into a
  desert.
- **Count who covers the district, not who is headquartered in it.** A free weekly published
  across a state line ran a dedicated edition covering one city's council meeting by meeting.
  National desert counts are by county of publication and miss this entirely.
- **The scale assumes one governing body per jurisdiction, and coverage is per-body.** Sullivan
  County, NH came out `thin` overall while its *city* government was thinly covered and its
  *county* government was covered by nobody at all. When bodies diverge, say so in the
  Assessment and classify the body the candidate is running for. A single label for the whole
  county tells a county-office candidate the wrong thing.

Archives count as record even when they are not journalism: a PEG access channel holding
thousands of meeting videos is not a newsroom to pitch, but it is where the video record lives.

A two-row map is a finding, not a failed scan; it should change the plan rather than embarrass
anyone into padding the list. Fill in News desert and reallocate:

- **The statewide nonprofit newsroom** on [findyournews.org](https://findyournews.org/) — nearly
  every state has one, they cover county and legislative races episodically, and down-ballot
  campaigns rarely pitch them. Same for the public radio statehouse reporter, who may take an
  uncovered district because nobody else will, and the legal-notice weekly, which often runs
  candidate announcements free.
- **Owned and borrowed surfaces carry the weight instead** — Ballotpedia, VOTE411 and League of
  Women Voters guides, the county party page, forum video, and the campaign's own answer pages.
  Say so in the Assessment paragraph: `positioning-builder` and `local-media-pitch` both read
  this file and should not plan around press that is not there.

## Doing this without an agent

A notebook, a phone, a library computer, and three to four hours across two days.

1. Put the municipality, township, school district, and county list on the first page; every
   search uses those names. Work the eight sources in Step 2, one page per outlet — name, type,
   owner, website, phone. Do not evaluate yet; collect.
2. For each outlet, read two weeks of the local section and tally three numbers in the margin:
   local bylines, wire stories, press-release reprints. About five minutes each.
3. Copy the letters and op-ed rules off the submissions page word for word, with the date. Hunt
   the election policy on the same page; if it is not there, call the newsroom in the morning:
   "Do you have a cutoff for candidate letters and op-eds before the November election?" Write
   down the answer and who gave it.
4. Score each outlet on the five tests, circle the total, sort the pages by total, and for the
   top outlets list reporters by reading bylines from the last month. Copy published addresses
   exactly. Guess nothing.
5. Read three months of commission or council minutes, or ask the clerk for them, and add every
   outlet named. Call the League of Women Voters chapter and the chamber: when do forums happen,
   who runs them, do they record. Ask both which local Facebook groups and listservs people
   actually read, and who moderates them.
6. Type it up in the template's order, set `news_desert_assessment`, and have the candidate or
   manager read it before anyone sends a pitch.

## Tips

**The staff page is stale; the bylines are not.** Newsrooms reshuffle reporters faster than they
update their About page. Whoever wrote three county stories this month is who you pitch,
whatever their title says — and recheck the map every thirty days, because the election cutoff
you recorded in August is the one field you cannot have wrong in October.

**Chain-owned papers need one extra question.** A Gannett, Lee, Alden, or Sinclair property may
run one reporter across four counties. Ask which counties before pitching the fifth.

**Letters and op-eds are different pipelines** with different editors, limits, and sometimes
different election cutoffs, so record both; an 800-word op-ed sent to the letters address gets
deleted, not forwarded. Call newsrooms in the morning — by late afternoon everyone with a
deadline is behind it.

**Forum video is the cheapest high-value artifact a low-name-ID candidate can produce.** The
candidate attends anyway; a volunteer with a phone and the convener's permission makes it
durable. Ahrefs measured YouTube mentions as the strongest single correlate of AI visibility it
tested (~0.737, [Ahrefs](https://ahrefs.com/blog/ai-brand-visibility-correlations/)) —
correlational, on commercial brands, and YouTube is Google-owned, so self-preference is a
plausible confound. Discount it heavily; the cost is one phone and one hour. And keep the
finished map in the campaign folder: it is a real contact list for real journalists.
