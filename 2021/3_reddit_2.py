#**Day 3:** [**Part 1**](https://adventofcode.com/2021/day/3) **- Python solution**

CountZero = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
CountOne = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
gamma = []
epsilon = []
gammac = 0
epsilonc = 0
cont=0

# Initialization

def binary_to_decimal(binary):
	return sum(val*(2**index) for index, val in enumerate(reversed(binary)))


# Function to convert a list of 0 and 1 into a decimal

def calc():
	cont = 0
	f =  open("3_input.txt", "r")
	line = f.readline()
	lenght = len(line)-1
	while (line := f.readline()):
		cont = cont + 1
	f.close()
	return lenght, cont

# Function which returns the bits of each rows and the number of rows


lg, num_el = calc()

print ("Number of elements in a row: " + str(lg))
print("Numbers of rows: " + str(num_el))

for i in range(lg):
	f =  open("3_input.txt", "r")
	for k in range(num_el):
		line = f.readline()
		if (line[i] == "1"):
			CountOne[i] += 1
		elif (line[i] == "0"):
			CountZero[i] += 1
	if(CountZero[i]>CountOne[i]):
		gamma.append(0)
		epsilon.append(1)
	else:
		gamma.append(1)
		epsilon.append(0)
	f.close()

# These loops iterate the i-nth element of each row
# Input.txt is opened and closed at the beginning and at the end of the nested loop

print("\n")
print("gamma")
print(gamma)
print("epsilon")
print(epsilon)
print("\n")

gammac = binary_to_decimal(gamma)
epsilonc = binary_to_decimal(epsilon)

print("Result (gamma x epsilon): " + str(gammac*epsilonc))