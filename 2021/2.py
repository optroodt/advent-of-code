# depth = 0
# position = 0

# with open('2_input.txt', 'r') as fh:
# 	for line in fh.readlines():
# 		instr, str_value = line.strip().split(' ')
# 		value = int(str_value)

# 		if instr == 'forward':
# 			position += value
# 		elif instr == 'up':
# 			depth -= value
# 		elif instr == 'down':
# 			depth += value

# print(position * depth)

depth = 0
position = 0
aim = 0

with open('2_input.txt', 'r') as fh:
	for line in fh.readlines():
		instr, str_value = line.strip().split(' ')
		value = int(str_value)

		if instr == 'forward':
			position += value
			depth += aim * value
		elif instr == 'up':
			# depth -= value
			aim -= value
		elif instr == 'down':
			# depth += value
			aim += value

print(position * depth)
