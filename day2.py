# An Intcode program is a list of integers separated by commas (like 1,0,0,3,99). 
# To run one, start by looking at the first integer (called position 0). 
# Here, you will find an opcode - either 1, 2, or 99. The opcode indicates what to do; 
# for example, 99 means that the program is finished and should immediately halt. Encountering an unknown opcode means something went wrong.
#
# Opcode 1 adds together numbers read from two positions and stores the result in a third position. 
# The three integers immediately after the opcode tell you these three positions - the first two indicate the positions 
# from which you should read the input values, and the third indicates the position at which the output should be stored.

# Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. 
#  Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.

# example = [1,1,1,4,99,5,6,0,99]

# 1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
# 2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
# 2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
# 1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.

# To do this, before running the program, replace position 1 with the value 12 and 
# replace position 2 with the value 2. What value is left at position 0 after the program halts?

solution = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,9,23,1,5,23,27,1,27,9,31,1,6,31,35,2,35,9,39,1,39,6,43,2,9,43,47,1,47,6,51,2,51,9,55,1,5,55,59,2,59,6,63,1,9,63,67,1,67,10,71,1,71,13,75,2,13,75,79,1,6,79,83,2,9,83,87,1,87,6,91,2,10,91,95,2,13,95,99,1,9,99,103,1,5,103,107,2,9,107,111,1,111,5,115,1,115,5,119,1,10,119,123,1,13,123,127,1,2,127,131,1,131,13,0,99,2,14,0,0]

def intcode(original):
	for n in range(100):
		for v in range(100):
			input = original[:]
			input[1] = n
			input[2] = v
			i = 0
			while i < (len(input)-4):
				opcode = input[i]
				number1 = input[input[i+1]]
				number2 = input[input[i+2]]
				dest = input[i+3]

				if opcode == 1:
					input[dest] = number2 + number1
				elif opcode == 2:
					input[dest] = number1 * number2
				elif opcode == 99:
					break
				else:
					raise "opcode invalid", opcode
				i += 4
			if input[0] == 19690720:
				return n, v
	# raise "there was an issue, program did not abort"
	# return input

print intcode(solution)