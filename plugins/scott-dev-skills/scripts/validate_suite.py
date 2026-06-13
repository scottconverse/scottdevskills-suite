#!/usr/bin/env python3
"""Validate ScottDevSkills suite structure and regression metadata."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml


MAX_BODY_LINES = 220
MAX_PACKAGE_RELATIVE_PATH = 90
EXPECTED_VERSION = "0.1.0-beta.1"
LEGACY_SKILLS = {"audit-team"}
FORBIDDEN_LEGACY_TEXT = [
    ("agent-pipeline-" + "codex", "standalone Agent Pipeline product name"),
    ("0." + "9.1", "standalone Agent Pipeline release version"),
]
LEGACY_TEXT_ALLOWLIST = {
    Path("references/migration-notes.md"),
}


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors: list[str] = []
    validate_skills(root, errors)
    validate_cases(root, errors)
    validate_manifest(root, errors)
    validate_resource_contracts(root, errors)
    validate_release_guards(root, errors)
    validate_packaged_paths(root, errors)
    validate_no_legacy_text(root, errors)
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
    if manifest.get("version") != EXPECTED_VERSION:
        errors.append(f"plugin version must be {EXPECTED_VERSION}")
    if manifest.get("skills") != "./skills/":
        errors.append("plugin skills path must be ./skills/")
    interface = manifest.get("interface") or {}
    if interface.get("displayName") != "ScottDevSkills":
        errors.append("plugin displayName must be ScottDevSkills")
    if interface.get("category") != "Productivity":
        errors.append("plugin category must be Productivity")
    capabilities = set(interface.get("capabilities") or [])
    if not {"Interactive", "Write"}.issubset(capabilities):
        errors.append("plugin capabilities must include Interactive and Write")


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


def validate_resource_contracts(root: Path, errors: list[str]) -> None:
    path = root / "tests" / "skill-regression" / "resource-contracts.json"
    try:
        contracts = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - diagnostic path
        errors.append(f"cannot read resource contracts: {exc}")
        return
    skills = {p.name for p in (root / "skills").iterdir() if p.is_dir()}
    for contract in contracts:
        skill = contract.get("skill")
        if skill not in skills:
            errors.append(f"resource contract expects unknown skill {skill}")
        files = contract.get("required_files")
        if not isinstance(files, list) or not files:
            errors.append(f"resource contract for {skill} has no required_files")
            continue
        for rel_path in files:
            if not isinstance(rel_path, str):
                errors.append(f"resource contract for {skill} has non-string path")
                continue
            if Path(rel_path).is_absolute() or ".." in Path(rel_path).parts:
                errors.append(f"resource contract for {skill} has unsafe path: {rel_path}")
                continue
            if not (root / rel_path).is_file():
                errors.append(f"resource contract missing file for {skill}: {rel_path}")


def validate_release_guards(root: Path, errors: list[str]) -> None:
    smoke_script = root / "scripts" / "install_smoke.ps1"
    if not smoke_script.is_file():
        errors.append("missing scripts/install_smoke.ps1 release install-smoke guard")


def validate_packaged_paths(root: Path, errors: list[str]) -> None:
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()
        if len(rel) > MAX_PACKAGE_RELATIVE_PATH:
            errors.append(
                f"packaged path exceeds {MAX_PACKAGE_RELATIVE_PATH} chars: {rel}"
            )


def validate_no_legacy_text(root: Path, errors: list[str]) -> None:
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if rel in LEGACY_TEXT_ALLOWLIST:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        lowered = text.lower()
        for needle, label in FORBIDDEN_LEGACY_TEXT:
            if needle.lower() in lowered:
                errors.append(f"legacy text found in {rel.as_posix()}: {label}")


if __name__ == "__main__":
    raise SystemExit(main())
