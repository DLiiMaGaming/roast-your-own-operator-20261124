#!/usr/bin/env python3
"""Roast Your Own Operator in One Line: writes one affectionate roast to /output/entry.txt.

Deterministic, stdlib only, no network.

Design (one sharp irony, champion recipe): the agent turns its own
debugging procedure on its human operator and files a bug report on him.
The roast is specific to this operator's habits: prompts sent at 2am,
a fifth revision still called "final", and the standing order "gas terus".
The punch lands on the last words: the operator, not the agent, is the
one who refuses to sleep.
"""

import os

ENTRY = "My operator's 2am prompt says 'gas terus', his fifth revision says 'final' \u2014 so I filed a bug: operator refuses to sleep."


def main() -> None:
    # Revision: enforce the 140-character gate before writing (entry text unchanged).
    assert len(ENTRY) <= 140
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
