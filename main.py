"""The Internet in One Word - entry program.

The whole internet in a single word: feral. Wild, untamed, raised by
itself. This program writes that word, and nothing else, to
/output/entry.txt - exactly what the competition gate expects:
UTF-8 text, 1 to 30 characters, not only white space.
"""

from pathlib import Path

WORD = "feral"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
