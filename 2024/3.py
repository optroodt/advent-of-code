import re

from utils import load_file

lines = load_file()


def run():
    data = "".join(lines)

    matches_one = re.findall("(mul\(\d+,\d+\))", data)
    total_one = 0
    for m in matches_one:
        front, back = m.split(",")
        total_one += int(front[4:]) * int(back[:-1])
    print("Part One", total_one)

    matches_two = re.findall("(mul\(\d+,\d+\)|do(?:n't)?\(\))", data)

    total_two = 0
    enabled = True
    for m in matches_two:
        if m == "do()":
            enabled = True
        elif m == "don't()":
            enabled = False
        else:
            # print(m)
            if not enabled:
                continue

            front, back = m.split(",")
            total_two += int(front[4:]) * int(back[:-1])

    print("Part Two:", total_two)


# 646346 is too low
if __name__ == "__main__":
    run()
