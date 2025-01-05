import itertools

from utils import load_file

lines = load_file()


class Cache:
    def __init__(self):
        self.lookup = {}

    def get(self, v, number_of_blinks):
        return self.lookup.get((v, number_of_blinks))

    def set(self, v, number_of_blinks, value):
        self.lookup[(v, number_of_blinks)] = value


cache = Cache()


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


def recurse(stones, blinks, current):
    if blinks == current:
        return len(stones)
    result = 0
    for stone in stones:
        value = cache.get(stone.value, current + 1)
        if value is None:
            value = recurse(stone.blink(), blinks, current + 1)
            cache.set(stone.value, current + 1, value)
        result += value
    return result


def run():
    starting_stones = [Stone(v) for v in lines[0].split(" ")]
    print(starting_stones)
    number_of_blinks = 25
    stones = starting_stones
    for i in range(number_of_blinks):
        stones = itertools.chain.from_iterable([stone.blink() for stone in stones])
    list_stones = list(stones)
    print("Part One:", len(list_stones))  # Correct answer: 190865

    the_answer = recurse(starting_stones, 75, 0)
    print("Part Two:", the_answer)  # Correct answer: 225404711855335


if __name__ == "__main__":
    run()
