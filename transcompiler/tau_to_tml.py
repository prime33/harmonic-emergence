import json
import os

GLOSSARY_PATH = "streams/glossary/phrases_index.json"

def load_phrase_map():
    if os.path.exists(GLOSSARY_PATH):
        with open(GLOSSARY_PATH) as f:
            return json.load(f)
    else:
        return {}

PHRASE_MAP = load_phrase_map()

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
        token = tokens[i]

        if isinstance(token, list):
            # recurse on nested list
            lines.extend(group_phrases(token, var))
            i += 1
            continue

        match = None
        max_len = 0

        for size in (3, 2, 1):
            if i + size <= len(tokens):
                phrase_tokens = tokens[i:i+size]
                if all(isinstance(t, str) for t in phrase_tokens):
                    phrase = " ".join(phrase_tokens)
                    if phrase in PHRASE_MAP:
                        match = PHRASE_MAP[phrase]
                        max_len = size
                        break

        if match:
            lines.append(f"{match}({var})")
            i += max_len
        else:
            lines.append(symbol_to_predicate(token, var))
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
