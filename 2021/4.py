import copy
import re
numbers = []
boards = []
score = "XXXXX"

def eval_board(board):
	for i in range(0, 25, 5):
		if ''.join(map(str, board[i:i+5])) == score:
			# print(''.join(map(str, board[i:i+5])))
			return True

	for i in range(5):
		indices = [n for n in range(i, 25, 5)]
		if ''.join([str(board[index]) for index in indices]) == score:
			# print(''.join([str(board[index]) for index in indices]))
			return True

	return False


def sum_board(board):
	return sum([i for i in board if i != "X"])

def mark_boards(digit, boards):
	for i in range(len(boards)):
		for n in range(len(boards[i])):
			if boards[i][n] == digit:
				boards[i][n] = "X"
		# set_digit(i, board)
	return boards

# def set_digit(i, board):
# 	for c in board:
# 		if c == i:
# 			c = "X"

with open('4_input.txt', 'r') as fh:
	lines = iter(fh.readlines())
	
	numbers = list(map(int, next(lines).strip().split(',')))
	print(numbers)

	
	board = []
	line_count = 0
	for line in lines:
		if line.strip() == '':
			continue

		board.extend(list(map(int, re.split(' +', line.strip()))))
		line_count += 1

		if line_count == 5:
			boards.append(board)
			board = []
			line_count = 0

# backup_boards = copy.deepcopy(boards)
# stop = False
# for i in numbers:
# 	mark_boards(i, boards)
# 	# print(boards)
# 	for board in boards:
# 		if eval_board(board):
# 			print(i, board)
# 			score = sum_board(board) * i
# 			print("BINGO!!", score)
# 			stop = True
# 			break
# 		if stop:
# 			break
# 	if stop:
# 		break
	# numbers = 
	# for line in :
	# 	inputs.append(int(line.strip()))
# print(boards)
# 1: correct 38594

print('sdfgfg')
# boards = backup_boards
stop = False
last_board = None
last_number = None
filtered_boards = []
for i in numbers:
	mark_boards(i, boards)
	# print(boards)
	for board in boards:
		if eval_board(board):
			print("BINGO")
			last_board = board
			last_number = i
		else:
			filtered_boards.append(board)
	boards = filtered_boards
	filtered_boards = []
# for board in boards:
# 	print(board)
print(eval_board(board))
# print(boards)
print(sum_board(last_board)*last_number)
# 2: correct 21184