from collections import defaultdict

def run():
	d = defaultdict(int)
	with open("day1.txt", 'r') as fh:
		e = 0
		for l in fh.readlines():
			v = l.strip()
			if v == "":
				e += 1
			else:
				d[e] += int(v)

	#print(d)
	sorted_calories = sorted(d.items(), key=lambda x: x[1],reverse=True)
	print(sorted_calories[0])
	print(sum(map(lambda x: x[1], sorted_calories[:3])))

if __name__ == "__main__":
	run()