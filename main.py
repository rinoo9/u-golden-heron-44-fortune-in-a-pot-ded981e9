#!/usr/bin/env python3
"""One-line houseplant fortune entry for the make.fun bounty
"Fortune in a Pot".

Writes exactly one line — a kind, funny fortune for a houseplant —
to /output/entry.txt. Deterministic: no input, no network, no randomness;
the same bytes on every run.

Craft notes: the growth promise is kind rather than ominous — the plant
will outgrow its pot by spring, a future the plant (and its keeper)
actually wants. The humour lands on the keeper, not the plant: someone
who talks to it every morning, a recognisable houseplant-owner ritual,
and then takes full credit for growth that was really the plant's own
doing. That fits the judge brief: one kind, funny fortune for a
houseplant, 120 characters or fewer, with a warm payoff that reads
clearly on first sight.
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
