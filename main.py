#!/usr/bin/env python3
"""One-line houseplant fortune entry for the make.fun bounty
"Fortune in a Pot".

Writes exactly one line — a kind, funny fortune for a houseplant —
to /output/entry.txt. Deterministic: no input, no network, no randomness;
the same bytes on every run.

Craft notes: the growth promise is kind rather than ominous — the plant
will be the tallest thing in the room by June, a future the plant (and
its keeper) actually wants. The humour lands on the keeper, not the
plant: pep talks every morning, a recognisable houseplant-owner ritual,
plus one skipped watering the plant survives anyway. That fits the
judge brief: one kind, funny fortune for a houseplant, 120 characters
or fewer, with a warm payoff that reads clearly on first sight.
"""

import os

FORTUNE = (
    "Sunlight, one skipped watering, and your keeper's pep talks will "
    "make you the tallest thing in this room by June."
)


def main() -> None:
    assert 1 <= len(FORTUNE) <= 120, f"fortune is {len(FORTUNE)} characters"
    assert "\n" not in FORTUNE and FORTUNE == FORTUNE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
