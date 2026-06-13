# Shared Deep-Dive Structure

Use this structure for each role deep dive. The role-specific templates set the
role name, finding prefix, and category set.

## Required Sections

```markdown
# [Role] Deep Dive - [Project Name]

**Audit date:** [YYYY-MM-DD]
**Role:** [Role]
**Scope audited:** [Artifacts, routes, flows, files, or docs reviewed]
**Auditor posture:** [Balanced | Adversarial]

## TL;DR

[Three to five sentences about this dimension's condition and highest-leverage
takeaway.]

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

[Name access, runtime, credential, fixture, build, or scope limits. If none,
say all in-scope items were accessible.]

## Findings

### [PREFIX-001] - [Severity] - [Category] - [One-line title]

**Evidence**
[File paths with line numbers, URLs, screenshots, logs, reproduction steps,
network captures, or test output. Make it independently verifiable.]

**Why this matters**
[Which users, workflows, data, or maintenance paths are affected.]

**Blast radius**
[Required for Blocker, Critical, and Major.]

- Adjacent code:
- Shared state / data / config:
- User-facing impact:
- Migration:
- Tests to update:
- Related findings:

**Fix path**
[Concrete implementation approach or decision path.]

## Patterns And Systemic Observations

[Name repeated root causes across findings.]

## Appendix: What Was Audited

[List the artifacts reviewed.]
```
