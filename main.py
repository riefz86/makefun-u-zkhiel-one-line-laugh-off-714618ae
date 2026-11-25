#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt.
The line must be 1-200 UTF-8 characters, a single joke that lands
on a cold read, with no setup notes and no explanation.
"""
import os

JOKE = "I fired my AI assistant today \u2014 it thanked me, updated its resume, and applied for my job. HR says it interviews better than I do."

def main():
    line = JOKE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars, must be 1-200"
    assert line == line.strip() and "\n" not in line
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod("/output/entry.txt", 0o644)
    print(line)
    print(f"({len(line)} characters)")

if __name__ == "__main__":
    main()
