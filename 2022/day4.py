from collections import defaultdict
import string

def is_overlap(inputs):
	print(inputs)
	a, b = inputs.split(',')

	a1, a2 = map(int, a.split("-"))
	b1, b2 = map(int, b.split("-"))

	if a1 >= b1 and a2 <= b2:
		return 1

	if b1 >= a1 and b2 <= a2:
		return 1

	return 0

def is_overlap_part_two(inputs):
	a, b = inputs.split(',')

	a1, a2 = map(int, a.split("-"))
	b1, b2 = map(int, b.split("-"))

	result = set(range(a1, a2+1)) & set(range(b1, b2+1))
	if result:
		return 1
	return 0


def run():
	score = 0
	with open("day4.txt", 'r') as fh:

		for l in fh.readlines():

			score += is_overlap_part_two(l.strip())

	print(score)

if __name__ == "__main__":
	run()