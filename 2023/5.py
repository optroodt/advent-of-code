import pathlib
import re
import string
import operator

path = pathlib.Path("5.txt")
with path.open("r") as fh:
    lines = list(map(str.strip, fh.readlines()))


MAP_KEYWORD = "map"
SEEDS = [int(x) for x in lines[0].split(": ")[1].split(" ")]
RANGES = {}
MAPPING_ORDER = []


class Range:
    def __init__(self, map_type, destination_range, start_range, length):
        self.map_type = map_type
        self.destination_range = destination_range
        self.start_range = start_range
        self.length = length
        self.offset = destination_range - start_range

    def __repr__(self):
        return f"<{self.map_type}: {self.destination_range} {self.start_range} {self.length}>"

    def __contains__(self, value):
        return self.start_range <= value < self.start_range + self.length

    def destination_value(self, value):
        return value + self.offset


for line in lines[2:]:
    if line == "":
        continue

    if MAP_KEYWORD in line:
        map_type, _ = line.split(" ")
        MAPPING_ORDER.append(map_type)
        RANGES[map_type] = []
        continue

    r = Range(map_type, *[int(x) for x in line.split(" ")])
    RANGES[map_type].append(r)

lowest_value = None
for seed in SEEDS:
    value = seed
    for mapping in MAPPING_ORDER:
        for r in RANGES[mapping]:
            if value in r:
                print(
                    f"Yup, {mapping} contains {value} -> {r.destination_value(value)}: {r}"
                )
                value = r.destination_value(value)
                break

    if lowest_value is None or value < lowest_value:
        lowest_value = value

print(lowest_value)
