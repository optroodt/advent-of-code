from collections import Counter
from utils import load_file

inputs = load_file()


values = [[] for i in range(12)]

for number in inputs:
    for i, num in enumerate(list(map(int, number))):
        values[i].append(num)

gamma = ""
epsilon = ""
for i, val in enumerate(values):
    if sum(val) > 500:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

# print(gamma, int(gamma, 2))
# print(epsilon, int(epsilon, 2))
print("Part One:", int(gamma, 2) * int(epsilon, 2))


def most_common_oxygen(values):
    result = Counter(values).most_common(2)

    if result[0][1] == result[1][1]:
        return "1"
    return result[0][0]


def least_common_co2(values):
    result = Counter(values).most_common(2)

    if len(result) < 2:
        if result[0][1] == "1":
            return "0"

        return "1"

    if result[0][1] == result[1][1]:
        return "0"

    return result[1][0]


safecopy = inputs.copy()

for pos in range(12):
    keep = most_common_oxygen([line[pos] for line in inputs])

    new_inputs = [line for line in inputs if line[pos] == keep]
    if len(new_inputs) == 1:
        oxygen = new_inputs[0]
        break
    inputs = new_inputs

inputs = safecopy
for pos in range(12):
    keep = least_common_co2([line[pos] for line in inputs])

    new_inputs = [line for line in inputs if line[pos] == keep]
    if len(new_inputs) == 1:
        co2 = new_inputs[0]
        break

    inputs = new_inputs

# correct:
# oxygen 011010110111 1719
# co2 100101100000 2400
# 4125600
# print("oxygen", oxygen, int(oxygen, 2))
# print("co2", co2, int(co2, 2))

print("Part Two:", int(oxygen, 2) * int(co2, 2))
