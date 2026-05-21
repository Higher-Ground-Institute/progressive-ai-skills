# FEC Filing Analysis

**Category:** Research & Data

Analyze Federal Election Commission (FEC) campaign finance filings — contributions, disbursements, loans, debts, and independent expenditures — without dumping massive datasets into the model's context window. Built around the [`fecfile`](https://pypi.org/project/fecfile/) Python library with an opinionated workflow for filings of any size, from a small state party monthly to a presidential campaign quarterly with hundreds of thousands of itemizations.

## Who it's for

Campaign finance researchers, journalists, opposition researchers, and policy analysts who want to answer questions like:

- Who are the top donors to a given committee this quarter?
- What did a campaign spend money on, and where?
- What independent expenditures were made supporting or opposing a candidate?
- How does this committee's fundraising compare period-over-period?

If you regularly pull data from [docquery.fec.gov](https://docquery.fec.gov) or wrangle FEC filings by hand, this skill automates the tedious parts.

## What it does

Given an FEC filing ID (e.g., `1896830`), the skill:

1. **Checks the filing size first** with `--summary-only` so you never accidentally blow up the context window on a half-million-row filing
2. **Pre-filters by schedule** (`--schedule A` for contributions, `--schedule B` for disbursements, etc.) so unused data is never loaded
3. **Post-filters with pandas** for aggregations like "top 10 vendors" or "contributions grouped by state"
4. **Streams as JSONL** (`--stream`) for filings too large to hold in memory — incremental aggregation with constant memory usage

It also includes authoritative field-mapping references for FEC forms (F1, F2, F3, F3P, F3X, F99) and schedules (A through E), so the model never guesses at field names.

## Prerequisites

- **[uv](https://docs.astral.sh/uv/)** — Python package manager that auto-installs dependencies
- **Python 3.9+**
- **Internet access** — to fetch filings from docquery.fec.gov

Optional but recommended for committee/filing discovery:

- **`fec-api` MCP server** — provides `search_committees` and `get_filings` tools. Requires a free [FEC API key](https://api.open.fec.gov/developers/). Without it, you can still use the skill by providing filing IDs directly (find them at [fec.gov](https://www.fec.gov) or in URLs like `https://docquery.fec.gov/dcdev/posted/1690664.fec`).

## How to use it

**With a filing ID in hand:**

Ask Claude something like "summarize FEC filing 1896830" or "show me the top 10 expenditures from filing 1896830" and the skill takes over.

**Without a filing ID (requires `fec-api` MCP server):**

Ask "show me the latest filing for the Utah Republican Party" or "find recent filings from ActBlue" and the skill chains `search_committees` → `get_filings` → `fetch_filing.py` for you.

**Common queries the skill is built for:**

- "What are the total receipts and disbursements?"
- "Who are the top 10 contributors?"
- "What are the largest expenditures, and what were they for?"
- "What contributions came from California?"
- "How much did this committee spend on advertising?"

## Tips and edge cases

- **Always check size first.** Major committees (ActBlue, WinRed, presidential campaigns) routinely file with hundreds of thousands of itemizations. The skill enforces a `--summary-only` check before any full pull. Trust this — it exists because of real failures.
- **Use the field references.** `references/FORMS.md` and `references/SCHEDULES.md` document the exact field names used in parsed filings. Don't let the model guess — point it at these.
- **Amendments matter.** Filings with `amendment_indicator: A` are amendments to a previous filing. Check `previous_report_amendment_indicator` to find the original. By default `get_filings` excludes superseded amendments; set `include_amended: true` to see them.
- **Itemization threshold is $200.** Contributions and expenditures under $200 don't appear in schedule itemizations — they only roll up into summary totals. If a search seems to be "missing" small donors, this is why.
- **API keys stay hidden.** If you use the `fec-api` MCP server, the FEC API key is loaded from the system keyring on first use and never exposed to the model or the conversation.

## Source and attribution

This skill is a verbatim copy of the [`fecfile` skill from agent-fecfile](https://github.com/hodgesmr/agent-fecfile) by **Matt Hodges**, distributed under the MIT License. We've mirrored it here so it's discoverable alongside other progressive-infrastructure skills; for upstream updates, the canonical source is hodgesmr/agent-fecfile.

The optional MCP server (`fec-api`) lives in the upstream repo — if you want committee/filing search rather than just filing-ID lookups, install via the upstream's instructions.
