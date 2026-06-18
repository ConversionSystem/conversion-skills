# Confidentiality, Permissions & Data Ownership

## You own your data
The vault is plain markdown in **your** folder, versioned in **your** git repo. No database, no platform lock-in. You can read, move, or export everything at any time. (Agency clients get an ownership/export story so a client vault survives the agency leaving.)

## The agency firewall (Agency profile)
Each client lives in `Clients/{slug}/`, and every file there is `confidential: true`. The rules:
- Work one client at a time; read **only** that client's folder.
- **Never** open a sibling `Clients/{slug}/`.
- Ambiguous items go to `Inbox/` for a human to route — never guessed into a client folder.
- Client deliverables use the client's voice, never the agency's.

This is enforced mechanically by **`scripts/check-firewall.sh`**, which fails if any client file references a sibling client or if confidential client material appears outside a `Clients/` workspace.

## Permissions are layered (and honestly labelled)
1. **AI-scoping** — `Team/{person}/access.md` and `_system/permissions.md` control what the AI loads for a given person.
2. **Storage ACLs** — shared-drive / git-repo permissions are the real access boundary. For hard isolation, an agency can use a separate repo per client.
3. **Audit trail** — external reads/writes are logged to `_system/audit/`, and the Operator stamps its own edits so human vs. agent edits are distinguishable.

We never market AI-scoping as encryption or hard access control.

## Secrets
Credentials never live in the vault. `Company/stack.md` lists *what tools exist and who owns them* — not passwords or tokens. `scripts/scan-secrets.sh` fails the build if a credential is found.

## Human-approval gates
The OS never autonomously sends messages, publishes content, deletes files, changes pricing/offers, edits permissions, or contacts clients. Anything outbound is drafted `status: draft` and escalated to the contact in `_system/config.md`.
