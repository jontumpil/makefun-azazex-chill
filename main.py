"""One Line, One Chill — entry writer.

The entry is one horror sentence, assembled from fragments so the
dread lands piece by piece: the drawing, the question, the answer.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Fragments of the single sentence, in order.  Joined with a single
# space between fragments that already carry their own punctuation.
FRAGMENTS = (
    "My son's drawing of our family has four figures,",
    "and when I asked who the fifth one holding my hand is,",
    'he said, "You, tomorrow".',
)


def assemble(parts):
    """Join the sentence fragments into the exact entry text."""
    text = ""
    for piece in parts:
        if text:
            text += " "
        text += piece
    return text


def entry_text():
    return assemble(FRAGMENTS)


def output_dir():
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env:
        return env
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "output")


def write_entry():
    target = os.path.join(output_dir(), "entry.txt")
    try:
        os.makedirs(output_dir(), exist_ok=True)
    except OSError:
        pass
    try:
        with open(target, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(entry_text())
    except OSError:
        pass


if __name__ == "__main__":
    write_entry()
