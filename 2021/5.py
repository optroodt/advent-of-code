from utils import load_file

lines = load_file("5.txt")

coordinates = []

for line in lines:
    a, b = line.split(" -> ")
    pair = [tuple(map(int, x.split(','))) for x in [a, b]]
    coordinates.append(pair)

max_x, max_y = 0, 0
for a, b in coordinates:
    max_x = max(max_x, a[0])
    max_x = max(max_x, b[0])
    max_y = max(max_y, a[1])
    max_y = max(max_y, b[1])


def get_straight(values):
    result = []
    for a, b in values:
        if a[0] == b[0] or a[1] == b[1]:
            result.append([a, b])
    return result


straight = get_straight(coordinates)


def calculate_index(x, y):
    return x + y * (max_x - 1)


def calculate_positions(a, b):
    x_correction = -1 if b[0] < a[0] else 1
    y_correction = -1 if b[1] < a[1] else 1
    xs = range(a[0], b[0] + x_correction, x_correction)
    ys = range(a[1], b[1] + y_correction, y_correction)
    # print(xs, ys)
    positions = []

    if a[0] != b[0] and a[1] != b[1]:
        for x, y in zip(xs, ys):
            positions.append((x, y))
    else:
        for x in xs:
            for y in ys:
                positions.append((x, y))

    return positions


def calculate_indices(positions):
    return [calculate_index(x, y) for x, y in positions]


for title, coords in [("Part One", straight), ("Part Two", coordinates)]:
    grid = [0] * (max_x * max_y)
    for a, b in coords:
        positions = calculate_positions(a, b)

        indices = calculate_indices(positions)
        for index in indices:
            grid[index] += 1

    count = 0
    for i in grid:
        if i > 1:
            count += 1

    print(f"{title}:", count)
