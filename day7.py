solution = [3,8,1001,8,10,8,105,1,0,0,21,42,67,88,101,114,195,276,357,438,99999,3,9,101,3,9,9,1002,9,4,9,1001,9,5,9,102,4,9,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,101,2,9,9,102,2,9,9,1001,9,5,9,4,9,99,3,9,102,4,9,9,1001,9,3,9,102,4,9,9,101,4,9,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,4,9,9,1002,9,5,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99]

# solution = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

# solution = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

from itertools import permutations

def intcode(original, phase_int, input_int, i):
	input = original[:]
	while i < (len(input)-1):
		string_opcode = str(input[i])
		opcode = input[i] % 100
		# print "opcode", opcode
		# print input[i:]

		if opcode == 99:
			# print "opcode 99"
			return None
		elif opcode == 3:
			# print "opcode 3"
			# print "phase_int", phase_int
			# print "i", i
			if i == 0:
				input[input[i+1]] = phase_int
			else:
				input[input[i+1]] = input_int
			i += 2
			continue
		elif opcode == 4:
			if input[i] >= 1000 and string_opcode[-4] is '1':
				return input[i+1], i+2, input
			else:
				return input[input[i+1]], i+2, input
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
	# print "a1"
	a1, ai, a_input = intcode(solution, a, 0, 0)
	# print "b1"
	b1, bi, b_input = intcode(solution, b, a1, 0)
	# print "c1"
	c1, ci, c_input = intcode(solution, c, b1, 0)
	# print "d1"
	d1, di, d_input = intcode(solution, d, c1, 0)
	# print "e1"
	e1, ei, e_input = intcode(solution, e, d1, 0)

	last_e1 = None
	i = 1
	while e1:
		i += 1
		try:
			a1, ai, a_input = intcode(a_input, None, e1, ai)
			# print "b", i
			b1, bi, b_input = intcode(b_input, None, a1, bi)
			# print "c", i
			c1, ci, c_input = intcode(c_input, None, b1, ci)
			# print "d", i
			d1, di, d_input = intcode(d_input, None, c1, di)
			# print "e", i
			e1, ei, e_input = intcode(e_input, None, d1, ei)
			last_e1 = e1
		except:
			return last_e1


# print amplifier_sequence(solution, 9,7,8,5,6)

def max_perms(solution):
	phase_perms = list(permutations(range(5, 10))) 
	max_thrust = 0

	for phase in phase_perms:
		a,b,c,d,e = phase
		val = amplifier_sequence(solution, a,b,c,d,e)
		if val > max_thrust:
			max_thrust = val
	return max_thrust

print max_perms(solution)
