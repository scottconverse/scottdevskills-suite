---
name: audit-init
description: Scaffold dual-agent audit handoff infrastructure for a Codex project. Use when the user asks to set up audit gates, audit protocols, self-audit documents, or cross-agent handoff files. Do not use for performing an audit; prefer audit-lite, audit-full, or walkthrough.
---

# Audit Init

## Purpose

Create or update audit infrastructure that later audits can rely on.

## Workflow

1. Confirm the target repo and whether the task is setup only.
2. Read `references/audit-init.md`.
3. Use the templates in `references/` for audit gate, audit protocol, and
   five-lens self-audit artifacts.
4. Keep generated infrastructure separate from audit findings.

## Evidence And Output

Report created or updated artifacts, skipped artifacts, and any repo-specific
assumptions. If the user wanted an actual review, route to `audit-full` or
`audit-lite` instead.
