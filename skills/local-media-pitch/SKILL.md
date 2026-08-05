---
name: local-media-pitch
description: Writes an outlet-specific cover email, story tip, interview offer, or document share after checking the pitch-type approval gate and the outlet's current acceptance rules. Uses fresh mechanics from campaign/district-media-map.md, never impersonates an independent source, and never sends. Use this for local press outreach or to route a candidate-approved op-ed/LTE placement to an outlet.
---

# Local Media Pitch

**Reads:** approved `campaign/positioning.md`; `campaign/district-media-map.md`; and either one
published answer/brief or one candidate-approved op-ed/LTE placement, as the routing table requires.
**Writes:** `campaign/pitches/<outlet>-<topic>.md`.

A pitch is not a press release with a salutation. It is one reporter, one story, one piece of
evidence they can check, and one ask small enough to say yes to in a hallway.

This skill owns outreach and cover copy. `placement-writer` owns the submission-ready op-ed or
LTE body. Do not duplicate that body in the cover-email field.

## Writes to journalists, never as them

No anonymous tips, supporter ghostwriting, "concerned parent" framing, or journalist voice.
Every pitch identifies the campaign and is signed by a named human with a real phone number.

## Output Format

Write to `campaign/pitches/<outlet>-<topic>.md` using
[`campaign-template/pitches/_template.md`](../../campaign-template/pitches/_template.md).
The frontmatter carries `outlet`, `reporter`, `reporter_email`, `beat`, `pitch_type`,
`source_artifact`, `word_limit`, `deadline`, `election_blackout_rule`, and lifecycle status
(`draft` | `candidate-approved` | `sent`). The body carries the recipient and rationale,
a subject line under 60 characters, the cover email, attachments or links, the self-check,
follow-up plan, and approval block.

`election_blackout_rule` is never blank. Either quote the rule with the URL where you found
it, or write "none published — confirmed with <name> on <date>."

## Routing and gates

| Pitch type | Required source | Position gate | Outlet gate | Output |
|---|---|---|---|---|
| Story tip | Published answer/brief at a live URL | If unresolved, facts only; no candidate stance | Outlet accepts tips and reporter covers the beat | Short attributed email linking the live artifact and primary record |
| Interview offer | Published answer/brief at a live URL | Topic is approved | Outlet accepts interview pitches and reporter covers the beat | Short attributed availability email |
| Document share | Published answer/brief at a live URL plus the described records | If unresolved, facts only; no candidate stance | Outlet/reporter accepts document tips | Short attributed email with records |
| Op-ed submission | Candidate-approved op-ed placement | Placement contains no missing-position marker | Outlet accepts candidate op-eds now | Cover email plus separate placement body/attachment |
| Letter to the editor | Candidate-approved LTE placement | Placement contains no missing-position marker | Outlet accepts candidate LTEs now | Cover email plus separate placement body/attachment |

For every type, `campaign/positioning.md` must be candidate-approved. An unknown position
stops op-eds, LTEs, and interview offers that would state a stance. A story tip or document
share may continue from a published factual brief only when the email states no candidate
position. This skill does not insert a marker into a single-topic email. Linked campaign
artifacts must be `published` and their URLs must load.

## Steps

1. **Apply the routing table first.** Select one eligible source. For direct op-ed/LTE
   submission, consume the candidate-approved placement from `placement-writer`; do not rewrite
   its body. For story tips, interview offers, and document shares, require a published
   answer/brief and live URL.
2. **For story tips, run the honest self-check now and record it in the file.**
   Ask: *is this actually news, or does the campaign just want coverage?* News is a new
   development, a public record nobody has reported, a decision with a date on it, or a
   consequence someone can point at. A candidate having an opinion is not news. **If the
   answer is "we want coverage," stop that story tip.** For other pitch types, apply the
   source, position, beat, and outlet-acceptance gates in the routing table.
3. **Use the media map before researching.** Match the artifact to the outlet using its
   citation-value ranking, not
   circulation. A nonprofit newsroom with 4,000 subscribers that covers the county commission
   beats a regional daily running wire copy, both for the reader and for what gets cited
   later. Reuse a complete row checked within the last 30 days. Recheck only fields that are
   missing, marked unverified, or older than 30 days; record the new source and check date.
4. **Use the route for the selected type.** Story tips, interview offers, and document shares
   go to one named beat reporter unless the outlet lists a dedicated intake. Op-eds go to the
   opinion route; LTEs go to the letters route. Never send the same pitch to multiple staff at
   one outlet.
5. **For reporter-routed pitches, read a recent relevant story and name it.** Record its URL
   and date. This step does not apply to a form-only opinion or letters intake.
6. **Verify that the outlet accepts this exact pitch type now.** Use fresh media-map mechanics;
   research only stale or incomplete fields. Required fields are acceptance of the type,
   recipient/route, word limit if applicable, exclusivity, deadline, and election-period rule:
   - **Word limit** — letters typically run a few hundred words and op-eds several hundred
     more, but the only number that counts is the one on that outlet's page. It is a hard
     limit, not a target. Count words, not characters.
   - **Exclusivity** — most op-ed desks require it. Submitting the same piece to two outlets
     in one market gets a campaign quietly blacklisted at both.
   - **Election-period restrictions on candidate copy** — many outlets stop running candidate
     letters and op-eds some number of weeks before an election, and campaigns get caught by
     this constantly. Read `election_date` from approved positioning, verify it, calculate any
     cutoff from that date, and record both the rule and calculated cutoff.
   - **Where it goes and who reads it** — the submission address is often not the newsroom
     address, and a form is often not optional.
7. **Write the cover email to the verified route.** Story tips should ordinarily stay under
   200 words; interview offers and document shares under 150. These are defaults, not limits on
   an op-ed/LTE body. For an op-ed or LTE, keep the cover email brief and place the
   candidate-approved body in the outlet-required separate field or attachment.
   Use five parts, in order: one sentence on what is
   happening and why it is news *now*; two or three sentences of specific evidence with the
   primary record linked — the ordinance, the minutes, the budget line, not the campaign's
   summary of them; what the campaign can provide (the candidate on the record, the underlying
   documents, a resident willing to talk); one concrete low-friction ask; then name, role,
   phone, email. Reporters read the first two sentences, so put the news in them.
8. **Check every fact against the source artifact.** Everything in the pitch is already
   sourced in the answer page or brief. If a number in the pitch is not in the artifact, one
   of the two is wrong. Never introduce a new claim in a pitch.
9. **Get human approval.** Show the candidate the exact cover email, separate placement body
   when applicable, recipient, and ask. Recheck recipient data only if stale or incomplete.
   Set `status: candidate-approved`. A named human sends it; this skill never sends.
10. **Follow up once.** One follow-up, one week later, one paragraph: the original ask,
    restated, plus anything new. Then stop. Record `sent_date` and the follow-up date in the
    activity log. Set `status: sent`, `sent_date`, and `sent_by` only after the named human
    confirms sending.

## When the media map is nearly empty

A `news_desert_assessment` of `thin` or `desert` is a real finding, and the honest response is
to send fewer pitches, not worse ones. Work outward in this order:

1. **The statewide nonprofit newsroom.** Most states now have one, they cover local government
   seriously, and down-ballot campaigns badly underuse them. Local nonprofit newsrooms carried
   substantial authority in the 2026 California primary
   ([Higher Ground](https://highergroundlabs.com/the-first-ai-midterms-early-signals-from-california/)),
   which makes them the highest citation value available in a desert.
2. **Regional dailies one county over** that occasionally cover this area — pitch them the
   pattern, not the incident. A single county's water rates are local; the same increase in
   four counties is regional.
3. **Wire services and state bureaus**, which pick up documented, verifiable stories from
   places nobody staffs.
4. **Trade and specialty press** — education, health, agriculture, utilities. A school board
   story that no daily wants may be exactly what an education outlet covers.

Then shift the weight. Where earned coverage does not exist, Ballotpedia, Vote411, forum
video, and the campaign's own source-of-record pages have to carry it. That is a
`canonical-presence` problem, not a media problem, and it deserves the hours the pitches would
have taken.

## Doing this without an agent

For freshness checks, outlet verification, pitch-type drafting, and human-send steps, follow the
full procedure in [`README.md`](README.md).

## Tips

**The subject line is the pitch.** Under 60 characters, says what the story is. "Jackson
County billed 340 households twice for stormwater" gets opened. "Candidate Marisol Vega
statement on utility fees" does not.

**One ask, and make it small.** "Fifteen minutes by phone Thursday or Friday" beats "we hope
you'll consider covering our campaign." A reporter can decline a vague ask without reading it.

**Link the record, not the press release.** Send the ordinance PDF, the minutes, the budget
line. Reporting is built on documents, and a campaign that supplies documents gets called
back. A campaign that supplies adjectives gets filtered.

**Never pitch two reporters at the same outlet.** They talk, and it reads as a mass mailing.
One reporter, and if there is no answer after the single follow-up, a different outlet.

**Timing beats volume.** A pitch tied to a meeting, a filing, or a decision that happens this
week has a reason to exist. The same pitch sent in a quiet week is a press release.

**Track what happens.** Record sent date, response, and outcome in the pitch file. Three
pitches with a note on each is a working relationship; thirty untracked emails is spam with
better intentions.
