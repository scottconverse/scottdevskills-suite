---
name: intake
description: Capture a plain-English product, repo, design, bug, or feature request into pipeline intake artifacts without starting execution. Use when the user wants a task drafted, scoped, or preserved for later pipeline work. Prefer new-run when a run skeleton is requested.
---

# Intake

## Purpose

Turn loose intent into durable pipeline intake without executing the pipeline.

## Workflow

1. Read `references/intake.md`.
2. Identify task intent, constraints, target repo, success criteria, risks,
   likely pipeline type, and missing decisions.
3. Draft intake, manifest, and scope-lock content only when the user requested
   artifact creation.
4. Stop before running stages or mutating source code.

## Output

Summarize captured intent, open questions, recommended pipeline type, and the
artifact paths if files were created.
