# ScottDevSkills Manual

Version: **v0.1b**

ScottDevSkills is a Codex plugin made of focused skills. Each skill is an
operating procedure: when it triggers, it tells Codex how to gather evidence,
what to avoid, which references to load, and what kind of answer or artifact to
produce.

## How To Think About The Suite

Use ScottDevSkills when the work needs discipline more than speed theater. The
suite is strongest when a task has real risk: a release decision, a UI that may
only be cosmetic, a prompt that needs regression cases, a long-running session,
or a project run that should leave a durable trail.

The skills are intentionally narrow. If a task is small, use the small skill.
If the task is broad, use the broad skill. If a skill is in audit mode, it
reports instead of fixing unless you explicitly switch to repair work.

## Audit Lite

**Good for:** a quick review of one bug fix, a small diff, a few touched files,
or a pre-merge sanity check.

Audit Lite reads the changed surface, follows nearby callers and tests, checks
the likely blast radius, and reports findings first. It is designed to be
short, skeptical, and useful between fixes.

Use it when you want to know:

- Did this fix introduce a regression?
- Are the tests meaningful for the changed behavior?
- Is there a small missing edge case?
- Is this ready for the next step?

Avoid it when the work touches a release boundary, multiple subsystems,
security-sensitive behavior, migration logic, or a complete product workflow.
Use Audit Full for that.

## Audit Full

**Good for:** release gates, whole-project readiness, customer handoff,
leadership review, and adversarial second opinions.

Audit Full reviews the project through five lenses:

- Principal engineering quality.
- UI/UX quality.
- Technical writing and documentation.
- Test strategy.
- QA and runtime behavior.

It produces a readiness verdict, severity-ranked findings, role deep dives,
blast-radius analysis, this-sprint actions, next-sprint watchlist, and a
verification summary.

Use it when you want to know:

- Is this ready to ship?
- What would break for real users?
- What are the highest-risk gaps?
- Which issues belong this sprint?
- Which issues can wait but should not disappear?

Audit Full is intentionally heavier than a code review. It should gather
evidence from source, tests, docs, runtime behavior, and project scripts where
feasible.

## Walkthrough

**Good for:** finished or nearly finished frontend work where the question is
whether the interface is actually wired.

Walkthrough uses browser exploration and source inspection to compare what the
UI promises against what the system does. It checks routes, buttons, forms,
menus, modals, state changes, mobile/desktop layouts, console errors, failed
network requests, persistence, auth assumptions, and test coverage.

Use it when you want to know:

- Which buttons do nothing?
- Which screens are cosmetic?
- Which documented flows are missing?
- Which backend capabilities are not surfaced?
- Which UI features are unsupported by real data?
- Which tests would catch the gaps?

Walkthrough is not a repair skill by default. It reports the wiring map and the
defects. Repair can happen afterward as a separate implementation task.

## Agent Pipeline

**Good for:** structured, manifest-driven project work that should not depend
on memory or vibes.

The Agent Pipeline skill is the router. It points Codex to the right stage:

- **pipeline-init** prepares a repo with pipeline templates and policy scripts.
- **intake** captures a task without starting execution.
- **new-run** creates a run skeleton.
- **validate-manifest** checks run shape before execution.
- **run-pipeline** executes or resumes a run.
- **show-run-status** inspects a run without mutating it.
- **audit-init** scaffolds audit-handoff infrastructure.

Use it when you want durable project execution with scope locks, stage
artifacts, verification, and clear stop conditions.

Avoid it for tiny one-off edits. The pipeline pays for itself when the work is
large enough that losing the thread would be expensive.

## Pipeline Init

**Good for:** preparing a repository for repeatable pipeline runs.

Pipeline Init adds the project-side materials needed by the pipeline: template
pipelines, policy scripts, run directory conventions, and starter guidance. It
does setup only. It should not start a run unless the user explicitly requests
that next step.

Use it when a repo needs to become pipeline-ready.

## Intake

**Good for:** preserving a loose idea as a structured task.

Intake turns plain-English intent into durable pipeline material: goal,
constraints, likely run type, success criteria, risks, and missing decisions.
It is useful when the project idea is real but not ready to execute yet.

Use it when you want to capture the work without starting the work.

## New Run

**Good for:** creating a fresh run skeleton.

New Run selects a pipeline template, creates the run structure, and prepares the
manifest and scope lock. It stops before execution.

Use it when the work is defined enough to become a pipeline run.

## Validate Manifest

**Good for:** checking a pipeline run before it starts.

Validate Manifest catches schema problems, missing fields, path issues, scope
lock mismatches, and policy-shape errors before execution. It reports pass/fail,
blockers, warnings, affected fields, and the smallest change needed to make the
run executable.

Use it when the run exists but you do not trust it yet.

## Run Pipeline

**Good for:** executing or resuming a pipeline run.

Run Pipeline follows the manifest, respects human gates, runs policy and
verification stages, records evidence, and stops when the run hits a gate,
failure, or unclear scope.

Use it when the run is ready to move.

## Show Run Status

**Good for:** read-only pipeline inspection.

Show Run Status summarizes run id, pipeline type, current stage, last completed
stage, blockers, required human decisions, and next valid action. It does not
resume or mutate the run.

Use it when you want situational awareness without changing anything.

## Audit Init

**Good for:** creating audit-handoff infrastructure.

Audit Init scaffolds audit gates, audit protocols, and five-lens self-audit
materials. It is setup for future audits, not the audit itself.

Use it when a project needs an audit discipline before implementation or
release work proceeds.

## Prompt Quality

**Good for:** prompt linting, prompt regression tests, eval design, and release
checks for prompt changes.

Prompt Quality reviews prompts for ambiguity, conflicting instructions, missing
output contracts, hidden context assumptions, injection exposure, tool-use
hazards, and untestable claims. It can also design a small evaluation set for
happy path, boundary path, malformed input, adversarial input, and known
failure reproduction.

Use it when you want to know:

- Is this prompt specific enough to test?
- What failure modes should be in the eval set?
- Does the output contract match downstream code?
- What changed in risk when the prompt changed?

Prompt Quality is most useful when prompts are treated like production logic.

## Context Discipline

**Good for:** long sessions, large output, handoffs, context pressure, and
careful pre-edit analysis.

Context Discipline helps Codex avoid drowning in its own working set. It favors
targeted reads, saved artifacts, summaries, search-first exploration, and
durable handoffs. For non-trivial code work, it pushes Codex to trace callers,
runtime paths, data contracts, render paths, persistence paths, and tests
before editing.

Use it when:

- The session is getting long.
- Tool output is too large.
- You need a handoff.
- The task spans many files.
- A careless edit would be expensive.

## Hardgate Templates

**Good for:** designing enforcement gates without installing active enforcement
by surprise.

Hardgate Templates helps design policy checks, final-response checks, preflight
scripts, hook templates, or release gates. In v0.1b, these are inert templates.
They describe what a gate should enforce, how it should pass, how it should
fail, how to test it, and how to avoid overfiring.

Use it when you want a gate design before deciding whether to install active
enforcement.

## Choosing The Right Skill

Use **Audit Lite** for one fix.

Use **Audit Full** for release readiness.

Use **Walkthrough** for UI wiring.

Use **Agent Pipeline** for structured multi-stage work.

Use **Prompt Quality** for prompt and eval work.

Use **Context Discipline** when the session itself is becoming a risk.

Use **Hardgate Templates** when you need enforcement design, not enforcement
surprises.

## Beta Notes

v0.1b is intentionally honest: the plugin is installable and validated, but the
suite should improve through real project use. The best future improvements are
more trigger regression cases, tighter output contracts, and examples from
successful audits and walkthroughs.
