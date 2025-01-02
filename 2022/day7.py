from pprint import pprint
from collections import defaultdict


sums = []
def get_sum(d, path="/"):
	total = 0

	cur_path = path
	for k, v in d.items():
		
		if isinstance(v, dict):
			cur_path = path + f"_{k}"	

			total += get_sum(v, path=cur_path)
			# print(cur_path, total)
		else:
			# cur_path = path	
			total += v
	print(path, total)
	sums.append((path, total))
	return total

def run():
	fs = {}
	stack = []

	with open('day7.txt', 'r') as fh:
		current = fs
		for l in fh.readlines():
			
			command = l.strip()
			if command == "$ cd /":
				current = fs
				stack = []
			elif command == "$ cd ..":
				stack.pop()
				current = fs
				for s in stack:
					current = current[s]

			elif command.startswith('$ cd '):
				directory = command[5:]
				stack.append(directory)
				if directory not in current:
					current[directory] = {}

				current = current.get(directory)
			elif command == '$ ls':
				# file listing will follow
				continue
			elif command.startswith('dir'):
				directory = command[4:]
				if directory not in current:
					current[directory] = {}
			else:
				parts = command.split(" ")
				size = int(parts[0])
				name = parts[1]
				current[name] = size


	pprint(fs)
	# print(get_sum(fs['a']['e']))
	# print(get_sum(fs['d']))
	get_sum(fs)
	print(sums)
	everything = 0
	for p, s in sums:
		if s < 100_000:
			everything += s

	print(everything)
	target_space = 30_000_000
	current_taken = 70_000_000 - 48_044_502
	print(current_taken)
	needed = target_space - current_taken
	print("needed", needed)
	current_best = current_taken
	for path, size in sums:
		# print(path, size)
		if needed - size < 0:
			# consider
			if size < current_best:
				current_best = size
				print(path, size)

	print (current_best)



			

if __name__ == "__main__":
	run()