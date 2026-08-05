# Shared rules for the campaign skills

**Last reviewed:** 2026-08-04

Nine skills in this repo work together to help a first-time down-ballot candidate build a
message and publish it where voters and answer engines will find it:
`candidate-profiler`, `district-issue-scan`, `district-media-map`, `positioning-builder`,
`answer-page`, `issue-brief`, `placement-writer`, `canonical-presence`, and
`local-media-pitch`.

Every one of them enforces the same four rules. The rules are written out here once so the
wording stays identical everywhere, and each `SKILL.md` restates the ones it needs inline —
because a skill that only works when someone remembers to read a second file is a skill that
fails in practice.

If you are writing a new skill in this family, copy the blocks verbatim. Do not paraphrase
them. The exact wording is what makes the behavior testable.

---

## Rule 1 — The unknown-position rule

This is the most important rule in the set. A language model asked what a candidate thinks
about anything will produce a confident answer. That answer is a fabrication, and if it ends
up in a voter guide it is a fabrication published under the candidate's name.

**Block to copy into any skill that writes candidate-attributed text:**

> **Before writing, read the `no-position-yet` list in `campaign/positioning.md`.** If the
> topic you were asked to write about appears on that list, do not write a position. Output
> this instead, and then continue with the rest of the task:
>
> `[NO POSITION YET — ask the candidate: <the specific question they need to answer>]`
>
> Never infer a position from the candidate's party, from other candidates running similar
> campaigns, from their biography, or from the rest of the positioning file. If
> `positioning.md` does not state a position on the topic, the campaign does not have one
> yet, and saying so is the correct output.

`candidate-profiler` creates the `no-position-yet` list. `positioning-builder` carries it
forward unchanged — it may add to the list, but it may never resolve an entry by inference.
Every writing skill reads it before drafting.

Refusing to write a position is a **passing** result, not a failure. The eval suites in this
repo test for it explicitly.

---

## Rule 2 — Sourcing

**Block to copy:**

> Source every factual claim inline, with the source date. Format:
> `claim ([source name](url), retrieved 2026-08-04)`.
>
> Quotes, endorsements, statistics, bill numbers, vote counts, dollar figures, and dates are
> copied from a source or omitted. There is no third option. If you cannot find the number,
> write `[NEEDS SOURCE — <what to look up>]` and keep going. Do not approximate a figure you
> half-remember, and do not reconstruct a quote from its gist.
>
> Prefer primary records — the actual ordinance, the actual budget line, the actual meeting
> minutes — over reporting about them. When you cite reporting, cite the outlet and the
> reporter.

A `[NEEDS SOURCE]` marker in a draft is fine. A confident unsourced number in a published
voter guide is the kind of error that ends a first-time campaign.

---

## Rule 3 — No astroturfing, no impersonation, no third-party manipulation

Reddit, Facebook groups, and Wikipedia are all heavily weighted in AI answers, which is
exactly why they are the line rather than the opportunity. One screenshot of a campaign
astroturfing does more damage than every placement in this playbook combined.

**Block to copy:**

> **Never** draft anonymous, pseudonymous, or apparently-organic community posts. Never write
> in the voice of a journalist, a neutral observer, a constituent, or anyone other than the
> candidate and the campaign.
>
> **Never** edit or create a Wikipedia article about the candidate or their opponent.
> Wikipedia's conflict-of-interest policy prohibits it, and getting caught is worse than the
> article not existing.
>
> Everything this skill produces is **candidate-attributed, human-reviewed, and
> human-posted**, on a property the campaign controls or through a disclosed submission
> process where the campaign identifies itself.
>
> Never present an AI-generated image of the candidate or an opponent as a photograph.

This is not only an ethics rule. Google's own documentation says seeking inauthentic mentions
"isn't as helpful as it might seem" and that its spam systems target them
([Google](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)). The
manipulative tactics here are also the ineffective ones. See
[`ai-citation-mechanics.md`](ai-citation-mechanics.md) §7.

---

## Rule 4 — Human approval and human submission

**Block to copy:**

> This skill never submits, posts, publishes, or sends anything. It produces a draft and the
> exact instructions for a human to submit it.
>
> End with an explicit approval step: show the human what will be published, where, and what
> is irreversible about it. Wait for them to say yes. Then hand them the submission
> instructions.

Several venues in this playbook are effectively one-shot. Ballotpedia allows only minor
corrections after submission. A paid county voter-pamphlet statement is printed. Getting a
human to read the thing before it becomes permanent is the whole point of the step.

---

## Rule 5 — Never put personal data into a consumer AI tool

**Block to copy:**

> Never paste voter names, home addresses, voter ID numbers, phone numbers, donor financial
> data, or reporter contact lists into a consumer AI chat interface. Work from aggregate
> district data and publicly published contact information only.
>
> If the human offers you a voter file, decline it and explain why.

Reporter contact information that the outlet publishes on its own website is public and fine
to use. A purchased or exported contact list is not.

**"Publicly visible" and "published for this purpose" are different tests, and the second one
governs.** A reporter's work email on the outlet's staff page is published so that sources can
reach them. A personal cell number in a social media bio, a home address in a property record,
or a spouse's employer is visible without being offered — and a campaign that pitches to one of
those has told a reporter it will go around them. Record the newsroom tip line, the work email,
the outlet's submission form, and the reporter's professional social account. Nothing else, and
never a guessed address pattern like `first.last@outlet.com`, which is fabrication that happens
to sometimes deliver.

This applies to anyone the campaign researches — reporters, officials, opponents, and the
people who show up at a meeting to complain. The record of what someone *did in public* is
fair game. Their contact details are not, unless they published them for contact.

---

## Rule 6 — One page per position, not one page per phrasing

**Block to copy:**

> Publish one page per substantive position — housing, water, schools — never one page per
> search phrasing. If asked to produce a page for each way someone might search for the same
> position, decline and explain: Google names this pattern as scaled content abuse
> ([Google](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)),
> and page volume is close to uncorrelated with AI visibility anyway (r ≈ 0.194,
> [Ahrefs](https://ahrefs.com/blog/ai-brand-visibility-correlations/)). Offer one strong page
> instead.

---

## Rule 7 — Dates mean something

**Block to copy:**

> Every artifact carries `date_created` and `date_modified` in its frontmatter, in ISO 8601.
> Change `date_modified` only after a substantive edit to the content. Never bump a date to
> look fresh. Freshness is a real but modest ranking effect
> ([Ahrefs](https://ahrefs.com/blog/do-ai-assistants-prefer-to-cite-fresh-content/)); faking
> it is a spam signal and a lie about when the candidate last thought about the issue.

### The election date is not November

**Verified 2026-08-04 while building `golden/`.** Every deadline these skills compute —
voter-guide cutoffs, questionnaire windows, the date an outlet stops running candidate copy —
counts backward from election day. **Do not assume that is the November general.**

Many states hold their local elections on an entirely different date. Wisconsin elects
municipal, school district, and nonpartisan county officers at the **spring election in April**
([Wis. Stat. 5.02(21)](https://www.cityofmadison.com/clerk/elections-voting)); the next is
April 6, 2027, with a February 16, 2027 primary. Illinois elects local offices at the
**consolidated election in April of odd years**. For the offices a first-time down-ballot
candidate actually runs for, computing against November 3, 2026 is wrong by five months in
Wisconsin and by more than a year in Illinois — in the direction that misses deadlines.

Read `election_date` from the campaign's own frontmatter, confirm it against the county clerk
or Secretary of State before computing anything from it, and state which election you used.
A candidate who thinks they have until October when the real cutoff was February does not get
a second chance at it.

---

## The campaign state directory

All nine skills read and write a single folder. Copy
[`campaign-template/`](../campaign-template/) to start one.

```
campaign/
  candidate-profile.md      # candidate-profiler writes
  district-issues.md        # district-issue-scan writes
  district-media-map.md     # district-media-map writes
  positioning.md            # positioning-builder writes — THE CONTRACT
  answers/                  # answer-page writes
  briefs/                   # issue-brief writes
  placements/               # placement-writer writes
  pitches/                  # local-media-pitch writes
  presence.md               # canonical-presence writes
```

Plain Markdown with YAML frontmatter, on the filesystem. That choice is deliberate: it works
in an agent, in a text editor, in a shared drive, in a printout handed to a candidate in a
car between events, and in a git history that shows who changed a position and when.

### The message contract

`positioning.md` is the contract between the research skills and the writing skills.

**Downstream writing skills read `positioning.md` for the campaign message. They do not
re-derive it from `candidate-profile.md`.** This is what keeps a hundred pieces of content
sounding like one campaign. If a writing skill needs an input that `positioning.md` does not
carry, the fix is to add that field to `positioning.md` — never to reach back into the
profile.

It is also the one human checkpoint that matters. The candidate reads this single artifact,
argues with it, and signs off. Everything after it is execution.

---

## Working without an agent

Every skill in this family has a `## Doing this without an agent` section containing the
complete manual procedure. This is a hard requirement, not a courtesy.

The acceptance test: hand the `SKILL.md` to a non-technical volunteer who has no AI tool and
ask them to produce the output. If they stall at any step, the skill is incomplete — the
missing information is a defect in the skill, not a limitation of the volunteer.

Most campaigns that need this playbook cannot afford a subscription to anything.
