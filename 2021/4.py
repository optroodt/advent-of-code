import re

from utils import load_file

lines = load_file()

numbers = []
boards = []
score = "XXXXX"


def eval_board(board):
    for i in range(0, 25, 5):
        if "".join(map(str, board[i : i + 5])) == score:
            return True

    for i in range(5):
        indices = [n for n in range(i, 25, 5)]
        if "".join([str(board[index]) for index in indices]) == score:
            return True

    return False


def sum_board(board):
    return sum([i for i in board if i != "X"])


def mark_boards(digit, boards):
    for i in range(len(boards)):
        for n in range(len(boards[i])):
            if boards[i][n] == digit:
                boards[i][n] = "X"
    return boards


numbers = list(map(int, lines[0].split(",")))
board = []
line_count = 0
for line in lines[1:]:
    if line.strip() == "":
        continue

    board.extend(list(map(int, re.split(" +", line.strip()))))
    line_count += 1

    if line_count == 5:
        boards.append(board)
        board = []
        line_count = 0


def part_one(boards):
    stop = False
    for i in numbers:
        mark_boards(i, boards)
        for board in boards:
            if eval_board(board):
                score = sum_board(board) * i
                # print("BINGO!!", score)
                stop = True
                break
            if stop:
                break
        if stop:
            break
    print("Part One:", score)


part_one(boards)  # correct" 38594


def part_two(boards):
    last_board = None
    last_number = None
    filtered_boards = []
    for i in numbers:
        mark_boards(i, boards)
        for board in boards:
            if eval_board(board):
                last_board = board
                last_number = i
            else:
                filtered_boards.append(board)
        boards = filtered_boards
        filtered_boards = []
    # print(last_board)
    print("Part Two:", sum_board(last_board) * last_number)


part_two(boards)  # correct: 21184
