# District Issue Scan

**Category:** Research & Data

Builds a ranked, sourced inventory of what people in one specific jurisdiction actually argue about. It finds the local government's meeting records — wherever they happen to live — reads them, checks local coverage, catalogs the ballot measures voters will see alongside the race, and writes `campaign/district-issues.md`.

## Who it's for

First-time, down-ballot candidates and the volunteers helping them: state legislature, county commission, city council, school board. Anyone who has been told to "run on local issues" and discovered that nobody has written down what those are.

## What it does

The core of the skill is a **detection procedure**, not a list. There is no national registry of local agenda software, so the skill works out where the records live for whatever jurisdiction you point it at:

1. Find the official agenda page for each governing body.
2. Read the hostname to identify the vendor — `{client}.legistar.com`, `{st}-{jurisdiction}.civicplus.com/AgendaCenter`, `{jurisdiction}.granicus.com`, PrimeGov, CivicClerk.
3. Pull the records through the vendor's API or a supported scraper. Legistar has a public web API; [`civic-scraper`](https://github.com/biglocalnews/civic-scraper) covers the rest.
4. Fall back to downloading agenda PDFs and reading them by hand, which is what most water districts and library boards require.

It scans city or village council, county commission, school board, water and sewer district, planning and zoning, library board, and transit authority. The boring bodies usually carry the sharpest local fights.

Issues are then **ranked by documented salience** — public-comment counts from the minutes, contested votes with the tally, rate increases with the dollar figure, petitions, repeated coverage. Not national issue polling, not what the campaign assumes.

Finally it runs a **contested-space survey**: for each issue, who already publishes a good answer, and how good it is. This is the field that decides whether writing about an issue is worth the campaign's time.

## Prerequisites

- The jurisdiction name and one street address inside the district
- Web access — that is genuinely it
- Optional: an Open States API key for state-legislative district lookups (free, rate-limited to roughly 10 requests per minute and 500 per day)

No paid data vendor is required, and the skill has a complete manual procedure for anyone working without an AI tool.

## How to use it

Ask for a district issue scan and name the jurisdiction: *"scan the issues in Cordwell County, Ohio for a county commission race."* The skill resolves the district boundary, detects the agenda vendor per body, pulls twelve months of records, and drafts the file.

Then read it with someone who knocks doors. Where the ranking does not match what they hear, go find the record — do not reorder on instinct.

Output goes to `campaign/district-issues.md`, which `positioning-builder` reads next.

## Tips and edge cases

- **Minutes, not agendas.** Agendas say what was scheduled. Minutes say who showed up, who spoke, and how the vote split. Salience lives in the minutes.
- **News deserts are a finding, not a failure.** If no outlet covers the water district, the skill says so in `## Dead ends and gaps` and leans harder on primary records. A short honest scan beats a padded one.
- **Dead ends get logged.** Every source checked appears in the sources table with its yield, including the zeros. That is how the next volunteer avoids re-running your searches.
- **The place-swap test.** Swap the county name for a different one. If the issue list still reads fine, it is national boilerplate and the scan failed.
- **Legistar client slugs are guessable but verify them.** The word before `.legistar.com` is the client name, and `https://webapi.legistar.com/v1/{Client}/Events` usually works without a key. Usually.

## Example

Searching `Cordwell County commissioners agenda` lands on `cordwellcounty.legistar.com/Calendar.aspx`. Hostname says Legistar, client slug is `cordwellcounty`, so events come from `https://webapi.legistar.com/v1/cordwellcounty/Events`. The school board turns out to be on CivicPlus and needs `civic-scraper`. The regional water district has no vendor at all — twelve months of PDFs on a WordPress site, read by hand, which is where the sewer-rate fight was hiding.

## What it has been exercised against

Stated precisely, because a repo about not fabricating claims should not fabricate its own test history.

- **Three eval cases** in [`evals/evals.json`](evals/evals.json), runnable by `npx agent-skills-eval`: source detection from a volunteer's raw search log, one row per governing body before any issue is named; the "top five issues, I don't need sources" request, which has to be refused rather than answered from general knowledge; and a contested-space survey over an issue list the campaign supplied. They run against an invented county with `example.org` hostnames.
- **Structural validation** on every pull request via `scripts/validate_skills.py`, which enforces the agentskills.io spec plus this repo's conventions.

**Not yet done:** the eval suite has not been run against a live model, so no assertion here has an observed pass rate, and no real campaign has scanned a real district with it. The manual procedure in `## Doing this without an agent` is written for a library computer and no AI tool, but nobody has walked it end to end. If you run it, please open an issue and say what broke.
