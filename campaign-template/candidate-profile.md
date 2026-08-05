---
candidate_name: ""
office_sought: ""            # e.g. "Ohio House of Representatives, District 24"
jurisdiction: ""             # e.g. "Franklin County, OH"
election_date: ""            # ISO 8601, e.g. "2026-11-03"
incumbent: false
party: ""
campaign_site: ""
interview_date: ""           # ISO 8601 — when this interview happened
interviewer: ""              # who ran it
date_created: ""
date_modified: ""
status: draft                # draft | candidate-reviewed
---

# Candidate profile — [NAME]

Written by `candidate-profiler` from an interview. Every claim here traces to something the
candidate said or to a public record. Nothing here is inferred.

## Biography

Where they are from, how long in the district, family, current work, prior work. Facts a
reporter could check.

- [ ] Verified spellings of every proper noun
- [ ] Verified dates and job titles against LinkedIn, an employer page, or the candidate's
      own résumé

## Career and credentials

Roles, dates, licenses, degrees, certifications. Include the years. Omit anything the
candidate cannot document.

## Community roles

Boards, volunteer work, congregations, unions, coaching, mutual aid, PTA, neighborhood
associations. These matter more than they look — they are where standing on a local issue
comes from.

## Earned standing

**The highest-value section in this file.** What has this person's actual work and life
earned them the right to talk about that a generic candidate has not?

Format each entry as: **topic** — the specific experience that grants standing — and what
they can say that nobody else in the race can.

> A nurse can talk about emergency room wait times because she has worked them. A former code
> enforcement officer can talk about slumlords because he has written the citations. Borrowed
> passion reads as borrowed, and voters are unusually good at detecting it.

## Positions held

One entry per position. Do not include a position the candidate has not actually stated.

### [Topic]

- **Position:** what they would do, stated concretely enough to be wrong about
- **Conviction:** settled / leaning / thinking out loud
- **Reasoning, in their words:** a real quote from the interview
- **Would they say this at a hostile town hall?** yes / no / not sure
- **Source:** interview, [date] — or a public statement with a URL

## No position yet

**Load-bearing. This list is what stops every downstream skill from inventing an answer.**

**This file is where the list originates. It is not where writing skills read it.**
`positioning-builder` carries every entry here forward into `positioning.md`, and the writing
skills read it there — so an entry dropped in that hand-off silently becomes a topic the
campaign will fabricate a position on. Carrying a topic forward is the default; removing one
requires the candidate to have actually answered the question.

List every topic that came up where the candidate does not have a settled position. For each
one, write the specific question they need to answer before anyone writes about it.

- **[Topic]** — question to resolve: *[the specific question]*

An empty list here means the interview was not thorough enough. Every first-time candidate
has topics they have not worked through yet. Naming them is preparation, not weakness.

## Voice and register

How this person actually talks. Capture:

- Three to five verbatim phrases they used that sound like them
- Words they conspicuously avoid
- Reading level and sentence length of their natural speech
- Do they use humor? Numbers? Stories? Scripture? Sports?

Later skills write in this voice. Without this section they default to a national-consultant
register that no local voter has ever heard a neighbor use.

## Committee facts

Registration details, copied from the filing — never from memory and never inferred.
`positioning-builder` carries these into `## Boilerplate` in `positioning.md`, and every
placement that requires a disclaimer draws on them. A wrong committee name on a printed voter
guide statement is a compliance problem, not a typo.

- **Committee legal name:** [exactly as filed]
- **Committee ID:** [state or FEC number]
- **Required disclaimer text:** [verbatim from the state's rule, including punctuation]
- **Verified against:** [link to the filing, with retrieval date]
- **Profile URLs the candidate controls:** [campaign site, official directory profiles — used
  for `sameAs` markup. Only pages that genuinely describe this candidate.]

## Hard nos

Things the candidate stated flatly they will not do, say, or support. Record them verbatim,
with the reasoning if they gave one. These become `## Hard nos` in `positioning.md`, which is
the list every writing skill checks before drafting.

A hard no is different from a `no-position-yet` entry: the candidate has decided, and the
decision is negative. Do not soften one into the other.

- **[The thing]** — *"[what they said]"*

## Vulnerabilities the candidate named

What they expect to be attacked on, and what they say about it. Kept here so downstream
writing does not walk into it unaware. Not for publication.

## Open follow-ups

Questions the interview did not get to, or answers that were too vague to use.

- [ ] [question]
