# Tau Transcompiler Guide

This guide outlines how the Tau transcompiler converts `.tau` logic streams into Boolean-valid Tau Meta-Language (TML).

---

## 🧠 Compiler Architecture

1. **Parser**: Reads `.tau` syntax (`declare`, `define`, `clause`, `interface`)
2. **Semantic Mapper**: Converts clause structures into logical trees
3. **TML Generator**: Emits Horn clauses and TML-compliant Boolean structures
4. **NSO Handler**: (Planned) Enables `{clause}` references for meta-logical statements

---

## ✅ Supported .tau Clause Types

| Pattern            | Compiles to TML |
|--------------------|-----------------|
| Implication        | Yes             |
| Negation           | Yes             |
| Conjunction        | Yes             |
| Disjunction        | Via rewriting   |
| Clause reference   | Soon (NSO)      |

---

## 🔁 Stream Coherence Criteria

A `.tau` stream is semantically coherent if:

- All `provides` concepts are declared
- No circular dependencies in `requires`
- Each `clause` is logically satisfiable (non-contradictory)

---

## 🚧 TODO

- Stream-to-TML converter prototype
- NSO curly-brace `{...}` syntax support
- Recursive clause expansion rules
- Coherence scoring (trace, structure, ethics)
