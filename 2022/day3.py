from collections import defaultdict
import string

LOOKUP = "_"+string.ascii_lowercase+string.ascii_uppercase

def find_common_part_two(one, two ,three):
	x = set(one) & set(two) & set(three)
	return list(x)[0]


def find_common(input):
	index = len(input)//2
	rest = input[index:]
	for c in input[:index]:
		if c in rest:
			return c

def get_priority(input, func):
	v = func(*input)
	return LOOKUP.index(v)

def run():
	score = 0
	with open("day3.txt", 'r') as fh:
		inputs = []
		counter = 0
		for l in fh.readlines():
			items = l.strip()

			inputs.append(items)
			if counter == 2:
				score += get_priority(inputs, find_common_part_two)
				counter = 0
				inputs = []
			else:
				counter += 1

	print(score)

if __name__ == "__main__":
	run()