# Sullivan County, NH — what worked and what broke

> **Real place, real records, no candidate.** Nothing here is attributed to anyone running for
> office. Scanned 2026-08-04.

This is the failure log for the Sullivan scan, and it is the more useful of the two. Whatcom
tested the procedure where it was designed to work. Sullivan tested it where a county has a
complete public record that every documented detection method fails to find.

The clean output is in [`district-issues.md`](district-issues.md) and
[`district-media-map.md`](district-media-map.md).

---

## Why this county

The *Eagle Times* closed in July 2025 after 192 years publishing from Claremont. Northwestern's
2025 State of Local News Report codes Sullivan as a **zero-source county** — the only one in
New Hampshire with no locally based paper.

It also had real records worth finding. Five weeks before the scan, the county delegation cut
**$500,000** from the jail's substance-use treatment program on a **7–5 vote**, and raised
county property taxes **6.45%**. No outlet covered either.

---

## What broke

### 1. Detecting the CMS tells you nothing about where the records are

The county site footer says *"Government Websites by CivicPlus®."* By the documented procedure
that means running `civic-scraper` against `/AgendaCenter`. **That path returns 404.**

The actual records live in **nine Microsoft SharePoint folders** linked out from
`/129/Agendas-Minutes`.

The procedure conflates two questions that were unrelated here: *who built the website* and
*where are the agendas*. Detect them separately. A CivicPlus footer is not a CivicPlus agenda
center.

### 2. Public document libraries are a missing vendor category

SharePoint, Google Drive, and Dropbox folders are common in small counties and they defeat
scripted retrieval completely. `curl` gets a login redirect or a JavaScript stub **even though
every document is fully public and opens fine in a browser.**

Every Sullivan document cited in the output was pulled by driving a browser session against
SharePoint's own REST endpoints.

This is the highest-stakes failure in either run: **a scan that stops at "no vendor found"
concludes that a county with a complete public record has none.** That is the difference
between a candidate who can cite the delegation's actual vote and one who believes the record
does not exist.

### 3. Image-only PDFs are indistinguishable from empty results

The ratified delegation minutes and Claremont's 206-page June 24 council packet are **scans
with no text layer**. Text extraction returns zero characters, search returns nothing, and
nothing anywhere raises an error.

The water and sewer rate tables exist in the output only because the pages were rasterized and
run through OCR.

**Heuristic worth adopting: if a PDF extracts to under roughly 100 characters per page, it is a
scan, not an empty document.** Related and non-obvious — the *draft* minutes of the July 2
delegation meeting had a text layer and the *ratified* version did not. Check both.

### 4. The news-desert scale assumes one governing body per jurisdiction

This run classified Sullivan as `thin` rather than `desert`, departing from the Medill
classification. Two things a county-of-publication count cannot see:

- A free weekly published across the state line in **Ludlow, Vermont** launched a Claremont
  edition and covers the city council meeting by meeting.
- A **PEG access nonprofit** holds 6,676 archived videos, including the county commissioners.

Against the skill's own behavioral thresholds that is `thin`. But the label is less useful than
the split it hides: **Claremont city government is thinly covered and Sullivan County
government is covered by nobody at all.** The three-way scale assumes one governing body per
jurisdiction, and the coverage gap here is per-body. A candidate for county office and a
candidate for city council in the same county face completely different media realities.

---

## Caveats on the output — read before quoting anything

- **Several dollar figures came out of OCR and should be re-read against the originals before
  anyone publishes them.**
- The TRAILS roll call is sourced to **draft** minutes, because the ratified version is
  unsearchable. Drafts get corrected.
- The Valley News publishes **conflicting letter word limits** — 350 on one page, 250 on
  another. Write to 250.
- CCTV's rules for candidate-produced programming are `UNVERIFIED`. A PEG channel will have
  written ones; they were not findable online.
