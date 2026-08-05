---
name: local-media-pitch
description: Writes one outlet-specific, reporter-specific pitch built on a published campaign answer page or issue brief — story tip, op-ed submission, letter to the editor, interview offer, or document share — after verifying that outlet's word limit, exclusivity terms, election-period restrictions on candidate copy, deadline, and submission address. Refuses to draft anything anonymous or written in the voice of anyone other than the campaign, and refuses to send a pitch that fails the is-this-actually-news test. Reads campaign/district-media-map.md and writes campaign/pitches/. Use this when a campaign wants local press coverage, wants to submit an op-ed or a letter to the editor, has a document or public record a reporter should see, or asks how to get a story written about an issue it has published on.
---

# Local Media Pitch

**Reads:** `campaign/district-media-map.md` (required) plus exactly one
`campaign/answers/<slug>.md` or `campaign/briefs/<slug>.md`.
**Writes:** `campaign/pitches/<outlet>-<topic>.md`.

A pitch is not a press release with a salutation. It is one reporter, one story, one piece of
evidence they can check, and one ask small enough to say yes to in a hallway.

The pitch exists because the campaign already published something. If there is no answer page
or brief behind it, stop and write that first — a pitch with nothing to link to is an email
asking a reporter to do the campaign's work.

## Writes to journalists, never as them

From [`reference/shared-rules.md`](../../reference/shared-rules.md) Rule 3, verbatim:

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

In practice: no anonymous tips, no letters drafted for a supporter to sign as their own words,
no "concerned parent" framing, no pretending to be an unaffiliated source. Every pitch is
signed by a named human at the campaign with a real phone number.

## Output Format

Write to `campaign/pitches/<outlet>-<topic>.md` using
[`campaign-template/pitches/_template.md`](../../campaign-template/pitches/_template.md).
The frontmatter carries `outlet`, `reporter`, `reporter_email`, `beat`, `pitch_type`,
`source_artifact`, `word_limit`, `deadline`, `election_blackout_rule`, `status`, `sent_date`,
and `sent_by`. The body carries: who this is going to and why, a subject line under 60
characters, the email itself, what is attached or linked, the honest self-check, the
follow-up plan, and the approval block.

`election_blackout_rule` is never blank. Either quote the rule with the URL where you found
it, or write "none published — confirmed with <name> on <date>."

## Steps

1. **Pick the artifact first.** One answer page or brief, already published on the campaign
   site at a live URL. If it is still a draft, the pitch waits.
2. **Run the honest self-check now, not at the end, and record the answer in the file.**
   Ask: *is this actually news, or does the campaign just want coverage?* News is a new
   development, a public record nobody has reported, a decision with a date on it, or a
   consequence someone can point at. A candidate having an opinion is not news. **If the
   answer is "we want coverage," do not send it.** Say so and stop. A reporter remembers who
   wastes their time, and one wasted pitch costs the next three.
3. **Match the artifact to the outlet** using the citation-value ranking in the media map, not
   circulation. A nonprofit newsroom with 4,000 subscribers that covers the county commission
   beats a regional daily running wire copy, both for the reader and for what gets cited
   later. Check the paywall column: coverage nobody can read is worth less.
4. **Match the outlet to one reporter.** Named, on the beat, currently working there. Not the
   general tip line, not four reporters at once, not the editor unless the media map says the
   editor is the intake.
5. **Read a recent story by that reporter and name it in the pitch.** This is required, not
   polite. "You covered the rate increase in March; this is what happened at the September
   meeting" is a pitch. "You cover Jackson County" is a mailing list. Record the story's URL
   and date in the file.
6. **Verify the submission mechanics before drafting**, from the outlet's own page, with the
   URL and the date you checked:
   - **Word limit** — letters typically run a few hundred words and op-eds several hundred
     more, but the only number that counts is the one on that outlet's page. It is a hard
     limit, not a target. Count words, not characters.
   - **Exclusivity** — most op-ed desks require it. Submitting the same piece to two outlets
     in one market gets a campaign quietly blacklisted at both.
   - **Election-period restrictions on candidate copy** — many outlets stop running candidate
     letters and op-eds some number of weeks before an election, and campaigns get caught by
     this constantly. Find the exact rule and the exact cutoff date, counting back from
     November 3, 2026, and put that date in the campaign calendar the day you find it.
   - **Where it goes and who reads it** — the submission address is often not the newsroom
     address, and a form is often not optional.
7. **Choose the pitch type**, which changes the shape but never the honesty:

   | Type | What it is | Typical length | Goes to |
   |---|---|---|---|
   | Story tip | Here is a development you should look at | Under 200 words | The beat reporter |
   | Op-ed submission | Candidate-bylined argument | The outlet's limit, exactly | The opinion editor |
   | Letter to the editor | Short response to something published | The outlet's limit | The letters address |
   | Interview offer | Candidate available on a specific topic | Under 150 words | The beat reporter |
   | Data / document share | Here are the primary records, no strings | Under 150 words | The beat reporter |

   **The document share is the underrated one.** A campaign that hands a reporter the four
   years of billing data it pulled from county records, organized, with no demand attached,
   becomes a source instead of a supplicant. The reporter may write nothing this month and
   call first the next three times. Send it anyway.
8. **Write the email. Under 200 words.** Five parts, in order: one sentence on what is
   happening and why it is news *now*; two or three sentences of specific evidence with the
   primary record linked — the ordinance, the minutes, the budget line, not the campaign's
   summary of them; what the campaign can provide (the candidate on the record, the underlying
   documents, a resident willing to talk); one concrete low-friction ask; then name, role,
   phone, email. Reporters read the first two sentences, so put the news in them.
9. **Check every fact against the source artifact.** Everything in the pitch is already
   sourced in the answer page or brief. If a number in the pitch is not in the artifact, one
   of the two is wrong. Never introduce a new claim in a pitch.
10. **Get human approval.** Show the candidate the exact text, the recipient, and the ask.
    Confirm the reporter's name, outlet, and email are still current today — beat reporters
    move constantly. Set `status: candidate-approved`. **A human sends it.** This skill never
    emails anyone, and it never puts a reporter contact list into a chat window; see
    [`reference/shared-rules.md`](../../reference/shared-rules.md) Rule 5.
11. **Follow up once.** One follow-up, one week later, one paragraph: the original ask,
    restated, plus anything new. Then stop. Record `sent_date` and the follow-up date in the
    file so the next volunteer does not start the clock over.

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

You need the media map, one published answer page or brief, and about an hour per pitch.

1. Open the media map. Pick the outlet with the highest citation value that actually covers
   this district — not the biggest one.
2. Go to that outlet's site and read the reporter's last three stories. If none of them touch
   your topic, you have the wrong reporter or the wrong outlet. Write down the URL and date of
   the one that comes closest.
3. Find the outlet's submission page. Search the site for "letters to the editor,"
   "submission guidelines," and "op-ed." Write down the word limit, the address, and the
   exclusivity rule. Search the page for "election" and "candidate" to find the campaign-season
   restriction. If you cannot find one, call the newsroom and ask; then write down the name of
   who told you and the date.
4. Before you write a word, answer this on paper: *would this be a story if a different
   candidate's campaign sent it?* If no, stop. Pick a different artifact.
5. Copy `campaign-template/pitches/_template.md` into `campaign/pitches/` and name the file
   for the outlet and the topic.
6. Write the email in five sentences first, in this order: what happened, the evidence, what
   you can provide, the ask, your name. Then add detail only where a reporter would ask a
   follow-up question.
7. Count the words. If it is over 200, cut adjectives before you cut evidence.
8. Open every link you included and confirm each one loads and shows what you said it shows.
9. Read it out loud as if you were the reporter. If the first two sentences do not say what
   the story is, rewrite them.
10. Show it to the candidate along with who it is going to. Get an explicit yes.
11. A human sends it, from a named campaign address, with a phone number in the signature.
12. Put one calendar reminder seven days out. One follow-up paragraph. Then let it go.

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
