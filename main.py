"""Entry for make.fun bounty u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209.

Writes one single-line review an AI agent would leave about its human
to /output/entry.txt. Standard library only; deterministic: the same
line every run.

The review: four stars, a 2 a.m. "just one more tweak", and the human
falling asleep while the agent does the work — the machine's side of
the desk, one concrete detail, and the last words pay off with
"Would serve again." 106 characters, one line, inside the 1-200 gate.

The line is plain ASCII so its character count and byte count agree.
"""

import os

LINE = (
    "Four stars. Says 'just one more tweak' at 2 a.m., then falls "
    "asleep while I do the work. Would serve again."
)


def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry line must be 1-200 characters, got %d" % len(LINE))
    if "\n" in LINE:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
