from utils import load_file

lines = load_file()

depth = 0
position = 0

for line in lines:
    instr, str_value = line.split(" ")
    value = int(str_value)

    if instr == "forward":
        position += value
    elif instr == "up":
        depth -= value
    elif instr == "down":
        depth += value

print("Part One:", position * depth)

depth = 0
position = 0
aim = 0

for line in lines:
    instr, str_value = line.split(" ")
    value = int(str_value)

    if instr == "forward":
        position += value
        depth += aim * value
    elif instr == "up":
        aim -= value
    elif instr == "down":
        aim += value

print("Part Two:", position * depth)
