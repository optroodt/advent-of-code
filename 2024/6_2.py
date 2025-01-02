import copy
import collections
import operator
import pathlib
import re
import string
import functools

path = pathlib.Path("6.txt")
with path.open("r") as fh:
    lines = list(map(str.strip, fh.readlines()))

H = len(lines)
W = len(lines[0])

obstructions = set(["#", "O"])
directions = ["^", ">", "v", "<"]


# directions ^>v<
# obstacles #
# visited = X
def find_start():
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c in directions:
                return c, j, i


path = []


def mark(x, y, c):
    if c == "X":
        path.append((x, y))
    lines[y] = lines[y][:x] + c + lines[y][x + 1 :]


def walk(direction, x, y):
    mark(x, y, "X")
    prev_x, prev_y = x, y
    if direction == "^":
        y -= 1
    elif direction == "v":
        y += 1
    elif direction == "<":
        x -= 1
    elif direction == ">":
        x += 1

    if not (-1 < x < W and -1 < y < H):
        return direction, -1, -1

    if lines[y][x] in obstructions:
        # print("Found #, rotating")
        direction = directions[(directions.index(direction) + 1) % 4]
        mark(prev_x, prev_y, direction)
        return direction, prev_x, prev_y

    mark(x, y, direction)

    return direction, x, y


def print_grid():
    for i, line in enumerate(lines):
        print(f"{i:02d}", line)


def count():
    x_count = 0
    for line in lines:
        for c in line:
            if c == "X":
                x_count += 1
    return x_count


def run():
    global lines
    print(W, H)
    start_d, start_x, start_y = find_start()
    d, x, y = start_d, start_x, start_y
    print(d, x, y)
    # for n in range(55):
    clean = copy.deepcopy(lines)
    while True:
        d, x, y = walk(d, x, y)
        if x == -1 and y == -1:
            break
    print_grid()

    path.pop(0)

    # print(len(path), len(set(path)), path)
    possible_obstructions = copy.deepcopy(set(path))
    # return
    options = 0
    for obs_x, obs_y in possible_obstructions:
        lines = copy.deepcopy(clean)
        # print_grid()
        route = set()
        route_order = []
        mark(obs_x, obs_y, "O")
        # print_grid()
        # while True:
        d, x, y = start_d, start_x, start_y
        while True:
            new_d, new_x, new_y = walk(d, x, y)
            if new_x == -1 and new_y == -1:
                # print_grid()
                break
            if new_d != d:
                d, x, y = new_d, new_x, new_y
                continue
            if (new_d, new_x, new_y) in route:
                # print(f"found {new_d} {new_x}, {new_y} in {route}")
                # print_grid()
                options += 1
                break
            else:
                route.add((new_d, new_x, new_y))
                route_order.append((x, y))

            d, x, y = new_d, new_x, new_y

    print(x, y)
    print("Options", options)


if __name__ == "__main__":
    run()
