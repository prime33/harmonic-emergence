# parser.py — Tau Syntax Parser (EBNF-driven)

import re

def tokenize(source_code):
    """Minimal tokenizer for .tau input."""
    tokens = re.findall(r'"[^"]*"|\b(?:stream|clause_\d+|define|as|and|or|not|implies|interface|provides|requires)\b|[a-zA-Z_][a-zA-Z0-9_]*|[\[\](){}.,:]', source_code)
    return tokens

def parse(tokens):
    """Stub parser: parses a list of tokens into basic clause trees (WIP)."""
    print("Tokens:", tokens)
    return {"parsed": "stream logic structure (todo)"}

if __name__ == "__main__":
    sample = """stream: streams.example.logic

clause_001 v0.1.0:
  define "example" as: A and not B implies C.

interface:
  provides: [example]
  requires: [A, B]
"""
    tokens = tokenize(sample)
    ast = parse(tokens)
    print(ast)
