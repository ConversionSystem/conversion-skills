# Confidentiality, Permissions, and Data Ownership

## You own your data
The vault is plain markdown in your folder, in your git repo. No database, no lock-in. You read, move, or export everything at any time. Agency clients get an ownership and export story, so a client vault survives the agency leaving.

## The agency firewall
Each client lives in `Clients/{slug}/`, and every file there is `confidential: true`. The rules:
- Work one client at a time. Read only that client's folder.
- Never open a sibling `Clients/{slug}/`.
- Ambiguous items go to `Inbox/` for a human to route. Never guessed into a client folder.
- Client deliverables use the client's voice, never the agency's.

`scripts/check-firewall.sh` enforces this. It fails the build if any client file references a sibling client, or if confidential client material appears outside a `Clients/` workspace. In test V4 a planted cross-client reference was caught and removed.

## Permissions are layered, and labelled honestly
1. AI scoping. `Team/{person}/access.md` and `_system/permissions.md` control what the AI loads for a given person.
2. Storage ACLs. Shared-drive and git-repo permissions are the real boundary. For hard isolation, an agency uses a separate repo per client.
3. Audit trail. External reads and writes log to `_system/audit/`. The Operator stamps its edits `CS // OPERATOR`, so human and agent edits are distinct.

We never call AI scoping encryption or hard access control.

## Secrets
Credentials never live in the vault. `Company/stack.md` lists the tools and who owns them. Not passwords, not tokens. `scripts/scan-secrets.sh` fails the build if a credential is found.

## Human-approval gates
The OS never sends a message, publishes content, deletes a file, changes pricing, edits permissions, or contacts a client on its own. Outbound is drafted `status: draft` and escalated to the contact in `_system/config.md`.

By Angel Castro · AI & Automation Lead · linkedin.com/in/anglcstr
