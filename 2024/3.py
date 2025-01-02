import copy
import collections
import operator
import pathlib
import re
import string
import functools

path = pathlib.Path("3.txt")
with path.open("r") as fh:
    lines = map(str.strip, fh.readlines())


def run():
    enabled = True
    data = "".join(lines)
    matches = re.findall("(mul\(\d+,\d+\)|do(?:n't)?\(\))", data)
    # print(matches)
    total = 0
    for m in matches:
        if m == "do()":
            enabled = True
        elif m == "don't()":
            enabled = False
        else:
            # print(m)
            if not enabled:
                continue

            front, back = m.split(",")
            total += int(front[4:]) * int(back[:-1])

    print(total)


# 646346 is too low
if __name__ == "__main__":
    run()
