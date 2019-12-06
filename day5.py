# Opcode 3 takes a single integer as input and saves it to the position given by its only parameter. 
# For example, the instruction 3,50 would take an input value and store it at address 50.
# Opcode 4 outputs the value of its only parameter. For example, the instruction 4,50 would output the value at address 50.


solution = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,32,43,225,101,68,192,224,1001,224,-160,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1001,118,77,224,1001,224,-87,224,4,224,102,8,223,223,1001,224,6,224,1,223,224,223,1102,5,19,225,1102,74,50,224,101,-3700,224,224,4,224,1002,223,8,223,1001,224,1,224,1,223,224,223,1102,89,18,225,1002,14,72,224,1001,224,-3096,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,1101,34,53,225,1102,54,10,225,1,113,61,224,101,-39,224,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1101,31,61,224,101,-92,224,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1102,75,18,225,102,48,87,224,101,-4272,224,224,4,224,102,8,223,223,1001,224,7,224,1,224,223,223,1101,23,92,225,2,165,218,224,101,-3675,224,224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,1102,8,49,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1107,226,226,224,1002,223,2,223,1005,224,329,1001,223,1,223,1007,677,226,224,1002,223,2,223,1006,224,344,1001,223,1,223,108,677,226,224,102,2,223,223,1006,224,359,1001,223,1,223,7,226,226,224,1002,223,2,223,1005,224,374,101,1,223,223,107,677,677,224,1002,223,2,223,1006,224,389,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,404,1001,223,1,223,1107,677,226,224,1002,223,2,223,1005,224,419,1001,223,1,223,108,226,226,224,102,2,223,223,1006,224,434,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,449,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,464,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,479,1001,223,1,223,1008,226,226,224,102,2,223,223,1005,224,494,101,1,223,223,7,677,226,224,1002,223,2,223,1005,224,509,101,1,223,223,8,226,677,224,1002,223,2,223,1006,224,524,1001,223,1,223,1007,226,226,224,1002,223,2,223,1006,224,539,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,554,101,1,223,223,1108,677,677,224,102,2,223,223,1006,224,569,101,1,223,223,1107,226,677,224,102,2,223,223,1005,224,584,1001,223,1,223,8,677,226,224,1002,223,2,223,1006,224,599,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,614,1001,223,1,223,7,226,677,224,1002,223,2,223,1005,224,629,101,1,223,223,107,226,677,224,102,2,223,223,1005,224,644,101,1,223,223,8,677,677,224,102,2,223,223,1005,224,659,1001,223,1,223,108,677,677,224,1002,223,2,223,1005,224,674,101,1,223,223,4,223,99,226]

# solution = [1002,4,3,4,33]

# solution = [3,0,4,0,99]

def intcode(original):
	i = 0
	input_int = 1
	input = original[:]
	while i < (len(input)-1):
		# print input[0:i+10]
		string_opcode = str(input[i])
		# print "opcode", string_opcode
		opcode = input[i] % 10

		if opcode == 99:
			break
		elif opcode == 3:
			# print "input"
			# print "i", i
			# print "input val, num1", input_int
			input[input[i+1]] = input_int
			i += 2
			continue
		elif opcode == 4:
			if input[i] >= 1000 and string_opcode[-4] is '1':
				print input[i+1]
			else:
				print input[input[i+1]]
			i += 2
			continue
		
		if i < (len(input)-4):			
			dest = input[i+3] # destinations are never immediate


		if input[i] >= 100 and string_opcode[-3] is '1':
			# print "no1 immediate", string_opcode[-3]
			number1 = input[i+1]
		else:
			# print "no1 position"
			# print '\t', i+1, input[i+1], input[input[i+1]]
			number1 = input[input[i+1]]

		if input[i] >= 1000 and string_opcode[-4] is '1':
			# print "no2 immediate", string_opcode[-4]
			number2 = input[i+2]
		else:
			# print "no2 position"
			number2 = input[input[i+2]]

		# if len(string_opcode) > 1:
		# 	# print "enumerate", string_opcode[:-2]
		# 	for index, num in enumerate(reversed(string_opcode[:-2])):
		# 		if index == 0:
		# 			if num == "1" or num == 1:
		# 				number1 = input[i+1]
		# 		if index == 1:
		# 			if num == "1" or num == 1:
		# 				number2 = input[i+2]
		# else:
		# 	if opcode < 3:	
		# 		number2 = input[input[i+2]]
		# 		number1 = input[input[i+1]]

		if opcode == 1:
			# print "add"
			# print "num1, num2", number1, number2
			# print "dest", dest
			input[dest] = number2 + number1
			i += 4
		elif opcode == 2:
			# print "multiply"
			# print "num1, num2", number1, number2
			# print "dest", dest
			input[dest] = number1 * number2
			i += 4
		else:
			print "opcode invalid", opcode
			# break
		
	# raise "there was an issue, program did not abort"
	# return input, input_int
	# return input

print intcode(solution)