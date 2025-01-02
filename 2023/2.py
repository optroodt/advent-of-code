import pathlib
import re
import string
from operator import methodcaller

path = pathlib.Path("2.txt")
with path.open("r") as fh:
    lines = map(str.strip, fh.readlines())

RED = "red"
GREEN = "green"
BLUE = "blue"
LIMITS = {RED: 12, GREEN: 13, BLUE: 14}


class Grab:
    def __init__(self, red=0, green=0, blue=0):
        self.red = red
        self.green = green
        self.blue = blue

    def is_valid(self, limits):
        for k, v in limits.items():
            if getattr(self, k) > v:
                return False
        return True


class Game:
    def __init__(self, game_number, grabs):
        self.game_number = game_number
        self.grabs = grabs
        self.max_values = {RED: 0, GREEN: 0, BLUE: 0}

    def find_maxes(self):
        for grab in self.grabs:
            for k in self.max_values.keys():
                v = getattr(grab, k)
                if v > self.max_values[k]:
                    self.max_values[k] = v

    def is_valid(self, limits):
        for grab in self.grabs:
            if not grab.is_valid(limits):
                return False
        return True

    def power(self):
        return (
            self.max_values.get(RED)
            * self.max_values.get(GREEN)
            * self.max_values.get(BLUE)
        )


def extract_game(value):
    g, rest = value.split(": ")
    game_number = int(g.split(" ")[1])

    grabs = rest.split("; ")
    grab_objects = []
    for grab in grabs:
        values = grab.split(", ")
        d = {v: int(k) for k, v in map(methodcaller("split", " "), values)}
        grab_objects.append(Grab(**d))
    return Game(game_number, grab_objects)


total = 0
total_power = 0

for line in lines:
    game = extract_game(line)
    game.find_maxes()
    if game.is_valid(LIMITS):
        total += game.game_number
    total_power += game.power()

print(total)  # 2600
print(total_power)  # 86036
