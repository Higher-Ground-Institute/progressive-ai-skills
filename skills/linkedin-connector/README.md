# LinkedIn Connection Tracker

*Contributed by [Adam Ruben](https://github.com/SnackAttack555).*

A Claude skill that scans your Google Calendar for recent meeting attendees, finds their LinkedIn profiles, and helps you stay on top of professional networking — without the manual busywork.

## What It Does

Run this skill on a schedule (e.g., weekly via Cowork) and it will:

1. Pull your calendar events from the past 7 days (or since the last run)
2. Extract attendees from your meetings
3. Filter out internal colleagues, known contacts, and people already presented in previous runs
4. Look up each new contact's LinkedIn profile via web search
5. If Claude in Chrome is available: open each profile in a browser tab, check whether the button says "Connect" or "Message," auto-close tabs for people you're already connected to, and leave only the actionable ones open
6. Present a summary with clickable links and a "Mark All as Done" button that saves contacts to persistent storage

Each run only surfaces genuinely new contacts. People you've already reviewed won't appear again.

## How It Works

### Smart Filtering

- **Internal domains**: Automatically excludes your org's email domain (configurable)
- **Named colleagues**: Excludes specific people you work with regularly (configurable)
- **Group call handling**: For meetings with 6+ attendees, only includes people who actually accepted the invite — avoids flooding you with names from big roundtable invite lists
- **Deduplication**: If someone appeared in three meetings this week, they show up once with all three meetings listed as context

### Name Resolution

Calendar invites don't always include full names. The skill handles this with a multi-step fallback chain:

1. Use the `displayName` from the calendar event
2. Check event titles and descriptions for name clues (e.g., "Lioz/Ruben" in the title + `alioz@naacpldf.org` → last name is "Lioz")
3. Derive a name from the email address (e.g., `j.smith@company.com` → "J Smith")
4. Search Gmail for threads with that email address, then pull full thread content via `get_thread` to extract names from email signatures, quoted reply headers, and forwarded message headers. (The `search_threads` endpoint strips display names — `get_thread` with `FULL_CONTENT` is required to get real names.)
5. Search the web for the person's name on org staff pages or nonprofit 990 filings
6. If all else fails, display the email with meeting context so you can search manually

### LinkedIn Lookup

Uses `site:linkedin.com/in/` web searches with the person's name and organization (extracted from their email domain). In testing, this reliably returns the correct profile as the first result for most people in the progressive/democracy/policy space.

When a profile can't be found, the skill generates a fallback LinkedIn search URL so you're one click away from finding them manually.

### Connection Status Detection (Claude in Chrome)

If Claude in Chrome is active, the skill opens each LinkedIn profile in a browser tab and reads the page to check the primary action button:

- **"Connect"** or **"Invite [Name] to connect"** → You're not connected. Tab stays open for you to click Connect.
- **"Message [Name]"** → Already connected. Tab auto-closes.
- **"Follow" / "Pending"** → Request already sent. Tab auto-closes.

**Prerequisites for Chrome features:**
- Google Chrome must be open with the Claude extension installed and running
- You must be **logged into LinkedIn** in Chrome — the skill reads your profile pages as you, so it needs your active LinkedIn session to see the Connect/Message buttons

If Chrome isn't available or you're not logged into LinkedIn, the skill falls back to an artifact with clickable profile links.

### Persistent Memory

Uses a JSON file (`linkedin-tracker-data.json`) in the workspace folder to track state across runs:

- `last-run` — Timestamp of the last scan, so the next run picks up where this one left off
- `presented-contacts` — Map of email → date presented, so contacts are never shown twice

## Required Integrations

| Tool | Required? | Purpose |
|------|-----------|---------|
| Google Calendar (MCP) | Yes | List events and extract attendees |
| Gmail (MCP) | Yes | Resolve ambiguous names via full thread content (signatures, reply headers) |
| web_search (built-in) | Yes | Find LinkedIn profile URLs |
| Claude in Chrome (MCP) | Optional | Open profiles, detect connection status, close already-connected tabs |
| Persistent Storage (JSON file) | Yes | Track presented contacts across runs |

**Claude in Chrome requirements:** Chrome must be open with the Claude extension running, and you must be logged into LinkedIn in Chrome. Without this, the skill still works but presents clickable links instead of opening tabs.

## Configuration

The skill ships with configuration for a specific user/org. To adapt it for your own use, edit the following sections in `SKILL.md`:

### Internal Domains to Exclude

```
- yourorg.com
```

Add your organization's email domain(s) so internal colleagues are automatically filtered out.

### Known Colleagues to Exclude

```
- Jane Smith
- Bob Jones
```

Add people you meet with regularly who you don't need LinkedIn connection prompts for (e.g., co-founders, board members, direct reports). The skill will also detect alternate email addresses for the same person — if a known colleague uses both a work and personal email, both are excluded.

### User Identity

The skill filters out the user by name and email domain. Update the `User's Own Identity` section in `SKILL.md` to match your own name and org email domain.

## Usage

### As a One-Off

> "Run my LinkedIn connect task"

or

> "Check my calendar for new contacts to connect with on LinkedIn"

### As a Scheduled Cowork Task

Set up a recurring Cowork task with a prompt like:

> "Run my LinkedIn connect task"

Weekly on Mondays works well with the 7-day lookback window.

### Trigger Phrases

The skill is designed to trigger on:

- "run my LinkedIn connect task"
- "check my calendar for new contacts"
- "networking follow-up from meetings"
- "who should I connect with"
- "LinkedIn connections from recent meetings"

## Limitations

- **LinkedIn API**: LinkedIn does not offer a public API for checking connections or sending requests. The skill works around this by using web search for profile discovery and Claude in Chrome for connection status detection.
- **Chrome dependency**: The tab-opening and connection status features require Chrome to be open with the Claude extension running, and you must be logged into LinkedIn in that Chrome session. Without this, the skill falls back to clickable links in an artifact.
- **LinkedIn rate limiting**: Opening too many profiles in rapid succession may trigger LinkedIn's login wall. The skill detects this and gracefully degrades, listing remaining contacts as "could not verify."
- **Gmail API quirk**: The `search_threads` endpoint strips display names from sender/recipient fields, returning only bare email addresses. The skill works around this by using `get_thread` with `FULL_CONTENT` format to extract names from signatures, quoted reply headers, and forwarded message headers. This is documented in the SKILL.md for anyone maintaining the skill.
- **Name matching**: For contacts with only a first name or a generic email (gmail, outlook), LinkedIn searches may return the wrong person or no results. The skill handles this with fallback search links.

## Contributing

This skill is part of the [Progressive AI Skills](https://github.com/Higher-Ground-Institute/progressive-ai-skills) collection. To suggest improvements or report issues, open an issue or PR in the main repo.

## License

See the repository's LICENSE file for details.
