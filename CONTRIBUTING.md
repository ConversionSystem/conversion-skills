# Contributing

## Add or change a skill
1. Write `skills/{name}/SKILL.md` in the house style: two-key frontmatter (`name`, `description`), then the sections When to use, Inputs, Process, Outputs, Guardrails, References.
2. The `description` is one line, no colon, with natural trigger phrases.
3. Run `./scripts/sync-skills.sh`. It validates every skill, regenerates `SKILLS.md` and `docs/commands.md`, and runs all six gates.
4. Open a pull request. CI runs the same gates. A red gate blocks the merge.

## Discipline sections (heavy skills)
Audits and high-stakes skills carry three extra sections before References. `scripts/check-sections.sh` requires them on the tagged list (the audits, `business-review`, `pipeline-review`, `churn-watch`, `client`, `operator`, `optimizer`, `win-loss`, `portfolio-watch`, `crm-mining`):
- **Red flags** · 4 to 6 self-detectors, signs the run is going wrong.
- **Verification** · a checklist of observable exit criteria. "Seems right" is never enough.
- **Rationalizations** · a two-column table, the excuse to the reality, that pre-arms the skill against skipping rigor.

## Optional skill mechanics
- **References.** A heavy skill may carry `skills/{name}/references/*.md` for detail instead of bloating `SKILL.md` (progressive disclosure).
- **User-only skills.** Add `disable-model-invocation: true` to the frontmatter so the skill fires only when a human runs it.
- **Bundled scripts.** A skill may ship `skills/{name}/scripts/` with a working engine; declare `allowed-tools: Bash` and keep a prose fallback so it still runs with no dependency.
- **Terms.** Reuse the canonical terms in `GLOSSARY.md`; do not redefine them per skill.

## The rules the gates enforce
- **Clean-room.** No foreign product names anywhere on the shipped surface.
- **Budgets.** Root `CLAUDE.md` 150 lines or fewer, folder routers 60 or fewer, context docs 150 or fewer.
- **Secrets.** No credentials in any file. They live in a secret manager.
- **Firewall.** No skill reads a sibling client. Client files are confidential.
- **Brand.** No em-dashes. No blocklist words. Read `BRAND.md` before writing copy.

## Voice
Numbers, not adjectives. Verbs, not nouns. Short sentences. Sign your work. See `BRAND.md`.
