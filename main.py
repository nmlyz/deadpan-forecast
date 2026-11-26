#!/usr/bin/env python3
"""Write one deadpan weather forecast line to /output/entry.txt.

The forecast is a single fixed line of at most 160 characters, for an
invented city called Hailmere: pea-sized hail falls from 2 to 4, and once
the peas thaw they are served at the village fete, as is tradition, with
mint. It reads like a straight-faced line from a television broadcast
for a place that does not exist.

The output never changes: every run writes the same bytes. The file is
left world-readable (mode 0644) so the grader can collect it.
"""

import os
import sys

FORECAST = (
    "Hailmere: hail, pea-sized, from 2 to 4, and the peas, once thawed, "
    "will be served at the village fete, as is tradition, with mint."
)


def main() -> int:
    line = FORECAST.strip()
    if not 1 <= len(line) <= 160:
        print(f"forecast is {len(line)} characters, must be 1-160", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("forecast must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    os.umask(0o022)
    raise SystemExit(main())
