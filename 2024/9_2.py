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

    print("".join(result))

    W = len(result) - 1
    print(W)
    free_space_required = 0
    seen = set()

    for i, c in enumerate(reversed(result)):
        hit = False
        # print(i, c)
        if c != "." and c not in seen:
            seen.add(c)
            free_space_required = result.count(c)
            # print("free space required", free_space_required, "for", c)
            start_indices = []
            for n, digit in enumerate(result):
                # print(digit)
                if n + i > W:
                    break
                if digit == ".":
                    start_indices.append(n)
                    if len(start_indices) == free_space_required:
                        # print(f"hit {c}", start_indices)

                        hit = True
                        # print()
                        break
                else:
                    hit = False
                    start_indices = []

                    continue
            if not hit:
                continue
            digit_pos = result.index(c)

            for j, index in enumerate(start_indices):
                # print(
                #     "swapping",
                #     result[index],
                #     result[digit_pos + j],
                #     "with",
                #     result[digit_pos + j],
                #     result[index],
                #     "index",
                #     index,
                #     digit_pos + j,
                # )
                result[index], result[digit_pos + j] = (
                    result[digit_pos + j],
                    result[index],
                )
                # print("".join(result))

    print("".join(result))
    total = 0

    for i, n in enumerate(result):
        if n == ".":
            continue
        total += i * int(n)

    print(total)


if __name__ == "__main__":
    run()
