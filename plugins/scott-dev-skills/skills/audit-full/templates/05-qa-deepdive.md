# QA Engineer Deep Dive - [Project Name]

**Audit date:** [YYYY-MM-DD]
**Role:** QA Engineer
**Finding prefix:** QA
**Scope audited:** [Runtime flows, browser paths, install path, smoke tests]
**Auditor posture:** [Balanced | Adversarial]

## TL;DR

[Summarize whether the built product works in realistic conditions and what
would stop a user or operator.]

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

[State unavailable environments, credentials, services, device coverage, or
runtime blockers.]

## Findings

Use IDs `QA-001`, `QA-002`, and so on. Consider:

- install and first-run path
- smoke-test coverage
- browser console and network errors
- data persistence
- permissions and auth states
- offline/error/retry behavior
- deploy or packaging checks
- user-visible regressions

### QA-001 - [Severity] - [Category] - [Title]

**Evidence**
[Runtime steps, route, screenshot, log, console/network issue, file path, or
package artifact.]

**Why this matters**
[User or release impact.]

**Blast radius**

- Adjacent flows:
- Shared runtime state:
- User-facing impact:
- Migration:
- Tests to update:
- Related findings:

**Fix path**
[Concrete verification or repair path.]

## Patterns And Systemic Observations

[Recurring QA root causes.]

## Appendix: What Was Audited

[Browsers, routes, commands, environments, artifacts, package paths reviewed.]
