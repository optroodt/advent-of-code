import itertools
import operator
import pathlib

path = pathlib.Path("7.txt")
with path.open("r") as fh:
    lines = list(map(str.strip, fh.readlines()))


def concat_op(a, b):
    return int(str(a) + str(b))


def get_operators(part=1):
    if part == 1:
        return [operator.add, operator.mul]

    return [operator.add, operator.mul, concat_op]


def get_operations(n, operations):
    yield itertools.product(operations, repeat=n - 1)


def calculate(values, operations):
    running = values[0]
    for o, v in zip(operations, values[1:]):
        running = o(running, v)
    return running


def run():

    for title, operators_in_part in [
        ("Part One:", get_operators()),
        ("Part Two:", get_operators(part=2)),
    ]:
        total = 0
        for line in lines:
            parts = line.split(": ")
            result = int(parts[0])
            digits = list(map(int, parts[1].split(" ")))
            for operators in get_operations(len(digits), operators_in_part):
                for ops in operators:
                    if result == calculate(digits, ops):
                        total += result
                        break
        print(title, total)


if __name__ == "__main__":
    run()
