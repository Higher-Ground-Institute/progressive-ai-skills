# Whatcom County, WA — what worked and what broke

> **Real place, real records, no candidate.** Nothing here is attributed to anyone running for
> office. Scanned 2026-08-04.

This is the failure log for the Whatcom scan. The clean output is in
[`district-issues.md`](district-issues.md) and
[`district-media-map.md`](district-media-map.md); this file is what a run actually costs.

---

## What worked

**Legistar hostname detection worked exactly as documented.** The official agenda page links to
`whatcom.legistar.com`, the hostname gives the vendor, the subdomain gives the client slug
`whatcom`, and `https://webapi.legistar.com/v1/whatcom/...` answers without authentication.
"Find the official agenda page first, then read the hostname" is the right first step and it
held here without modification.

**`/Events` was the single highest-yield call in the exercise.** It returns the full meeting
list with agenda and minutes PDF URLs attached directly to each record. Once that call
succeeded the rest of the county-council scan was mechanical. If you make one API call, make
this one.

---

## What broke

### 1. `/Matters/{id}/Histories` does not return vote tallies

`MatterHistoryTally` was null on every record checked. Every roll call in
`district-issues.md` came out of a minutes PDF instead.

This is not a Whatcom quirk. The Madison run hit identical behavior on an unrelated instance in
another state — see [`../madison-dane-county-wi/NOTES.md`](../madison-dane-county-wi/NOTES.md).
Two instances, two states, same null. **Treat "read the tally from the minutes" as the primary
method and the API as the thing that will not have it.**

The danger is the direction of the error. An empty tally read as consensus turns a contested
vote into "unanimous," and a split vote is exactly the thing worth finding.

### 2. `/Matters` silently caps at 1,000 records

A twelve-month window on a mid-size county hits the cap. You get a truncated result set, no
error, and no indication anything is missing. Page the results or narrow the date window, and
never conclude that a body was quiet because the list looked short.

### 3. One special district's portal could not be found at all

Whatcom Fire Protection District No. 1 has no locatable agenda portal. Its levy measure turned
up only by working backwards from the **county auditor's ballot-resolution page**, which lists
the measures each district has certified for the ballot.

That is a detection method the procedure does not currently teach, and it generalizes: when a
special district has no findable portal, the county auditor or elections office knows what it
put on the ballot even when the district publishes nothing.

### 4. A 403 is not a dead outlet

Of 93 unique URLs checked across this run and the Sullivan run, 78 returned 200, **9 returned
403 to a scripted request while loading perfectly in a browser**, and 4 timed out. The Northern
Light was among the 403s.

A scan that treats 403 as "outlet is gone" will classify a county with healthy local news as a
desert. Every 403 in these files is labeled in place as reachable-by-browser rather than
dropped.

### 5. Nobody asked which bodies are actually on the ballot

**No Whatcom County Council seat is on the November 2026 ballot.** The scan surfaced good,
well-sourced council fights, but for a candidate planning this cycle their usefulness is
different from what it looks like — they are context, not the race.

There is no step in `district-issue-scan` that asks which of the scanned bodies a candidate can
actually run for in the cycle being planned. There should be, and it belongs near the top.

---

## Caveats on the output

- The November 3 ballot list may not be final. The resolution deadline was the same day as the
  scan.
- Community-platform rows are marked `UNVERIFIED` rather than filled in. Member counts and
  moderator names were not published anywhere checkable, and inventing them was not an option.
- Submission rules and election cutoffs are `UNVERIFIED` for the outlets whose sites returned
  403 or timed out.
