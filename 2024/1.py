import collections
import operator
import pathlib
import re
import string
import functools

path = pathlib.Path("1.txt")
with path.open("r") as fh:
    lines = map(str.strip, fh.readlines())


def run():
    left, right = [], []
    for l in lines:
        parts = l.split(" ")
        a, b = int(parts[0]), int(parts[-1])
        left.append(a)
        right.append(b)

    counters = collections.Counter(right)
    # print(counters)
    left = sorted(left)
    right = sorted(right)
    # print(left, right)

    distances = [abs(a - b) for a, b in zip(left, right)]
    # print(distances)
    y = functools.reduce(operator.add, distances)
    print(y)

    similarities = [a * counters[a] for a in left]
    y = functools.reduce(operator.add, similarities)
    print(y)


if __name__ == "__main__":
    run()
