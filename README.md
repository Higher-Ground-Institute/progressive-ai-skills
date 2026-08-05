# Progressive AI Skills Repository

A curated collection of tested, ready-to-use AI skills for campaigns, organizing, and progressive infrastructure. Each skill is a drop-in automation for [Claude Code](https://docs.anthropic.com/en/docs/claude-code) or [Cowork](https://claude.ai) that handles a specific, common task.

Built and maintained by [Higher Ground Institute](https://highergroundlabs.com).

## What is a "skill"?

A skill is a SKILL.md file -- a set of instructions that tells Claude exactly how to handle a specific task. Drop it into your Claude Code or Cowork setup, and it just works. No coding required.

Think of it like a recipe: instead of explaining from scratch every time you want meeting notes summarized or a resource formatted, the skill handles the process automatically with consistent, high-quality output.

## Browse skills

Visit **[progressive-ai-skills]([https://higher-ground-institute.github.io/progressive-ai-skills/](https://aicampaignstack.org/skills))** in HGI's AI Campaign Stack to search, filter, and copy skills without needing a GitHub account.

Or browse the folders below:

| Skill | What it does | Category |
|-------|-------------|----------|
| [resource-formatter](skills/resource-formatter/) | Formats URLs into styled entries for the HGL AI Resource Guide | Content & Comms |
| [meeting-notes-to-actions](skills/meeting-notes-to-actions/) | Extracts decisions, action items, and follow-ups from meeting notes or transcripts | Operations |
| [event-recap-generator](skills/event-recap-generator/) | Turns event/webinar notes or transcripts into shareable recaps | Content & Comms |
| [contact-extractor](skills/contact-extractor/) | Scans Gmail on a schedule and builds a deduplicated contact spreadsheet | Operations |
| [linkedin-connector](skills/linkedin-connector/) | Finds recent meeting attendees worth connecting with on LinkedIn | Operations |
| [confess](skills/confess/) | Honest audit of AI output — confidence levels, shortcuts, assumptions, and weakest parts | Meta & Process |
| [brown-mm](skills/brown-mm/) | Catches every error after you spot the first one. When you find a mistake in Claude's output, Brown M&M runs a four-pass audit — fact verification, internal consistency, logic review, and a fresh-eyes re-read — then delivers a corrected version with a full accounting of what it found. Based on Van Halen's famous brown M&M test: one small failure is a reliable signal that others are hiding. Works on any output type: emails, code, reports, research, plans. | Meta & Process |

### For candidates — the campaign message set

Nine skills that take a first-time, down-ballot candidate from an interview to a position of
record published where voters and AI answer engines will actually find it. They compose in
order, they share one campaign folder, and **every one of them works as a written procedure a
volunteer can follow with no AI tool at all.**

| # | Skill | What it does | Category |
|---|-------|-------------|----------|
| 1 | [candidate-profiler](skills/candidate-profiler/) | Interviews the candidate and writes the profile of record — including what they have *no* position on yet | Research & Data |
| 2 | [district-issue-scan](skills/district-issue-scan/) | Finds what people in one specific place actually argue about, from meeting records and primary sources | Research & Data |
| 3 | [district-media-map](skills/district-media-map/) | Builds a working contact map of who covers this place, ranked by citation value rather than circulation | Research & Data |
| 4 | [positioning-builder](skills/positioning-builder/) | Picks the three to five topics the campaign will own, and argues against each one before keeping it | Content & Comms |
| 5 | [answer-page](skills/answer-page/) | Writes one dated, sourced position page that answers the question in its first paragraph | Content & Comms |
| 6 | [issue-brief](skills/issue-brief/) | Writes the best available reference on one narrow local issue — useful to someone who will never vote for you | Content & Comms |
| 7 | [placement-writer](skills/placement-writer/) | Renders a position down to fit Ballotpedia, Vote411, a state statement, or an op-ed. Never submits | Content & Comms |
| 8 | [canonical-presence](skills/canonical-presence/) | Audits the site for crawlability, then triages every venue by open / closed / always open | Content & Comms |
| 9 | [local-media-pitch](skills/local-media-pitch/) | Pitches a reporter with the right story, the right rules, and the campaign's own name on it | Content & Comms |

**Start here:** copy [`campaign-template/`](campaign-template/) and run 1, 2, and 3 in any
order. They converge on `positioning.md`, which is the one artifact the candidate personally
signs off on. Everything after that is execution.

**Why these refuse things.** A model asked what a candidate thinks about anything will produce
a confident answer, and that answer published under the candidate's name is a fabrication. So
these skills will not write a position on a topic the candidate has not taken one on, will not
generate a page per search phrasing, will not draft anonymous posts or edit Wikipedia, and will
not submit anything to any venue. Declining is a passing result, and the eval suites test for
it. See [`reference/shared-rules.md`](reference/shared-rules.md).

Supporting material: [`reference/`](reference/) for the research these are built on,
[`evals/`](evals/README.md) for how the eval suites run, and [`golden/`](golden/) for real
district research used as reference output.

## How to use a skill

**In Cowork (Claude desktop app):**
1. Open the skill folder and copy the SKILL.md file
2. Place it in your Cowork skills directory
3. The skill will automatically activate when you do the relevant task

**In Claude Code:**
1. Create a `.claude/skills/` directory in your project (or use your global skills path)
2. Copy the SKILL.md file into a subfolder there
3. Claude Code will pick it up and use it when relevant

**Manual use (any Claude interface):**
1. Copy the contents of the SKILL.md file
2. Paste it at the start of your conversation as context
3. Proceed with your task -- Claude will follow the skill's instructions

## Categories

Skills are organized by what kind of work they support:

- **Content & Comms** -- writing, formatting, social media, newsletters
- **Operations** -- meeting notes, project tracking, internal workflows
- **Research & Data** -- lookups, data extraction, analysis
- **Field & Organizing** -- volunteer management, event coordination, outreach
- **Training & Onboarding** -- guides, templates, learning resources
- **Meta & Process** -- working with AI effectively, quality checks, workflow patterns

## Contributing

We want skills from practitioners -- the people actually doing the work. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to submit a skill or request one.

**Quick version:**
- **Submit a skill:** Open a PR with your SKILL.md in a new folder under `skills/`
- **Request a skill:** [Open an issue](../../issues/new?template=skill-request.yml) describing what you need
- **Report a problem:** [Open an issue](../../issues/new?template=bug-report.yml) with what went wrong

## Quality standards

Every skill in this repo has been tested and meets these criteria:

- **It works.** Tested with real data, not just hypothetical inputs.
- **It's specific.** Solves one clear task, not a vague category of work.
- **It's documented.** README explains what it does, who it's for, and how to use it.
- **It's practical.** Built for the kind of work progressive orgs actually do.

### Validation

Structural checks run on every pull request — no model calls, no API key, a couple of seconds:

```bash
python3 scripts/validate_skills.py
```

It enforces the [Agent Skills](https://agentskills.io/specification.md) frontmatter and naming
rules (including that `name` must match the parent directory), checks that relative links
resolve and that `evals.json` parses, and greps eval fixtures for anything shaped like real
personal data. See [`evals/README.md`](evals/README.md) for the eval format and how to run it.

## License

MIT -- use these however you want. Attribution appreciated but not required.

## Contact

Questions, ideas, or want to get involved? Reach out to kate@cooperativeimpactlab.org or join us at an upcoming [AI Study Hall or Open Mic](https://highergroundlabs.com).
