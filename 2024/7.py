import copy
import collections
import itertools
import operator
import pathlib
import re
import string
import functools

path = pathlib.Path("7.txt")
with path.open("r") as fh:
    lines = list(map(str.strip, fh.readlines()))


def concat_op(a, b):
    return int(str(a) + str(b))


def get_operators(n):
    yield itertools.product([operator.add, operator.mul, concat_op], repeat=n - 1)


def calculate(values, operations):
    # print(values, operations)
    running = values[0]
    for o, v in zip(operations, values[1:]):
        # print(o)
        running = o(running, v)
    return running


def run():
    total = 0
    for line in lines:
        parts = line.split(": ")
        result = int(parts[0])
        digits = list(map(int, parts[1].split(" ")))
        for operators in get_operators(len(digits)):
            for ops in operators:
                if result == calculate(digits, ops):
                    # print(result, calculate(digits, ops), digits)
                    total += result
                    break
        # break
    print(total)


if __name__ == "__main__":
    run()
