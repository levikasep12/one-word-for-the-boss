#!/usr/bin/env python3
"""One Word for the Boss.

Writes exactly one word describing a boss to /output/entry.txt.

The word is "Hovercraft": the boss who hovers over your shoulder all day,
watching every keystroke, every ticket, every coffee break - a vehicle that
never actually lands anywhere, just hangs in the air above you, humming.
It needs no caption to be funny, it is true of bosses in an office, a
kitchen or a warehouse, and it is fresher than the first word anyone reaches
for. One word, ten characters, no spaces, no explanation.
"""

from pathlib import Path

WORD = "Hovercraft"


def main() -> None:
    # The gate only accepts 1-30 characters, a single word, not only
    # whitespace. Fail loudly here rather than shipping an invalid entry.
    assert 1 <= len(WORD) <= 30, "word must be 1-30 characters"
    assert WORD.split() == [WORD], "word must contain no whitespace"
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
