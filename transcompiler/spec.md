# Transcompiler Spec — TauLang Bridge Protocol

This document outlines the specification for converting `.tau` semantic streams into TauLang-executable Boolean logic.

---

## 🎯 Purpose

To allow `.tau` streams — written in declarative human-readable logic — to be compiled into `.tml` (Tau Meta Language) for execution and verification on TauNet.

---

## 🧱 Key Translation Units

| `.tau` Form                 | TML Equivalent                         |
|-----------------------------|----------------------------------------|
| declare concept "X".        | declare X                              |
| define "X" as: Y            | X := Y                                 |
| if (A) then (B)             | A → B                                  |
| requires: [foo, bar]        | all inputs must satisfy foo ∧ bar      |

---

## 🧠 Challenges

- Handling conditionals with `therefore`
- Tracing versioned clause ancestry
- Mapping stream references to identifiers
- Encoding `alignment_with_being` and value models

---

## 🔁 Transcompiler Phases

1. Parse `.tau` into AST of concepts, clauses, and metadata
2. Resolve references and dependencies
3. Emit propositional logic per clause
4. Generate `.tml` block for executable inference

---

## 🗓️ Next Milestones

- [ ] Transcompile `rights_and_agency.tau`
- [ ] Create clause diff visualizer
- [ ] Link agent stream trace to compiled block
