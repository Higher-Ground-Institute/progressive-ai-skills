# District Media Map

**Category:** Research & Data

Builds `campaign/district-media-map.md`: current outlet contacts, reusable submission
mechanics, exact election-period deadlines, community-platform rules, candidate forums, and a
body-specific news-desert assessment.

## Who it's for

Down-ballot campaigns preparing for `local-media-pitch` or deciding where earned media is
realistically available.

## Prerequisites

- Campaign frontmatter containing `election_date`
- Official district geography
- Web access and a phone for human follow-up
- Three to four hours for an initial pass

No paid media database is needed. Use only contact details publicly published for work use.

## How to use it

Request a media map for a named district. The skill verifies the election, inventories and
sorts submission deadlines, profiles outlets, scores citation value, and drafts the map. Reuse
mechanics in `local-media-pitch` while their recorded freshness window remains valid; re-check
expired or unconfirmed fields.

## Manual procedure

Use a notebook or spreadsheet first, then transfer the result to the Markdown template.

1. Read `election_date` from campaign frontmatter. Confirm the election name and date against
   the county clerk/elections office or Secretary of State. Record the official URL, retrieval
   date, election name, and confirmed ISO date. Do not assume a November election.
2. List every municipality, township, school district, and county touched by the race. Search
   on those names rather than the district number alone.
3. Build a preliminary outlet and forum list from the press association, Institute for
   Nonprofit News, LION, NPR stations, campus outlets, legal-notice publisher, clerk press
   list, and three months of governing-body minutes or video.
4. Before profiling coverage, create one deadline row per letters, op-ed, questionnaire,
   endorsement, debate, and forum process. Copy the rule, source URL, and checked date. Convert
   relative election cutoffs to exact dates using the verified `election_date`.
5. Mark dates confirmed only when supported by a published policy or a direct response. For
   missing rules, prepare a short question for a campaign human to send or call. Record the
   respondent and response date. The skill itself contacts no one.
6. Sort the deadline inventory earliest first. Flag `[UNCONFIRMED — ask outlet]` items for
   immediate follow-up.
7. For each outlet, read fourteen days of local coverage. Count named local bylines, wire
   stories, and press-release reprints. Test non-200 pages in a browser before treating the
   outlet as unavailable.
8. Score the five citation-value tests in `SKILL.md`, show every component, total them, and
   rank by score. Do not use circulation as a scoring term.
9. Identify current beat reporters from recent bylines and staff pages. Copy only work contact
   details the outlet or reporter published for source contact. Never guess an email pattern
   or copy personal cells or addresses from social profiles.
10. Record letters and op-ed mechanics separately: word limits, submission paths, frequency,
    residency, verification, exclusivity, turnaround, candidate restrictions, deadlines,
    sources, and checked dates. Add `fresh through` when the policy supplies a period;
    otherwise set a recheck date no more than 30 days away.
11. Record questionnaire and endorsement owners and timing. Record community-platform
    candidate rules. Record forum conveners, contacts, deadlines, and whether recording and
    reuse are allowed.
12. Classify coverage for the governing body the candidate seeks: healthy, thin, or desert.
    Explain differences across bodies and accept a short map rather than padding it.
13. Transfer the data to `campaign/district-media-map.md`. Have the candidate or manager review
    every contact, deadline, and unconfirmed item before any pitch or submission.

Never paste the finished contact map, voter data, personal addresses, personal phone numbers,
or donor financial data into a consumer AI chat. A human sends every email and submission.

## What it has been exercised against

- Three cases in [`evals/evals.json`](evals/evals.json): citation scoring versus circulation,
  testing masthead claims against bylines, and preserving a short news-desert map.
- Structural validation through `scripts/validate_skills.py`.

The eval suite has not been run against a live model, and the manual procedure has not been
validated on a real campaign media map.
