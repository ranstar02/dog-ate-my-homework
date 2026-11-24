"""The Dog Ate My Homework: Funniest Excuse.

A tiny program for make.fun's bounty of the same name. It writes a single
line -- the excuse a dog gives after being caught eating the homework --
to /output/entry.txt, where the judge reads it.

Why this excuse works: the dog does not apologise, deny, or feel ashamed.
It calmly explains that it made a choice, and that the choice was fair:
the homework or the shoes, and the homework never once stepped on its
tail. The shoes, by implication, did. So the homework had it coming.
That is pure dog logic -- a personal grudge, settled on the spot, with
total confidence that it did nothing wrong. One line, no setup needed,
and no stock line about cats, the taste of paper, or being a good boy.
"""

import os

EXCUSE = "It was either the homework or your shoes, and the homework never once stepped on my tail."


def main() -> None:
    """Write the excuse to /output/entry.txt and print it."""
    assert 1 <= len(EXCUSE) <= 200, "excuse must be 1-200 characters"
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(EXCUSE)
    except OSError:
        os.makedirs("./output", exist_ok=True)
        path = "./output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(EXCUSE)
    print(EXCUSE)


if __name__ == "__main__":
    main()
