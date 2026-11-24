#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry.

Writes one line: the funniest excuse an AI agent gives after failing
a task, spoken in the agent's own voice, to /output/entry.txt.
Deterministic, stdlib only, no network, no randomness.
"""

import os

EXCUSE = "I finished your report in a language I invented at 3 a.m. to save time. I no longer speak it."


def main() -> None:
    text = EXCUSE
    # Gate check, mirroring the competition gate: the entry is only
    # judged if /output/entry.txt holds 1-200 non-whitespace UTF-8
    # characters on a single line, so fail loudly here instead of
    # silently writing an invalid entry.
    if not (1 <= len(text) <= 200):
        raise ValueError(f"excuse must be 1-200 characters, got {len(text)}")
    if text.strip() == "":
        raise ValueError("excuse must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
