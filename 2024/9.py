import copy
import collections
import itertools
import operator
import pathlib
import re
import string
import functools

path = pathlib.Path("9.txt")
with path.open("r") as fh:
    lines = list(map(str.strip, fh.readlines()))


def run():
    line = lines[0]
    # print(line, len(line))
    result = []
    _id = 0
    current_digit = 1
    is_file = True
    for i in line:
        if is_file:
            result += [str(_id)] * int(i)
            _id += 1
            is_file = False
        else:
            result += ["."] * int(i)
            is_file = True
    # print(result)
    # result = list(result)
    print(result)

    W = len(result) - 1
    print(W)
    # exit()
    for i, c in enumerate(reversed(result)):
        # print(i, c)

        if c != ".":
            for n in range(len(result)):
                if i + n >= W:
                    break
                if result[n] == ".":
                    result[n] = c
                    result[W - i] = "."
                    break
        if i + n >= W:
            break
        # print("".join(result), i, n)
    # result = "".join(result)
    print("".join(result))
    total = 0
    for i, n in enumerate(result[: result.index(".")]):
        total += i * int(n)
    # print("0099811188827773336446555566..............")
    print(total)

    # 85801094642 too low
    # 6349606724455


if __name__ == "__main__":
    run()
