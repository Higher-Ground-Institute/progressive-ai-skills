---
name: district-media-map
description: Builds an actionable map of outlets, beat reporters, community platforms, and candidate forums reaching one district. Verifies the campaign election date, inventories election and submission deadlines before deep outlet profiling, records reusable submission mechanics, and ranks outlets by local relevance and citation value rather than circulation. Use before local-media-pitch or whenever a campaign needs current media contacts, submission rules, forums, or a news-desert assessment.
---

# District Media Map

**Reads:** campaign frontmatter for `election_date` and public outlet, directory, clerk, and
meeting-record sources.
**Writes:** `campaign/district-media-map.md`, using
[`campaign-template/district-media-map.md`](../../campaign-template/district-media-map.md).

Every outlet row must answer who to contact, about what, through which submission path, by what
date, under which rule, and when that information was checked.

> Never paste voter names, home addresses, voter ID numbers, personal phone numbers, donor
> financial data, or reporter contact lists into a consumer AI chat. A reporter's work email,
> newsroom phone, or professional handle may be recorded only when the outlet or reporter has
> publicly published it for work contact. Public visibility alone is not consent: do not use a
> personal cell or private address from a social profile, guess an email pattern, or buy,
> scrape, or import a contact database.
>
> If the human offers a voter file, decline it and explain why.

## Election and deadline inventory first

Read `election_date` from campaign frontmatter; never assume a November general election.
Confirm the election name and date against the county clerk/elections office or Secretary of
State. In `## Assessment`, record the election name, confirmed ISO date, official source, and
retrieval date used. If sources conflict, stop deadline calculations and log the conflict.

Before deep outlet profiling:

1. Resolve every municipality, township, school district, and county touched by the race.
2. Build a preliminary outlet and forum inventory from the sources below.
3. For each candidate venue, find the letters, op-ed, questionnaire, endorsement, debate, and
   forum rules. Convert every relative election rule into an exact date using the confirmed
   `election_date`.
4. Record a deadline as confirmed only when supported by a published policy or direct human
   confirmation. Otherwise mark it `[UNCONFIRMED — ask outlet]`. This skill contacts no one;
   a campaign human sends any inquiry.
5. Sort the deadline inventory earliest first. Only then spend time on deep reporting and
   citation-value profiles.

## Source inventory

Use the union of:

- State press-association member directory
- [Institute for Nonprofit News](https://findyournews.org/)
- [LION Publishers members](https://www.lionpublishers.com/members/)
- [NPR stations by ZIP](https://www.npr.org/stations/)
- Nearby campus papers and journalism bureaus
- Official legal-notice newspaper of record
- Clerk's press notification list, requested as a public record when needed
- Three months of governing-body minutes and video to identify who actually attends

Do not rely on campaign memory or a prebuilt national contact database.

## Output Format

Write the template's frontmatter exactly: `jurisdiction`, `map_date`, `outlets_found`,
`news_desert_assessment`, `date_created`, and `date_modified`. Then write `## Assessment`,
`## Outlets`, `## Community platforms`, `## Forums and candidate events`, and
`## News desert`, in that order.

For every outlet record:

- Type, owner, coverage area, original-local-reporting test, citation score, and paywall
- Beat reporter's name, beat, publicly published work contact, and recent relevant story
- Letters mechanics: word limit, submission address/form, frequency, residency, verification,
  election restriction, exact deadline, source URL, and checked date
- Op-ed mechanics: word limit, path, exclusivity, turnaround, candidate-bylines rule, election
  restriction, exact deadline, source URL, and checked date
- Questionnaire/endorsement process, owner, expected or exact date, status, source, checked date
- A `Mechanics freshness` line: `fresh through [date]` when a policy states an effective period,
  otherwise `recheck after [date]` no later than 30 days from verification

This is a reuse contract for `local-media-pitch`: when the relevant mechanics are still within
their recorded freshness window, reuse them without repeating discovery; re-check expired,
unconfirmed, or pitch-specific fields before drafting. A checked date alone does not override a
policy change visible on the outlet's current site.

Record community-platform posting rules and forum contact, timing, deadline, recording policy,
and source. Never draft anonymous, pseudonymous, apparently organic, journalist-voiced, or
constituent-voiced posts. All campaign material must be candidate-attributed, human-reviewed,
and human-posted through a disclosed process.

## Deep profiling and citation scoring

After the deadline inventory, read the last fourteen days of each outlet's local section.
Count original reports with a named local byline and a local body, meeting, or person in the
lede. Exclude wire copy, syndicated work, and press-release reprints.

Score each outlet 0, 1, or 2 on each test:

| Test | 0 | 1 | 2 |
|---|---|---|---|
| Original reporting on this district's governing bodies | none | regional only | covers these meetings |
| Geographic overlap | metro-wide only | partial | core coverage area |
| Access for candidate copy | none | letters only | letters, op-eds, questionnaire |
| Durable, readable archive | hard paywall/dead links | soft paywall | free, dated, stable |
| Pickup by other outlets | never | occasionally | routinely |

Totals of 8–10 are high, 5–7 medium, and 0–4 low. Show the component scores and rank by total,
not circulation. Resolve ties by coverage of the body for which the candidate is running.

## News-desert classification

- **Healthy:** at least two outlets produce original reporting on the relevant governing body
  most weeks.
- **Thin:** one outlet does, or coverage is roughly monthly.
- **Desert:** no outlet covered that body in the last 90 days.

Test non-200 pages in a browser before calling an outlet dead. Count outlets that cover the
district even when headquartered elsewhere. Classify coverage for the candidate's governing
body and explain material differences across bodies. A short map is valid; never pad it with
regional outlets that do not cover the district.

## Steps

1. Verify and record the campaign election name and `election_date`.
2. Resolve geography and build the preliminary outlet/forum inventory.
3. Build and sort the election/submission deadline inventory.
4. Test original reporting, identify current bylines, and apply citation scoring.
5. Capture all submission mechanics and explicit freshness windows.
6. Record community platforms and candidate-posting rules.
7. Record forum conveners, deadlines, contacts, and recording/reuse policies.
8. Classify the candidate's governing body as healthy, thin, or desert.
9. Have a human review contacts, confirmed versus unconfirmed deadlines, and stale fields.
   This skill sends no email and submits nothing.

## Rules that do not bend

- Use only publicly published work-contact details; never guess or enrich private PII.
- Use the verified campaign election date for every calculated deadline and state the election
  used.
- Preserve separate mechanics and deadlines for letters, op-eds, questionnaires,
  endorsements, and forums.
- Show citation-score components; do not rank by circulation.
- Keep every source URL and checked date so `local-media-pitch` can test freshness.
- Never contact, post, pitch, or submit on the campaign's behalf.

## Doing this without an agent

For the complete no-agent workflow, see [`README.md`](README.md#manual-procedure). The privacy
guardrail, election verification, deadline-first order, output contract, scoring, and
human-action gate above still apply.

## Tips

Contact freshness and mechanics freshness are separate. A current submissions policy does not
prove the named reporter still holds the beat; re-check each field on its own schedule.
