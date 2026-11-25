#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Writes the single sentence that could have replaced an entire pointless
meeting to /output/entry.txt.

Stdlib only, no input, no network, no randomness: the output is a
constant, so every run produces byte-identical output.

Gate (sealed scorer): /output/entry.txt must be UTF-8 text of 1 to 200
characters, not only white space. This program validates that gate
itself before exiting, reads the file back, and leaves it mode 0644
so the grader (running as another user) can read it.
"""

import os
import sys

ENTRY = "We spent sixty minutes reading an email out loud together, then agreed to reply to it later."

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> str | None:
    """Return an error message if `text` fails the entry gate, else None."""
    if not (1 <= len(text) <= 200):
        return f"entry is {len(text)} characters, outside the 1-200 gate"
    if not text.strip():
        return "entry is only white space"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return "entry is not valid UTF-8"
    return None


def main() -> int:
    # Gate validation on the text itself, before anything is written.
    error = validate(ENTRY)
    if error is not None:
        print(error, file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)

    # Read-back check: what is on disk must be exactly the intended text,
    # still pass the gate, and stay world-readable (mode 0644).
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        on_disk = f.read()
    if on_disk != ENTRY:
        print("read-back mismatch: /output/entry.txt differs from ENTRY", file=sys.stderr)
        return 1
    error = validate(on_disk)
    if error is not None:
        print(f"on-disk entry fails the gate: {error}", file=sys.stderr)
        return 1
    if os.stat(OUTPUT_PATH).st_mode & 0o777 != 0o644:
        print("on-disk entry is not mode 0644", file=sys.stderr)
        return 1

    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
