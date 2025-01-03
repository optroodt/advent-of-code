from utils import load_file

inputs = list(map(int, load_file()))

it = iter(inputs)

last = next(it)

counter = 0

for i in it:
    if i > last:
        counter += 1

    last = i

print("Part One:", counter)

input_count = len(inputs)
values = []
results = []

it = iter(inputs)
values.append([next(it)])
sums = []

for i in it:
    for val in values:
        val.append(i)
    values.append([i])
    if len(values[0]) == 3:
        sums.append(sum(values.pop(0)))

it = iter(sums)
last = next(it)
counter = 0

for i in it:
    if i > last:
        counter += 1

    last = i

print("Part Two:", counter)
