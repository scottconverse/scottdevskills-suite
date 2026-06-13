# Migration Notes

## Included In V1

- `audit-lite` from codex-audit-skills.
- `audit-full` from codex-audit-skills.
- `walkthrough` from the local Codex walkthrough skill.
- `agent-pipeline` and stage skills from the namespaced Agent Pipeline for
  Codex plugin.
- `prompt-quality` from prompttools and promptlint patterns.
- `context-discipline` from careful-coding, context-mode, efficiency, and
  handoff patterns.
- `hardgate-templates` from hardgate concepts, shipped inert.

## Deliberately Not Included

- Legacy duplicate full-audit aliases are not shipped. Use `audit-full`.
- Civic, patent, Amazon, and app/product domain suites: keep as domain packs.
- Claude/Cowork/Antigravity-specific launch mechanics: harvest concepts only.
- Active hooks: not enabled in v1.

## Porting Rule

When harvesting from older repos, preserve the behavior pattern but rewrite the
skill for Codex surfaces, Codex tools, and suite output contracts.
