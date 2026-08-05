# District Issue Scan

**Category:** Research & Data

Builds `campaign/district-issues.md`: a ranked, sourced inventory of local issues, the
governing bodies responsible, ballot measures on the campaign's confirmed election ballot,
and who already explains each issue.

## Who it's for

Down-ballot candidates and volunteers who need local issue research before
`positioning-builder`.

## Prerequisites

- Campaign frontmatter containing `election_date`
- The jurisdiction and one address in the district
- Web access
- Optional Open States access for state-legislative boundary checks

## How to use it

Request a scan for a named jurisdiction and race. The skill verifies the election, resolves
the boundary, separates bodies on the ballot from context bodies, applies the shared agenda
record procedure, ranks issues by local evidence, and drafts the output for human review.

## Manual procedure

Plan for roughly two working days with a browser, notebook, and spreadsheet or the Markdown
template.

1. Read `election_date` from campaign frontmatter. Confirm the election name and date using the
   county clerk/elections office or Secretary of State. Record the official URL, retrieval
   date, election name, and ISO date used. Do not substitute a November general election.
2. Resolve the district boundary from official maps or election records. Record the OCD-ID if
   available.
3. Obtain the official certified ballot or official candidate-and-measure list for the
   confirmed election. Inventory county, municipal, school, water/sewer, planning, library,
   transit, hospital, and other relevant bodies. Label each `on-ballot` or `context-only`.
4. Set a scan window of at least twelve months. Give each body a separate worksheet or notebook
   page.
5. For each body, follow
   [`reference/local-agenda-systems.md`](../../reference/local-agenda-systems.md) exactly.
   Record the official records URL, detected vendor or `none-found`, retrieval method, window,
   date checked, and yield.
6. Treat empty API responses and null tally fields as unknown, not absence. Open blocked or
   JavaScript document libraries in a browser. For image-only PDFs, OCR the pages and verify
   every number against the original image.
7. Read minutes and packets. Mark contested votes, public-comment counts, rate or tax changes
   with amounts and dates, petitions, repeat appearances, and unresolved decisions. Do not
   infer a tally from an agenda or API field.
8. Search local outlet archives, legal notices, government explainer pages, incumbents, and
   relevant organizations for each marked item. Record paywalls and searches that yield
   nothing.
9. Catalog local measures only from the certified ballot or official measure list for the
   verified election.
10. Rank issues by the marked evidence. Keep the responsible body's ballot classification
    visible. Cut generic issues and accept fewer than three when the record supports fewer.
11. For each retained issue, record who currently explains it and score the explanation for
    completeness, recency, sourcing, and readability.
12. Fill the template, including every dead end and zero-yield source. Show it to someone who
    works doors; make changes only when additional evidence supports them.

## What it has been exercised against

- Three cases in [`evals/evals.json`](evals/evals.json): source detection before naming issues,
  refusal to provide unsourced "top issues," and contested-space analysis.
- Structural validation through `scripts/validate_skills.py`.

The eval suite has not been run against a live model, and the manual procedure has not been
validated on a real campaign district.
