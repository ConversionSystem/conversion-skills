---
type: context
status: active
owner: system
reviewed: 2026-06-18
tags: [config, system]
confidential: false
source: Conversion OS Setup
generated: false
---

# _system/config.md — operating config

## Profile
profile: solo

## Operator
cadence: daily            # hourly | daily | twice-daily | custom-cron
escalation_contact: steve@conversionsystem.com
signature: "— Conversion Operator"   # stamp on agent-written edits

## Per-run budgets (hard caps; stop cleanly + escalate when hit)
reads: 40
writes: 25
transcripts: 15
emails: 25
dms: 3
housekeeping: 10
