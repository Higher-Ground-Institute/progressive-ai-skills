# Contact Extractor

**Category:** Operations
*Contributed by [Adam Ruben](https://github.com/SnackAttack555).*

Automatically builds and maintains a contact spreadsheet from your Gmail. Runs on a schedule (or manually), scans recent emails, and pulls out names, email addresses, phone numbers, organizations, and titles — then saves everything to a deduplicated `.xlsx` file.

## Who it's for

Anyone at a campaign, advocacy org, or progressive organization who meets a lot of people over email and wants to keep a running contact list without manually copying info out of signatures and forwards. Especially useful if your organization has a data retention policy that deletes emails after some period--this will capture contact info you would otherwise lose.

## What it does

For each email in the scan window, the skill extracts contacts from four places:

1. **Email headers** — From, To, and CC fields
2. **Forwarded message blocks** — nested forwards, Outlook-style forwards, quoted headers
3. **Signature blocks** — phone numbers, titles, organizations, alternate emails
4. **Body text** — phone numbers always; email addresses only when explicitly shared as contact info (not incidental links or footers)

Contacts are saved to a spreadsheet with these columns: First Name, Last Name, Organization, Email, Cell Phone, Work Phone, Notes, Source (email subject line), and Date Entered.

The skill deduplicates on email address and merges new info into existing rows — so if you get someone's cell number in a later email, it gets added to their existing entry without creating a duplicate.

## Prerequisites

- **Gmail MCP connector** — the skill needs to search and read your email
- **Cowork or Claude Code** — for scheduled/recurring runs
- **A workspace folder** — where the output spreadsheet lives

During first-run setup, the skill will ask you to configure your own email addresses (so it can filter you out), your preferred schedule, and the output file location.

## How to use it

**As a scheduled task (recommended):**
Set it up once and it runs automatically — weekly by default, with a retry day to catch missed runs. Each run scans the last 7 days of email and appends any new contacts to the spreadsheet.

**Manually:**
Ask Claude to "extract contacts from my recent emails" or "scan my Gmail for new contacts" and it will run a one-time pass.

**First run:**
The skill will do a 30-day backfill on its first run to seed the spreadsheet, then switch to the rolling weekly window.

## Tips and edge cases

- **Phone number handling is opinionated.** The skill distinguishes between cell and work phones based on labels in signatures (`(c)`, `(m)`, `cell` → Cell Phone; `(o)`, `office`, `direct` → Work Phone). An unlabeled number defaults to Work Phone since it can't be confirmed as a cell. Once a cell number is captured for someone, the skill stops collecting additional numbers for them.
- **It won't grab junk.** System addresses (`noreply@`, `notifications@`, etc.), unsubscribe links, and mailing list addresses are automatically filtered out.
- **Forwarded emails are gold.** The skill parses nested forward headers to catch contacts you were introduced to but never directly emailed. This is where a lot of the value comes from in coalition and partnership work.
- **Notes accumulate context.** When the same contact appears in multiple emails, the skill appends context to the Notes field with dates, so you can see the thread of how you're connected.

## Example

You receive an email with the subject "Intro: Jane Smith / Acme Civic Tech" that contains a forwarded message with Jane's signature including her title, office number, and cell. The skill extracts:

| First Name | Last Name | Organization | Email | Cell Phone | Work Phone | Notes |
|---|---|---|---|---|---|---|
| Jane | Smith | Acme Civic Tech | jane@acmecivictech.org | (555) 123-4567 | (555) 987-6543 | CTO; intro via forwarded message |

If a later email reveals a second email address for Jane, it gets noted rather than overwriting her primary.

## Tested with

- Organizational inboxes with high volumes of introductions and forwards
- Emails with nested/multiple forwarding layers
- Mixed signature formats (labeled phone numbers, unlabeled, Outlook-style, plain text)
- Deduplication across 100+ contacts over a 30-day backfill window
