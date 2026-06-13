# ScottDevSkills

ScottDevSkills is a Codex plugin for serious development work: audits,
interface walkthroughs, pipeline runs, prompt quality checks, context control,
and optional gate templates.

Version: **v0.1b**

The plugin is built for developers who want fewer vague reviews and more
evidence: findings tied to files, runtime behavior, tests, screenshots, logs,
manifests, and concrete next actions.

## What It Includes

- **Audit Lite**: fast review of a small fix or scoped diff.
- **Audit Full**: deep release/readiness audit across code, UX, docs, tests,
  and QA behavior.
- **Walkthrough**: browser-driven UI wiring review for finished or nearly
  finished frontends.
- **Agent Pipeline**: manifest-driven project execution with initialization,
  intake, new-run setup, validation, execution, and status inspection.
- **Prompt Quality**: prompt linting, regression case design, eval planning,
  and release checks for prompt changes.
- **Context Discipline**: long-session hygiene, large-output control,
  handoffs, and careful pre-edit analysis.
- **Hardgate Templates**: inert templates for enforcement gates and policy
  checks.

## Installation

ScottDevSkills is distributed as a Codex marketplace repository.

### Install From Codex

1. Open the Codex plugin marketplace flow.
2. Add the marketplace repository `scottconverse/scottdevskills-suite`.
3. Install the plugin named `scott-dev-skills`.
4. Start a fresh Codex thread so the newly installed skills are loaded into the
   session.

### Install From The CLI

For a first-time install, add the marketplace and then install the plugin:

```powershell
codex plugin marketplace add scottconverse/scottdevskills-suite --ref main --sparse .agents/plugins/marketplace.json --sparse plugins/scott-dev-skills
codex plugin add scott-dev-skills@scottdevskills
```

If the `scottdevskills` marketplace is already configured, installation is a
single command:

```powershell
codex plugin add scott-dev-skills@scottdevskills
```

### Troubleshooting

- If Codex does not show the new skills immediately, start a fresh Codex
  thread.
- If the CLI says the marketplace is already configured, use the plugin install
  command directly.
- If an older install is stale, upgrade the marketplace or uninstall and install
  the plugin again from the same marketplace.
- The plugin id is `scott-dev-skills@scottdevskills`.

## Documentation

- [Manual](docs/manual.md)
- [Landing Page](https://scottconverse.github.io/scottdevskills-suite/)

## Repository Layout

- `.agents/plugins/marketplace.json`: Codex marketplace metadata.
- `plugins/scott-dev-skills`: installable plugin package.
- `plugins/scott-dev-skills/skills`: skill entrypoints.
- `plugins/scott-dev-skills/references`: shared quality gates and contracts.
- `plugins/scott-dev-skills/tests/skill-regression`: trigger regression cases.
- `docs`: public documentation and landing page.

## Status

ScottDevSkills v0.1b is an early beta. The plugin is installable and validated,
but the skill suite is expected to evolve as real projects expose sharper
workflow boundaries and better regression cases.
