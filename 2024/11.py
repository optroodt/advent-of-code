import collections
import copy
import functools
import itertools
import operator
import pathlib
import re
import string

from utils import load_file

lines = load_file()


class Stone:
    def __init__(self, value):
        self.value = int(value)
        self.length = len(str(self.value))

    def __repr__(self):
        return f"<Stone v={self.value}>"

    def blink(self):
        if self.value == 0:
            return [Stone(1)]
        elif self.length % 2 == 0:
            mid = self.length // 2
            return [Stone(str(self.value)[:mid]), Stone(str(self.value)[mid:])]
        else:
            return [Stone(self.value * 2024)]


def run():
    starting_stones = [Stone(v) for v in lines[0].split(" ")]
    print(starting_stones)
    number_of_blinks = 25
    stones = starting_stones
    for i in range(number_of_blinks):
        stones = itertools.chain.from_iterable([stone.blink() for stone in stones])
    list_stones = list(stones)
    print("Part One:", len(list_stones))  # , list_stones)


if __name__ == "__main__":
    run()
