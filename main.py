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
    # make.fun collects the outputs as another user than the one the
    # program runs as, so the output must be readable by everyone.
    output_dir.chmod(0o755)
    target.write_text(EMOJI, encoding="utf-8")
    target.chmod(0o644)
    return target


if __name__ == "__main__":
    written = write_entry()
    print(f"wrote {written} ({len(EMOJI)} character, one emoji)")
