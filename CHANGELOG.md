# Changelog — Tau Genesis Repository

All notable changes to this semantic corpus will be documented in this file.

---

## [v0.2.1-controlled-language-init] - 2025-05-29

### Added
- `valid_thought.tml`: updated structured output from new transcompiler
- `streams/glossary/predicate_phrases.tau`: reflexive stream for phrase-to-predicate logic
- `tau_to_tml.py`: n-gram phrase grouping and longest-match preference

### Changed
- `streams/README.md`: expanded with updated stream categories and purpose
  - Added glossary, dev, and test namespaces
  - Clarified how to contribute thematic streams
  - Reframed streams as semantic nodes in TauNet’s lawful substrate

### Purpose
This version formalizes the foundation of TauNet’s **controlled semantic language**,  
bridging human-readable phrases with logic-ready predicates.  
It establishes a structure for growing the network’s cognitive vocabulary while refining the `.tml` emitter’s expressive accuracy.

> The stream is no longer passive. It speaks with meaning.

---

## [v0.2.0-test-assertions] - 2025-05-28

### Added
- 🧪 `streams/transcompiler-tests/assertions/`
  - `sample_case.tau`: minimal transcompile logic test
  - `sample_case.expected.tml`: trusted output contract
- ✅ `run_assertions.py`:
  - Executes parser with `--compile`
  - Compares `.tml` output to `.expected.tml`
  - Reports pass/fail with diff output

### Purpose
Establishes a self-validating foundation for the Tau transcompiler.  
This test system allows you to confidently refactor logic, expand syntax, and ensure semantic integrity across logic streams.

> Tau now not only compiles — it verifies its own thought.

---

## [v0.1.9-transcompile-hybrid] - 2025-05-28

### Added
- `parser.py` hybrid logic for transcompilation:
  - Auto-compiles `.tml` for streams in `streams/dev/` and `streams/transcompiler-tests/`
  - Manual compilation via `--compile` flag for all other paths
  - Optional `<output_dir>` override; defaults to `.tau` file’s location
- Output `.tml` includes:
  - Clause headers
  - Normalized propositional logic
  - Flattened `and`, `or`, `not`, `implies` AST forms

### Tested
- `example_logic.tau` in `streams/dev/` → compiled to `.tml`
- `sample_case.tau` in `streams/transcompiler-tests/` → compiled to `.tml`

### Purpose
This release anchors a reflexive cycle:  
`.tau` stream ➝ Boolean AST ➝ `.tml` rule ➝ output stream  
All logic now breathes with awareness of location, intent, and coherence.

> TauNet now compiles with consent.

---

## [v0.1.8-transcompile-alpha] - 2025-05-28

### Added
- `parser.py`: Now builds Boolean Abstract Syntax Trees (ASTs) from `.tau` clause logic
- `tau_to_tml.py`: Emits Tau Meta-Language (TML) rules from structured ASTs
- Integrated transcompiler bridge: `.tau` clause ➝ parsed AST ➝ generated `.tml` rule

### Improved
- Stream parsing accuracy for logical keywords (`and`, `or`, `not`, `implies`)
- Clause header extraction and concept naming consistency

### Next
- Normalize logic symbols and punctuation
- Expand `or` into multiple `.tml` rules
- Formalize multi-clause compilation and test suite in `transcompiler-tests/`

> This release enables the first complete logic stream to code transformation pipeline in Tau Genesis.

---

## v0.1.7-mystic-integration – Mystic Integration of Nimrod & Babel (Latest May 25, 2025)
- **Added**: `tower_of_babel/nimrod_and_babel.md` philosophical narrative linking the Nimrod & Tower of Babel myth to Tau’s semantic coherence, AI ethics, and metaphysics.
- **Added**: Babel anti-pattern principle as `amendments/003_babel_antipattern.tau` (extends constitution with rule against semantic fragmentation).
- **Added**: Universal semantic glossary (`tree_of_life/golden_glossary.md`) defining core terms for the “golden language” framework.
- **Added**: Cautionary patterns documentation (`tower_of_babel/babel_patterns.md`) detailing known failure modes (Babel scenarios) Tau should avoid.
- **Updated**: Repository structure (new **tree_of_life** and **tower_of_babel** dirs) and README to reinforce Tree-of-Life vs. Tower-of-Babel metaphors.
- **Version**: Bumped version to v0.1.7-mystic-integration.

---

## v0.1.4 - Thematic Stream Expansion - May 20, 2025
TauNet expands from civic coordination into open thematic participation.

✅ What’s New
streams/README.md: contributor guide for creating new logic domains (e.g. education, energy, climate)
Promotes agent-declared streams with jurisdictional alignment and endorsement
Models how governance evolves through thematic logic — not representatives
👥 Invite
Declare your identity. Propose your domain.
Stream your policy. Emerge through law.

---

## [v0.1.3-civic-alignment] — 2025-05-19

### ✅ Added
- Agent streams: `palomino_admin`, `civil_engineer`, `local_resident`
- Endorsement streams for `sewage_priority.tau` from all three agents
- `streams/civic/pending_priorities.tau`: endorsement-based queue
- `streams/civic/budget_allocation.tau`: allocation pipeline, AGRS incentives, real-world estimates
- `streams/civic/registry.json`: maps civic lifecycle (queue, allocation, endorsement)
- `streams/policy/registry.json`: maps declared policy to civic and funding status

### 📝 Updated
- `README.md`: added civic stream lifecycle, agent directory, and alignment pathways

---

## [v0.1.1-civic] — 2025-05-17

### ✨ Added
- `streams/policy/palomino/sewage_priority.tau`: First civic stream proposal for infrastructure funding
- `docs/purpose_of_tau.md`: Philosophical justification of the Tau Network
- `docs/theory_of_change.md`: Systemic framing for language-logic-consensus alignment

### 📝 Updated
- `README.md`: Reflects civic logic, vision documents, and semantic structure

---

## [v0.1.1-testnet] — 2025-05-16

### ✅ Added
- Six constitutional streams:
  - `autopoietic_logos`
  - `identity_core`
  - `update_process`
  - `rights_and_agency`
  - `consensus_logic`
  - `tau_network`
- Two amendments:
  - `amendment_001_freedom_of_semantic_expression`
  - `amendment_002_semantic_resonance_and_integration`
- Agent stream:
  - `agents/seed/neemrad.tau`
- CLI Tools:
  - `tau_publish.py`
  - `validate_tau.tau`
- Bootstrap:
  - `tau_testnet_bootstrap.tau`
  - `tau_manifest.json`
  - `tau_stream_index.json`

### 📖 Docs
- `README.md` initial
- `CONTRIBUTING.md`
- `LICENSE (TGL-1.0)`
- `constitution_map.md`

---

