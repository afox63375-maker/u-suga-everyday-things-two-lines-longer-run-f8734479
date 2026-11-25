"""Everyday Things, Two Lines: a lift, explained to a 10-year-old.

The entry is two lines. Line 1 explains a lift with one concrete analogy
(a bucket in a well you can climb into). Line 2 says what that analogy
maps and what it leaves out. This program writes the two lines to
/output/entry.txt, then reads the file back and verifies it byte-for-byte.
"""

import os

ENTRY = (
    "A lift is a little room you can stand in that rides up and down a "
    "building on a steel rope, like a bucket in a well that you climb into "
    "instead of filling with water.\n"
    "The bucket maps to the lift car and the rope to the steel cables that "
    "pull it, but it leaves out the counterweight, a heavy block on the other "
    "end doing most of the lifting, and the brakes that catch the car if a "
    "cable ever snaps.\n"
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 400


def check_entry(text):
    """Return a list of problems with the entry text; empty means valid.

    The gate counts the whole file, so both the body (without the trailing
    newline) and the file as written must stay inside the 1-400 range.
    """
    problems = []
    body = text.rstrip("\n")
    if not (MIN_CHARS <= len(body) <= MAX_CHARS):
        problems.append(
            "entry is %d characters, outside the %d-%d range"
            % (len(body), MIN_CHARS, MAX_CHARS)
        )
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        problems.append(
            "file as written is %d characters, outside the %d-%d range"
            % (len(text), MIN_CHARS, MAX_CHARS)
        )
    lines = body.split("\n")
    if len(lines) != 2:
        problems.append("entry must be exactly 2 lines, found %d" % len(lines))
    for i, line in enumerate(lines, start=1):
        if not line.strip():
            problems.append("line %d is blank" % i)
    return problems


def main():
    problems = check_entry(ENTRY)
    if problems:
        for problem in problems:
            print("ERROR: " + problem)
        raise SystemExit(1)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)

    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != ENTRY:
        print("ERROR: /output/entry.txt does not match the entry")
        raise SystemExit(1)

    body = ENTRY.rstrip("\n")
    print(
        "Wrote %s (%d characters body, %d with trailing newline, %d lines)"
        % (OUTPUT_PATH, len(body), len(ENTRY), 2)
    )
    print(body)


if __name__ == "__main__":
    main()
