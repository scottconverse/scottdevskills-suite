# ScottDevSkills Suite

Codex-native development skills for evidence-first software work.

The installable plugin lives at `plugins/scott-dev-skills`. It contains lean
skill entrypoints plus on-demand references for audits, UI walkthroughs,
manifest-driven pipeline runs, prompt quality checks, context discipline, and
optional gate templates.

V1 intentionally does not ship old duplicate names such as `audit-team`, and it
does not include domain packs for civic, patent, Amazon, or product-specific
workflows.

## Installation

ScottDevSkills is distributed as a Codex marketplace repo. Add the
`scottconverse/scottdevskills-suite` marketplace in Codex, then install the
`scott-dev-skills` plugin from the `scottdevskills` marketplace.

The marketplace file lives at `.agents/plugins/marketplace.json`, and the
plugin package lives at `plugins/scott-dev-skills`.

After installation, start a fresh Codex thread so the newly installed skills are
loaded into the session.
