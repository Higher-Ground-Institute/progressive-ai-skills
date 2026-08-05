---
name: linkedin-connector
description: Scan recent calendar meetings, find new attendees, look up their LinkedIn profiles, and present connection links. Use this skill whenever the user asks to find people they've met with recently who they should connect with on LinkedIn, or asks to check calendar meetings for networking follow-ups, or mentions connecting with meeting attendees on LinkedIn, or asks "who should I connect with" after meetings. Also triggers for variations like "run my LinkedIn connect task", "check my calendar for new contacts", or "networking follow-up from meetings".
---

# LinkedIn Connection Tracker

Scan the user's Google Calendar for recent meeting attendees, filter out known/internal contacts, check which people have already been presented in previous runs, look up LinkedIn profiles for new contacts, and present a clean list of clickable LinkedIn profile links.

## Overview

This skill is designed to run periodically (e.g., weekly via Cowork) to help the user stay on top of networking. It:

1. Pulls calendar events from the past 7 days (or since the last run)
2. Extracts unique external attendees
3. Filters out internal domains and known colleagues
4. Checks persistent storage for people already presented
5. Resolves ambiguous names via Gmail full-thread content
6. Searches for LinkedIn profiles of new contacts via web_search
7. Opens each profile in Chrome via Claude in Chrome
8. Reads each page to check if the button says "Connect" or "Message"
9. Closes tabs for people already connected (Message button), leaves Connect tabs open
10. Presents a summary artifact with results and marks contacts as presented
11. Records presented contacts to persistent storage so they aren't shown again

## Required Tools

- **Google Calendar** (MCP) — to list recent events and extract attendees
- **Gmail** (MCP) — to resolve attendee identities via full thread content (signatures, headers)
- **web_search** (built-in) — to search for LinkedIn profile URLs
- **Claude in Chrome** (MCP) — to open LinkedIn profiles in browser tabs, read the page to detect Connect vs Message buttons, and close tabs for already-connected contacts
- **Persistent Storage** (artifact storage API or workspace JSON file) — to track previously presented contacts

## Configuration

Before first run, ask the user to provide:

### Internal Domains to Exclude

Filter out any attendee whose email matches these domains. Example:
- `yourcompany.com`
- `yourcompany.org`

### Known Colleagues to Exclude (by name)

Always exclude these people regardless of email domain. Also detect alternate email addresses for the same person (e.g., if a known colleague uses both a work email and a personal email, exclude both). Example:
- Jane Smith
- Bob Jones

### User's Own Identity

Exclude the user from attendee lists. Match by name or by any known email alias.

## Workflow

### Step 1: Determine Time Window

Check persistent storage for the timestamp of the last run. Persistent storage is a JSON file in the workspace folder named `linkedin-tracker-data.json`.

- If found: use that timestamp as the start of the search window
- If not found: use 7 days ago as the start
- End time: now

### Step 2: Pull Calendar Events

Use `Google Calendar:list_events` with the computed time window. Request all events (use a reasonable page_size like 250).

### Step 3: Extract Attendees

From each event, collect all attendees. For each attendee, extract:
- **email** (the unique key)
- **displayName** (if available, otherwise derive from email — see below)
- **responseStatus** (`accepted`, `declined`, `needsAction`, `tentative`)
- **event title** (for context on how you met)
- **event date**
- **event size** (total number of attendees on that event)

**Group call filtering**: For events with more than 5 attendees (large group calls, roundtables, etc.), only include attendees whose `responseStatus` is `accepted` or `tentative`. This avoids presenting dozens of people from big invite lists who may not have actually attended. For small meetings (5 or fewer attendees), include everyone regardless of RSVP status — small meetings are more intentional and people often don't bother RSVPing.

**Name derivation from email**: When an attendee has no `displayName`, try to derive it:
1. Split the email local part on `.`, `-`, or `_`
2. Capitalize each segment
3. Example: `j.smith@company.org` → initial guess "J Smith"
4. Example: `mjohnson42@gmail.com` → initial guess "Mjohnson"

**Name derivation from event context**: Check event titles, descriptions, and other contextual clues:
- Event title "Smith/Jones" + email `jsmith@company.org` → last name is likely "Smith"
- Event description mentioning "Jane Smith is inviting you" → full name resolved
- Parallel events listing full names → names for attendees on the main event

Consolidation rules:
- Deduplicate by email (case-insensitive)
- For each unique email, keep a list of all meeting titles/dates where they appeared

### Step 4: Filter

Remove attendees that match any of these criteria:
- Email domain is in the internal domains list
- Name matches any known colleague (fuzzy match — ignore case, allow partial match on first+last name)
- The attendee is the user themselves (match by name or any known email alias)
- The attendee email is a "resource" (contains `resource.calendar.google.com` or similar non-person addresses)
- The attendee has no meaningful name or email (e.g., empty or `Unknown`)
- The email looks like a generic info address (e.g., `info@organization.org`)

### Step 5: Check Already-Presented

Read the `presented-contacts` field from the persistent storage JSON file. This is an object mapping email addresses to the date they were first presented.

Remove any attendee whose email is already in this map.

### Step 6: Resolve Ambiguous Names via Gmail

Before searching LinkedIn, check if any remaining contacts have incomplete or ambiguous identities — specifically:
- No display name (only an email-derived guess)
- Only a first name (no last name)
- Name derived from email looks like a username rather than a real name

**CRITICAL: The Gmail `search_threads` API strips display names from the `sender` field.** It returns bare email addresses (e.g., `sean@example.com`) even when the actual email has a full display name (e.g., `Sean Smith <sean@example.com>`). You **cannot** rely on the `sender` field from `search_threads` to resolve names.

**Two-step Gmail name resolution process:**

**Step 6a: Find relevant threads** — Search Gmail using `Gmail:search_threads` with a query like:
```
from:their@email.com OR to:their@email.com
```
This identifies threads involving the contact. Note the `threadId` of the most promising thread (preferably one where the contact sent a message, or one with replies).

**Step 6b: Pull full thread content** — For each thread found, call `Gmail:get_thread` with `messageFormat: "FULL_CONTENT"` to retrieve the complete email bodies. Then extract the full name from:
1. **Email signatures** in the message body (e.g., `"-- \nJane Smith\nDirector of Operations..."`)
2. **Quoted reply headers** (e.g., `"On Apr 24, Jane Smith <jsmith@company.org> wrote:"`)
3. **Forwarded message headers** (e.g., `"From: Jane Smith <jsmith@company.org>"`)

These are all present in the `plaintextBody` field of the full content response and are reliable sources of display names.

**Why this matters**: In testing, `search_threads` failed to return display names for every single contact tested. The `get_thread(FULL_CONTENT)` approach resolved names from signatures and headers in every case where email correspondence existed. This is the single most important implementation detail in this skill.

**Additional name resolution strategies when Gmail doesn't help:**
- **Web search for org staff**: Search `"Organization Name" "FirstName" staff OR team OR director` to find the person on org websites or 990 filings
- **Nonprofit 990 filings**: Search ProPublica Nonprofit Explorer or similar for the organization to find staff names and titles
- **Event context clues**: Use event titles, descriptions, and other attendee names to narrow down identity

This step is only for contacts with missing or ambiguous names. Skip it for anyone who already has a clear first + last name from the calendar data.

### Step 7: LinkedIn Profile Lookup

For each remaining attendee (the new contacts), search for their LinkedIn profile.

Use the built-in `web_search` tool with a query like:
```
site:linkedin.com/in/ "FirstName LastName" OrganizationName
```

If the attendee has a company domain in their email (e.g., `@acmecorp.com`), extract the org name and include it in the search to improve accuracy. If the domain is generic (gmail, outlook, etc.), search with just the name.

From the search results, pick the most relevant LinkedIn profile URL — one that:
1. Matches `linkedin.com/in/` (not `/company/` or `/pub/`)
2. Has a name or title that plausibly matches the attendee

If no LinkedIn profile is found, still include the person in the output but provide a fallback LinkedIn search URL:
```
https://www.linkedin.com/search/results/all/?keywords=FirstName+LastName
```

**Rate limiting**: Space out web_search calls. For large batches (10+ people), consider doing them sequentially rather than in a burst.

### Step 8: Open LinkedIn Profiles in Chrome

For each contact where a LinkedIn profile URL was found, use `Claude in Chrome:navigate` to open the profile in the browser. Use `Claude in Chrome:tabs_create_mcp` to create new tabs so profiles open in parallel without replacing each other.

**Batch navigation for efficiency**: Create all needed tabs first, then navigate them all in a single `browser_batch` call, then read pages in batches of 4-5 at a time.

Process tabs:
1. Navigate to the LinkedIn profile URL in a new tab
2. Wait for the page to load
3. Use `Claude in Chrome:read_page` with `filter: "interactive"` to get the accessibility tree
4. Look for the primary action button on the profile. LinkedIn profiles show one of:
   - **"Connect"** or **"Invite [Name] to connect"** — you are NOT connected. Leave this tab open.
   - **"Message [Name]"** — you ARE already connected. Close this tab using `Claude in Chrome:tabs_close_mcp`.
   - **"Follow"** or **"Pending"** — connection request already sent or they don't accept connections. Close the tab.
5. Record the result for each contact: `connected` (Message), `not_connected` (Connect), `pending`, or `unknown`

If a profile URL wasn't found for a contact, skip the Chrome step for that person — they'll appear in the summary artifact with a manual search link.

**Important**: LinkedIn may show login walls or rate-limit if too many profiles are opened rapidly. If `read_page` returns a login prompt or CAPTCHA instead of a profile, stop opening new tabs and note the remaining contacts as "could not verify" in the summary.

**Bonus**: While reading profile pages, look for useful data in the "People also viewed" or "People you may know" sections — these sometimes contain LinkedIn URLs for other contacts on your list who you hadn't found via web search.

### Step 9: Present Summary

After processing all tabs, build an artifact that displays a summary.

**Header**: Date range scanned, total new contacts found, breakdown of results.

**Sections**:
- **Not Connected (Action Needed)**: Contacts whose LinkedIn profiles showed "Connect" — show name, org, email, meeting context, and a "View Profile" link. These are the ones to click Connect on.
- **Already Connected (Closed)**: Contacts whose profiles showed "Message" — already in your network, tabs were auto-closed. Show name and org for your records.
- **Pending**: Contacts whose profiles showed a pending connection request.
- **Could Not Find Profile**: Contacts where web_search didn't return a LinkedIn match. Show name, email, meeting context, and a "Search LinkedIn" link.
- **Could Not Verify**: Contacts where Chrome couldn't read the page (login wall, rate limit). Show name with LinkedIn URL so the user can check manually.

### Step 10: Update Persistent Storage

After presenting results, update the `linkedin-tracker-data.json` file in the workspace folder:

1. **`last-run`**: Set to the current ISO timestamp
2. **`presented-contacts`**: Merge ALL new contacts into the existing map (regardless of whether they were connected, not connected, or unverified — we don't want to show them again next run). Each entry should be `{ email: datePresentedISO }`.

The `last-run` timestamp should be updated as soon as the calendar scan completes (so even if the process is interrupted, the time window advances).

## Edge Cases

- **No new contacts**: If all attendees have already been presented or are filtered out, show a friendly "No new contacts to connect with since [last run date]" message.
- **Calendar API pagination**: If the user has a very busy calendar, handle pagination with `pageToken`.
- **Attendees with no name**: Use the local part of the email as a display name fallback, then try Gmail full-thread resolution.
- **Search rate limits or failures**: If a web_search fails, still show the contact with a manual search link. Don't let one failure block the whole list.
- **LinkedIn login walls**: If Chrome encounters a login wall when opening profiles, stop the tab-opening loop and present remaining contacts as "could not verify" with their URLs.
- **Chrome not available**: If Claude in Chrome tools are not loaded or not responding, fall back to the artifact-only mode — present all contacts with clickable LinkedIn profile links instead of opening tabs.
- **Unresolvable names**: If a contact has no display name, Gmail full-thread search returns nothing, web search for org staff returns nothing, and the email-derived name is too ambiguous for a LinkedIn search, still include them in the output with just their email and meeting context. The user may recognize them and search manually.
- **Known colleague alternate emails**: Some colleagues may use multiple email addresses (e.g., personal gmail, different org email). When you encounter someone deeply involved in internal operations (reviewing drafts, discussing contracts, on recurring team calls), consider whether they might be a known colleague with a different email address. Exclude if so.
- **Tab group disconnection**: Chrome tab groups may get disconnected during long runs. If tabs are lost, the artifact serves as the permanent record — all profile links are preserved there.

## Storage Schema

```json
{
  "last-run": "2026-04-25T12:00:00Z",
  "presented-contacts": {
    "jane.doe@example.com": "2026-04-25T12:00:00Z",
    "bob.smith@acme.org": "2026-04-25T12:00:00Z"
  }
}
```

## Notes

- LinkedIn does not offer a public API for checking existing connections or sending requests. Claude in Chrome bridges this gap by reading the profile page UI to detect connection status.
- Claude in Chrome cannot click the "Connect" button on the user's behalf — this is an irreversible action on a third-party platform that requires the user's explicit action. The skill leaves the right tabs open; the user clicks Connect.
- web_search with `site:linkedin.com/in/` queries is the most reliable method for finding LinkedIn profile URLs from names.
- The persistent storage ensures this skill is useful as a recurring task — each run only surfaces genuinely new contacts.
- If Chrome encounters rate limiting from LinkedIn (e.g., login walls after too many profile views), the skill degrades gracefully by noting unverified contacts in the summary.
- **Gmail API limitation**: The `search_threads` endpoint strips display names from sender/recipient fields, returning only bare email addresses. Always use `get_thread` with `messageFormat: "FULL_CONTENT"` to resolve names from email signatures, quoted reply headers, and forwarded message headers. This is the single most important lesson from building this skill.
