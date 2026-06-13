---
name: pipeline-init
description: Initialize a repo for the ScottDevSkills Agent Pipeline by scaffolding pipeline templates, policy scripts, run directories, gitignore support, and starter agent guidance. Use when setup is requested. Prefer new-run for one run and run-pipeline for execution.
---

# Pipeline Init

## Purpose

Prepare a project so future pipeline runs have templates, policy gates, and
expected directories.

## Workflow

1. Read `references/pipeline-init.md`.
2. Copy the required bundled payload from `../../p/` into the target repo
   according to that reference. The short internal path is intentional: it keeps
   Windows marketplace installs below path-length limits.
3. Preserve existing project instructions and merge starter guidance carefully.
4. Do not start a run unless explicitly requested after initialization.

## Output

List initialized areas, pre-existing files preserved, skipped files, and the
recommended next stage.
