# Reply to PR Reviews

**Category:** Development Workflow
**Effort to set up:** 5 minutes
**Tested with:** Claude Code

## What it does

Takes a PR number or URL, fetches all review comments, and replies to each one individually as a threaded response. For each comment, it checks whether an existing commit on the branch already addresses the feedback. If so, it links the commit. If not, it reads the relevant code and writes a concise technical explanation of why the current approach is correct. Uses the GitHub CLI (`gh`) to post replies directly to the PR.

## Who it's for

Developers and technical staff at progressive organizations who use GitHub for code review. Especially useful for teams where PRs accumulate review comments that need systematic responses -- campaign tech teams, nonprofit engineering departments, or anyone maintaining open-source tools for the movement.

## Example

**Input:** `/reply-to-pr-reviews 47`

**Output:**

Each review comment on PR #47 gets an individual threaded reply posted to GitHub. The user sees a summary table in their terminal:

```
| Comment | File            | Action    | Detail                        |
|---------|-----------------|-----------|-------------------------------|
| #201    | src/voter.ts:42 | Addressed | commit a1b2c3d                |
| #202    | src/match.ts:10 | Refuted   | already validated upstream    |
| #203    | src/api.ts:88   | Addressed | commit e4f5g6h                |
```

## Customization

You can adjust the reply style (more or less formal), add your own signature line, or modify the rules for what counts as "addressed." If your team uses a specific format for PR replies, update the reply templates in the SKILL.md.

## How to use

Drop the SKILL.md into your skills directory. Then give it a PR number or URL: `/reply-to-pr-reviews 47` or `/reply-to-pr-reviews https://github.com/org/repo/pull/47`. The skill handles fetching comments, reading code, and posting replies. Requires the GitHub CLI (`gh`) to be installed and authenticated.
