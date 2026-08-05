# Venues — where a down-ballot candidate can publish a statement of record

**All facts below verified 2026-08-04.** Every claim carries a source URL and a label:

- **(VENDOR)** — the organization's own page, form, statute, or manual
- **(SECONDARY)** — news, third party, or a local affiliate's document illustrating a pattern
- **UNVERIFIED** — could not confirm. Do not rely on it.

**Used by:** `placement-writer`, `canonical-presence`
**State-by-state candidate statement programs:** [`state-voter-guides.md`](state-voter-guides.md)

---

## Read this first

**Ballotpedia Candidate Connection is the only always-open, free, self-serve, national option
we could verify.** Everything else is either invitation-only, state-specific, paid, or already
closed for this cycle.

If a campaign has one hour, spend it there.

---

## Ballotpedia Candidate Connection

**Entry point:** [ballotpedia.org/Survey](https://ballotpedia.org/Survey) — returns HTTP 200
directly with no redirect (VENDOR). The actual form lives on a LimeSurvey instance behind the
"CLICK HERE TO BEGIN THE SURVEY" button. **Link to `/Survey`, never to a form ID** — the form
URL rotates between cycles.

### Eligibility

Universal for submission, limited for coverage. Verbatim (VENDOR):

> "All candidates for office can complete our survey. We will make a profile for you and add
> your survey responses to it. However, please note that our full election results coverage is
> limited to the largest 100 cities, state capitols, and largest 200 school boards. If you are
> a local candidate outside of this scope, we will make a basic profile for you as noted but
> will not cover the results of your election."

So a county commission or small school-board candidate **does** get a profile with their
answers on it. They just do not get election-results coverage. State legislative candidates
are fully in scope.

### Cost

No fee appears anywhere on the survey page or the form. The only price language is a scam
warning: *"Verification is free, and Ballotpedia will never request payment to verify. If you
receive such a request, please notify editor@ballotpedia.org."* (VENDOR)

**Ballotpedia never affirmatively states the survey itself is free.** Absence of a fee plus
that warning is strong evidence but not a quote. Treat "free" as inferred.

### ⚠️ The live 2026 form is much shorter than Ballotpedia's own FAQ says

The form self-identifies as **Version 3.1a**. Confirmed by reading the rendered form on
2026-08-04:

| Section | Required? | Contents |
|---|---|---|
| Your Election | Yes | Name, email, party, office type, state, office, seat, year, date |
| Your Key Messages | Yes | Three key-message fields + one policy-passion field |
| Your Campaign | No | Endorsements text + three link fields |
| Photo | No | Upload + license checkbox |
| Links | No | Campaign site, campaign Facebook, personal LinkedIn |
| Verification | Yes | Filing status, election agency, contact, method, cell, attestation |

**Every free-text field is capped at 750 characters, hard-enforced.** The form contains exactly
five `maxlength="750"` attributes — the three key messages, the policy-passion answer, and the
endorsements answer — each with a live counter. Two further fields cap at 60 characters.

Verbatim question text (VENDOR):

- *"Please list below 3 key messages of your campaign. What are the main points you want
  voters to remember about you and your candidacy?"* → three separate fields
- *"What areas of public policy are you personally passionate about?"*
- *"What organizations or individuals have endorsed your campaign?"*

**The FAQ is stale.** It still references a *"Who are you? Tell us about yourself"* question and
a *"full 200-word answer"* — neither exists in the live form. A grep of the rendered form for
"who are you" returns zero matches. **Draft against the 750-character fields, not the FAQ.**

Also stale: [ballotpedia.org/LocalSurvey](https://ballotpedia.org/LocalSurvey) describes a
45–50 minute instrument, but it is explicitly titled "Local Candidate Survey 2021." Do not send
2026 candidates there.

**Time to complete:** *"around 30 minutes... depending on the number of optional questions and
length of responses."* (VENDOR)

Progress saves — there is an orange "Resume Later" button.

### Identity verification

Vendor is **Truepic** (product: Vision by Truepic). The candidate gets a text with a link,
downloads the app, and photographs a photo ID. Accepted: driver's license, state ID, military
ID, employee ID, passport, student ID, tribal ID. Not published; deleted from Ballotpedia's
server six months after the November general. (VENDOR)

**Two alternatives exist for candidates without a smartphone**, and they are easy to miss:

1. **Official filed email.** A confirmation message to the email address submitted with the
   official candidacy filing.
2. **Social media post.** X, Facebook, Instagram, or Bluesky. The account must have a profile
   photo of the candidate, the candidacy in the bio, a header image, at least four posts, and
   at least one month of activity.

Verification is not technically required, but: *"Ballotpedia will not upload responses for
which we do not receive sufficient identity verification."* (VENDOR)

### Publication

*"Once you have verified your responses, please allow up to one week for them to be uploaded.
Responses are uploaded in the order that they are verified, not in the order they were
submitted. Photos will take an extra day."* (VENDOR)

**The clock starts at verification, not submission.** A candidate who submits and never
completes Truepic is never published.

No 2026 submission deadline is published anywhere. Whether an unpublished internal cutoff
exists is UNVERIFIED. Given the one-week lag, submitting and verifying by roughly mid-October
is prudent — that timing is our inference, not Ballotpedia policy.

### ⚠️ Editing after submission — you cannot change what you said

This is the single most important operational fact about Ballotpedia, and it is why
`placement-writer` drafts offline and pressure-tests before anyone opens the form.

On the form: *"Once submitted, your answers are final... Small grammatical corrections can be
made upon request."* The
[full policy](https://ballotpedia.org/Ballotpedia:Our_approach_to_Candidate_Connection_survey_edit_and_removal_requests)
(VENDOR):

| Request | Ballotpedia's response |
|---|---|
| Fix a typo or grammar | Edits the existing response directly |
| Answer additional questions | Adds them to the existing response |
| **Change the substance of an answer** | **Refuses. Offers a timestamped note above the original.** |
| **Remove a response** | **Refuses. Offers a timestamped note or a new response above the original.** |
| Submit a second full response | Publishes both, timestamped, newest first |

One narrow exception: if a staffer without authority submitted it, the candidate or campaign
manager may email and replace the response **one time**.

Reciprocal right: *"If Ballotpedia has edited the existing response and the candidate writes in
to disagree with the edit, they can ask for the survey to be removed in full and Ballotpedia
will comply."*

Corrections go to `editor@ballotpedia.org`.

Worth telling candidates: *"Ballotpedia relies on the integrity of candidates to be honest and
does not perform background checks or fact-checks on their responses."* (VENDOR)

### Where responses surface

1. The candidate's profile, under a heading called **"Campaign Themes"**
2. Ballotpedia's **Sample Ballot Lookup Tool**
3. The Candidate Connection showcase carousel on the program page
4. **Ballotpedia's licensed data products** — easy to miss and worth knowing: *"Ballotpedia
   also reserves the right to license access to all or a portion of this database."* (VENDOR)

One gate applies to federal candidates only: without an FEC filing, *"Ballotpedia will not make
a profile for you until the filing deadline for your state passes and you make it onto the
ballot."*

---

## VOTE411 / League of Women Voters

**Invitation-only, always, and administered by the local or state League — not nationally.**
There is no self-serve door: `vote411.org/candidates` returns 404 (VENDOR, verified
2026-08-04).

### How access works

The League running the guide emails a unique per-candidate response link, usually to the
address on the official candidacy filing. Leagues are explicitly instructed not to work around
it. LWV Minnesota, in caps in their own volunteer guide (VENDOR):

> "IMPORTANT: DO NOT OFFER TO ENTER OR SUBMIT RESPONSES ON BEHALF OF CANDIDATES OR SUGGEST
> THAT CANDIDATES CAN EMAIL THEIR RESPONSES. Candidates MUST respond by submitting their own
> responses directly through the online system."

**If no invitation arrives:** check spam, then email the League and ask them to resend or
change the address on file. LWV Minnesota routes this to `vote411@lwvmn.org`; other Leagues
have their own coordinator.

**Find your League:**
[lwv.org/local-leagues/find-local-league](https://www.lwv.org/local-leagues/find-local-league)
(VENDOR). Note that `my.lwv.org/find-local-league` is **not** a valid URL — it 404s.

**Whether your race is covered at all is a local League's discretionary decision.** LWV Texas,
for instance, covers statewide races, State Board of Education, Courts of Appeals, and
congressional and legislative districts *"not covered by a local League"* (VENDOR). County
commission and school board coverage depends on whether a local League exists and picked that
race.

### Character limits — per-League, never national

From LWV's national instructions to Leagues building guides (VENDOR):

> "You'll need to come up with the questions and a character limit (not word limit) for each
> response... **Leagues tend to have between a 250 and 500-character limit but you can set it
> to whatever you like.**"

It is always a **character** limit and it counts spaces and punctuation. Documented examples:

| League | Limit | Label |
|---|---|---|
| LWV Utah | 750 characters per answer | VENDOR |
| LWV Bucks County PA | 750 per question; 300 each for education and experience | SECONDARY |
| LWV national template default | 750 characters | SECONDARY |
| LWV national guidance to Leagues | 250–500 typical, ≤1000 recommended max | VENDOR |

**Verify the limit with your League before drafting.** A 250-character answer and a 750-
character answer are different documents, and `placement-writer` renders down rather than
padding up.

Number of questions is also per-League; four is a common template, at *"about 15 minutes"*.

### Non-response is published

This is the strongest argument for responding: silence is printed, not omitted.

> "Candidates who have not responded will have 'Candidate has not yet responded' by their name
> until they respond." (SECONDARY — local League FAQ describing standard platform behavior)

LWV Texas attempts contact at least three times before that stands (VENDOR).

There is a separate content-moderation failure mode. LWV Texas: *"Negative references to
opponents, including officeholders, or specific persons are not allowed. If a response does
not meet the criteria... the Voters Guide will state 'Response removed; does not meet
criteria'."* (VENDOR) **Do not name an opponent in a Vote411 answer.**

### ⚠️ Two deadlines, and campaigns miss the important one

| Track | Deadline | Editable |
|---|---|---|
| **Online** | Typically the day before the election | Yes, freely, as often as you like |
| **Print** | Weeks earlier, tied to the publication date | **No** |

A real example (SECONDARY): *"Vote411 will go live on Friday, April 18th and will stay active
until Election Day"* — but *"We will be downloading a copy on Monday, April 28th to publish in
the Bucks County Herald. Any changes made after that date will not appear in the print guide."*

**Ask your League for the print cutoff explicitly.** Do not assume the "until the day before"
window applies to print. No national deadline exists for the Nov 3 2026 general; it is set
per-League. UNVERIFIED for any specific jurisdiction.

---

## Endorsement and advocacy questionnaires

**The pattern across every organization checked: the questionnaire is an input to an
endorsement decision, not a publication venue.** What gets published is the endorsement — a
yes or no. Your answers usually are not.

This is the opposite of Ballotpedia and Vote411, and a first-time candidate should understand
it before spending three hours on one.

| Organization | Where to apply | Notable mechanics |
|---|---|---|
| **Sierra Club** | The **chapter**, not national. Some use a self-serve intake form. | Non-incumbents get the questionnaire; incumbents may be judged on record. Endorsement needs supermajority at multiple levels. (VENDOR) |
| **Planned Parenthood** | The affiliate's **advocacy arm**, not the health-care provider | *"Only candidates with a 100% score on the questionnaire will be considered."* Deadlines run very early — one large affiliate closed non-incumbent primary consideration on 2026-02-10. (VENDOR) |
| **AFL-CIO** | **Your Central Labor Council** for local office; the state federation only for state and federal | The most common routing mistake. Michigan AFL-CIO: *"Candidates for local office should contact their respective Central Labor Council."* Often requires an interview and a two-thirds delegate vote. (VENDOR) |
| **Working Families Party** | Form-fillable PDF to a central submission portal; separate local questionnaire | Notably transactional — asks you to commit to describing yourself as WFP-endorsed, becoming a dues-paying member, and meeting quarterly. Read before submitting. (VENDOR) |

Labor endorsements are genuinely not partisan-exclusive: *"We have a proud record of endorsing
Democrats, Republicans, and non-partisan candidates."* (VENDOR)

**UNVERIFIED:** intake processes for League of Conservation Voters affiliates, NEA and AFT
state affiliates, Everytown, Giffords, HRC, Emily's List, and Run for Something.

---

## County and municipal voter guides

Highly local, and the variance is the finding. Three counties in one state came back with
150-, 200-, and 300-word limits and three different deadline formulas. **Teach the lookup, do
not tabulate the counties.**

### The lookup procedure

1. **Work out which office runs your race's pamphlet — often not the one you filed with.**
   King County, WA (VENDOR): *"The Secretary of State's Office accepts voters' pamphlet
   submissions for federal, statewide, legislative, Court of Appeals and Superior Court
   offices. All other offices file with their county elections office."*
2. **Go to the county elections office's "for candidates" section**, not the voter-facing one.
   Look for a Candidate Manual, Voters' Pamphlet Filing page, or Local Voters' Pamphlet
   Administrative Rules. The rules are almost always in a PDF, not on an HTML page.
3. **Find the word-limit table.** It is usually keyed to office type or to the number of
   registered voters in the jurisdiction, not uniform across the county.
4. **If the district crosses county lines, file separately in each county.** Both Washington
   and Oregon require this, and the statements do not have to be identical.
5. **Assume the deadline is tied to the filing period, not the election**, and assume no edits
   after it.
6. **If nothing turns up, call.** In many counties the local pamphlet is optional — individual
   jurisdictions opt in and pay for it. No web page is not proof there is no pamphlet.

### Verified examples

| Jurisdiction | Limit | Nov 2026 deadline | Notes |
|---|---|---|---|
| **King County, WA** | 300 / 200 / 150 words by jurisdiction size | **2026-08-07, 5:00 pm** | Paragraph caps tied to word count. No lists, tables, or bullets. Primary statement carries forward automatically. No edits after the deadline — withdraw and re-file. (VENDOR) |
| **Multnomah County, OR** | 325 words | **2026-08-25, 5:00 pm** | Fee or petition required. Naming an endorser requires a signed JCVP-02 form from them or the name is struck. Shared form across four counties. (VENDOR) |
| **Island County, WA** | 200-word statement + 100-word bio under four fixed headings | 4:30 pm, 11th day after filing week closes | Overlong submissions *"will be shortened by the Auditor's Office without notice and without consulting the candidate."* (VENDOR) |
| **Grant County, WA** | 150 words | — | Same statement used for both primary and general. (VENDOR) |
| **Nevada County, CA** | Per CA Elections Code | Tied to nomination filing | *"Candidate statements are provided by the candidate and printed at their own expense."* (VENDOR) |

---

## What we could not verify

Listed so nothing above gets mistaken for confirmed.

- Whether the Ballotpedia survey is affirmatively free, as opposed to having no stated fee
- Whether Ballotpedia enforces an unpublished 2026 submission cutoff
- Whether a candidate arriving with a pre-filled invitation token sees questions beyond the
  six free-text fields on the public form
- Any national Vote411 deadline for the Nov 3 2026 general — deadlines are per-League
- Whether the "Candidate has not yet responded" label is platform-wide or a per-League display
  setting
- Whether Sierra Club, AFL-CIO bodies, or WFP ever publish questionnaire responses rather than
  just endorsements
- Local pamphlet deadlines for any Washington county other than King, Island, and Grant
