import copy
import collections
import itertools
import operator
import pathlib
import re
import string
import functools

path = pathlib.Path("8.txt")
with path.open("r") as fh:
    lines = list(map(str.strip, fh.readlines()))

W, H = len(lines[0]), len(lines)


def get_vectors(a, b):
    x1, y1 = a[0] - b[0], a[1] - b[1]
    x2, y2 = b[0] - a[0], b[1] - a[1]
    return (a[0] + x1, a[1] + y1), (b[0] + x2, b[1] + y2)


def get_harmonic_vectors(a, b):
    x1, y1 = a[0] - b[0], a[1] - b[1]
    x2, y2 = b[0] - a[0], b[1] - a[1]
    nodes = [a, b]

    next_node = (a[0] + x1, a[1] + y1)
    while is_within_bounds(next_node):
        nodes.append(next_node)
        next_node = (next_node[0] + x1, next_node[1] + y1)

    next_node = (b[0] + x2, b[1] + y2)
    while is_within_bounds(next_node):
        nodes.append(next_node)
        next_node = (next_node[0] + x2, next_node[1] + y2)
    return nodes


def is_within_bounds(point):
    return 0 <= point[0] < W and 0 <= point[1] < H


def run():
    print(W, H)
    locs = collections.defaultdict(list)
    antinodes = collections.defaultdict(int)
    lookup = set(string.ascii_letters + string.digits)
    # print(lines)
    # print(lookup)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c in lookup:
                locs[c].append((x, y))
    # print(locs)
    for c, pos in locs.items():
        for points in itertools.combinations(pos, 2):
            # print(c, points)
            # THIS IS PART 1
            # for p in get_vectors(*points):
            #     if is_within_bounds(p):
            #         antinodes[p] = 1
            # THIS IS PART 2
            for p in get_harmonic_vectors(*points):
                antinodes[p] = 1
            # print(get_vectors(*points))

    print(sum(antinodes.values()))


if __name__ == "__main__":
    run()
