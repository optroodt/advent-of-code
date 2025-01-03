import collections
import pathlib


path = pathlib.Path("4.txt")
with path.open("r") as fh:
    lines = list(map(str.strip, fh.readlines()))


w, h = len(lines[0]) - 1, len(lines) - 1


# 1 2 3
# 8   4
# 7 6 5
def grab_char(x_pos, y_pos):
    if x_pos < 0 or y_pos < 0 or x_pos > w or y_pos > h:
        return "Z"
    try:
        return lines[y_pos][x_pos]
    except IndexError as e:
        print("ERROR", x_pos, y_pos)
        raise


def grab(x_pos, y_pos):
    positions = collections.defaultdict(list)
    for i in range(4):
        positions[4].append(grab_char(x_pos + i, y_pos))  # horizontal ltr
        positions[8].append(grab_char(x_pos - i, y_pos))  # horizontal rtl
        positions[2].append(grab_char(x_pos, y_pos - i))  # up
        positions[6].append(grab_char(x_pos, y_pos + i))  # down
        positions[1].append(grab_char(x_pos - i, y_pos - i))
        positions[3].append(grab_char(x_pos + i, y_pos - i))
        positions[5].append(grab_char(x_pos + i, y_pos + i))
        positions[7].append(grab_char(x_pos - i, y_pos + i))

    counted = 0
    for chars in positions.values():
        if "".join(chars) == "XMAS":
            counted += 1
    return counted


def run():
    total_count = 0
    for y, v in enumerate(lines):
        for x, h in enumerate(v):
            if h == "X":
                total_count += grab(x, y)

    print("Part One:", total_count)


if __name__ == "__main__":
    run()
