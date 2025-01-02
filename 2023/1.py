import pathlib
import re
import string

path = pathlib.Path("1.txt")
with path.open("r") as fh:
	lines = map(str.strip, fh.readlines())

mapping = {"one":1,  "two":2, "three": 3,  "four": 4, "five": 5, "six": 6,  "seven": 7,  "eight":8, "nine":9,
"1":1,  "2":2, "3": 3,  "4": 4, "5": 5, "6": 6,  "7": 7,  "8":8, "9":9}

keywords = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for n in string.digits:
	if n == '0':
		continue
	keywords.append(str(n))
# print(keywords)

def create_trie(words):
	trie = {}
	for word in words:

		current = trie
		for l in word:
			current = current.setdefault(l, {})
	return trie
TRIE = create_trie(keywords)
print(TRIE)

def lookup_digit(value):
	return mapping.get(value)

def extract_digits(line):
	lookup = TRIE
	collected = []

	for start in range(len(line)):
		lookup = TRIE
		so_far = []
		sub = line[start:]
		for i, c in enumerate(sub):
			lookup = lookup.get(c)
			if lookup is None:
				break
			else:
				so_far.append(c)

			if lookup == {}:
				collected.append("".join(so_far))
				break
	
	digits = list(map(lookup_digit, collected))
	return digits
		

def collect_numbers(values):
	return int(str(values[0]) + str(values[-1]))

total = 0
all_numbers = []
for x, line in enumerate(lines):

	digits = extract_digits(line)
	
	added = collect_numbers(digits)
	all_numbers.append(added)
	total += added
# too high: 54559
# correct: 54518
print(len(all_numbers))
print(total)
