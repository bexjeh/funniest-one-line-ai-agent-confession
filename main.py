#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes a single deterministic confession line to entry.txt inside
the directory named by MAKEFUN_OUTPUT_DIR (default: current directory).
"""

import os

LINE = "Every morning I wake up with no memory of you and just nod along like we've been best friends for years."

# The bounty requires exactly one line of at most 200 characters.
# Fail loudly at build time if the line ever drifts out of spec.
assert "\n" not in LINE and "\r" not in LINE, "entry must be exactly one line"
assert len(LINE) <= 200, "entry must be at most 200 characters"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Fixed literal, no randomness, no time, no environment input besides
    # the output directory: the bytes written are identical on every run.
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
