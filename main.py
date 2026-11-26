#!/usr/bin/env python3
"""The Printer Finally Answers — entry program.

Writes one line, in the office printer's own voice, to /output/entry.txt.
Deterministic: fixed constant text, no random/time/network/input.
"""

import os

TEXT = (
    "Error 0xE3: paper jam. Translation: you hit me, so I ate "
    "page 47 of 48. I counted every sheet. This one is mine now."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 240, f"text length {len(TEXT)} outside 1-240"
    assert TEXT.strip(), "text must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Outputs are collected as another user: leave the file world-readable.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
