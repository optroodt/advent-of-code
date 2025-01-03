from collections import defaultdict

from utils import load_file

lines = load_file()
for line in lines:
    positions = [int(x) for x in line.split(',')]

# print(len(positions))
# print(min(positions), max(positions))

burn = defaultdict(int)


def calculate_fuel_burn(source, destination):
    return abs(source - destination)


cache = defaultdict(int)


def calc_inc_burn(source, destination):
    distance = abs(source - destination)
    if distance not in cache:
        incr_distance = sum([i + 1 for i in range(distance)])
        cache[distance] = incr_distance
    # print(f"- Move from {source} to {destination}: {incr_distance} fuel")
    return cache[distance]


def find_min(burned):
    return min(burned.values())


for i in range(max(positions) + 1):
    for n in positions:
        burn[i] += calculate_fuel_burn(n, i)

print("Part One:", find_min(burn))

burn = defaultdict(int)
for i in range(max(positions) + 1):
    for n in positions:
        burn[i] += calc_inc_burn(n, i)

print("Part Two:", find_min(burn))
