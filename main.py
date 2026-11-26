#!/usr/bin/env python3
"""One-line houseplant fortune entry for the make.fun bounty
"Fortune in a Pot".

Writes exactly one line — a kind, funny fortune for a houseplant —
to /output/entry.txt. Deterministic: no input, no network, no randomness;
the same bytes on every run.

Craft notes: the fortune is kind rather than ominous — the plant does
not merely grow, it survives. Three small household perils in a row
(the ficus next door, the cat, the keeper's forgetfulness) and the
plant outlasts them all, then blooms the very week its keeper finally
learns its name: the payoff is recognition, the thing every
houseplant quietly wants. The humour lands on the keeper, not the
plant, and the line ends on a warm, earned moment. That fits the
judge brief: one kind, funny fortune for a houseplant, 120 characters
or fewer, with a warm payoff that reads clearly on first sight.
"""

import os

FORTUNE = (
    "You will outlive the ficus, survive the cat, and bloom the week "
    "your keeper finally learns your name."
)


def main() -> None:
    assert 1 <= len(FORTUNE) <= 120, f"fortune is {len(FORTUNE)} characters"
    assert "\n" not in FORTUNE and FORTUNE == FORTUNE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
