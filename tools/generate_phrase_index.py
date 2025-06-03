import os
import re
import json
from pathlib import Path

glossary_dir = Path(__file__).resolve().parent.parent / "streams" / "glossary"
output_path = glossary_dir / "phrases_index.json"
source_streams = list(glossary_dir.glob("*.tau"))

phrase_map = {}

for stream in source_streams:
    with open(stream) as f:
        lines = f.readlines()

    phrase = alias = None
    for line in lines:
        if line.strip().startswith("phrase:"):
            phrase = line.split(":", 1)[1].strip().strip('"').lower()
        elif line.strip().startswith("alias:"):
            alias = line.split(":", 1)[1].strip().strip('"')
        if phrase and alias:
            phrase_map[phrase] = alias
            phrase = alias = None  # Reset for next pair

# Write the output index
with open(output_path, "w") as f:
    json.dump(phrase_map, f, indent=2)

print(f"✔️ Glossary index written to: {output_path} with {len(phrase_map)} entries.")
