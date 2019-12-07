# solution = [3,8,1001,8,10,8,105,1,0,0,21,42,67,88,101,114,195,276,357,438,99999,3,9,101,3,9,9,1002,9,4,9,1001,9,5,9,102,4,9,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,101,2,9,9,102,2,9,9,1001,9,5,9,4,9,99,3,9,102,4,9,9,1001,9,3,9,102,4,9,9,101,4,9,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,4,9,9,1002,9,5,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99]

solution = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

# solution = [3,0,4,0,99]

from itertools import permutations

def intcode(original, phase_int, input_int):
	i = 0

	input = original[:]
	while i < (len(input)-1):
		string_opcode = str(input[i])
		opcode = input[i] % 100
		# print "opcode", opcode
		# print input

		if opcode == 99:
			break
		elif opcode == 3:
			if i < 1:
				input[input[i+1]] = phase_int
			else:
				input[input[i+1]] = input_int
			i += 2
			continue
		elif opcode == 4:
			if input[i] >= 1000 and string_opcode[-4] is '1':
				return input[i+1]
			else:
				return input[input[i+1]]
			i += 2
			continue
		
		if i < (len(input)-4):			
			dest = input[i+3] # destinations are never immediate


		# Determine instruction mode
		if input[i] >= 100 and string_opcode[-3] is '1':
			number1 = input[i+1]
		else:
			number1 = input[input[i+1]]

		if input[i] >= 1000 and string_opcode[-4] is '1':
			number2 = input[i+2]
		else:
			number2 = input[input[i+2]]

		# The rest of the opcodes
		if opcode == 1:
			input[dest] = number2 + number1
			i += 4
		elif opcode == 2:
			input[dest] = number1 * number2
			i += 4
		elif opcode == 5:
			if number1 != 0:
				i = number2
			else:
				i += 3
		elif opcode == 6:
			if number1 == 0:
				i = number2
			else:
				i += 3
		elif opcode == 7:
			if number1 < number2:
				input[dest] = 1
			else:
				input[dest] = 0
			i += 4
		elif opcode == 8:
			if number1 == number2:
				input[dest] = 1
			else:
				input[dest] = 0
			i += 4
		else:
			print "opcode invalid", opcode
			break

# print intcode(solution)

def amplifier_sequence(solution, a,b,c,d,e):
	a1 = intcode(solution, a, 0)
	b1 = intcode(solution, b, a1)
	c1 = intcode(solution, c, b1)
	d1 = intcode(solution, d, c1)
	e1 = intcode(solution, e, d1)
	return e1

print amplifier_sequence(solution, 9,8,7,6,5)

def max_perms(solution):
	phase_perms = list(permutations(range(5, 10))) 
	max_thrust = 0

	for phase in phase_perms:
		a,b,c,d,e = phase
		val = amplifier_sequence(solution, a,b,c,d,e)
		if val > max_thrust:
			max_thrust = val
	return max_thrust

# print max_perms(solution)
