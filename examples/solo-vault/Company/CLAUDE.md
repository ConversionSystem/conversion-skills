---
type: context
status: active
owner: system
reviewed: 2026-06-18
tags: [router, company]
confidential: false
source: Conversion OS Setup
generated: false
---

# Company/ · local rules
Purpose: identity & slow-changing truth. Who we are, what we sell, who we serve.

## Read
- `profile.md`, `brand.md`, `offers.md`, `icp.md`, `strategy.md`, `stack.md`.
- `departments/` only exists on team/agency profiles.

## Write
- One concept per file. Update the file in place and bump `reviewed:`.
- Quote offers/pricing ONLY from `offers.md`; never invent.

## Never
- Never store credentials in `stack.md` (names of tools + owners only).
- Never exceed 150 lines per context doc (Optimizer enforces).

## Hand-off
- Identity truth lives HERE; metric truth lives in `Memory/kpi-ledger.md`.
