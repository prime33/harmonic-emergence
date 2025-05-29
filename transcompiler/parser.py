# parser.py — Tau Syntax Parser + Final Hybrid TML Generator

import re
import sys
import os
from tau_to_tml import emit_tml

def tokenize(source_code):
    tokens = re.findall(r'"[^"]*"|\b(?:stream|clause_\d+|define|as|and|or|not|implies|interface|provides|requires)\b|[a-zA-Z_][a-zA-Z0-9_]*|[\[\](){}.,:]', source_code)
    return tokens

def extract_clauses(source_code):
    pattern = r"(clause_\d+ v[0-9.]+:\s+define\s+\".*?\"\s+as:\s+.*?)(?=\nclause_|\ninterface|\Z)"
    matches = re.findall(pattern, source_code, re.DOTALL)
    clauses = []
    for m in matches:
        header = re.search(r"(clause_\d+ v[0-9.]+):", m).group(1)
        definition = re.search(r"define\s+\"(.*?)\"\s+as:\s+(.*)", m, re.DOTALL)
        logic = definition.group(2).strip().replace("\n", " ")
        ast = parse_logic(logic)
        tml = emit_tml(ast, head=definition.group(1).strip())
        clauses.append({
            "id": header,
            "concept": definition.group(1).strip(),
            "logic": logic,
            "ast": ast,
            "tml": tml
        })
    return clauses

def parse_logic(expr):
    expr = expr.replace("(", " ( ").replace(")", " ) ").strip()
    tokens = expr.split()
    return parse_implication(tokens)

def parse_implication(tokens):
    if "implies" in tokens:
        i = tokens.index("implies")
        return {
            "implies": {
                "if": parse_or(tokens[:i]),
                "then": parse_or(tokens[i+1:])
            }
        }
    return parse_or(tokens)

def parse_or(tokens):
    if "or" in tokens:
        parts = []
        current = []
        for token in tokens:
            if token == "or":
                parts.append(parse_and(current))
                current = []
            else:
                current.append(token)
        parts.append(parse_and(current))
        return {"or": parts}
    return parse_and(tokens)

def parse_and(tokens):
    if "and" in tokens:
        parts = []
        current = []
        for token in tokens:
            if token == "and":
                parts.append(parse_not(current))
                current = []
            else:
                current.append(token)
        parts.append(parse_not(current))
        return {"and": parts}
    return parse_not(tokens)

def parse_not(tokens):
    if tokens and tokens[0] == "not":
        return {"not": tokens[1]}
    return tokens[0] if len(tokens) == 1 else tokens

def write_tml(output_path, clauses):
    with open(output_path, "w") as f:
        for clause in clauses:
            f.write(f"# {clause['id']} — {clause['concept']}\n")
            f.write(clause["tml"] + "\n\n")

def should_auto_compile(path):
    return (
        "streams/dev/" in path or
        "streams\\dev\\" in path or
        "streams/transcompiler-tests/" in path or
        "streams\\transcompiler-tests\\" in path
    )

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 parser.py <file.tau> [--compile [<output_dir>]]")
        sys.exit(1)

    file_path = sys.argv[1]
    output_path = None

    if "--compile" in sys.argv:
        compile_index = sys.argv.index("--compile")
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        if compile_index + 1 < len(sys.argv) and not sys.argv[compile_index + 1].startswith("--"):
            output_dir = sys.argv[compile_index + 1]
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, base_name + ".tml")
        else:
            output_path = os.path.join(os.path.dirname(file_path), base_name + ".tml")

    elif should_auto_compile(file_path):
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        output_path = os.path.join(os.path.dirname(file_path), base_name + ".tml")

    with open(file_path, "r") as f:
        source = f.read()

    tokens = tokenize(source)
    print("Tokens:", tokens)
    print()

    clauses = extract_clauses(source)
    for clause in clauses:
        print(f"Clause ID: {clause['id']}")
        print(f"Concept: {clause['concept']}")
        print(f"Logic: {clause['logic']}")
        print("AST:", clause['ast'])
        print("TML:", clause['tml'])
        print("---")

    if output_path:
        write_tml(output_path, clauses)
        print(f"\nTML written to: {output_path}")
