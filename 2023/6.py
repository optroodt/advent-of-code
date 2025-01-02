import pathlib
import re
import string
import operator

path = pathlib.Path("6.txt")
with path.open("r") as fh:
    lines = list(map(str.strip, fh.readlines()))


def win_count(t, d):
    count = 0
    for i in range(t):
        distance = i * (t - i)
        if distance > d:
            count += 1
    return count


def run():
    times = list(map(int, re.split(" +", lines[0].split(":")[1])[1:]))
    distances = list(map(int, re.split(" +", lines[1].split(":")[1])[1:]))
    print(times, distances)

    times = [int("".join(map(str, times)))]
    distances = [int("".join(map(str, distances)))]
    total = 1
    for t, d in zip(times, distances):
        print(t, d)
        total *= win_count(t, d)

    print(total)


if __name__ == "__main__":
    run()
