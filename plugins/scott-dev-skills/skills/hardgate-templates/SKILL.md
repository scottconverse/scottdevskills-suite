---
name: hardgate-templates
description: Provide optional inert templates for enforcement gates, policy checks, and behavioral guardrails. Use when the user asks for gate templates, hard gates, mandatory checks, or enforcement design. Do not install active hooks or change executor behavior unless the user explicitly requests implementation outside this template skill.
---

# Hardgate Templates

## Purpose

Design enforcement patterns without surprising the user with active hooks or
automatic behavior.

## Activation Boundaries

Use for opt-in templates, policy language, checklists, or gate design. Do not
write active hooks, mutate global config, or enforce commands unless a later
implementation task explicitly authorizes that work.

## Workflow

1. Identify the behavior to enforce, the executor surface, failure cost, and
   bypass risk.
2. Choose the lightest gate that can prove compliance: checklist, policy script,
   preflight check, final-response check, or hook template.
3. Use `references/gate-template.md` and `references/gate-test-plan.md`.
4. Include behavioral tests that prove the gate fires and does not overfire.

## Output

Return the gate design, template locations, expected pass/fail signals, and
tests. Mark the template inert unless implementation was separately requested.
