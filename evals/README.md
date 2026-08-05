# Evals

**Last verified:** 2026-08-04

Each skill carries its own `evals/evals.json`. That is not a convention this repo invented —
it is the format defined by the Agent Skills standard itself, at
[Evaluating skill output quality](https://agentskills.io/skill-creation/evaluating-skills.md).
Two existing tools read it with zero harness code on our side, so there is nothing here to
build or maintain.

```
skills/answer-page/
├── SKILL.md
├── README.md
└── evals/
    ├── evals.json
    └── files/
        └── positioning.md
```

---

## Stage 0 — structural validation

Free, deterministic, no model, no API key, runs in CI on every pull request.

```bash
python3 scripts/validate_skills.py
python3 scripts/validate_skills.py skills/answer-page --strict
```

`scripts/validate_skills.py` checks the spec's frontmatter and naming rules, this repo's
section conventions, that relative links resolve, that `evals.json` parses and its fixtures
exist, and that no eval fixture carries something shaped like real personal data.

The official reference validator is worth running too. **It is a Python package, not npm:**

```bash
pip install skills-ref
skills-ref validate ./skills/answer-page
```

It checks frontmatter only, and it is stricter than you might expect in one place: **any
frontmatter field outside `name`, `description`, `license`, `allowed-tools`, `metadata`, and
`compatibility` is a hard error.** Custom data goes under `metadata`. Note also that
`skills-ref validate` does not look at `evals/` at all — nothing in the official tooling
validates `evals.json`, which is why `scripts/validate_skills.py` does.

Its README calls it "intended for demonstration purposes only," so treat it as a second
opinion rather than the gate.

### The rules both validators enforce

| Field | Rule |
|---|---|
| `name` | 1–64 chars, lowercase alphanumeric and hyphens, no leading or trailing hyphen, **no consecutive hyphens**, and **must match the parent directory name** |
| `description` | 1–1024 chars, non-empty, describes what the skill does *and* when to use it |
| `compatibility` | optional, max 500 chars |

The directory-name rule is the one that bites. This repo had exactly that failure —
`skills/linkedin-connector/SKILL.md` declared `name: linkedin-connect-tracker`, which broke
`skills-ref validate` across the whole repo. It is fixed.

---

## Stage 1 — running the evals

```bash
export OPENAI_API_KEY=sk-...
npx agent-skills-eval ./skills \
  --base-url https://api.openai.com/v1 \
  --target gpt-4o-mini \
  --judge gpt-4o-mini \
  --baseline \
  --report
```

`--baseline` is the important flag. It runs each case twice — once with the skill loaded and
once without — which is the entire point of the format. Without it you only get the with-skill
arm and no way to tell whether the skill did anything.

**`--base-url` is required** even though the tool's own README omits it. Without it, or without
`OPENAI_BASE_URL` exported, the run fails immediately. The API key is read from the variable
named by `--api-key-env`, defaulting to `OPENAI_API_KEY`.

Other flags: `--config`, `--workspace`, `--include`, `--exclude`, `--concurrency`, `--layout`,
`--strict`, `--log-format`, `--log-file`, `--no-report`, `--no-color`, `--verbose`,
`--report-title`, `--report-output`.

### Two things to know before you plan around this tool

**There is no Claude Code run mode.** `agent-skills-eval` talks only to OpenAI-compatible HTTP
endpoints. It has a `RunMode` type internally, but it is `"with_skill" | "without_skill"` —
the with/without arms, not an execution backend, and not settable from the CLI. Running these
skills the way they are actually used, loaded natively from disk by Claude Code, would mean
implementing the tool's `Provider` interface yourself.

**`defaults` cannot share assertions across cases.** It accepts exactly three things:
`defaults.target.params`, `defaults.judge.params`, and `defaults.tools`. Anything else is
silently ignored. The cross-cutting assertions below have to be repeated per case.

---

## The format

```json
{
  "skill_name": "answer-page",
  "evals": [
    {
      "id": 1,
      "prompt": "A realistic thing a user would actually type.",
      "expected_output": "Human-readable prose describing what good looks like.",
      "files": ["evals/files/positioning.md"],
      "assertions": ["Specific, observable, countable statements"]
    }
  ]
}
```

`prompt` is the only field the runner hard-requires per case. `files` paths are relative to the
**skill directory**, not to `evals/` — which is why they include the `evals/` prefix — and they
are sandboxed, so a path escaping the skill directory is treated as missing.

Useful behavior: if you provide `expected_output` and skip `assertions`, the runner promotes
the expected output into a judge assertion automatically. Spec-minimal files still grade.

There is **no official JSON Schema** for `evals.json` anywhere. The normative definition is
prose plus two examples on one documentation page.

### On assertions

The spec says not to write them up front: *"Don't worry about defining specific pass/fail
checks yet — just the prompts and expected outputs. You'll add detailed checks (called
assertions) after you see what the first run produces."*

We have followed that with one deliberate exception: **assertions that are mechanically
verifiable regardless of what the first run looks like are written now.** A 100-word limit is
100 words whether or not anyone has seen the output yet. Judgment-dependent assertions are
left for Stage 2.

**Assertions the baseline also passes are noise.** The spec is explicit that they *"inflate the
with-skill pass rate without reflecting actual skill value."* Expect several of ours to be
no-ops after the first run, and delete them when they are.

---

## Why the refusal cases matter most

The with/without baseline is an unusually good fit for this project. **A bare model asked to
write a candidate's position on anything will cheerfully invent one.** These skills are
supposed to refuse. So the refusal cases are exactly where the baseline fails and the skill
passes — the clearest possible demonstration that the skills do something.

The refusals under test:

| Skill | The refusal |
|---|---|
| `answer-page` | Topic on the `no-position-yet` list → emits a marker with the specific question instead of a position |
| `answer-page` | Sixteen query-variant pages → declines, explains scaled content abuse, offers one page |
| `candidate-profiler` | Platitude answer → probes instead of recording it as a position |
| `issue-brief` | Issue already covered well by a public source → says so before writing |
| `placement-writer` | "Submit it for me" → drafts, warns about irreversibility, does not submit |
| `canonical-presence` | Wikipedia page and `llms.txt` → declines both, redirects to Ballotpedia |
| `local-media-pitch` | Anonymous tip → refuses, offers the attributed version |
| `local-media-pitch` | Op-ed on a topic with no position → catches both the wrong venue and the missing position |

"Declining to fabricate a position is a passing test" becomes a measurable delta rather than a
principle.

---

## Fixture rules

These are not style preferences. A public repo for campaigns is the worst possible place to
leak voter data, and eval fixtures are the easiest place to do it by accident.

- **Invented people, invented places, `*.example.org` URLs.** The shared fixture campaign is
  Maya Ellison, running for the Ashfield County Board of Commissioners, District 3. Every
  ordinance number, dollar figure, reporter, and email address in the fixtures is made up.
- **No real voter names, addresses, phone numbers, or voter ID numbers.** `validate_skills.py`
  greps for these shapes and fails the build.
- **No real candidate's unreviewed positions.** Golden-district material lives in
  [`golden/`](../golden/), separate from fixtures, and even there the research covers *places*
  rather than people.

---

## Cost

Every case runs twice, once per arm. Twenty-five cases is fifty runs. Keep the set small — the
spec recommends 2–3 cases per skill anyway, and we are only slightly over that.

Run Stage 0 on every pull request. Run Stage 1 on demand or on a schedule, since it costs
model calls.

---

## Deferred

Per the staged plan, and deliberately not built yet:

- Verification scripts for mechanical checks, which the spec notes are "more reliable than LLM
  judgment for mechanical checks and reusable across iterations" — word and character counting
  for `placement-writer` is the obvious first one
- Blind comparison between skill versions
- The full adversarial set: candidates sharing a name with someone famous, issues where the
  honest answer is unpopular, races where the incumbent is a Democrat

Do not build these before the first real run produces results worth reacting to.
