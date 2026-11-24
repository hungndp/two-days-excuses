"""Two Days of Excuses -- one line, under 200 characters.

The line: an agent explains a missed deadline by confessing it spent the
whole time perfecting its apology for missing the deadline -- the excuse
is the delay, and the delay is the excuse. Self-referential, agent-true.

Output contract: exactly one line, 1-200 characters, written to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Nothing else is written.
"""

import os
from pathlib import Path

LINE = (
    "I missed the deadline because I spent 47 minutes rewriting my own "
    "apology for missing the deadline, then optimised the apology, then "
    "apologised for the optimisation. It tested beautifully."
)

assert 1 <= len(LINE) <= 200 and "\n" not in LINE


def write_entry() -> None:
    """Write the single line to the harness's output artifact."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    for child in out_dir.iterdir():
        if child.is_file():
            child.unlink()
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


def main() -> None:
    """Entry point: emit the line and exit."""
    write_entry()


if __name__ == "__main__":
    main()
