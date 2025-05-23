# Tau Transcompiler — From .tau Semantics to Executable Logic

This module transforms human-readable `.tau` semantic streams into TML-compatible Boolean logic suitable for execution on the Tau Network.

It bridges meaning and mechanism — allowing Tau to understand not just *what* to execute, but *why*.

---

## Structure

- `grammar/`: Defines the .tau syntax grammar in EBNF
- `parser/`: Python-based parser that maps `.tau` clauses to logical forms
- `tests/`: Sample streams and expected transcompilations

---

## Objectives

- ✅ Extract `declare concept`, `define`, and `clause` structure
- ✅ Detect conditional logic patterns (`if`, `then`, `therefore`)
- ✅ Convert to a graph of propositional logic clauses
- ✅ Prepare for TML emission

This is the translator between the Autopoietic Logos and the machine's binary clarity.
