from collections import defaultdict

ROCK = "A"
PAPER = "B"
SCISSOR = "C"

DRAW = "Y"
LOSE = "X"
WIN = "Z"

LOOKUP_POINTS = {ROCK:1, PAPER:2, SCISSOR:3}
LOOKUP = {"Y": PAPER, "X": ROCK, "Z":SCISSOR}
LOOKUP_INVERTED = {v:k for k,v in LOOKUP.items()}
#LOOKUP_DAY_TWO = {"Y": "DRAW", "X": ROCK, "Z":SCISSOR}
BEATS = {ROCK:SCISSOR, PAPER:ROCK, SCISSOR: PAPER}
LOSES = {ROCK:PAPER, PAPER:SCISSOR, SCISSOR: ROCK}

def get_score(them, other):
	you = LOOKUP.get(other)
	score = LOOKUP_POINTS.get(you)
	if them == you:
		score += 3
	elif BEATS.get(them) != you:
		score += 6

	return score

def get_score_part_two(them, result):
	if result == DRAW:
		you = LOOKUP_INVERTED.get(them)
	elif result == LOSE:
		you = LOOKUP_INVERTED.get(BEATS.get(them))
	else:
		you = LOOKUP_INVERTED.get(LOSES.get(them))
	return get_score(them, you)


def run():
	guide = list()
	with open("day2.txt", 'r') as fh:

		for l in fh.readlines():
			guide.append(l.strip().split(" "))

	total = sum(map(lambda x: get_score_part_two(x[0], x[1]), guide ))
	print(total)

if __name__ == "__main__":
	run()