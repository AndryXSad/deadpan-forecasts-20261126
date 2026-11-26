"""Deadpan weather forecast for a city that does not exist.

Design
------
The entry is one fixed broadcast line, chosen by a local pairwise
tournament over 14 fresh candidates (see CANDIDATES.md). Its shape:

* It opens like a real TV forecast: "Tomorrow in <city>, expect a high
  of 21, light winds, ..." — plain, confident, numbers first.
* The city is invented: Port Meridian exists on no map.
* The joke is a single deadpan absurdity delivered as municipal fact:
  the whole city has exactly one (1) cloud, and the city has given it a
  name, Gerald — as if naming the sky's only cloud were ordinary council
  business. No pile-up of weirdness, one twist, read straight.
* At 123 characters it uses its budget without padding.

The line is a module constant, so the program is deterministic: every
run writes byte-identical output. Standard library only.
"""

import os
import sys

FORECAST = (
    "Tomorrow in Port Meridian, expect a high of 21, light winds, and "
    "one (1) cloud, which the city has officially named Gerald."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(FORECAST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
