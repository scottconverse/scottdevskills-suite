# Test Engineer Deep Dive - [Project Name]

**Audit date:** [YYYY-MM-DD]
**Role:** Test Engineer
**Finding prefix:** TEST
**Scope audited:** [Unit, integration, e2e, fixtures, CI, coverage strategy]
**Auditor posture:** [Balanced | Adversarial]

## TL;DR

[Summarize whether the tests protect the important behavior and whether failures
would be meaningful.]

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

[State tests that could not be run, missing services, time limits, or fixtures.]

## Findings

Use IDs `TEST-001`, `TEST-002`, and so on. Consider:

- coverage of core workflows
- regression tests for known risks
- fixture realism
- mocking boundaries
- CI reliability
- failure diagnostics
- performance of the test loop
- missing negative/error-path tests

### TEST-001 - [Severity] - [Category] - [Title]

**Evidence**
[Test file/line, command result, coverage gap, CI log, or reproduction.]

**Why this matters**
[Risk.]

**Blast radius**

- Adjacent tests:
- Shared fixtures:
- User-facing impact:
- Migration:
- Tests to update:
- Related findings:

**Fix path**
[Concrete test addition or strategy change.]

## Patterns And Systemic Observations

[Recurring test strategy root causes.]

## Appendix: What Was Audited

[Test files, CI jobs, fixtures, commands, coverage artifacts reviewed.]
