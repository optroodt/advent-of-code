from collections import Counter, defaultdict

lookup = {3:7, 4:4, 2:1, 7:8}
pairs = []
with open('8_input.txt', 'r') as fh:
	for line in fh.readlines():
		inputs, outputs = line.strip().split(" | ")
		inputs = inputs.split(' ')
		outputs = outputs.split(' ')
		pairs.append((inputs, outputs))

# print(pairs)

counter = 0
for inputs, outputs in pairs:
	for digit in outputs:
		if len(digit) in lookup:
			counter += 1

print(counter)

def find_digit(digit, inputs):
	l = 1000
	for k,v in lookup.items():
		if v == digit:
			l = k
			break

	for i in inputs:
		if len(i) == l:
			return i

	return None

# def figure_out()
D_LOOKUP = {
	'cf': 1, 'abcdfg': 9, 'acf': 7, 'bcdf': 4, 'acdeg': 2, 'acdfg': 3, 'abcefg': 0, 'abdfg':5, 'abdefg':6, 'abcdefg':8
}

def assemble_digit(builder, pattern):
	v = ''
	for c in pattern:
		v += builder.get(c)

	output_pattern = ''.join(sorted(v))
	return D_LOOKUP[output_pattern]

total = 0 

for inputs, outputs in pairs:
	assembled = dict()

	print(inputs, outputs)
	known_digits = dict()
	for i in [1,4,7,8]:
		known_digits[i] = find_digit(i, inputs)
	print(known_digits)
	if known_digits[1] and known_digits[7]:
		seg_a = set(known_digits[7]) - set(known_digits[1])
		assembled['a'] = seg_a.pop()

	# rem = set(known_digits[8]) - set(known_digits[4])
	# seg_eg = rem - set(known_digits[7])

	loop_count = 1
	while len(known_digits) < 10 or len(assembled.keys()) < 7:
		print(f'Loop {loop_count}')
		loop_count += 1
	# for _ in range(10):
		for i in inputs:
			dig_set = set(i)
			if len(i) == 6:
				res = dig_set & set(known_digits[1])
				if len(res) == 1:
					known_digits[6] = i
					assembled['c'] = (set(known_digits[1]) - res).pop()
					# assembled['f'] = (set(known_digits[1]) - set(assembled['c'])).pop()
				else:
					if 5 in known_digits:
						res = dig_set - (set(known_digits[5]) | set(known_digits[1]))
						if len(res) == 0:
							known_digits[9] = i
							res_2 = dig_set - (set(known_digits[4]) | set(known_digits[7]))
							assembled['g'] = res_2.pop()
							continue

						res = dig_set - set(known_digits[5])
						if len(res) == 1:
							known_digits[9] = i
							assembled['c'] = res.pop()
							continue

						if len(res) == 2:
							known_digits[0] = i
							# assembled['e'] = res.pop()
							res_2 = set(known_digits[8]) - dig_set
							assembled['d'] = res_2.pop()
							continue
				# res = set(known_digits[8]) - dig_set
				# if len(res) == 1:
				# 	assembled['d'] = res.pop()


			if len(i) == 5:
				res = dig_set & set(known_digits[1])
				if len(res) == 2:
					known_digits[3] = i
					res_2 = set(known_digits[4]) - dig_set
					assembled['b'] = res_2.pop()
					continue

				res = dig_set - (set(known_digits[4]) | set(known_digits[7]))
				if len(res) == 2:
					known_digits[2] = i
					assembled['c'] = (dig_set & set(known_digits[1])).pop()
				elif len(res) == 1:
					known_digits[5] = i
					assembled['f'] = (dig_set & set(known_digits[1])).pop()

				if 9 in known_digits:
					res = dig_set - set(known_digits[9])
					if len(res) == 1:
						known_digits[2] = i
						assembled['e'] = res.pop()
						continue



	print(len(known_digits))
	print(known_digits)

	print(assembled)
	print(len(assembled))
	assert len(set(assembled.keys())) == 7, ''.join(assembled.keys())
	assert len(set(assembled.values())) == 7, ''.join(assembled.values())
	inverted = {v:k for k,v in assembled.items()}
	# we now have everything we need

	temp_num = ''
	for n in outputs:
		# print(n)
		number = assemble_digit(inverted, n)
		temp_num += str(number)
	# print(number)
	total += int(temp_num)

print(total) # correct answer 1043101
