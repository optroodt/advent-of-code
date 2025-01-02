import pathlib
import re
import string
import operator

path = pathlib.Path("4.txt")
with path.open("r") as fh:
    lines = list(map(str.strip, fh.readlines()))


class Card:
    def __init__(self, card_number, winning_numbers, scratched_numbers):
        self.card_number = int(card_number)
        self.winning_numbers = winning_numbers
        self.scratched_numbers = scratched_numbers

    def matches(self):
        return self.winning_numbers & self.scratched_numbers

    def score(self):
        matches = self.matches()

        if not matches:
            return 0
        count = len(matches)
        if count == 1:
            return 1
        return 2 ** (count - 1)

    def get_copies_indices(self):
        match_count = len(self.matches())
        return [
            i - 1
            for i in range(self.card_number + 1, self.card_number + 1 + match_count)
        ]


def split_numbers(value):
    return {int(x) for x in re.split(" +", value) if x}


def run(lines):
    cards = []
    total_value = 0
    total_card_counts = []
    for line in lines:
        card, rest = line.split(": ")
        # print(card)
        _, card_number = re.split(" +", card)
        # print(card_number)
        winning, scratched = rest.split(" | ")

        winning_numbers = split_numbers(winning)
        scratched_numbers = split_numbers(scratched)
        c = Card(card_number, winning_numbers, scratched_numbers)
        cards.append(c)
        total_value += c.score()

    print(f"total value: {total_value}")

    total_card_counts = [1 for x in cards]
    for i, c in enumerate(cards):
        for j in range(total_card_counts[i]):
            indices = c.get_copies_indices()
            # print(indices)
            for k in indices:
                total_card_counts[k] += 1

    print(total_card_counts)
    print(sum(total_card_counts))


if __name__ == "__main__":
    run(lines)
