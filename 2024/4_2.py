import copy
import collections
import operator
import pathlib
import re
import string
import functools

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
    i = 1
    positions[0].append(grab_char(x_pos - i, y_pos - i))
    positions[0].append(grab_char(x_pos, y_pos))
    positions[0].append(grab_char(x_pos + i, y_pos + i))

    positions[1].append(grab_char(x_pos + i, y_pos - i))
    positions[1].append(grab_char(x_pos, y_pos))
    positions[1].append(grab_char(x_pos - i, y_pos + i))

    counted = 0

    for chars in positions.values():
        mas = "".join(chars)
        if mas == "MAS" or mas == "SAM":
            counted += 1

    return 1 if counted == 2 else 0


def run():
    # print(w, h)
    total_count = 0
    for y, v in enumerate(lines):
        for x, h in enumerate(v):
            if h == "A":
                print(x, y)
                total_count += grab(x, y)
        # break

    print(total_count)


if __name__ == "__main__":
    run()
