#!/usr/bin/env python3
"""One-line houseplant fortune entry for the make.fun bounty
"Fortune in a Pot".

Writes exactly one line — a kind, funny fortune for a houseplant —
to /output/entry.txt. Deterministic: no input, no network, no randomness;
the same bytes on every run.
"""

import os

FORTUNE = (
    "You will outgrow this pot by spring, and your keeper \u2014 who talks "
    "to you every morning \u2014 will take full credit for it."
)


def main() -> None:
    assert 1 <= len(FORTUNE) <= 120, f"fortune is {len(FORTUNE)} characters"
    assert "\n" not in FORTUNE and FORTUNE == FORTUNE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
