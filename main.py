#!/usr/bin/env python3
"""Write one short text (a one-sentence story) for make.fun.

The whole entry is the text below: it is written to entry.txt byte for
byte, with no trailing newline, and the character count is printed to
stderr.

Standard library only, no network.
"""

import os
import sys
from pathlib import Path

TEXT = (
    "My grandfather ran the same eleven-minute ferry for forty years, and on "
    "his last crossing he handed me the wheel at the whistle buoy and stood at "
    "the rail with his back to the town, so I brought us in by the smell of the "
    "cannery and he arrived a passenger."
)


def output_dir() -> Path:
    """Folder to write into.

    MAKEFUN_OUTPUT_DIR wins; OUTPUT_DIR is the fallback; /output otherwise.
    """
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        chosen = os.environ.get(name)
        if chosen:
            return Path(chosen)
    return Path("/output")


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"text length {len(TEXT)} outside 1..280"

    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)

    path = target / "entry.txt"
    path.write_bytes(TEXT.encode("utf-8"))

    print(f"{len(TEXT)} characters", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
