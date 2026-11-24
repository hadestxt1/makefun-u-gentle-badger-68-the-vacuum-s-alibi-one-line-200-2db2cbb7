#!/usr/bin/env python3
"""The Vacuum's Alibi (rebuild) — one deadpan line from a robot vacuum.

Writes a single excuse, at most 200 characters, to /output/entry.txt
and to stdout. Deterministic: no clock, no randomness, no network,
standard library only.
"""

import os

LINE = "Log 04:12: the crumb under the fridge filed for squatter's rights. I do not evict tenants without a court order."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
