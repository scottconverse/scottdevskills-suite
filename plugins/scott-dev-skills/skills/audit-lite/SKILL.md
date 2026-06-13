---
name: audit-lite
description: Fast evidence-first review of a small diff, bug fix, or scoped change. Use for quick audit, smoke audit, sanity check, pre-merge review, or asking if one fix is ready. Do not use for full release reviews, whole-repo audits, or UI walkthroughs; prefer audit-full for broad readiness and walkthrough for runtime interface wiring.
---

# Audit Lite

## Purpose

Find concrete risks in a small change without producing a large audit package.

## Activation Boundaries

Use when the request is scoped to a recent fix, narrow diff, a few files, or a
pre-merge check. If the change expands into multiple subsystems, security
boundaries, migrations, or release readiness, escalate to `audit-full`.

Do not modify code during audit mode unless the user explicitly asks for repair.

## Workflow

1. Identify the changed files, intended behavior, tests touched, and likely
   blast radius.
2. Read callers, data contracts, UI/runtime paths, and tests relevant to the
   changed behavior.
3. Run or recommend the smallest meaningful verification available from repo
   scripts, CI config, or local test conventions.
4. Report findings first, ordered by severity. If there are no findings, say so
   directly and name residual test gaps.

## Evidence Standard

Each finding needs the affected file/line or runtime path, expected behavior,
actual risk, impact, and a targeted fix or test. Use
`../../references/quality-gates.md` for severity and evidence rules.

## Output Shape

Follow `../../references/output-contracts.md#audit-lite`.

## Failure Modes

- If the diff is unavailable, reconstruct scope from git status, recent files,
  user prompt, and nearby tests.
- If verification cannot run, report why and continue with static evidence.
- If findings imply wider risk, recommend `audit-full` and explain the trigger.
