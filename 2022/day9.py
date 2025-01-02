from copy import deepcopy
import itertools
def print_canvas(canv):
	for row in reversed(canv):
		print("".join(row))

def get_canvas_size(instructions):
	current_x, current_y = 0,0

	min_x, max_x, min_y, max_y = 0,0,0,0
	bounds = {"R": 0, "L":0, "U":0, "D":0}
	for d, u in instructions:
		if d == "R":
			current_x += u
		elif d == "U":
			current_y += u
		elif d == "D":
			current_y -= u
		elif d == "L":
			current_x -= u

		if current_x > max_x:
			max_x = current_x
		elif current_x < min_x:
			min_x = current_x
		elif current_y > max_y:
			max_y = current_y
		elif current_y < min_y:
			min_y = current_y

	print(min_x, max_x, min_y, max_y)
	print(max_x - min_x + 1, max_y-min_y + 1)
	return max_x - min_x + 1, max_y-min_y + 1, abs(min_x), abs(min_y)

def generate_canvas(x, y):
	canvas = []
	for i in range(y):
		canvas.append(["."] * x)

	return canvas

def instruction_to_steps(instruction):
	d, u = instruction
	# print(instruction)
	if d == "R":
		y = [0]
		x = [1]
	elif d == "U":
		y = [1]
		x = [0]
	elif d == "D":
		y = [-1]
		x = [0]
	elif d == "L":
		y = [0]
		x = [-1]
	# print(x, y)
	return list(itertools.zip_longest(x*u, y*u))

def new_tail_pos(hpos, tpos):
	abs_x = abs(hpos[0] - tpos[0])
	abs_y = abs(hpos[1] - tpos[1])
	# print(abs_x, abs_y)
	if abs_x > 1 or abs_y > 1:
		diagonal = False

		if abs_x != 0 and abs_y != 0:
			if hpos[0] > tpos[0]: # move right
				tpos[0] += 1
			elif hpos[0] < tpos[0]: # move left
				tpos[0] -= 1

			if hpos[1] > tpos[1]: # move up
				tpos[1] += 1			
			elif hpos[1] < tpos[1]: # move down
				tpos[1] -= 1					
			diagonal = True
		else:

			if hpos[0] > tpos[0]: # move right
				tpos[0] += 1
			elif hpos[0] < tpos[0]: # move left
				tpos[0] -= 1
			elif hpos[1] > tpos[1]: # move up
				tpos[1] += 1			
			elif hpos[1] < tpos[1]: # move down
				tpos[1] -= 1						
		# print("move tpos", hpos, tpos, "diagonal" if diagonal else "")
		# print(abs_x, abs_y)
		# print('new tpos', tpos)

	return tpos
		

		

def move(canvas, start, instructions):
	head = deepcopy(canvas)
	height = len(canvas[0])

	hpos = deepcopy(start)
	tpos = deepcopy(start)
	for instruction in instructions:
		for step in instruction_to_steps(instruction):
			hpos[0] += step[0]
			hpos[1] += step[1]

			
			tpos = new_tail_pos(hpos, tpos)
			# print(hpos, tpos)
			canvas[tpos[1]][tpos[0]] = '#'
		# print(hpos)
		# print_canvas(canvas)
		# print('---------')


	# print_canvas(canvas)

def run():

	with open('day9.txt', 'r') as fh:
		instructions = []
		for l in fh.readlines():
			d, u = l.strip().split(" ")
			instructions.append((d, int(u)))
			

	x, y, start_x, start_y = get_canvas_size(instructions)

	canvas = generate_canvas(x,y)

	move(canvas, [start_x, start_y], instructions)
	print_canvas(canvas)
	print(x,y)
	print(list(itertools.chain(*canvas)).count('#'))



if __name__ == "__main__":
	run()