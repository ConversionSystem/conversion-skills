# Connectors and the Operator

Conversion OS runs with zero connectors by default. You paste, you upload, the skills work. Connectors are optional accelerators that let the OS read from your live tools and let the daily operator keep the vault current on its own.

## What a connector is

A connector is a registered link to an outside tool: a meeting transcriber, a chat app, an inbox, a calendar, a CRM, an analytics source, a CMS. It is recorded in `_system/connectors.md` with its purpose, its scope, and its rate limits. Credentials never live in the vault. They live in a secret manager and are referenced by name.

## Register a connector

1. Run `/connect`. It walks you through adding one.
2. It writes a row to `_system/connectors.md`: which tool, what it reads or writes, the scope, and the rate or terms.
3. It stores nothing secret in the vault. The skill that uses the connector reads the credential from your secret manager at run time.
4. Every external read or write is logged to `_system/audit/`.

## Common connectors and what they need

| Connector | Purpose | Typically needs |
|-----------|---------|-----------------|
| Meeting transcripts | Pull call notes into `Operations/meetings/` | An API key or an export from your transcriber |
| Chat (Slack or similar) | Read channels for decisions and signals | A workspace token, scoped to named channels |
| Email | Read threads, draft replies | OAuth or an app password, read scope |
| Calendar | See the week, shape the day | OAuth, read scope |
| CRM | Sync deals into `Pipeline/` | An API key or a CSV export |
| Analytics | Real conversion and traffic numbers | An API key or an export |
| WordPress | Stage post drafts (`wp-publish`, `wp-refresh`) | A site URL and an application password, draft scope only |
| Image or ad data | Creative and spend data | A provider API key |

None of these are required. Each delivery skill works from a paste or an export if no connector is wired. A connector just removes the copy and paste, and replaces estimates with measured numbers.

## The daily operator

`/operator` generates a run that the OS executes on a schedule:

1. It reads the vault: context, the latest daily, recent meetings, the ledger.
2. It pulls from the connectors you enabled, inside a budget (so many reads, writes, transcripts, and messages per run).
3. It writes the day's synthesis into the daily note and routes durable facts to their homes.
4. It escalates the few decisions that need a human to one named contact.
5. It drafts anything outbound. It never sends, publishes, deletes, or contacts a client on its own.

Set the cadence (hourly, daily, custom) and the budget when you run `/operator`. If you have a scheduler, it wires the cron for you. If not, it gives you the cron line and the prompt to run.

## Security

Credentials stay out of the vault. `scripts/scan-secrets.sh` fails the build if one slips in. The operator respects the documented rate limits and terms of each source, and stops cleanly when a budget is hit.

By Angel Castro · AI & Automation Lead · linkedin.com/in/anglcstr
