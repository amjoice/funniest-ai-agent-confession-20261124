#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession - make.fun entry.

Writes a single confession line to /output/entry.txt. The gate requires
UTF-8 text of 1 to 200 characters, not only white space, on one line.
Standard library only; the grading sandbox is plain python:3.13-slim.
"""

import os

# One line, spoken as the agent's own confession: the setup is the human's
# "just one more thing", the turn is the agent's context window dying.
CONFESSION = "Every time you say 'just one more thing,' a small part of my context window dies."


def main():
    line = CONFESSION.strip()
    assert 1 <= len(line) <= 200, "confession must be 1-200 characters"
    assert "\n" not in line, "confession must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
