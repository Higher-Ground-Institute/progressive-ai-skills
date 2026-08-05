#!/usr/bin/env python3
"""Structural validation for skills in this repo.

Checks the Agent Skills structural rules plus this repo's own conventions. No model calls,
no API key, no network, no third-party dependencies — it runs in a couple of seconds in CI
on every pull request.

    python3 scripts/validate_skills.py              # all skills
    python3 scripts/validate_skills.py skills/answer-page
    python3 scripts/validate_skills.py --strict     # treat warnings as failures

Exit code 0 if every skill passes, 1 otherwise.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
NAME_MAX = 64
DESCRIPTION_MAX = 1024
COMPATIBILITY_MAX = 500

# Per the spec, and enforced as a hard error by the reference validator: anything else in
# frontmatter is rejected outright. Custom data belongs under `metadata`.
ALLOWED_FRONTMATTER = {
    "name",
    "description",
    "license",
    "allowed-tools",
    "metadata",
    "compatibility",
}

# Repo convention, not part of the spec: skills stay executable and depth goes in reference/.
SKILL_LINES_TARGET = 200
SKILL_LINES_HARD = 260

# Skills contributed before these conventions existed. New skills must satisfy everything.
LEGACY_SKILLS = {
    "brown-mm",
    "confess",
    "contact-extractor",
    "event-recap-generator",
    "linkedin-connector",
    "meeting-notes-to-actions",
    "resource-formatter",
}

CAMPAIGN_SECTIONS = ("## Output Format", "## Steps", "## Doing this without an agent", "## Tips")

EXAMPLE_SUFFIXES = (".example.org", ".example.com", ".example.gov", ".example.net")
EXAMPLE_HOSTS = {"example.org", "example.com", "example.gov", "example.net"}

# Public directories a realistic fixture will legitimately point at. These host no campaign
# content of ours, so a link to one is not a sign that real candidate material leaked in.
PUBLIC_DIRECTORY_HOSTS = {"ballotpedia.org", "www.vote411.org", "vote411.org", "schema.org"}


class Report:
    def __init__(self, skill: str) -> None:
        self.skill = skill
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


def parse_frontmatter(text: str) -> tuple[dict[str, str], str | None]:
    """Minimal YAML frontmatter reader.

    Handles the two shapes used in this repo: `key: value` and `key: >` with an indented
    folded block. Deliberately not a YAML parser — a dependency-free CI check is worth more
    here than full YAML coverage, and anything it cannot read is reported rather than
    guessed at.
    """
    if not text.startswith("---\n"):
        return {}, "SKILL.md does not begin with a '---' frontmatter delimiter"

    end = text.find("\n---", 3)
    if end == -1:
        return {}, "frontmatter is never closed with '---'"

    body = text[4:end]
    fields: dict[str, str] = {}
    key: str | None = None
    folded: list[str] = []

    for line in body.split("\n"):
        if not line.strip():
            continue
        if line[0] in " \t" and key is not None:
            folded.append(line.strip())
            continue
        if key is not None:
            fields[key] = " ".join(folded).strip()
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not match:
            return {}, f"cannot parse frontmatter line: {line!r}"
        key, inline = match.group(1), match.group(2).strip()
        folded = []
        if inline and inline != ">" and inline != "|":
            fields[key] = inline.strip("'\"")
            key = None

    if key is not None:
        fields[key] = " ".join(folded).strip()

    return fields, None


def check_skill(skill_dir: Path) -> Report:
    name = skill_dir.name
    rep = Report(name)
    legacy = name in LEGACY_SKILLS

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        rep.error("SKILL.md is missing")
        return rep

    if not (skill_dir / "README.md").is_file():
        rep.error("README.md is missing")

    text = skill_md.read_text(encoding="utf-8")
    fields, parse_error = parse_frontmatter(text)
    if parse_error:
        rep.error(parse_error)
        return rep

    # --- name ---
    declared = fields.get("name")
    if not declared:
        rep.error("frontmatter has no 'name'")
    else:
        if declared != name:
            rep.error(
                f"frontmatter name {declared!r} does not match directory name {name!r} — "
                "the spec requires them to be identical"
            )
        if len(declared) > NAME_MAX:
            rep.error(f"name is {len(declared)} chars, max is {NAME_MAX}")
        if not NAME_RE.match(declared):
            rep.error(
                f"name {declared!r} must be lowercase alphanumeric and hyphens, with no "
                "leading, trailing, or consecutive hyphens"
            )

    # --- description ---
    description = fields.get("description")
    if not description:
        rep.error("frontmatter has no 'description'")
    else:
        if len(description) > DESCRIPTION_MAX:
            rep.error(f"description is {len(description)} chars, max is {DESCRIPTION_MAX}")
        if len(description) < 60:
            rep.warn(f"description is only {len(description)} chars — it likely will not trigger reliably")

    compatibility = fields.get("compatibility")
    if compatibility and len(compatibility) > COMPATIBILITY_MAX:
        rep.error(f"compatibility is {len(compatibility)} chars, max is {COMPATIBILITY_MAX}")

    extra = set(fields) - ALLOWED_FRONTMATTER
    if extra:
        rep.error(
            f"frontmatter has fields the spec does not allow: {', '.join(sorted(extra))} — "
            f"only {', '.join(sorted(ALLOWED_FRONTMATTER))} are permitted, put custom data under 'metadata'"
        )

    # --- repo conventions ---
    line_count = len(text.splitlines())
    if line_count > SKILL_LINES_HARD and not legacy:
        rep.error(f"SKILL.md is {line_count} lines, hard cap is {SKILL_LINES_HARD} — move depth to reference/")
    elif line_count > SKILL_LINES_TARGET and not legacy:
        rep.warn(f"SKILL.md is {line_count} lines, target is {SKILL_LINES_TARGET}")

    if not legacy:
        for heading in CAMPAIGN_SECTIONS:
            if not re.search(rf"^{re.escape(heading)}\s*$", text, re.MULTILINE):
                rep.error(f"missing required section {heading!r}")

    # --- relative links resolve ---
    for target in re.findall(r"\]\((\.\./[^)#]+)", text):
        if not (skill_dir / target).resolve().exists():
            rep.error(f"broken relative link: {target}")

    check_evals(skill_dir, rep)
    return rep


def check_evals(skill_dir: Path, rep: Report) -> None:
    evals_file = skill_dir / "evals" / "evals.json"
    if not evals_file.is_file():
        if skill_dir.name not in LEGACY_SKILLS:
            rep.warn("no evals/evals.json")
        return

    try:
        data = json.loads(evals_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        rep.error(f"evals.json is not valid JSON: {exc}")
        return

    if data.get("skill_name") != skill_dir.name:
        rep.error(
            f"evals.json skill_name {data.get('skill_name')!r} does not match directory {skill_dir.name!r}"
        )

    cases = data.get("evals")
    if not isinstance(cases, list) or not cases:
        rep.error("evals.json has no 'evals' array")
        return

    seen_ids: set[object] = set()
    for index, case in enumerate(cases):
        where = f"evals[{index}]"
        for required in ("id", "prompt", "expected_output"):
            if not case.get(required):
                rep.error(f"{where} is missing '{required}'")
        case_id = case.get("id")
        if case_id in seen_ids:
            rep.error(f"{where} reuses id {case_id!r}")
        seen_ids.add(case_id)

        for rel in case.get("files", []):
            if not (skill_dir / rel).is_file():
                rep.error(f"{where} references a missing fixture: {rel}")

        assertions = case.get("assertions")
        if assertions is not None and (
            not isinstance(assertions, list) or not all(isinstance(a, str) for a in assertions)
        ):
            rep.error(f"{where} 'assertions' must be a list of strings")

    for fixture in (skill_dir / "evals" / "files").glob("*"):
        if fixture.is_file():
            check_fixture_hygiene(fixture, rep)


def check_fixture_hygiene(fixture: Path, rep: Report) -> None:
    """Eval fixtures must contain invented people and invented places.

    Real voter data in a public repo is the house rule this project is most likely to break
    by accident, so it gets a mechanical check rather than a note in a README.
    """
    try:
        text = fixture.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return

    ssn_like = re.search(r"\b\d{3}-\d{2}-\d{4}\b", text)
    if ssn_like:
        rep.error(f"{fixture.name} contains something shaped like an SSN")

    phones = re.findall(r"\b\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}\b", text)
    real_phones = [p for p in phones if "555" not in p]
    if real_phones:
        rep.warn(f"{fixture.name} contains a phone number that is not a 555 number: {real_phones[0]}")

    urls = re.findall(r"https?://([^/\s)\"']+)", text)
    real_hosts = sorted(
        {
            host
            for host in urls
            if not host.endswith(EXAMPLE_SUFFIXES)
            and host not in EXAMPLE_HOSTS
            and host not in PUBLIC_DIRECTORY_HOSTS
        }
    )
    if real_hosts:
        rep.warn(
            f"{fixture.name} links to non-example hosts ({', '.join(real_hosts[:3])}) — "
            "confirm no real candidate's unreviewed positions are in this fixture"
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="*", help="skill directories to check (default: all)")
    parser.add_argument("--strict", action="store_true", help="treat warnings as failures")
    args = parser.parse_args()

    if args.paths:
        targets = [Path(p).resolve() for p in args.paths]
    else:
        targets = sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir())

    reports = [check_skill(t) for t in targets]

    failed = 0
    for rep in reports:
        if rep.errors:
            failed += 1
            print(f"FAIL  {rep.skill}")
            for msg in rep.errors:
                print(f"        error: {msg}")
            for msg in rep.warnings:
                print(f"        warn:  {msg}")
        elif rep.warnings:
            if args.strict:
                failed += 1
            print(f"{'FAIL' if args.strict else 'WARN'}  {rep.skill}")
            for msg in rep.warnings:
                print(f"        warn:  {msg}")
        else:
            print(f"ok    {rep.skill}")

    print(f"\n{len(reports) - failed}/{len(reports)} skills passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
