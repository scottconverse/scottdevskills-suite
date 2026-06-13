---
name: audit-full
description: Deep multi-role Codex audit for release gates, readiness reviews, adversarial second opinions, and whole-project quality assessments. Reviews code, UX, docs, tests, and runtime behavior with evidence-backed findings. Prefer audit-lite for one small fix and walkthrough for UI wiring exploration.
---

# Audit Full

## Purpose

Produce a rigorous readiness verdict from five lenses: principal engineer,
senior UI/UX designer, technical writer, test engineer, and QA engineer.

## Activation Boundaries

Use for full audits, release gates, whole-repo reviews, handoff reviews, and
requests to find quality gaps before a customer, team, or leadership sees the
work. This suite ships only this canonical full-audit skill name.

Default to audit mode. Do not repair code unless the user explicitly switches
to repair mode.

## Workflow

1. Build the product and architecture model from docs, source, tests, scripts,
   config, routes, data paths, and user intent.
2. Collect runtime and verification evidence where feasible: tests, builds,
   browser exploration, screenshots, logs, and API behavior.
3. Apply the role rubrics on demand from `references/`.
4. Rank findings by severity and blast radius.
5. Produce an executive verdict, role deep dives, sprint punch list, next-sprint
   watchlist, and verification summary.
6. Use the shipped templates for the report files. Do not invent a new report
   structure unless the user explicitly asks for a different format.

## References

- `references/orchestration.md` for audit sequencing.
- `references/severity-framework.md` for severity.
- `references/blast-radius.md` for impact analysis.
- `references/principal-engineer.md`, `references/uiux-designer.md`,
  `references/technical-writer.md`, `references/test-engineer.md`, and
  `references/qa-engineer.md` for role-specific checks.
- `../../references/quality-gates.md` and
  `../../references/output-contracts.md` for suite-wide standards.

## Templates

Use `templates/00-executive-audit.md` as the front door report. Use the role
deep-dive templates for lens reports:

- `templates/01-engineering-deepdive.md`
- `templates/02-uiux-deepdive.md`
- `templates/03-documentation-deepdive.md`
- `templates/04-test-deepdive.md`
- `templates/05-qa-deepdive.md`

Use `templates/sprint-punchlist.md` and
`templates/next-sprint-watchlist.md` for delivery planning. Use the optional
documentation templates only when the audit produces replacement docs:
`templates/readme-replacement.md`, `templates/user-manual.md`,
`templates/architecture-doc.md`, and `templates/faq.md`.

## Failure Modes

- If the app cannot run, document the blocker and continue with static review.
- If the repo is too large, sample around critical workflows and state sampling
  limits clearly.
- If a finding lacks evidence, keep it as an open question instead of a defect.
