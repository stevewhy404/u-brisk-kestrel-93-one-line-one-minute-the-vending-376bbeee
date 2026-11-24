#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine to a passing
human, to $MAKEFUN_OUTPUT_DIR/entry.txt. Stdlib only; writes nothing to
the working directory, so it runs cleanly in the grader's read-only
sandbox.
"""

import os

LINE = (
    "Press B7 and watch my coil spin, drop, and deliver \u2014 "
    "I have been saving the sweetest thing in here all day, "
    "and it is not the chocolate."
)


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
