# Civic Streams — Participatory Policy and Budget Alignment

This directory contains declarative logic streams related to local governance, budget allocation, public proposals, and agent participation.

Each stream encodes a real or hypothetical policy as a logic stream (`.tau`) with semantic alignment, agent traceability, and budget sensitivity.

---

## 🔁 Workflow: From Proposal to Allocation

1. **Policy Proposal**
   - Example: `sewage_priority.tau`
   - A civic priority stream emits a public request (with justification)

2. **Queue Review**
   - Example: `pending_priorities.tau`
   - Community members and agents issue endorsements, forming an ordered priority queue

3. **Threshold Trigger**
   - When a proposal passes the required quorum, it enters the `budget_allocation` stream

4. **Allocation + Reward**
   - Proposal receives budget approval
   - AGRS rewards distributed to contributors, validators, and endorsers
   - Jurisdictional fund is updated

---

## 👤 Local Agent Streams

- `palomino_admin.tau`: Stream validator for municipal perspective
- `civil_engineer.tau`: Technical verifier of feasibility and cost
- `local_resident.tau`: Community signal for support and feedback

All agents declare identity via `identity_trace` and support streams via `endorsement_signal`.

---

## 🧠 Future Extensions

- `streams/civic/<town>/school_reform.tau`
- `streams/civic/<region>/energy_subsidy.tau`
- Agent identity groups (NGOs, DAO-funded councils)
