import os
import json
import hashlib
import argparse

INDEX_FILE = "tau_stream_index.json"
MANIFEST_FILE = "tau_manifest.json"

def sha256_hash(file_path):
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def validate_index(index_path, schema_path):
    try:
        import jsonschema
        with open(index_path) as f:
            index = json.load(f)
        with open(schema_path) as f:
            schema = json.load(f)
        jsonschema.validate(instance=index, schema=schema)
        print("✅ Index file is valid.")
        return index
    except Exception as e:
        print(f"❌ Validation error: {e}")
        return None

def build_manifest(index):
    manifest = {}
    all_paths = [index["genesis"]] + index["constitution"] + index["amendments"] +                 list(index["meta"].values()) + [index["docs"]] + index["tools"]
    for path in all_paths:
        if os.path.exists(path):
            manifest[path] = sha256_hash(path)
        else:
            manifest[path] = None
            print(f"⚠️  Warning: File not found: {path}")
    return manifest

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--index", default=INDEX_FILE, help="Path to stream index JSON")
    parser.add_argument("--schema", default="tau_stream_index.schema.json", help="Path to schema file")
    parser.add_argument("--out", default=MANIFEST_FILE, help="Output manifest file")
    args = parser.parse_args()

    index = validate_index(args.index, args.schema)
    if index:
        manifest = build_manifest(index)
        with open(args.out, "w") as f:
            json.dump(manifest, f, indent=2)
        print(f"✅ Manifest saved to {args.out}")

if __name__ == "__main__":
    main()
