# tau_to_tml.py — Convert parsed Boolean ASTs into .tml rules

def emit_tml(ast, head="conclusion"):
    """Convert a Boolean AST into a Tau Meta-Language (TML) rule."""
    body = flatten_logic(ast)
    return f"{normalize(head)}() :- {', '.join(body)}."

def flatten_logic(ast):
    """Flatten AST into a list of TML logic body components."""
    if isinstance(ast, str):
        return [normalize(ast)]
    elif isinstance(ast, dict):
        if "not" in ast:
            return [f"not {normalize(ast['not'])}"]
        elif "and" in ast:
            return [item for part in ast["and"] for item in flatten_logic(part)]
        elif "or" in ast:
            return [f"({ ' ; '.join(flatten_logic(p)) })" for p in ast["or"]]
        elif "implies" in ast:
            return flatten_logic(ast["implies"]["if"])
    return []

def normalize(symbol):
    return symbol.strip().lower().replace("`", "").replace(",", "").replace(".", "")

# Example usage
if __name__ == "__main__":
    sample_ast = {
        "implies": {
            "if": ["condition_a", {"not": "condition_b"}],
            "then": "conclusion_c"
        }
    }

    print(emit_tml(sample_ast, head=sample_ast["implies"]["then"]))
