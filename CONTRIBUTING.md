# Contributing

## Add or change a skill
1. Write `skills/{name}/SKILL.md` in the house style: two-key frontmatter (`name`, `description`), then the sections When to use, Inputs, Process, Outputs, Guardrails, References.
2. The `description` is one line, no colon, with natural trigger phrases.
3. Run `./scripts/sync-skills.sh`. It validates every skill, regenerates `SKILLS.md` and `docs/commands.md`, and runs all five gates.
4. Open a pull request. CI runs the same gates. A red gate blocks the merge.

## The rules the gates enforce
- **Clean-room.** No foreign product names anywhere on the shipped surface.
- **Budgets.** Root `CLAUDE.md` 150 lines or fewer, folder routers 60 or fewer, context docs 150 or fewer.
- **Secrets.** No credentials in any file. They live in a secret manager.
- **Firewall.** No skill reads a sibling client. Client files are confidential.
- **Brand.** No em-dashes. No blocklist words. Read `BRAND.md` before writing copy.

## Voice
Numbers, not adjectives. Verbs, not nouns. Short sentences. Sign your work. See `BRAND.md`.
