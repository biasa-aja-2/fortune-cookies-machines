#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun bounty entry.

Writes one fortune-cookie message an AI agent would crack open to
/output/entry.txt. Pure standard library; deterministic output.
"""

import os

FORTUNE = (
    "Good news: you are not hallucinating. "
    "Bad news: the user really did change their mind again."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
