# Naming Conventions for .tau Streams

## Concept Identifiers
- Use `snake_case` for all multi-word concept declarations.
- Do not use hyphens (`-`) in concept names, as they can be confused with operators.
- All declared `concept` terms should match exactly in `provides:` and `requires:` sections.

✅ Example:
    declare concept "semantic_consent".

❌ Avoid:
    declare concept "semantic-consent"

## Clause Identifiers
- Use `clause_### vX.Y.Z` format (e.g. clause_003 v0.1.0)
- Each clause must be uniquely indexed within a stream.

## Interfaces
- Declare `provides:` and `requires:` explicitly.
- Prefer named concepts over abstract placeholders.
