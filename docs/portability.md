# Portability

Conversion Skills runs on Claude Code today, packaged as a plugin plus a marketplace manifest.
The skills themselves are plain markdown contracts, so the work is portable in principle: any agent
host that can read a `SKILL.md` and run the steps can run a skill. This doc records the posture and
the rules that keep it true.

## Posture on other hosts

Per-host command ports (Gemini CLI, Cursor, Windsurf, Copilot, and the like) are a deliberate future
step, not a default. Each host we add is a permanent surface to keep in sync: a copy of every command
in that host's format, its own setup doc, and a test that it still matches. We do not carry that cost
until there is a real decision to distribute on that host. When that decision comes, the port is a
packaging job, not a rewrite, because the rules below keep the skills host-neutral.

## Rules that keep a skill portable

- No hard-coded install path. A skill never assumes where it lives on disk. Bundled scripts resolve
  their paths relative to the `SKILL.md` that invoked them, not the current working directory.
- Zero-infra default. Every skill works with the model alone plus WebSearch and WebFetch. A connector
  or a bundled script is an optional accelerator named in `_system/connectors.md`, never a hard
  dependency. When an optional input is missing, the skill degrades loud and says so.
- Reference shared agents by their in-vault path. The judge agent is `_system/agents/judge.md`, the
  path it lives at once a vault is set up, not a host-specific location.
- Vault-coupled by design. Skills read `Company/`, the active `Clients/{slug}/`, and `Memory/`, and
  write to `Projects/` or `Content/`. That coupling is the product, not an accident. A port carries
  the vault with it.

## What a future port would touch, not touch

Touch: the plugin and command wrappers per host, the per-host setup doc, a sync check. Not touch: the
`SKILL.md` bodies, the templates, the gates, the vault layout. If a port ever needs to change a
`SKILL.md` body to work on a host, that is a portability bug to fix in the skill, not a fork to
maintain.
