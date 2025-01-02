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


def is_safe(level, allow_errors=1):
    # print(level)
    prev = level[0]
    errors = 0
    direction = get_direction(prev, level[1])
    for n in level[1:]:
        new_direction = get_direction(prev, n)

        abs_dist = abs(prev - n)
        if abs_dist > 3 or new_direction != direction:
            errors += 1

        # print(errors)
        if errors > allow_errors:
            return False
            break

        direction = new_direction
        prev = n
    else:
        return True


def run():
    levels = []
    for l in lines:
        levels.append(list(map(int, l.split(" "))))

    safe_counter = 0
    safe = False
    for level in levels:
        # print(list(filter(lambda x: x > 1, collections.Counter(level).values())))
        if len(list(filter(lambda x: x > 1, collections.Counter(level).values()))) > 1:
            # print(level)
            continue

        if is_safe(level):
            print(level)
            safe_counter += 1
            safe = True
        else:
            continue

            for i in range(0, len(level)):
                lvl = [n for j, n in enumerate(level) if j != i]
                # print(lvl)
                if is_safe(lvl, allow_errors=0):
                    safe_counter += 1
                    safe = True
                    break
            else:
                pass
                # print(level)

    print(safe_counter)


if __name__ == "__main__":
    run()
