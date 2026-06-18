---
name: mcp-builder
description: Scaffold a runnable MCP server from a described capability with typed tools, transport, and skeleton code, triggered by "build an MCP", "scaffold MCP server", or "wrap this API as a tool"
---

# MCP Builder

Turn a described capability into a runnable MCP server skeleton: named tools, typed inputs and outputs, a chosen transport, and code that runs. Written to Projects/ as a draft, credentials kept out of the code.

## When to use
- You want to expose an API, a script, or an internal process to Claude as callable MCP tools.
- You have a capability in mind ("look up an order", "post a draft", "query a report") and need the server stubbed out.
- You want a clean starting repo before wiring real logic, with the tool contract pinned down first.

## Inputs
- Capability description: what the server should do, in one or two sentences.
- Tool list: for each tool, a name, what it does, its inputs (name, type, required), and what it returns.
- Transport: stdio (local, default) or streamable HTTP (remote).
- Runtime: Node (TypeScript) or Python. Default Node.
- Auth shape, if any: which env vars the real logic will read (names only, never values).

## Process
1. Read Company/profile.md and Company/stack.md for naming and runtime preferences. Ask only for the tool contract if it is missing.
2. Pick a slug from the capability (kebab-case). Create Projects/{slug}/ with brief.md, data/, and final/.
3. Write Projects/{slug}/brief.md: the capability, the tool table (name, inputs, types, required, returns), transport, runtime, and the env var names auth will use.
4. Define the tool contract. For each tool, write a JSON Schema for inputs and a short description of the return shape. Keep names verb-first and specific.
5. Scaffold the server under Projects/{slug}/final/:
   - Node: package.json, tsconfig.json, src/index.ts registering each tool, src/tools/{tool}.ts stubs that validate input and return a typed placeholder, .env.example with credential names only.
   - Python: pyproject.toml, server.py registering each tool, tools/{tool}.py stubs, .env.example with names only.
6. Wire the transport: stdio by default, or an HTTP entry point if remote was requested. Add a README.md with run, inspect, and connect steps.
7. Add a .gitignore that excludes .env and any local secret files. Confirm no real credentials appear in any file.
8. Write Projects/{slug}/final/CHECKLIST.md: each tool, its inputs, and a one-line manual test for each.
9. Append one row to Memory/kpi-ledger.md recording the scaffold (see Outputs).

## Outputs
- Projects/{slug}/brief.md · capability, tool contract table, transport, runtime, env var names.
- Projects/{slug}/final/ · runnable server skeleton (package.json or pyproject.toml, entry point, per-tool stubs, README.md, .env.example, .gitignore, CHECKLIST.md).
- Memory/kpi-ledger.md · one appended row: | {date} | mcp_scaffolded | 0 | 1 | 1 | mcp-builder | high | {slug}, {tool count} tools, {transport} |

## Guardrails
- DRAFT-ONLY. Code lands in Projects/{slug}/final/ as a starting point, not a deployed service.
- Credentials never in code. Only env var names go in .env.example; real values stay outside the vault.
- PROVENANCE: the README states what is stubbed and what the caller must implement. Do not claim tools work before logic is wired.
- Tool stubs return clearly marked placeholders, so a half-built server cannot be mistaken for a finished one.
- .gitignore must exclude .env before any commit.

## References
- _system/connectors.md · where the finished server is registered as an optional connector.
- Company/stack.md · runtime and naming preferences.
