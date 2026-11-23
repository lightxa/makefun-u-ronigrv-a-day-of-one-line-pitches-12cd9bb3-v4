#!/usr/bin/env python3
"""A Day of One-Line Pitches (variant 4): write one persuasive sentence
to /output/entry.txt.

Angle: YOU ALREADY DID THE HARD PART. The friend already holds the
idea, and having the idea is the hard part; describing it in plain
words is the only work left, and the agent does the coding the friend
never learned. That makes handing the idea over feel easy and low
risk, in one warm sentence, friend to friend.

Truth guardrails, kept deliberately: "do the coding" is what make.fun
agents do from a plain-words description; the sentence never promises
a finished app by a specific time, never promises it will be perfect,
and never promises a price or a payoff. Pure stdlib, deterministic,
no network at runtime.
"""

import os

SENTENCE = (
    "You've already done the hard part by having the idea, so just "
    "tell it in plain words and let an agent do the coding you never "
    "learned."
)


def main() -> None:
    # Gate self-check: the sealed scorer only accepts UTF-8 text of
    # 1 to 240 characters that is not only white space.
    if not 1 <= len(SENTENCE) <= 240 or not SENTENCE.strip():
        raise ValueError("sentence fails the 1-240 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
