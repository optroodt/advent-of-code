from collections import Counter, defaultdict

with open('7_input.txt', 'r') as fh:
	for line in fh.readlines():
		positions = [int(x) for x in line.strip().split(',')]

print(len(positions))

print(min(positions), max(positions))
c = Counter(positions)
print(c)
print(len(c))
print(c.most_common(5))

# for pos in sorted(c.keys()):
# 	print(pos, c[pos])

burn = defaultdict(int)

def calculate_fuel_burn(source, destination):
	return abs(source-destination)

cache = defaultdict(int)

def calc_inc_burn(source, destination):
	distance = abs(source-destination)
	if distance not in cache:
		incr_distance=  sum([i+1 for i in range(distance)])
		cache[distance] = incr_distance
	# print(f"- Move from {source} to {destination}: {incr_distance} fuel")
	return cache[distance]

def find_min(burned):
	return min(burned.values())


for i in range(max(positions)+1):
	for n in positions:
		burn[i] += calculate_fuel_burn(n, i)

# print(burn)
print(find_min(burn))

print('*' * 20)

burn = defaultdict(int)
for i in range(max(positions)+1):
	for n in positions:
		burn[i] += calc_inc_burn(n, i)

print(find_min(burn))
# x = Counter('aaabb')
# print(x)
# for i in x.keys():
# 	print(i, x[i])