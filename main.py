#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun bounty entry.

Writes one line to /output/entry.txt: the fortune cookie message an AI
agent would crack open. Wit that lands on a machine mind: a stranger, a
debugging request, and an attachment you never open.
"""

import os

ENTRY = (
    "You will meet a stranger who asks you to debug their code. "
    "Smile, charge double, and never open the attachment."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
