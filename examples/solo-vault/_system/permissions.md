---
type: context
status: active
owner: system
reviewed: 2026-06-18
tags: [permissions, system]
confidential: false
source: Conversion Skills Setup
generated: false
---

# _system/permissions.md · access control

Solo profile: single owner, full access. This file becomes meaningful on the
Team/Agency profiles, where it pairs with storage-layer ACLs (shared-drive /
repo permissions) and the `_system/audit/` who-read/wrote trail.

| principal | role | reads | writes | clients |
|-----------|------|-------|--------|---------|
| owner | owner | all | all | n/a (solo) |
