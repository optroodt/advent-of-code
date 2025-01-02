import math
import operator

def get_operator(text):
	parts = text.split("=")[1].split(" ")[1:]

	parsed = []
	for part in parts:
		if part == "old":
			parsed.append(part)
		elif part == "*":
			op = operator.mul
		elif part == "+":
			op = operator.add
		else:
			parsed.append(int(part))

	return op, parsed

def get_test(text):
	v = int(text[0].split(" ")[-1])
	t = int(text[1].split(" ")[-1])
	f = int(text[2].split(" ")[-1])
	return v, t, f

class Monkey:
	def __init__(self, text):
		self.id = int(text[0].split(" ")[1].split(":")[0])
		self.items = list(map(int, text[1].split(":")[1].split(",")))
		self.operator, self.operands = get_operator(text[2])
		self.div_value, self.target_true, self.target_false = get_test(text[3:])
		self.inspections = 0

	def __repr__(self):
		return f"<Monkey id={self.id}, items={self.items} operator={self.operator} test={self.div_value}>"

	def receive(self, item):
		self.items.append(item)

	def iter_items(self):
		while self.items:
			yield self.items.pop(0)

	def inspect(self, worry):
		self.inspections += 1
		params = []

		for o in self.operands:
			if o == "old":
				params.append(worry)
			elif isinstance(o, int):
				params.append(o)

		return self.operator(*params)
		

	def target_monkey(self, worry_level):
		if worry_level % self.div_value == 0:
			return self.target_true
		else:
			return self.target_false

def run():
	monkeys = []
	with open('day11.txt', 'r') as fh:
		monkey_text = []
		for l in fh.readlines():
			line = l.strip()
			if line =="":
				monkeys.append(Monkey(monkey_text))
				monkey_text = []
				continue
			monkey_text.append(line)
	monkeys.append(Monkey(monkey_text))

	divisors = [m.div_value for m in monkeys]
	lcm = math.lcm(*divisors)
	print(f"Least common multiple: {lcm}")

	for i in range(10000):
		for monkey in monkeys:
			for item in monkey.iter_items():
				worry_level = monkey.inspect(item)
				new_worry_level = worry_level % lcm

				target = monkey.target_monkey(new_worry_level)
				monkeys[target].receive(new_worry_level)
	
	# print(monkeys)
	for m in monkeys:
		print(f"Monkey {m.id} inspected items {m.inspections} times.")
	print(math.prod(sorted([m.inspections for m in monkeys])[-2:]))

	# print(math.gcd(23, 19, 13, 17))
	# too high
	# 24022055084 
	# 18816098508
	# 18170818354


if __name__ == "__main__":
	run()