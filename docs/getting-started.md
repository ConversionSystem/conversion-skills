# Getting Started

Conversion OS is a folder of markdown files that Claude reads and writes. It holds your business context, a memory ledger, and 44 skills that do real work and record what moved. No database. No platform. You own the files.

This guide takes you from nothing to a populated, governed vault in about 10 minutes.

## 1. What you need

| Need | Detail |
|------|--------|
| Claude | Claude Code (terminal, desktop, or IDE) or Cowork. |
| A folder | Empty. Best inside a synced drive (Google Drive, Dropbox, iCloud) so it backs up and syncs. |
| Git | Optional, recommended. Your history and your undo button. Install from git-scm.com. |
| A database | None. The files are the database. Git is the journal. |
| API keys or connectors | Optional. Only if you wire the daily operator or a delivery skill to a live tool. See `connectors.md`. The default needs none. |

You do not need to be technical. If you can use a chat box and a folder, you can run this.

## 2. Install

Two ways. Pick one.

### A. Zero infra (fastest)
1. Make an empty folder, ideally in a synced drive.
2. Open Claude in that folder (Claude Code: `cd` into it, or open the folder in the desktop app).
3. Run `/setup`. That is it. Setup installs the structure as it goes.

### B. As a Claude Code plugin
1. Add the marketplace:
   ```
   /plugin marketplace add ConversionSystem/OS-AI
   ```
2. Install the plugin:
   ```
   /plugin install conversion-os@conversion-system
   ```
3. Open an empty folder and run `/setup`.

## 3. Pick a profile

`/setup` asks which one. One architecture, three shapes.

- **Solo.** One operator. Adds a sales pipeline.
- **Team.** People, roles, real permissions, an audit trail.
- **Agency.** Firewalled workspaces, one per client. No cross-client reads.

You can start Solo and grow into Team or Agency later. Nothing gets rebuilt. See `setup-guide.md`.

## 4. Your first 10 minutes

1. Run `/setup`.
2. Pick your profile.
3. Paste your website URL. Drop a few docs if you have them (a deck, a pricing page, an about page). Setup reads them first, so it confirms what it can infer instead of asking you to type it.
4. Answer a few short questions. One-liner, what you sell, who you serve, your voice, your top goal for the next 90 days. Every question is skippable.
5. Setup builds the vault, seeds your first KPI baselines, and hands you a first deliverable plus a report card that shows what is solid, thin, or missing.

## 5. What you get

A folder like this:

```
CLAUDE.md     the map. Claude reads it first every session.
_system/      config, rules, permissions, audit log.
Company/      who you are: profile, brand, offers, ICP, strategy, stack.
Memory/       the KPI ledger (append-only), decisions, lessons, glossary.
Pipeline/     deals, accounts, prospects (Solo and Team).
Projects/     internal work.
Content/      your published marketing.
Operations/   SOPs, meetings, reviews, tasks.
Daily/        one note per day, plus weekly reviews.
Library/      reusable playbooks, templates, prompts, your brand voice.
Inbox/        drop anything here, triage daily.
```

Agency adds `Clients/{name}/` (firewalled). Team adds `Team/{person}/`.

## 6. What to do next

- Tomorrow morning, run `/daily` for your brief and Top 3.
- Read `daily-use.md` for the operating rhythm.
- Read `commands.md` for the full list of what you can ask for.
- When you want the OS to update itself from meetings and email, read `connectors.md`.

## Troubleshooting

- **"Nothing happened when I typed /setup."** Make sure Claude is pointed at the folder, and that the plugin is installed (path B) or that you are running in Claude Code (path A).
- **"It is asking me a lot of questions."** Skip the ones you do not know. The report card tells you what to fill in later. You do not need a complete answer to start.
- **"I want to undo something."** If you used git, every session is a commit. Roll back to any point. This is why git is recommended.
- **"Where do my files live?"** In your folder. Open it in Finder or Explorer any time. They are plain markdown.

By Angel Castro · AI & Automation Lead · linkedin.com/in/anglcstr
