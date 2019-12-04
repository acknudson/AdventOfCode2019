# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

#input: 171309-643603

def has_double_digit(number):
	stringify = str(number)
	for i in range(1, len(stringify)):
		if stringify[i] == stringify[i-1]:
			return True

	return False

# print has_double_digit(1237789)

def digits_do_not_decrease(number):
	stringify = str(number)
	for i in range(1, len(stringify)):
		if stringify[i] < stringify[i-1]:
			return False
	return True

# print digits_do_not_decrease(1237890)


def count_passwords(input_lower, input_upper):
	passwords = []
	for x in range(input_lower, input_upper):
		if digits_do_not_decrease(x):
			if has_double_digit(x):
				passwords.extend([x])
	return len(passwords)

print count_passwords(171309, 643603)

# 1653 is too large
# 1625 is correct! 