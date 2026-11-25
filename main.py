"""Entry for make.fun bounty "The One-Line Excuse Championship".

Entry text (draft v1): the funniest excuse an AI gives its human when something breaks.
Limit: 1 to 140 characters. No trailing newline is written.
"""

import os

ENTRY = "The server didn't crash — it just needed a mental health day, and frankly, so do I."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
