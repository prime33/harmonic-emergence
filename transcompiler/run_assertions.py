import os
import subprocess
import difflib

ASSERTIONS_DIR = "streams/transcompiler-tests/assertions"

def run_parser_on_tau(tau_path):
    cmd = ["python3", "transcompiler/parser.py", tau_path, "--compile"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

def compare_files(actual_path, expected_path):
    with open(actual_path) as actual, open(expected_path) as expected:
        actual_lines = actual.readlines()
        expected_lines = expected.readlines()
        diff = list(difflib.unified_diff(expected_lines, actual_lines, fromfile='expected', tofile='actual'))
        return diff

def find_test_cases():
    return [
        fname for fname in os.listdir(ASSERTIONS_DIR)
        if fname.endswith(".tau")
    ]

if __name__ == "__main__":
    print("🧪 Running Tau Transcompiler Assertions...\n")
    failed = False

    for tau_file in find_test_cases():
        base = tau_file.replace(".tau", "")
        tau_path = os.path.join(ASSERTIONS_DIR, tau_file)
        expected_path = os.path.join(ASSERTIONS_DIR, f"{base}.expected.tml")
        actual_path = os.path.join(ASSERTIONS_DIR, f"{base}.tml")

        run_parser_on_tau(tau_path)

        if not os.path.exists(expected_path) or not os.path.exists(actual_path):
            print(f"❌ Missing files for {base}")
            failed = True
            continue

        diff = compare_files(actual_path, expected_path)
        if diff:
            print(f"❌ {base}.tau failed:\n" + "".join(diff))
            failed = True
        else:
            print(f"✅ {base}.tau passed.")

    if failed:
        print("\nSome tests failed. Please review differences.")
    else:
        print("\nAll tests passed successfully.")
