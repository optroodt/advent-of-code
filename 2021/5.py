coordinates = []
max_x, max_y = 0,0
with open('5_input.txt', 'r') as fh:
	for line in fh.readlines():

		a, b = line.strip().split(" -> ")
		pair = [tuple(map(int, x.split(','))) for x in [a,b]]
		coordinates.append(pair)

for a, b in coordinates:
	max_x = max(max_x,a[0])
	max_x = max(max_x,b[0])
	max_y = max(max_y,a[1])
	max_y = max(max_y,b[1])

# print(coordinates, len(coordinates))
print(max_x, max_y)
grid = [0] * (max_x * max_y)
def get_straight(values):
	result = []
	for a, b in values:
		if a[0] == b[0] or a[1] == b[1]:
			result.append([a,b])
	return result

straight = get_straight(coordinates)
print(len(straight))

def calculate_index(x, y):
	return x + y*(max_x-1)

def calculate_positions(a, b):
	x_correction = -1 if b[0] < a[0] else 1
	y_correction = -1 if b[1] < a[1] else 1
	xs = range(a[0], b[0] + x_correction, x_correction)
	ys = range(a[1], b[1] + y_correction, y_correction)
	# print(xs, ys)
	positions = []

	if a[0] != b[0] and a[1] != b[1]:
		for x,y in zip(xs, ys):
			positions.append((x,y))
	else:
		for x in xs:
			for y in ys:
				positions.append((x,y))

	return positions

def calculate_indices(positions):

	return [calculate_index(x,y) for x,y in positions]

# for a,b in straight:
for a,b in coordinates:
	# print(a,b)
	positions = calculate_positions(a,b)
	
	indices = calculate_indices(positions)
	for index in indices:
		# print(index, len(grid))
		grid[index] += 1

count = 0
for i in grid:
	if i > 1:
		count += 1

print(count)