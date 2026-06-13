---
name: prompt-quality
description: Review, lint, test, or design evaluations for LLM prompts and prompt-driven workflows. Use for prompt linting, prompt regression cases, eval design, prompt harness planning, output contracts, cost-risk review, and release checks for prompt changes. Do not use for general code review; prefer audit-lite or audit-full.
---

# Prompt Quality

## Purpose

Make prompt changes testable, maintainable, and less fragile.

## Workflow

1. Identify the prompt surface, target model or provider if known, expected
   output contract, inputs, tools, safety constraints, and failure examples.
2. Check for ambiguity, hidden assumptions, missing refusal/edge behavior,
   output-schema drift, context bloat, injection exposure, and untestable claims.
3. Design regression cases for happy path, boundary path, adversarial input,
   malformed input, and known failures.
4. Recommend prompt edits only when they directly reduce a named risk.
5. For release readiness, apply `references/prompt-release-checklist.md`.

## References

- `references/prompt-lint-rules.md` for lint categories.
- `references/eval-design.md` for regression and scoring design.
- `references/prompt-release-checklist.md` for release review.
- `../../references/output-contracts.md#prompt-quality` for report shape.

## Output

Lead with prompt risks, then suggested edits, test/eval cases, and residual
uncertainty. If the prompt is acceptable, say what evidence supports that.
