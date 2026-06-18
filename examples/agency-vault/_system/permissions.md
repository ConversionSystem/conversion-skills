---
type: context
status: active
owner: system
reviewed: 2026-06-18
tags: [permissions, system]
confidential: false
source: Conversion OS Setup
generated: false
---

# _system/permissions.md · access control (agency)
Pairs AI-scoping with storage-layer ACLs + the `_system/audit/` trail.

| principal | role | clients | reads | writes |
|-----------|------|---------|-------|--------|
| steve | owner | all | all | all |
| dana | member | northwind | northwind | northwind |
| marco | contractor | acme-robotics | acme-robotics | acme-robotics |
