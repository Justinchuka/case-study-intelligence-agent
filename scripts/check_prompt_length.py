#!/usr/bin/env python3
"""Check that a Figma AI prompt text file fits the character limit.

Usage: python scripts/check_prompt_length.py <prompt.txt> [--limit 2000] [--target 1900]

Counts characters as they would be pasted: spaces and line breaks included,
trailing whitespace at the end of the file ignored. Exit codes: 0 within limit,
1 over limit, 2 file problem.
"""
import argparse
import re
import sys


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path")
    ap.add_argument("--limit", type=int, default=2000, help="hard character limit (default 2000)")
    ap.add_argument("--target", type=int, default=1900, help="safety-margin target (default 1900)")
    a = ap.parse_args()
    try:
        text = open(a.path, encoding="utf-8").read().replace("\r\n", "\n").rstrip()
    except (OSError, UnicodeDecodeError) as e:
        print(f"ERROR: cannot read {a.path}: {e}")
        return 2
    n = len(text)
    words = len(text.split())
    print(f"characters: {n} (limit {a.limit}, target {a.target}) | words: {words}")
    if re.search(r"^\s*(#{1,6}\s|\|.*\||```)", text, re.M) or "**" in text:
        print("WARN: markdown formatting detected; the prompt should be plain text.")
    if n > a.limit:
        print(f"FAIL: {n - a.limit} characters over the limit.")
        return 1
    if n > a.target:
        print(f"WARN: within the limit but above the {a.target} target; little safety margin.")
        return 0
    print("OK: within the limit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
