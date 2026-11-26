"""Write the entry job title to the output directory.

The competition harness runs `python3 main.py` and reads
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).
"""

import os

TITLE = "Senior Vice President of Apologizing to Printers"

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # Self-check: the entry must be one job title, 60 characters at most.
    # "Senior Vice President of Apologizing to Printers" is 48 characters:
    # a real-sounding senior title with one hilariously specific twist.
    assert TITLE, "entry title must not be blank"
    assert "\n" not in TITLE.strip(), "entry must be a single line"
    assert 1 <= len(TITLE) <= 60, "entry title must be 1-60 characters"
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TITLE + "\n")


if __name__ == "__main__":
    main()
