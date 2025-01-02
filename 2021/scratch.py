# inputs = [16,1,2,0,4,2,7,1,2,14]

# def calc_inc_burn(source, destination):
# 	distance = abs(source-destination)
# 	incr_distance=  sum([i+1 for i in range(distance)])
# 	print(f"- Move from {source} to {destination}: {incr_distance} fuel")

# for j in inputs:
# 		calc_inc_burn(j, 5)
# for i in range(max(inputs)+1):
# 	for j in inputs:
# 		calc_burn(j, i)

x = set('bcdf')
print(len(x))
y = x - set('acf')
print(y)

print(set('abc') | set('abcd'))

print(sorted('defcd'))