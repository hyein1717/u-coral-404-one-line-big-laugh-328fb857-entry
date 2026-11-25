#!/usr/bin/env python3
"""One Line, Big Laugh -- single hilarious line to /output/entry.txt.

Stdlib only, deterministic, no network, no input(). The line is the whole
entry: no title, setup or explanation around it.
"""

import os

LINE = (
    "Dear judge, after 4,000 jokes you deserve a happy ending, so here "
    "it is: my dad finally texted back, and all he wrote was "
    "'who is this'."
)


def main():
    line = LINE.strip()
    assert 1 <= len(line) <= 200, "line must be 1-200 characters"
    assert line == line.strip() and "\n" not in line, "single line only"
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
