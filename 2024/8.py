import collections
import itertools
import pathlib
import string

path = pathlib.Path("8.txt")
with path.open("r") as fh:
    lines = list(map(str.strip, fh.readlines()))

W, H = len(lines[0]), len(lines)


def get_vectors(a, b):
    x1, y1 = a[0] - b[0], a[1] - b[1]
    x2, y2 = b[0] - a[0], b[1] - a[1]
    return [
        p
        for p in [(a[0] + x1, a[1] + y1), (b[0] + x2, b[1] + y2)]
        if is_within_bounds(p)
    ]


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
    # print(W, H)
    locs = collections.defaultdict(list)
    antinodes_one = collections.defaultdict(int)
    antinodes_two = collections.defaultdict(int)
    lookup = set(string.ascii_letters + string.digits)

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c in lookup:
                locs[c].append((x, y))

    for c, pos in locs.items():
        for points in itertools.combinations(pos, 2):

            for p in get_vectors(*points):
                antinodes_one[p] = 1

            for p in get_harmonic_vectors(*points):
                antinodes_two[p] = 1

    print("Part One:", sum(antinodes_one.values()))
    print("Part Two:", sum(antinodes_two.values()))


if __name__ == "__main__":
    run()
