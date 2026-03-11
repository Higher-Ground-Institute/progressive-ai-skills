# Refine Ticket

**Category:** Operations
**Effort to set up:** 10 minutes
**Tested with:** Claude Code
**Requires:** Linear MCP integration

## What it does

Takes a Linear issue ID and refines the ticket: picks the right template (feature, bug, spike, support, refactor, discovery, or feature planning), rewrites the description, checks that acceptance criteria are specific and verifiable, re-evaluates priority, and cancels tickets that aren't worth doing. Posts the refined version as a comment so the original description is preserved.

## Who it's for

Engineering leads, project managers, and anyone responsible for backlog quality. Useful for organizations that use Linear for project management and want consistently well-structured tickets without spending time manually rewriting them.

## Example

**Input:** "Refine ENG-142"

**Output:**

The skill fetches the full issue, evaluates it against quality criteria, and posts a comment with the refined description. For example, a vague ticket like:

> Fix the export bug

Becomes a structured bug report posted as a comment:

> ## Problem
> CSV exports from the dashboard timeout when the dataset exceeds 10k rows. Users see a generic "Something went wrong" error with no retry option.
>
> ## Steps to Reproduce
> 1. Navigate to Dashboard > Exports
> 2. Select a dataset with more than 10,000 rows
> 3. Click "Export CSV"
>
> ## Expected Behavior
> Export completes successfully or fails with a clear error and retry option.
>
> ## Acceptance Criteria
> - [ ] CSV exports succeed for datasets up to 50k rows
> - [ ] Exports exceeding the limit show a specific error message with guidance

The skill also adjusts priority (e.g., bumping production bugs to High) and suggests labels if they're missing.

## Customization

The SKILL.md includes seven ticket templates and a set of label suggestions. Adjust the templates to match your team's conventions, swap the label names for your own, and modify the priority rules to fit how your organization triages work.

## How to use

Drop the SKILL.md into your skills directory. You'll need a Linear MCP integration so the skill can fetch and update issues. Then say something like "refine ENG-142" or "clean up this ticket" with an issue ID. The skill will activate automatically.
