---
name: district-issue-scan
description: Builds a ranked, evidence-backed inventory of issues in one jurisdiction from official meeting records, local reporting, public participation, and the certified ballot. Distinguishes governing bodies on the current ballot from bodies scanned for context, ranks by documented local salience rather than national polling, and surveys who already publishes a useful answer. Use for local issue research, governing-body records, ballot measures, and contested-space analysis.
---

# District Issue Scan

**Reads:** campaign frontmatter for `election_date`, a jurisdiction name, a street address in
the district, and public sources.
**Writes:** `campaign/district-issues.md`, using
[`campaign-template/district-issues.md`](../../campaign-template/district-issues.md).

An issue belongs in the output only when a local record supports its salience. A generic topic
with a place name attached does not qualify.

## Required source procedure

Follow [`reference/local-agenda-systems.md`](../../reference/local-agenda-systems.md) for every
governing body. That procedure is mandatory and is the source of truth for vendor detection,
APIs, scraping, record limits, vote-tally handling, browser retrieval, OCR, clerk requests, and
manual extraction. Do not recreate or shortcut it from memory.

Apply these skill-specific controls:

- An empty or null API field is **not evidence of absence**. Never infer unanimity from a
  missing tally or no activity from an empty result.
- If scripted retrieval returns a login page, JavaScript stub, 403, or empty document, try the
  public link in a browser before calling it unavailable.
- If extraction yields little or no text, test whether the PDF is image-only, rasterize and
  OCR it, and re-check every quoted number against the original image.
- Use minutes for attendance, public comment, and vote tallies. If the tally cannot be
  retrieved, say so and identify the meeting record that still needs review.
- Log vendor, retrieval method, date range, and every zero-yield source.

## Election and governing-body scope

Read `election_date` from campaign frontmatter; do not assume a November general election.
Verify the election name and date against the county clerk/elections office or Secretary of
State before selecting the ballot or calculating a window. In `## Sources checked`, record the
official election source, retrieval date, confirmed ISO date, and election name used.

Resolve the district boundary and classify each body before issue research:

- **On ballot:** this body's seat, levy, bond, referendum, or other question appears on the
  confirmed ballot for this election.
- **Context only:** the body affects district residents but has no seat or question on that
  ballot.

Scan relevant context bodies, including county, municipal, school, water/sewer, planning,
library, transit, hospital, and other taxing or rate-setting districts. But never present a
context body's issue as part of the office being elected. Put bodies in
`governing_bodies_on_ballot` or `governing_bodies_context` and mark the classification in
source-table rows. When a special district has
no findable records portal, work backward from certified ballot resolutions and clerk records.

For boundary lookup, use official county or municipal records for local offices. Open Civic
Data IDs and Open States may help with legislative districts but do not establish local ballot
coverage.

## Output Format

Follow the template field for field: frontmatter (`jurisdiction`, `ocd_id`, `election_name`,
`election_date`, `scan_date`, `scan_window`, `governing_bodies_on_ballot`,
`governing_bodies_context`, `agenda_vendor`, `date_created`, `date_modified`), then:

1. `## Sources checked`
2. `## Ranked issues`
3. `## Contested space summary`
4. `## Ballot measures on the same ballot`
5. `## Dead ends and gaps`

Each ranked issue must include what it is, salience evidence, who is affected and how many,
stage, decision-maker, the decision-maker's `on-ballot` or `context-only` status, who currently
speaks on it, quality of existing explanations, and primary records. Produce three to eight
issues only when the evidence supports that many; a shorter result is valid and must not be
padded.

## Steps

1. Read and officially verify `election_date`; record the election name, date, source, and
   retrieval date.
2. Resolve the district boundary and OCD-ID where available. Inventory relevant governing
   bodies and classify each as `on-ballot` or `context-only` from the certified ballot.
3. Set a scan window of at least twelve months unless the campaign specifies a longer one.
4. Apply the mandatory local-agenda-systems procedure once per body. Record the vendor or
   `none-found`, retrieval method, browser/OCR fallback, window, and yield.
5. Read agendas, minutes, packets, and verified tallies. Search outlet archives and legal
   notices. When news is absent, use primary records, public-comment records, correspondence
   packets, rate filings, and ballot resolutions, and report the coverage gap.
6. Catalog every local measure on the confirmed ballot from an official certified ballot or
   official measure list.
7. Rank only by documented local salience: public-comment counts, contested votes with
   tallies, rates or taxes with amounts and effective dates, petition signatures, recurrence,
   and repeated local coverage. National polling and assumed importance do not rank.
8. For every issue, survey incumbents, government explainers, local outlets, and relevant
   organizations. Record who offers an answer and whether it is complete, current, sourced,
   and readable.
9. Fill every source row, including zero-yield checks and retrieval failures. Describe every
   unresolved record in `## Dead ends and gaps`.
10. Have a campaign human compare the ranking with what they hear at doors. Change a rank only
    when new evidence supports the change, and record why.

## Rules that do not bend

> Source every factual claim inline with source and retrieval date.
>
> Copy quotes, endorsements, statistics, measure numbers, vote counts, dollar figures, and
> dates from a source or omit them. If a value remains unavailable, write
> `[NEEDS SOURCE — what to look up]`; never approximate or reconstruct it.
>
> Prefer primary records. When citing reporting, name the outlet and reporter.

- Null, empty, blocked, or extraction-free results are not proof that no record exists. Apply
  the browser and OCR fallbacks before reaching that conclusion.
- Log every dead end and zero yield; never leave the Yield field blank.
- Keep on-ballot bodies distinct from context-only bodies in research, ranking, and prose.
- A short evidence-backed scan is complete. Never add generic issues to reach a target count.

## Doing this without an agent

For the full no-agent workflow, see [`README.md`](README.md#manual-procedure). The mandatory
agenda-system procedure, sourcing rules, election verification, body classification, output
contract, and fallbacks above still apply.

## Tips

When official records disagree, preserve the conflict in `## Dead ends and gaps`, identify
which authority controls the fact, and do not resolve it from secondary coverage.
