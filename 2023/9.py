import math
import pathlib
import re
import string
import operator
from collections import Counter

path = pathlib.Path("9.txt")
with path.open("r") as fh:
    lines = list(map(str.strip, fh.readlines()))


def run():
    total = 0
    for line in lines:
        values = list(map(int, re.split(" +", line)))
        sequences = [values]

        while set(values) != {
            0,
        }:
            sequence = []
            for i, value in enumerate(values[:-1]):
                sequence.append(values[i + 1] - value)
            values = sequence
            sequences.append(values)
        # print(sequences, len(sequences))

        the_range = len(sequences) - 1
        for i in range(the_range):
            addition = sequences.pop().pop(0)  # for day 2, make it 0
            # sequences[-1].append(sequences[-1][-1] + addition)
            sequences[-1].insert(0, sequences[-1][0] - addition)

        total += sequences.pop().pop(0)

    # too high: 1992273665
    # too low:  1054315252
    # this:     1992273652
    print(total)


if __name__ == "__main__":
    run()
