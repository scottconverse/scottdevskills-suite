---
name: validate-manifest
description: Validate an Agent Pipeline manifest before execution using the same strict schema and scope checks enforced by the policy stage. Use when the user asks to check, validate, debug, or preflight a pipeline manifest. Prefer run-pipeline for execution.
---

# Validate Manifest

## Purpose

Catch manifest, scope-lock, and policy-shape issues before a pipeline run
starts or resumes.

## Workflow

1. Locate the manifest and related scope lock.
2. Use the pipeline validation script from initialized pipeline assets when
   available.
3. Check schema, paths, stage order, gates, required fields, and policy
   consistency.
4. Report errors as blockers and warnings as risks.

## Output

Return pass/fail, blocking errors, warnings, affected manifest fields, and the
minimum change needed to make the run executable.
