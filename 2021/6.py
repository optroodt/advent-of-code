import collections

from utils import load_file

lines = load_file("6.txt")

for line in lines:
    states = [int(x) for x in line.split(",")]


class Fish:
    def __init__(self, timer=8):
        self.timer = timer

    def __repr__(self):
        return f"<{self.__class__.__name__} timer={self.timer}>"

    def reset(self):
        self.timer = 7

    def pass_day(self):
        if self.timer == 0:
            self.timer = 6
            return Fish()
        else:
            self.timer -= 1


fishes = [Fish(timer=x) for x in states]
c = collections.Counter([f.timer for f in fishes])


def count_fishes(days):
    timeline = [0] * days
    fish_count = len(fishes)
    for k, count in c.items():
        timeline[k] += count

        for i in range(k + 7, days, 7):
            timeline[i] += count

    for d in range(0, days):
        new_fishes = timeline[d]
        fish_count += new_fishes

        for i in range(d + 9, days, 7):
            timeline[i] += new_fishes

    return fish_count


print("Part One:", count_fishes(80))  # correct: 351188
print("Part Two:", count_fishes(256))  # correct: 1595779846729

# below version is too slow
# days = 80
# for day in range(days):
#     new_fishes = []
#     for fish in fishes:
#         result = fish.pass_day()
#         if result is not None:
#             new_fishes.append(result)
#     if new_fishes:
#         fishes.extend(new_fishes)
#
#     print(day, len(new_fishes), len(fishes))
