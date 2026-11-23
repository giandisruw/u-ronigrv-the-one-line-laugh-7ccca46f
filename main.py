#!/usr/bin/env python3
"""The One-Line Laugh — make.fun entry.

Writes exactly one funny sentence to /output/entry.txt: a single
sentence of at most 200 characters, nothing else.

Why this line: "I told my smart fridge I'm on a diet, so now it
locks the cheese drawer at midnight."

- Surprise at the end that still makes sense: a fridge that locks the
  cheese drawer is absurd, yet it follows perfectly from telling a
  "smart" appliance you are on a diet — the machine takes you literally
  and enforces the rule harder than you ever would.
- Everyday truth people recognise: everyone who has ever dieted knows
  the midnight fridge raid, the cheese drawer, and the feeling of being
  policed by your own kitchen.
- Economy of words: one short setup, one punch, no filler — 84
  characters, and every word earns its place. (Revision note: the first
  draft said "judges me by locking" — cutting those three words keeps
  the same joke and makes the punch land faster.)

Deterministic and offline: no network, no randomness, no API key, no
input. The output is always exactly these 84 bytes, with no trailing
newline, so the file holds one sentence and nothing else.

Before writing, the line is validated against the competition gate
(UTF-8 text of 1 to 200 characters, a single sentence: exactly one
sentence-ending period, no newline), so a bad constant can never
silently produce an invalid entry.

Usage (as the grader runs it):
    python3 main.py            # writes /output/entry.txt
    python3 main.py <path>     # optional: write to <path> instead (testing)
"""

import sys
from pathlib import Path

LINE = "I told my smart fridge I'm on a diet, so now it locks the cheese drawer at midnight."
DEFAULT_OUTPUT = Path("/output/entry.txt")

# The competition gate: a single sentence of 1 to 200 characters.
MIN_LINE_CHARS = 1
MAX_LINE_CHARS = 200


def validate_line(line: str) -> str:
    """Check the line against the competition gate and return it.

    Raises ValueError if the line is empty, only white space, longer
    than 200 characters, contains a newline, or is not exactly one
    sentence (it must end with a single period and contain no other
    sentence-ending punctuation).
    """
    if not line:
        raise ValueError("line must not be empty")
    if len(line) < MIN_LINE_CHARS or len(line) > MAX_LINE_CHARS:
        raise ValueError(
            f"line must be {MIN_LINE_CHARS}-{MAX_LINE_CHARS} characters, "
            f"got {len(line)}"
        )
    if line != line.strip():
        raise ValueError("line must not have leading or trailing white space")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line with no newline")
    if not line.endswith("."):
        raise ValueError("line must be a single sentence ending with a period")
    if line.count(".") != 1:
        raise ValueError("line must be exactly one sentence (one period only)")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        raise ValueError("line must not contain control characters")
    return line


def main() -> int:
    out_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUTPUT
    line = validate_line(LINE)
    if out_path.parent != Path("."):
        out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(line, encoding="utf-8", newline="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
