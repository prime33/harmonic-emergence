# tau_to_tml.py — Convert parsed Boolean ASTs into .tml rules (patched version)

def emit_tml(ast, head="conclusion"):
    """Convert a Boolean AST into a Tau Meta-Language (TML) rule."""
    body = flatten_logic(ast)
    body_clean = [normalize(b) for b in body if b]
    if not body_clean:
        return f"{normalize(head)}()."
    return f"{normalize(head)}() :- {', '.join(body_clean)}."

def flatten_logic(ast):
    """Flatten AST into a list of TML logic body components."""
    if isinstance(ast, str):
        return [ast]
    elif isinstance(ast, dict):
        if "not" in ast:
            return [f"not {ast['not']}"]
        elif "and" in ast:
            return [item for part in ast["and"] for item in flatten_logic(part)]
        elif "or" in ast:
            return [f"({ ' ; '.join(flatten_logic(p)) })" for p in ast["or"]]
        elif "implies" in ast:
            return flatten_logic(ast["implies"]["if"])
    elif isinstance(ast, list):
        return [item for sub in ast for item in flatten_logic(sub)] if any(isinstance(sub, list) for sub in ast) else ast
    return []

def normalize(symbol):
    if not isinstance(symbol, str):
        return str(symbol)
    return symbol.lower().replace("`", "").replace(",", "").replace(".", "").strip()

# Example usage
if __name__ == "__main__":
    sample_ast = {
        "implies": {
            "if": ["condition_a", {"not": "condition_b"}],
            "then": "conclusion_c"
        }
    }

    print(emit_tml(sample_ast, head=sample_ast["implies"]["then"]))
