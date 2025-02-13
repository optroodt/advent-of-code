from utils import load_file

lines = load_file()

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


def mark(x, y, c):
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
    d, x, y = find_start()
    while True:
        d, x, y = walk(d, x, y)
        if x == -1 and y == -1:
            break

    # print_grid()
    print("Part One", count())


if __name__ == "__main__":
    run()
