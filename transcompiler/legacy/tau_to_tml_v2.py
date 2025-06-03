import json
import os
import re

GLOSSARY_PATH = "streams/glossary/phrases_index.json"

IGNORE_TOKENS = {"the", "a", "of", "with", "and", "or", "to", "its", "own", "that", "which", "by", "in", ",", ".", ":", ";", "whose", "unless"}

def load_phrase_map():
    if os.path.exists(GLOSSARY_PATH):
        with open(GLOSSARY_PATH) as f:
            return json.load(f)
    return {}

def emit_tml(ast, head="conclusion", var="X"):
    phrase_map = load_phrase_map()

    def flatten_ast(node):
        if isinstance(node, str):
            return tokenize(node)
        elif isinstance(node, list):
            tokens = []
            for item in node:
                tokens.extend(flatten_ast(item))
            return tokens
        elif isinstance(node, dict):
            tokens = []
            if "not" in node:
                tokens.extend(["not"] + flatten_ast(node["not"]))
            elif "and" in node:
                for sub in node["and"]:
                    tokens.extend(flatten_ast(sub))
            elif "or" in node:
                parts = [" ; ".join(group_phrases(flatten_ast(opt), phrase_map, var)) for opt in node["or"]]
                return parts
            return tokens
        return []

    body = flatten_ast(ast)
    lines = group_phrases(body, phrase_map, var)
    if not lines:
        return None
    if isinstance(lines, list):
        return f"{head}({var}) :-\n  " + ",\n  ".join(lines) + "."
    return None

def tokenize(text):
    return re.findall(r"\w+|[.,:;]", text)

def symbol_to_predicate(word, var):
    return f"{word}({var})"

def group_phrases(tokens, phrase_map, var="X"):
    lines = []
    i = 0
    while i < len(tokens):
        matched = False
        for j in range(min(6, len(tokens) - i), 0, -1):
            phrase = " ".join(tokens[i:i+j]).lower()
            if phrase in phrase_map:
                lines.append(f"{phrase_map[phrase]}({var})")
                i += j
                matched = True
                break
        if not matched:
            token = tokens[i].lower()
            if token not in IGNORE_TOKENS and not token.endswith(f"({var})"):
                lines.append(symbol_to_predicate(token, var))
            i += 1
    return lines
