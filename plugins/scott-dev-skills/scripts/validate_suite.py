#!/usr/bin/env python3
"""Validate ScottDevSkills suite structure and regression metadata."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml


MAX_BODY_LINES = 220
LEGACY_SKILLS = {"audit-team"}


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors: list[str] = []
    validate_skills(root, errors)
    validate_cases(root, errors)
    validate_manifest(root, errors)
    if errors:
        print("Suite validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Suite validation passed: {root}")
    return 0


def validate_manifest(root: Path, errors: list[str]) -> None:
    path = root / ".codex-plugin" / "plugin.json"
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - diagnostic path
        errors.append(f"cannot read plugin manifest: {exc}")
        return
    if manifest.get("name") != "scott-dev-skills":
        errors.append("plugin name must be scott-dev-skills")
    if manifest.get("skills") != "./skills/":
        errors.append("plugin skills path must be ./skills/")


def validate_skills(root: Path, errors: list[str]) -> None:
    skills_root = root / "skills"
    if not skills_root.is_dir():
        errors.append("missing skills directory")
        return
    names = {path.name for path in skills_root.iterdir() if path.is_dir()}
    for legacy in sorted(LEGACY_SKILLS & names):
        errors.append(f"legacy duplicate skill is shipped: {legacy}")
    for skill_dir in sorted(path for path in skills_root.iterdir() if path.is_dir()):
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            errors.append(f"{skill_dir.name} missing SKILL.md")
            continue
        text = skill_md.read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        if not match:
            errors.append(f"{skill_dir.name} invalid frontmatter")
            continue
        try:
            frontmatter = yaml.safe_load(match.group(1))
        except yaml.YAMLError as exc:
            errors.append(f"{skill_dir.name} frontmatter yaml error: {exc}")
            continue
        if frontmatter.get("name") != skill_dir.name:
            errors.append(f"{skill_dir.name} frontmatter name mismatch")
        if not frontmatter.get("description"):
            errors.append(f"{skill_dir.name} missing description")
        body_lines = text[match.end() :].splitlines()
        if len(body_lines) > MAX_BODY_LINES:
            errors.append(f"{skill_dir.name} body has {len(body_lines)} lines")
        for ref in re.findall(r"`([^`]*references/[^`]*)`", text):
            ref_file = ref.split("#", 1)[0]
            ref_path = (skill_dir / ref_file).resolve()
            if not ref_path.exists():
                errors.append(f"{skill_dir.name} references missing file: {ref}")


def validate_cases(root: Path, errors: list[str]) -> None:
    path = root / "tests" / "skill-regression" / "cases.json"
    try:
        cases = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - diagnostic path
        errors.append(f"cannot read regression cases: {exc}")
        return
    skills = {p.name for p in (root / "skills").iterdir() if p.is_dir()}
    for case in cases:
        expected = case.get("expected_skill")
        if expected not in skills:
            errors.append(f"case {case.get('id')} expects unknown skill {expected}")
        if not case.get("prompt"):
            errors.append(f"case {case.get('id')} has empty prompt")


if __name__ == "__main__":
    raise SystemExit(main())
