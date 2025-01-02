import itertools
import math
import operator
WIDTH = None
HEIGHT = None
trees = ""
seen_trees = [""]
enable_print = False

def print_grid(grid):
	for i in range(0, len(grid), WIDTH):
		print(" ".join([f"{x}".center(3, " ") for x in grid[i:i+WIDTH]]))

def _position_to_coords(i):
	y = i//HEIGHT
	x = i - (y* HEIGHT)
	return x, y

def _coords_to_position(x,y):
	return x + y * HEIGHT

def get_tree_at_position(x, y):
	index = _coords_to_position(x,y)
	return int(trees[index])

def mark_position(x, y):
	index = _coords_to_position(x,y)
	seen_trees[index] = "X"

def look_vertical(x):
	for ranges in [range(HEIGHT), reversed(range(HEIGHT))]:
		last_tree = -1
		for i in ranges:
			tai = get_tree_at_position(x, i)
			if tai > last_tree:
				last_tree = tai
				mark_position(x, i)

def look_horizontal(y):
	for ranges in [range(WIDTH), reversed(range(WIDTH))]:
		last_tree = -1
		for i in ranges:
			tai = get_tree_at_position(i, y)
			if tai > last_tree:
				last_tree = tai
				mark_position(i, y)

# def get_scores(current_tree, x=None, y=None, range_a=[], range_b=[]):
# 	for ranges in [list(range_a), list(range_b)]:
# 		sub_score = 0
# 		last_tree = current_tree

# 		trees_seen = []
# 		for j in ranges:
# 			tai = get_tree_at_position(x, j)
# 			# print(tai)
# 			sub_score +=1
# 			if tai >= last_tree:
# 				print("Bumped into", tai, "while I am", t, ". Seen", trees_seen, "sub-score is now", sub_score)
# 				trees_seen = []
# 				last_tree = t
# 				break 

# 			last_tree = tai
# 			trees_seen.append(tai)

# 		total_score.append(sub_score)
# 		sub_score = 0

def output(stuff):
	# global enable_printenable_print = False
	if not enable_print:
		return

	print(*stuff)

def calculate_scenic_score(i):
	global enable_print
	x,y = _position_to_coords(i)
	if x in (0,WIDTH-1) or y in (0, HEIGHT-1): #shortcut
		# print(f"skipping {x},{y}")
		return 0
	enable_print = False
	if x == 7 and y == 49:
		enable_print = True

	t = get_tree_at_position(x,y)
	# print(x,y)

	output([f"Tree at ({x}, {y}), value {t}"])
	total_score = []
	output(["VERTICAL"])
	for ranges in [list(reversed(range(y))), list(range(y+1, HEIGHT))]:
		sub_score = 0
		last_tree = t
		# print(ranges, t)
		trees_seen = []
		for j in ranges:
			tai = get_tree_at_position(x, j)
			# print(tai)
			sub_score +=1
			if tai >= t:
				output(["Bumped into", tai, "while I am", t, ". Seen", trees_seen, "sub-score is now", sub_score])
				trees_seen = []
				# last_tree = t
				break 

			# last_tree = tai
			trees_seen.append(tai)

		total_score.append(sub_score)
		sub_score = 0

	output(["HORIZONTAL"])
	for ranges in [list(reversed(range(x))), list(range(x+1, WIDTH))]:
		sub_score = 0
		last_tree = t
		# print(ranges, t)
		trees_seen = []
		for j in ranges:
			tai = get_tree_at_position(j, y)
			sub_score +=1 
			if tai >= t:
				output(["Bumped into", tai, "while I am", t, ". Seen", trees_seen, "sub-score is now", sub_score])
				# last_tree = t
				break
			
			# last_tree = tai
		total_score.append(sub_score)
		sub_score = 0
	product = math.prod(total_score)

	output(["Values:", total_score, ", product", product, f"Tree at ({x}, {y}), value {t}"])
	return product

def look_around():
	scenic_scores = [0] * WIDTH * HEIGHT

	for i, t in enumerate(trees):
		scenic_score = calculate_scenic_score(i)
		# print(scenic_score)
		scenic_scores[i] = scenic_score

	# print(scenic_scores)
	
	print_grid(scenic_scores)
	print("----------")
	print_grid([t for t in trees])

	print(f"Maximum scenic score: {max(scenic_scores)}")

def run():
	global trees, seen_trees, WIDTH, HEIGHT
	with open('day8.txt', 'r') as fh:
		for i, l in enumerate(fh.readlines(), start=1):
			row = l.strip()
			trees += row
			# print(row)
		WIDTH = len(row)
		HEIGHT = i
	seen_trees = seen_trees * WIDTH * HEIGHT

	# print(trees, WIDTH, HEIGHT)

	# for i in range(WIDTH):
	# 	look_vertical(i)
	# for i in range(HEIGHT):
	# 	look_horizontal(i)

	# print(seen_trees)
	# print(seen_trees.count("X"))

	look_around()

if __name__ == "__main__":
	run()