import copy
import collections
import operator
import pathlib
import re
import string
import functools

path = pathlib.Path("2.txt")
with path.open("r") as fh:
    lines = map(str.strip, fh.readlines())


def get_direction(a, b):
    dist = b - a
    if dist > 0:
        new_direction = True
    elif dist < 0:
        new_direction = False
    else:
        new_direction = None

    return new_direction


def is_safe(level):
    for i in range(len(level) - 1):
        cur_val, next_val = level[i], level[i + 1]
        if abs(next_val - cur_val) > 3:
            return False

        new_direction = get_direction(cur_val, next_val)
        if i == 0:
            direction = new_direction
        elif direction != new_direction or direction is None:
            return False
    return True


def run():
    levels = []
    for l in lines:
        levels.append(list(map(int, l.split(" "))))

    safe_counter = 0
    safe = False
    for n, level in enumerate(levels):
        for i in range(len(level)):
            lvl = level[:i] + level[i + 1 :]
            if is_safe(lvl):
                # print(n, level)
                safe_counter += 1
                break
    print(safe_counter)


if __name__ == "__main__":
    run()
