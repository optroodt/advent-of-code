import pathlib
import re
import string
import operator
from collections import Counter

path = pathlib.Path("7.txt")
with path.open("r") as fh:
    lines = list(map(str.strip, fh.readlines()))

JOKER = "J"
CARDS = "AKQJT98765432"
CARDS = "AKQT98765432J"
CARD_VALUES = string.ascii_lowercase[: len(CARDS)][::-1]
TYPE_FIVE = 7
TYPE_FOUR = 6
TYPE_FULL_HOUSE = 5
TYPE_THREE = 4
TYPE_TWO_PAIR = 3
TYPE_PAIR = 2
TYPE_HIGH = 1


def determine_rank(cards):
    c = Counter(cards)

    # print(c)
    values = list(c.values())
    # print(values)
    if len(c) == 1:
        return TYPE_FIVE
    elif 4 in values:
        return TYPE_FOUR
    elif 3 in values and 2 in values:
        return TYPE_FULL_HOUSE
    elif 3 in values:
        return TYPE_THREE
    elif Counter(values).get(2) == 2:
        return TYPE_TWO_PAIR
    elif 2 in values:
        return TYPE_PAIR
    else:
        return TYPE_HIGH


def determine_highest_rank(cards):
    if JOKER not in cards:
        return determine_rank(cards)

    c = Counter(cards)
    joker_count = c.pop(JOKER)
    cards_left = len(c)
    # print(joker_count, cards_left)
    if joker_count == 5:
        return TYPE_FIVE
    elif joker_count == 4:
        return TYPE_FIVE
    elif joker_count == 3:
        if cards_left == 1:
            return TYPE_FIVE
        else:
            return TYPE_FOUR
    elif joker_count == 2:
        if cards_left == 1:
            return TYPE_FIVE
        elif cards_left == 2:
            return TYPE_FOUR
        elif cards_left == 3:
            return TYPE_THREE
    elif joker_count == 1:
        values = list(c.values())
        if cards_left == 1:
            return TYPE_FIVE
        elif cards_left == 2:
            if 3 in values:
                return TYPE_FOUR
            else:
                return TYPE_FULL_HOUSE
        elif cards_left == 3:
            return TYPE_THREE
        elif cards_left == 4:
            return TYPE_PAIR


def determine_value(cards, rank):
    value = str(rank)
    for c in cards:
        value += CARD_VALUES[CARDS.index(c)]
    return value


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)
        self.rank = determine_rank(self.cards)
        self.value = determine_value(self.cards, self.rank)

    def __repr__(self):
        return f"<Hand {self.cards} bid={self.bid} rank={self.rank} value={self.value}>"


class HandTwo:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)
        self.rank = determine_highest_rank(self.cards)
        self.value = determine_value(self.cards, self.rank)

    def __repr__(self):
        return f"<Hand {self.cards} bid={self.bid} rank={self.rank} value={self.value}>"


def run():
    hands = []
    for line in lines:
        hands.append(HandTwo(*line.split(" ")))

    hands = sorted(hands, key=operator.attrgetter("value"))
    print(hands)
    total = 0

    for i, hand in enumerate(hands, start=1):
        # print(i, hand.bid)
        total += i * hand.bid

    # too high: 251556448
    # correct:  251136060
    print(total)

    # part two:
    # correct: 249400220


if __name__ == "__main__":
    run()
