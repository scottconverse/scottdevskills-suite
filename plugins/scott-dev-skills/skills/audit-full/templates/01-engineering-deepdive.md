# Principal Engineer Deep Dive - [Project Name]

**Audit date:** [YYYY-MM-DD]
**Role:** Principal Engineer
**Finding prefix:** ENG
**Scope audited:** [Source, architecture, data paths, build, deployment, config]
**Auditor posture:** [Balanced | Adversarial]

## TL;DR

[Summarize architecture and code readiness. Name the highest-leverage technical
risk or say why the implementation is sound.]

## Severity Roll-Up

| Severity | Count |
| --- | --- |
| Blocker | [N] |
| Critical | [N] |
| Major | [N] |
| Minor | [N] |
| Nit | [N] |

## What Is Working

- **[Specific strength]** - [Evidence.]
- **[Specific strength]** - [Evidence.]

## What Could Not Be Assessed

[State limits or say all in-scope engineering artifacts were accessible.]

## Findings

Use IDs `ENG-001`, `ENG-002`, and so on. Consider:

- correctness and edge cases
- data flow and state ownership
- error handling and recovery
- concurrency and idempotency
- security and privacy exposure
- architecture boundaries
- dependency and build risk
- maintainability and blast radius

### ENG-001 - [Severity] - [Category] - [Title]

**Evidence**
[File/line, test output, reproduction, or runtime evidence.]

**Why this matters**
[Impact.]

**Blast radius**

- Adjacent code:
- Shared state / data / config:
- User-facing impact:
- Migration:
- Tests to update:
- Related findings:

**Fix path**
[Concrete path.]

## Patterns And Systemic Observations

[Recurring engineering root causes.]

## Appendix: What Was Audited

[Files, commands, routes, configs, docs, or tests reviewed.]
