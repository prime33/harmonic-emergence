import re
import json
import os
import argparse
from pathlib import Path

def parse_tau_v3_clause(text):
    lines = text.strip().splitlines()
    head = None
    phrases = []
    clause_name = lines[0].split()[0].strip(" ")
    description = ""
    for line in lines:
        if line.strip().startswith("stream_name"):
            head = line.split(":", 1)[1].strip()
        elif line.strip().startswith("description"):
            description = line.split(":", 1)[1].strip()
        elif ":" in line and "phrase_predicates" not in line:
            phrase, pred = line.split(":", 1)
            phrases.append((phrase.strip().strip('-" '), pred.strip()))
    return clause_name, head, description, phrases

def emit_tml_from_phrases(head, phrases, var="X"):
    if not phrases:
        return None
    body = [f"{pred}({var})" for _, pred in phrases if pred]
    return f"{head}({var}) :-\n  " + ",\n  ".join(body) + "."

def update_indexes(clause_name, stream_name, description, phrases):
    os.makedirs("index", exist_ok=True)

    stream_index_path = Path("index/stream_index.json")
    glossary_path = Path("index/glossary.json")

    if stream_index_path.exists():
        with open(stream_index_path) as f:
            stream_index = json.load(f)
    else:
        stream_index = {}

    if glossary_path.exists():
        with open(glossary_path) as f:
            glossary = json.load(f)
    else:
        glossary = {}

    if stream_name not in stream_index:
        stream_index[stream_name] = {
            "description": description,
            "provided_by": []
        }
    if clause_name not in stream_index[stream_name]["provided_by"]:
        stream_index[stream_name]["provided_by"].append(clause_name)

    for phrase, pred in phrases:
        if not phrase.startswith("clause_") and phrase:
            glossary[phrase] = pred

    with open(stream_index_path, "w") as f:
        json.dump(stream_index, f, indent=2)

    with open(glossary_path, "w") as f:
        json.dump(glossary, f, indent=2)

def compile_tau_file(file_path, emit_index=True):
    with open(file_path) as f:
        tau = f.read()

    all_clauses = tau.strip().split("\n\n")
    tml_out = []

    for block in all_clauses:
        if block.startswith("clause_") and "meta" not in block:
            clause_name, stream_name, description, phrases = parse_tau_v3_clause(block)
            if emit_index:
                update_indexes(clause_name, stream_name, description, phrases)
            tml = emit_tml_from_phrases(stream_name, phrases)
            if tml:
                tml_out.append(tml)

    return tml_out

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tau Transcompiler v3")
    parser.add_argument("file", help="Path to .tau stream")
    parser.add_argument("--compile", action="store_true", help="Compile stream to TML")
    args = parser.parse_args()

    if args.compile:
        results = compile_tau_file(args.file)
        full_tml = "\n\n".join(results)
        print(full_tml + "\n")
        out_path = Path(args.file).with_suffix(".tml")
        with open(out_path, "w") as f:
            f.write(full_tml + "\n")
        print(f"[✓] TML written to {out_path}")
