# Tau Transcompiler v3 — Stream Format

Each clause must include:

- `stream_name`: the logical head predicate
- `description`: human-readable purpose of the clause
- `phrase_predicates`: declared mappings from phrase → predicate

A `meta:` block can also declare:
- `provides`: list of logical streams this file outputs
- `requires`: list of upstream dependencies
