---
name: reply-to-pr-reviews
description: >
  Use when asked to reply to PR review comments, respond to code review feedback, or address
  reviewer requests on a pull request. Triggers on: "reply to the PR comments", "respond to
  the review", "address the PR feedback", "handle review comments on PR #123", or when given
  a PR number or URL with intent to respond to reviewer feedback.
---

# Reply to PR Review Comments

Reply to every review comment on a PR with either a commit link that addresses the feedback
or a reasoned refutation.

## Usage

```
/reply-to-pr-reviews <PR number or URL>
```

## Workflow

### 1. Identify the PR

Parse the argument. If a number, use the current repo. If a URL, extract owner/repo/number.

```bash
# Get PR details
gh pr view <number> --json number,url,headRefName,baseRefName,title
```

### 2. Fetch all review comments

```bash
# Get all review comments (not issue comments)
gh api repos/{owner}/{repo}/pulls/{number}/comments --paginate --jq '.[] | {id, path, line, body, user: .user.login, in_reply_to_id, created_at}'
```

### 3. Fetch commits on the PR branch

```bash
# Get commits with their SHAs and messages
gh pr view <number> --json commits --jq '.commits[] | {oid: .oid[0:7], messageHeadline}'
```

### 4. Filter to unaddressed top-level comments

A comment is "addressed" if it already has a reply from you. Only process:
- Top-level review comments (where `in_reply_to_id` is null)
- That do NOT already have a reply containing your signature

### 5. Process comments ONE AT A TIME

<CRITICAL>
You MUST post a SEPARATE `gh api` call for EACH comment. One comment = one POST.

FORBIDDEN actions:
- Posting a single summary comment to the PR
- Combining multiple replies into one comment
- Using `gh pr comment` (this posts an issue comment, not a threaded reply)
- Composing all replies first and then posting -- you must post each reply BEFORE moving to the next comment

The ONLY way to reply is `gh api repos/{owner}/{repo}/pulls/{number}/comments --method POST` with `-F in_reply_to=<comment_id>`.
</CRITICAL>

Process comments sequentially. For each comment, complete all steps before moving to the next:

**Step A: Read the relevant code**

```bash
gh pr diff <number> -- <path>
```

Look at the comment's `path` and `line`. Check if any commit modifies that area in a way that
satisfies the reviewer's request.

**Step B: Compose the reply**

If a commit addresses it:
```
Addressed in <commit SHA> -- <brief description>.
```

If no commit addresses it, write a refutation (2-4 sentences). Read the file first -- do not
fabricate justifications.
```
<Technical explanation of why the current approach is correct.>
```

**Step C: Post the reply immediately**

```bash
gh api repos/{owner}/{repo}/pulls/{number}/comments \
  --method POST \
  -f body="<your reply>" \
  -F in_reply_to=<comment_id>
```

**Step D: Confirm the POST succeeded, then move to the next comment.**

Repeat steps A-D for every unaddressed comment. If there are 5 comments, you run 5 separate
POST calls.

### 6. Summary

After replying to all comments (individually, using `in_reply_to` for each one), output a
summary table FOR THE USER ONLY (do NOT post this table to GitHub):

```
| Comment | File | Action | Detail |
|---------|------|--------|--------|
| #123 | src/foo.ts:42 | Addressed | commit abc1234 |
| #456 | src/bar.ts:10 | Refuted | already validated upstream |
```

<CRITICAL>
This summary table is CLI output for the user.
DO NOT post this table as a GitHub comment.
DO NOT post any kind of "summary comment" to the PR.
</CRITICAL>

## Rules

- **ONE POST PER COMMENT. NO EXCEPTIONS.** Each review comment gets its own `gh api` POST with `in_reply_to`. If you post fewer `gh api` calls than there are unaddressed comments, you have failed. Never use `gh pr comment` or `gh pr review`.
- **Read before replying.** Always read the file and surrounding code before composing a refutation.
- **Never fabricate commits.** Only link to commits that actually exist on the PR.
- **Skip bot comments.** Ignore comments from bots (github-actions, dependabot, etc.).
- **Be concise.** Commit-addressed replies should be one line plus signature. Refutations should be 2-4 sentences max.
- **Ask if uncertain.** If a comment is ambiguous and you can't determine whether it's addressed, flag it for the user rather than guessing.
