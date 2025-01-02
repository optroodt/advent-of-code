from collections import defaultdict

def get_containers(line):
	containers = []
	# print(line)
	for i in range(0, len(line), 4):
		index = i//3
		container = line[i:i+3]
		containers.append(container)

	return containers

def execute(stacks, instruction):
	parts = instruction.split(" ")
	# print(parts)
	count, source, target = map(int, [parts[1], parts[3], parts[5]])
	# print(count, source, target)
	for i in range(count):
		stacks[target-1].insert(0, stacks[source-1].pop(0))

def execute_part_two(stacks, instruction):
	parts = instruction.split(" ")
	# print(parts)
	count, source, target = map(int, [parts[1], parts[3], parts[5]])
	# print(count, source, target)
	temp = []
	temp, stacks[source-1] = stacks[source-1][:count], stacks[source-1][count:]

	stacks[target-1] = temp + stacks[target-1]

def run():
	stacks = defaultdict(list)

	c_section = True

	with open('day5.txt', 'r') as fh:
		for l in fh.readlines():
			line = l.strip("\n")

			if c_section:
				containers = get_containers(line)
				for i, c in enumerate(containers):

					if c != "   ":
						stacks[i].append(c)
			else:
				# print(line)
				execute_part_two(stacks, line)

			if line == "":
				c_section = False
				for k, v in stacks.items():
					v.pop()

	word = []
	for k in sorted(stacks.keys()):
		word.append(stacks[k][0][1])

	print("".join(word))


if __name__ == "__main__":
	run()