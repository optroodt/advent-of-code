import collections
import copy
import functools
import itertools
import operator
import pathlib
import re
import string

from utils import load_file

lines = [list(map(int, list(l))) for l in load_file()]
W = len(lines[0])
H = len(lines)
print(W, H)


def find_trailheads(inputs):
    trailheads = []
    for y, line in enumerate(inputs):
        for x, d in enumerate(line):
            if d == 0:
                trailheads.append((x, y))
    return trailheads


def value_at_pos(pos):
    return lines[pos[1]][pos[0]]


def is_within_bounds(pos):
    return 0 <= pos[0] < W and 0 <= pos[1] < H


def next_positions(pos):
    current_value = value_at_pos(pos)
    return [
        p
        for p in [
            (pos[0], pos[1] - 1),  # u
            (pos[0], pos[1] + 1),  # d
            (pos[0] - 1, pos[1]),  # l
            (pos[0] + 1, pos[1]),  # r
        ]
        if is_within_bounds(p) and value_at_pos(p) == current_value + 1
    ]


def explore(pos):
    if value_at_pos(pos) == 9:
        return [pos]

    results = [explore(v) for v in next_positions(pos)]
    return set(itertools.chain.from_iterable(results))


def run():
    trailheads = find_trailheads(lines)
    # print(trailheads)
    total_score = 0
    for trailhead in trailheads:
        total_score += len(explore(trailhead))
    print("Part One:", total_score)


if __name__ == "__main__":
    run()
