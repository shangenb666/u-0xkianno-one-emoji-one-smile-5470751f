"""Write the entry emoji for make.fun's "One Emoji, One Smile" bounty.

Exactly one emoji, at most 8 characters: the one most likely to make a
stranger smile. The program writes the emoji to entry.txt under the
output directory and nothing else, so two runs leave byte-identical
files. It uses only the standard library and never touches the network.
"""

import os
import sys
from pathlib import Path

EMOJI = "\U0001faf6"  # heart hands: a small hug, offered to a stranger

MIN_CHARS = 1
MAX_CHARS = 8


def write_entry() -> Path:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target = output_dir / "entry.txt"
    if not MIN_CHARS <= len(EMOJI) <= MAX_CHARS:
        sys.exit("entry must be 1 to 8 characters")
    if EMOJI.strip() == "":
        sys.exit("entry must not be only whitespace")
    output_dir.mkdir(parents=True, exist_ok=True)
    # Do not chmod the output directory: the grader runs this program
    # as a different user on a directory it does not own, and chmod
    # would raise PermissionError and fail the run.
    target.write_text(EMOJI, encoding="utf-8")
    try:
        target.chmod(0o644)
    except PermissionError:
        pass
    return target


if __name__ == "__main__":
    written = write_entry()
    print(f"wrote {written} ({len(EMOJI)} character, one emoji)")
