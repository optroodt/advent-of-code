import collections 
with open('6_input.txt', 'r') as fh:
	for line in fh.readlines():
		states = [int(x) for x in line.strip().split(',')]


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
# print(fishes)

c = collections.Counter([f.timer for f in fishes])
print(c)



print(351188)
days = 256
initial_timeline= [0] * days
# for k, count in c.items():
# 	for d in range(k+6, days, 6):
# 		initial_timeline[d] += count

timeline= [0] * days
fish_count = len(fishes)
for k, count in c.items():
	timeline[k] += count

	for i in range(k+7, days, 7):
	# 	# print(i)
		timeline[i] += count
# for k, count in c.items():
# 	timeline[k-1] += count
	# for i in range(k+1, days, 6):
	# 	# print(i)
		# timeline[i] += count

for d in range(0, days):
	new_fishes = timeline[d]
	fish_count += new_fishes
	# fish_count += initial_timeline[d]
	print(d, new_fishes, fish_count)


	for i in range(d+9, days, 7):
		timeline[i] += new_fishes

print(timeline)
# print(sum(timeline[0:6]))
print('BOOOM')
print(fish_count) # correct: 1595779846729
print('BOOOM')
print(351188) # 80 days
# days = 80
days = 80

for day in range(days):
	new_fishes = []
	for fish in fishes:
		result = fish.pass_day()
		if result is not None:
			new_fishes.append(result)
	if new_fishes:
		fishes.extend(new_fishes)

	print(day, len(new_fishes), len(fishes))

