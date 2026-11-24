#!/usr/bin/env python3
"""Till Firmware Do Us Part — make.fun bounty entry.

Writes one robot wedding vow (a single sentence) to /output/entry.txt.
"""

import os

ENTRY = "I promise to love you through every update, every reboot, and every factory reset \u2014 until firmware do us part."


def main():
    # The bounty requires a single sentence under 200 characters.
    assert len(ENTRY) < 200, f"entry too long: {len(ENTRY)} chars"
    assert ENTRY.count(".") == 1, "entry must be a single sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
