import pathlib
import re
import string
import operator

path = pathlib.Path("3.txt")
with path.open("r") as fh:
    lines = list(map(str.strip, fh.readlines()))

NUMBERS = set(string.digits)
EMPTY = "."
NUMBER_OR_EMPTY = NUMBERS ^ {EMPTY}

print(NUMBER_OR_EMPTY)
ROWS = len(lines)
COLUMNS = len(lines[0])
print(COLUMNS, ROWS)


def get_positions(lines):
    symbol_positions = []
    part_numbers = []
    for rownum, line in enumerate(lines):
        number = ""
        y = rownum
        start_x = None
        end_x = None
        for colnum, char in enumerate(line):
            if char in NUMBERS:
                if start_x is None:
                    start_x = colnum
                number += char
            elif start_x is not None:
                end_x = colnum - 1
                part_numbers.append((number, (start_x, y), (end_x, y)))
                start_x = None
                end_x = None
                number = ""

            if char not in NUMBER_OR_EMPTY:
                symbol_positions.append(((colnum, rownum), char))

        if start_x is not None:
            end_x = colnum
            part_numbers.append((number, (start_x, y), (end_x, y)))

    # print(part_numbers)
    return part_numbers, symbol_positions


def generate_bounding_boxes(values):
    bounding_boxes = []
    for number, start, end in values:
        ys = set([max(0, start[1] - 1), start[1], min(ROWS - 1, start[1] + 1)])
        positions = {
            (x, y) for y in ys for x in range(max(0, start[0] - 1), end[0] + 2)
        }
        bounding_boxes.append((number, positions))

    return bounding_boxes


parts, sympos = get_positions(lines)

positions = generate_bounding_boxes(parts)

print("=" * 10)

total = 0
total_gears = 0
gear_positions = []
gear_connected = []
for number, poss in positions:
    include = False

    for symbol, character in sympos:
        if symbol in poss:
            include = True
            if character == "*":  # 730
                total_gears += 1
                gear_positions.append(symbol)
                gear_connected.append((number, poss))
    if not include:
        pass
    else:
        total += int(number)

# too low: 543410
# too high: 547025
# correct: 546312
print(f"The sum is {total}")
print("=" * 10)

pairs = []
while gear_connected:
    num_1, box_1 = gear_connected[0]
    found_one = False
    for i, (num_rest, box_rest) in enumerate(gear_connected[1:], start=1):
        for g, gear_pos in enumerate(gear_positions):
            if gear_pos in (box_1 & box_rest):
                # print(num_1, num_rest)
                pairs.append((int(num_1), int(num_rest)))
                print(f"dropping {gear_connected[0][0]} and {gear_connected[i][0]}")
                gear_connected.pop(i)
                gear_connected = gear_connected[1:]
                found_one = True
                gear_positions.pop(g)  # remove, because we've used it
                break
        if found_one:
            break
    if not found_one:
        print(f"removing {gear_connected[0][0]}")
        gear_connected = gear_connected[1:]  # remove, not connected

# too low: 76750112
# too low: 83791244
# correct: 87449461
print("Sum of all gears: ", sum([operator.mul(*x) for x in pairs]))
