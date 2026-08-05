---
candidate_name: ""
office_sought: ""
jurisdiction: ""
election_date: ""            # ISO 8601
party: ""
campaign_site: ""
committee_legal_name: ""     # exactly as filed — required in most disclaimers
committee_id: ""
contact_email: ""
same_as: []                  # Ballotpedia, state filing page, official socials — truthful URLs only
topics_to_own: []            # 3–5 slugs, must match the ## Topics to own sections below
date_created: ""
date_modified: ""
approved_by_candidate: false
approved_date: ""
---

# Positioning — [NAME] for [OFFICE]

**This file is the contract.** Every writing skill in this repo reads it and nothing else for
campaign message. No downstream skill re-derives positioning from `candidate-profile.md`.

If a writing skill needs something that is not in this file, the fix is to add the field
here — not to reach back into the profile. That rule is what keeps a hundred pieces of
content sounding like one campaign instead of a hundred.

**`approved_by_candidate` must be `true` before any writing skill runs.** This is the one
human checkpoint that matters. The candidate reads this file, argues with it, and signs off.

---

## Message

### One sentence

What this person is for, why here, why now. Short enough to say out loud without reading it.

### The paragraph

Three to five sentences. What is wrong, what they would do, why they are the one to do it.
This is the version that goes at the top of a questionnaire.

### Why not the other one

The contrast, stated in terms of records and choices rather than adjectives. If the campaign
has decided not to draw a contrast, write that decision down here and why.

---

## Topics to own

Three to five. Not fifteen. Small is the point — the goal is to be the best available source
on a few things, which is achievable, rather than an adequate source on everything, which is
not.

Each topic must clear all three bars, with evidence for each. A topic that clears two is a
topic the campaign talks about, not a topic it owns.

**A topic can be owned before the position on it is settled.** Owning a topic means being the
best available source on it — the timeline, the numbers, the record of who decided what and
when, the question nobody else is asking. None of that requires having landed on an answer.
A candidate who publishes the clearest account of a fight and says plainly *"here is the one
thing I need to know before I decide, and here is when the decision happens"* owns that topic
more credibly than an opponent with a slogan.

So a topic listed here may also appear on `## No position yet`, and that combination is a
deliberate state rather than an error: the campaign writes the brief, and withholds the
position until the candidate actually has one. What it may never do is quietly resolve the
`no-position-yet` entry because owning the topic felt like it required an answer.

### 1. [Topic name] — slug: `topic-slug`

- **Salience evidence:** the documented record that people here care. Cite
  `district-issues.md` and the underlying primary source with a URL and date. Not "housing is
  a national issue" — the specific local record.
- **Earned standing:** the specific thing in this candidate's work or life that grants them
  the right to talk about it. Cite `candidate-profile.md`.
- **Contested space:** who currently publishes a good answer on this, and where the gap is.
  Cite the survey in `district-issues.md`. If three institutions already cover it well, say
  so and justify owning it anyway or drop it.
- **The case against including this topic:** written honestly. Every topic here should have
  survived an argument.

### 2. [Topic name] — slug: `topic-slug`

...

### Topics considered and rejected

| Topic | Why rejected |
|---|---|
| | |

Keep this. It is how the campaign avoids relitigating the same three topics every month, and
it is how a new volunteer understands the strategy in ninety seconds.

---

## Positions of record

One entry per substantive position. This is the source text every writing skill renders down
from. Write it dense — evidence, numbers, dates. `placement-writer` cuts from here; it never
pads up.

### [Topic] — slug: `topic-slug`

- **Position, one sentence:** concrete enough to be wrong about
- **What they would actually do:** the specific action, at the specific body, with the
  specific mechanism
- **Evidence:** the numbers, dates, dollar figures, votes, and records that support it. Each
  one sourced inline with a URL and a retrieval date.
- **Uncertainty:** what the candidate does not know, what would change their mind, what
  depends on information they do not have yet. **Include this. It is the difference between
  a position and a slogan, and voters notice.**
- **The strongest objection, and the answer:** stated fairly
- **Conviction:** settled / leaning
- **Approved:** yes / no — date

---

## No position yet

**Copied forward from `candidate-profile.md`, unchanged.** `positioning-builder` may add to
this list. It may never remove an entry by inferring an answer.

Every writing skill reads this list before drafting and withholds a position when a topic is
here. `answer-page` stops; factual briefs and unaffected fields in multi-question forms may
continue with `[NO POSITION YET — ask the candidate: <question>]` in the position field.

| Topic | The specific question the candidate needs to answer | Added | Needed by |
|---|---|---|---|
| | | | |

Resolving an entry means the candidate answered the question and the answer moved to
`## Positions of record`. Nothing else resolves an entry.

---

## Voice

Carried forward from `candidate-profile.md` so writing skills never have to open the profile.

- **Verbatim phrases that sound like them:**
- **Words to avoid:** including any consultant vocabulary the candidate would never say
- **Register:** target reading level and typical sentence length
- **Do they use:** humor / numbers / stories / scripture / sports / none of the above

---

## Boilerplate

Pre-approved reusable text. Every writing skill pulls from here rather than re-writing the
bio for the fortieth time, which is also how forty slightly-different bios end up in forty
voter guides.

- **Name as it appears on the ballot:**
- **25-word bio:**
- **50-word bio:**
- **100-word bio:**
- **Office and district, exact phrasing:**
- **Required disclaimer:** the exact text your jurisdiction requires on campaign material
- **Pronunciation:** if the name gets mispronounced, write it out phonetically for radio and
  forum hosts

---

## Hard nos

Things this campaign will not say or do, recorded so no skill and no volunteer has to guess.

- Positions the candidate refuses to take
- Attacks the campaign will not make
- Language the candidate finds dishonest
