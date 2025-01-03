import copy
import pathlib

path = pathlib.Path("6.txt")
with path.open("r") as fh:
    lines = list(map(str.strip, fh.readlines()))

H = len(lines)
W = len(lines[0])

obstructions = {"#", "O"}
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
    start_d, start_x, start_y = find_start()
    d, x, y = start_d, start_x, start_y
    clean = copy.deepcopy(lines)
    while True:
        d, x, y = walk(d, x, y)
        if x == -1 and y == -1:
            break
    # print_grid()

    path.pop(0)

    possible_obstructions = copy.deepcopy(set(path))
    options = 0
    for obs_x, obs_y in possible_obstructions:
        lines = copy.deepcopy(clean)
        route = set()
        route_order = []
        mark(obs_x, obs_y, "O")

        d, x, y = start_d, start_x, start_y
        while True:
            new_d, new_x, new_y = walk(d, x, y)
            if new_x == -1 and new_y == -1:
                break
            if new_d != d:
                d, x, y = new_d, new_x, new_y
                continue
            if (new_d, new_x, new_y) in route:

                options += 1
                break
            else:
                route.add((new_d, new_x, new_y))
                route_order.append((x, y))

            d, x, y = new_d, new_x, new_y

    print("Part Two:", options)


if __name__ == "__main__":
    # This one is rather slow, I'm brute forcing it. :)
    run()
