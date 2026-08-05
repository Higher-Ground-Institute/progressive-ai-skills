# campaign-template

Copy this whole folder to start a campaign:

```bash
cp -r campaign-template/ ~/my-campaign/campaign/
```

Everything the nine campaign skills read and write lives in here. Plain Markdown with YAML
frontmatter — readable in a text editor, printable, diffable in git, and portable between
Claude Code, Cowork, and a volunteer with a laptop and no AI tool at all.

## What writes what

| File | Written by | Read by |
|---|---|---|
| `candidate-profile.md` | `candidate-profiler` | `positioning-builder` |
| `district-issues.md` | `district-issue-scan` | `positioning-builder`, `issue-brief` |
| `district-media-map.md` | `district-media-map` | `positioning-builder`, `local-media-pitch` |
| `positioning.md` | `positioning-builder` | **every writing skill** |
| `answers/*.md` | `answer-page` | `placement-writer`, `local-media-pitch` |
| `briefs/*.md` | `issue-brief` | `placement-writer`, `local-media-pitch` |
| `placements/*.md` | `placement-writer` | `canonical-presence` |
| `pitches/*.md` | `local-media-pitch` | — |
| `presence.md` | `canonical-presence` | — |

## The order to run them in

```
candidate-profiler ──┐
district-issue-scan ─┼─→ positioning-builder ─→ answer-page ─┬─→ placement-writer
district-media-map ──┘         (the contract)   issue-brief ─┘   local-media-pitch
                                                                 canonical-presence
```

The three research skills are independent of one another — run them in parallel, or on
different days, or hand two of them to volunteers.

Everything downstream of `positioning.md` reads `positioning.md`. Nothing downstream
re-derives the message from the profile. That is the rule that keeps a hundred pieces of
content sounding like one campaign.

## Before you go past positioning

`positioning.md` is the only artifact the candidate personally has to read, argue with, and
sign off on. Do not start writing answer pages until they have. Everything after that
checkpoint is execution, and execution based on positioning the candidate does not actually
agree with is worse than no content at all.

## The one field that stops the worst failure

`no-position-yet` in `positioning.md`. If a topic is on that list, every writing skill in
this repo refuses to write a position on it and asks you a specific question instead. Keep
that list honest. An empty `no-position-yet` list on a first-time campaign is not a sign of a
well-prepared candidate; it is a sign that somebody guessed.

See [`reference/shared-rules.md`](../reference/shared-rules.md) for the full rule set.
