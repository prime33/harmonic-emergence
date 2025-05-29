# tau_to_tml.py — Phrase-Aware Tau Meta-Language Emitter (N-Gram Matching)

PHRASE_MAP = {
    "preserves origin trace": "preserves_origin_trace",
    "aligns with defined concepts": "aligns_with_defined_concepts",
    "semantic structure": "semantic_structure",
    "prior reasoning": "prior_reasoning",
    "amendment status": "amendment_status",
    "thought coherence": "thought_coherence",
    "origin trace": "origin_trace",
    "reflexive integrity": "reflexive_integrity",
    "introduce terms": "introduce_terms",
    "violating integrity": "violating_integrity",
    "provides or requires interface": "provides_or_requires_interface"
}

def emit_tml(ast, head="conclusion", var="X"):
    body_lines = flatten_logic(ast, var)
    deduped = sorted(set(body_lines), key=lambda x: (len(x), x))
    if not deduped:
        return f"{normalize(head)}({var})."
    return f"{normalize(head)}({var}) :-\n  " + ",\n  ".join(deduped) + "."

def flatten_logic(ast, var):
    if isinstance(ast, str):
        return [symbol_to_predicate(ast, var)]
    elif isinstance(ast, dict):
        if "not" in ast:
            return [f"not {symbol_to_predicate(ast['not'], var)}"]
        elif "and" in ast:
            return flatten_logic(ast["and"], var)
        elif "or" in ast:
            parts = [" ; ".join(flatten_logic(opt, var)) for opt in ast["or"]]
            return [f"({p})" for p in parts]
        elif "implies" in ast:
            return flatten_logic(ast["implies"]["if"], var)
    elif isinstance(ast, list):
        return group_phrases(ast, var)
    return []

def group_phrases(tokens, var):
    lines = []
    i = 0
    while i < len(tokens):
        match = None
        max_len = 0
        # Try 3-gram, 2-gram, then 1
        for size in (3, 2, 1):
            if i + size <= len(tokens):
                phrase = " ".join(tokens[i:i+size])
                if phrase in PHRASE_MAP:
                    match = PHRASE_MAP[phrase]
                    max_len = size
                    break
        if match:
            lines.append(f"{match}({var})")
            i += max_len
        else:
            lines.append(symbol_to_predicate(tokens[i], var))
            i += 1
    return lines

def symbol_to_predicate(symbol, var):
    phrase = normalize(symbol)
    return f"{phrase}({var})"

def normalize(symbol):
    if not isinstance(symbol, str):
        return str(symbol)
    return (
        symbol.lower()
              .replace("`", "")
              .replace(",", "")
              .replace(".", "")
              .replace("’", "")
              .strip()
              .replace(" ", "_")
    )

# Example usage
if __name__ == "__main__":
    sample_ast = {
        "implies": {
            "if": [
                "preserves", "origin", "trace",
                {"not": "contradiction"},
                "aligns", "with", "defined", "concepts"
            ],
            "then": "valid_thought"
        }
    }
    print(emit_tml(sample_ast["implies"], head=sample_ast["implies"]["then"]))
