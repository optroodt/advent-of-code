import pathlib
import re
import string
import operator

path = pathlib.Path("5.txt")
with path.open("r") as fh:
    lines = list(map(str.strip, fh.readlines()))


class SeedRange:
    def __init__(self, start, length):
        self.start = start
        self.length = length
        self.end = self.start + self.length

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.start} {self.start + self.length}>"

    def __contains__(self, value):
        return self.start <= value <= self.end


MAP_KEYWORD = "map"
SEEDS = []
for i, x_ in enumerate(lines[0].split(": ")[1].split(" "), start=1):
    x = int(x_)
    if i % 2 == 1:
        seed = [x]
    else:
        seed.append(x)
        SEEDS.append(SeedRange(*seed))


RANGES = {}
MAPPING_ORDER = []


class Range:
    def __init__(self, map_type, destination_range, start_range, length):
        self.map_type = map_type
        self.destination_range = destination_range
        self.start_range = start_range
        self.start = start_range
        self.length = length
        self.end = start_range + length
        self.offset = destination_range - start_range

    def __repr__(self):
        return f"<{self.map_type}: {self.start_range} - {self.end} ({self.destination_range} - {self.destination_range + self.length})>"

    def __contains__(self, value):
        return self.start_range <= value < self.start_range + self.length

    def destination_value(self, value):
        return value + self.offset

    def is_intersection(self, seedrange):
        if (
            self.start_range <= seedrange.start <= self.start_range + self.length
            or self.start_range <= seedrange.end <= self.start_range + self.length
        ):
            return True

        return False

    def intersect(self, seedrange):
        new_seed_ranges = []
        if (
            self.start in seedrange
            and self.end in seedrange
            # or seedrange.start in self
            # or seedrange.end in self
        ):
            # if seedrange.start in self or seedrange.end in self:
            print(f"Mapping is within {seedrange} {self}")

            # new_range = (max(self.start, seedrange.start), min(self.end, seedrange.end))
            # print(new_range)

            values = sorted(
                # [seedrange.start, seedrange.end, new_range[0], new_range[1]]
                [seedrange.start, seedrange.end, self.start, self.end]
            )
            # print(values)

            new_seed_ranges.append(SeedRange(values[0], values[1] - values[0]))

            new_seed_ranges.append(
                SeedRange(
                    self.destination_value(values[1]),
                    self.destination_value(values[2])
                    - self.destination_value(values[1]),
                )
            )
            new_seed_ranges.append(SeedRange(values[2], values[3] - values[2]))

            return new_seed_ranges
        elif self.start in seedrange:
            new_seed_ranges.append(
                SeedRange(seedrange.start, self.start - seedrange.start)
            )
            # convert this one
            new_seed_ranges.append(
                SeedRange(
                    self.destination_value(self.start),
                    self.destination_value(seedrange.end)
                    - self.destination_value(self.start),
                )
            )
            return new_seed_ranges
        elif self.end in seedrange:
            # convert this one
            new_seed_ranges.append(
                SeedRange(
                    self.destination_value(seedrange.start),
                    self.destination_value(self.end)
                    - self.destination_value(seedrange.start),
                )
            )
            new_seed_ranges.append(SeedRange(self.end, seedrange.end - self.end))
            return new_seed_ranges
        # else:
        #     return seedrange

        # if self.start_range > seedrange.self.start or self.start_range + self.length
        # self.start_range, self.start_range + self.length
        # return range(max(x[0], y[0]), min(x[-1], y[-1])+1)

        # s1--------------e1
        #            s2--------------e2

        # s1--------------e1
        #       s2----e2

        #          s1--------------e1
        #     s2-------------e2


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

current_ranges = SEEDS
print(f"Started with {len(SEEDS)} SeedRanges")
for mapping in MAPPING_ORDER:
    new_ranges = []
    print(mapping)
    print(f"Current rnages {len(current_ranges)}")
    for seed in current_ranges:
        for r in RANGES[mapping]:
            # print(r, seed)
            # this gets me the new ranges after conversion.
            result = r.intersect(seed)

            if result is not None:
                print(result)
                new_ranges.extend(result)
                break
        else:
            # print("No overlap")
            new_ranges.append(seed)

    current_ranges = new_ranges
    # if lowest_value is None or value < lowest_value:
    #     lowest_value = value

print(f"Now have {len(current_ranges)} SeedRanges")
# print(current_ranges)
# print(lowest_value)
lowest_value = 13071831978

# Too high: 54982184
# Too high: 54982183
#           23043868
# Too low:   3340848
# this      34039469
GOAL = 34039469
# print(current_ranges)
for r in current_ranges:
    if r.start < lowest_value:
        lowest_value = r.start
print(lowest_value)
if lowest_value == GOAL:
    print("!!! YESSSS YOU GOT IT")
