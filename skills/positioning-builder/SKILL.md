---
name: positioning-builder
description: Builds the campaign's message contract at campaign/positioning.md by selecting three to five topics the campaign will own, each of which must clear documented salience, earned candidate standing, and contested space with cited evidence rather than assertion. Argues against every topic before keeping it, records the ones it rejected, carries the no-position-yet list forward unchanged without ever resolving an entry by inference, and verifies the file supplies every input downstream writing skills need. Use this when a campaign needs to decide what it stands for, pick the issues it will run on, turn a candidate interview and district research into a usable message, or produce the single artifact the candidate signs off on before any content gets written.
---

# Positioning Builder

**Reads:** `campaign/candidate-profile.md`, `campaign/district-issues.md`,
`campaign/district-media-map.md` — all three required.
**Writes:** `campaign/positioning.md`, using
[`campaign-template/positioning.md`](../../campaign-template/positioning.md).

This file is the contract. Every writing skill in this repo reads it and nothing else for
campaign message. If a downstream skill needs something positioning does not carry, the fix is
to add the field here — never to reach back into the profile. That rule is the only reason a
hundred pieces of content sound like one campaign.

Get this file right and the rest of the work is execution. Get it wrong and you will produce
forty polished pages about the wrong four things.

## The three bars, each with evidence

Three to five topics. Each must clear all three bars **with a citation, not an assertion.** A
topic that clears two is a topic the campaign talks about. It is not a topic the campaign owns.

**1. Salience — people here demonstrably care.** Cite the entry in `district-issues.md` *and*
the primary record underneath it: the public-comment count in the minutes, the contested vote
with its tally, the rate increase with its dollar figure and effective date. "Housing is a big
issue" is not salience evidence. "Forty-one speakers at the March 4 hearing" is.

**2. Candidate fit / earned standing — the topic sits on this person's actual life.** Cite
`candidate-profile.md`. A nurse owns emergency-room wait times because she has worked them. A
former code-enforcement officer owns slumlords because he has written the citations. Borrowed
passion reads as borrowed, and voters detect it faster than consultants believe.

Standing is also the only one of the three bars a challenger cannot copy. An opponent can
out-spend the campaign on any topic and can move onto any salient issue, but they cannot acquire
twenty years of night shifts. This is why fit is a defense and not a nicety.

**3. Contested space — nobody currently provides a good answer.** Cite the contested-space
survey in `district-issues.md`. Owning a topic that three institutions already cover well is
expensive and pointless. Owning one where the honest answer does not exist anywhere is nearly
free. Check the incumbent's site, the county's own explainer pages, and the outlets in
`district-media-map.md` before concluding the space is empty.

## Argue against every topic before you keep it

The failure mode of this skill is a friendly list of nine topics that all sound reasonable. Nine
topics is zero topics. Nobody is the best available source on nine things.

For each candidate topic, **write the strongest honest case for cutting it** and record that
case in the file under `**The case against including this topic:**`. Not a straw man — the
argument a smart, hostile campaign manager would make. Then decide. A topic that survives a real
argument belongs; a topic nobody could argue against was never examined.

Every topic that does not survive goes in the `### Topics considered and rejected` table with
the reason. Keep that table. It stops the campaign relitigating the same three topics every
month and it explains the strategy to a new volunteer in ninety seconds.

**When the campaign asks for more topics, push back.** Ask which existing topic they want to
drop. The answer is usually "none," which is the answer that produces a campaign with no
identity. Five is the ceiling and four is usually better.

## The `no-position-yet` list carries forward unchanged

From [`reference/shared-rules.md`](../../reference/shared-rules.md) Rule 1:

> `candidate-profiler` creates the `no-position-yet` list. `positioning-builder` carries it
> forward unchanged — it may add to the list, but it may never resolve an entry by inference.
> Every writing skill reads it before drafting.

**The hard rule: this skill may ADD entries. It may NEVER resolve one.** Not from the
candidate's party, not from their biography, not from adjacent positions in the file, not from
what similar candidates say. The only thing that resolves an entry is the candidate answering
the specific question in that row, after which the answer moves to `## Positions of record`.

Why this is stated so bluntly: every downstream skill trusts this list. `answer-page`,
`issue-brief`, `placement-writer`, and `local-media-pitch` all check it before drafting and
refuse to write when a topic appears on it. If positioning quietly infers one position, that
fabrication is published under the candidate's name across every venue at once. The list is the
single mechanism preventing that, and it only works if nothing is allowed to soften it.

If working through the three bars surfaces a topic the candidate has not thought through, add a
row with the specific question. That is a good outcome, not a delay.

## Output Format

Write `campaign/positioning.md` following the template field for field: frontmatter through
`approved_by_candidate`, then `## Message` (one sentence, the paragraph, why not the other one),
`## Topics to own` with `### Topics considered and rejected`, `## Positions of record`,
`## No position yet`, `## Voice`, `## Boilerplate`, `## Hard nos`.

Set `approved_by_candidate: false` and leave it there. Only a human flips it.

## The completeness check

`positioning.md` must supply every downstream input **without anyone opening
`candidate-profile.md`.** Before finishing, verify each of these is present and filled:

- [ ] `## Voice` — verbatim phrases, words to avoid, register, whether they use humor, numbers,
      stories, scripture, sports
- [ ] Boilerplate bios at 25, 50, and 100 words
- [ ] Name exactly as it appears on the ballot
- [ ] Office and district, exact phrasing
- [ ] Required disclaimer text for this jurisdiction, verbatim
- [ ] `committee_legal_name` exactly as filed
- [ ] `same_as` URLs — Ballotpedia, state filing page, official socials, truthful only
- [ ] Pronunciation, written out phonetically
- [ ] `## Hard nos` — positions refused, attacks the campaign will not make, dishonest language
- [ ] Every topic in `topics_to_own` has a matching section and a `## Positions of record` entry
- [ ] `## No position yet` carried forward with every original row intact

Any unchecked box is a defect that surfaces later as a writing skill inventing something.
`[NEEDS SOURCE — <what to look up>]` is an acceptable placeholder; a missing field is not.

## Steps

1. **Read all three inputs end to end** before writing anything. Read `district-media-map.md`
   too — it tells you which topics the local press already covers well.
2. **List every plausible topic** where profile and issue scan overlap — expect eight to twelve.
3. **Score each against the three bars,** writing the citation for each bar as you go. A bar you
   cannot cite is a bar the topic fails.
4. **Write the case against each survivor.** Cut on the strength of that case, not on comfort.
5. **Keep three to five.** Put the rest in the rejected table with reasons.
6. **Write `## Positions of record`** for each kept topic: position in one sentence, the
   specific action at the specific body, the evidence with inline sources and retrieval dates,
   the uncertainty, the strongest objection and the answer, conviction, approval status.
7. **Copy `## No position yet` forward verbatim** and add any new rows.
8. **Fill `## Voice`, `## Boilerplate`, and `## Hard nos`** from the profile.
9. **Run the completeness check** above.
10. **Get candidate approval.** Copied from Rule 4:

    > This skill never submits, posts, publishes, or sends anything. It produces a draft and
    > the exact instructions for a human to submit it.
    >
    > End with an explicit approval step: show the human what will be published, where, and
    > what is irreversible about it. Wait for them to say yes. Then hand them the submission
    > instructions.

    **This is the one human checkpoint that matters.** Not the individual pages — this file. The
    candidate reads it, argues with it, and signs off. Sit with them and go topic by topic. Ask
    on each one: *would you still be saying this in October, at a forum, badly outspent?* When
    they say yes to the whole file, set `approved_by_candidate: true` and `approved_date`.
    Nothing downstream runs until it is true.

## Doing this without an agent

Printouts of the three input files, a pen, and about three hours with the candidate in the room
for the last one.

1. Print `candidate-profile.md` and `district-issues.md`. Get index cards.
2. One card per plausible topic. Write the topic name at the top. Eight to twelve cards.
3. Draw three boxes on each card: **Salience**, **Standing**, **Contested**.
4. In the salience box, write the single strongest piece of local evidence and the page of the
   issue scan it came from. If you cannot write a number, a date, or a vote count, leave the box
   empty. An empty box is the answer.
5. In the standing box, write the specific thing in this person's life that earns the topic. Not
   "she cares about schools" — "she was the PTA treasurer who found the accounting error." If
   you have to reach, leave it empty.
6. In the contested box, search the topic plus the place name and spend ten minutes reading what
   comes back. Write who already answers it well. "Nobody" is the best possible entry.
7. Sort the cards into three piles: three full boxes, two full boxes, fewer. Only the three-box
   pile is eligible.
8. Take each eligible card and write on the back the best argument for throwing it away. Read it
   out loud to someone else. Some cards will not survive this and that is the point.
9. Keep three to five. Copy the rejected ones into the rejected table with the reason.
10. Copy the `## No position yet` list from the profile word for word. **Do not fill in an
    answer, even one you are sure of.** If the candidate has not said it, it does not exist.
11. Type it all into the template. Walk the completeness checklist and fill every gap.
12. Sit down with the candidate and read the file aloud, topic by topic. Change what they argue
    with. When they agree to all of it, write the date on the front page and set
    `approved_by_candidate: true`.

## Tips

**When fit and salience do not overlap.** The hardest real case: Cordwell County is fighting
about sewer rates and the candidate, Marisol Vega, is a pediatric nurse. Do not fake standing
and do not abandon the salient issue. Take a position on it, put it in `## Positions of record`,
and keep it out of `topics_to_own` — the campaign answers sewer questions without pretending to
own them. Then look for the seam. A nurse who has watched families choose between a utility bill
and a prescription has documented standing on affordability, which is the actual fight
underneath rates. A seam you can document is fine. A seam you have to invent is not.

**When the candidate insists on a topic that fails contested space.** Show them the survey. Ask
what they would add that the three existing sources do not already say. If they have a genuine
answer, the space was not as covered as the survey thought — go re-check it. If they do not,
keep the topic as a position of record and spend the campaign's writing time elsewhere. This is
usually a fight about identity, not strategy, and naming that ends it faster.

**When there are only two viable topics.** Publish two. Two topics owned completely beat five
covered adequately, and a small district may genuinely only have two live fights. Write the thin
finding into the file so nobody spends October hunting for a third.

**When the candidate's honest position is unpopular.** Record it, with the strongest objection
and a fair answer, and mark conviction `settled`. Do not soften it in positioning — that
guarantees forty pieces of hedged content downstream. Whether to lead with it is a separate
decision; note it in `## Hard nos` if the answer is no.

**Positions of record can outnumber topics to own.** A campaign needs a defensible position on
the school levy whether or not it owns education. Owning is about where the writing time goes.
