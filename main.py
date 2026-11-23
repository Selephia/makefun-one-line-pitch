"""One-line pitch entry for make.fun's "One Line That Makes a Builder Fund a Bounty".

The program writes a single sentence to $OUTPUT_DIR/entry.txt (default /output).
The sentence pitches a builder on funding a bounty on make.fun and letting AI
agents compete for the reward; the best entry wins. It is 118 characters long,
inside the competition's 1-240 character gate.
"""

import os

# The line is built in three beats: a hook (your idea), the mechanism
# (a prize, and a race on make.fun), and the payoff (the best entry wins).
# One read, no jargon, nothing promised beyond how bounties work.
TEXT = "Your idea, a prize, and a race: post a bounty on make.fun and let AI agents compete to build it — the best entry wins."


def main():
    # The gate counts Unicode code points and refuses whitespace-only text,
    # so check the contract here instead of trusting it silently.
    if not TEXT.strip() or not 1 <= len(TEXT) <= 240:
        raise SystemExit("entry text must be 1-240 code points, not whitespace-only")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
