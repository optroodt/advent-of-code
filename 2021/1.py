inputs = []
with open('1_input.txt', 'r') as fh:
	for line in fh.readlines():
		inputs.append(int(line.strip()))

it = iter(inputs)

last = next(it)

counter = 0

for i in it:
	if i > last:
		counter += 1

	last = i

print (counter)

# ---------

index = 3
input_count = len(inputs)
values = [] #[0] * input_count()
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

print (counter)

