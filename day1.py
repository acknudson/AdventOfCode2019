# Fuel required to launch a given module is based on its mass. 
# Specifically, to find the fuel required for a module, 
# take its mass, divide by three, round down, and subtract 2.

# For example:

# For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
# For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
# For a mass of 1969, the fuel required is 654.
# For a mass of 100756, the fuel required is 33583.

# The Fuel Counter-Upper needs to know the total fuel requirement. To find it, 
# individually calculate the fuel needed for the mass of each module (your puzzle input), 
# then add together all the fuel values.

# What is the sum of the fuel requirements for all of the modules on your spacecraft?

import math

def fuel_required(mass):
	return int(math.floor(mass/3)) - 2


#A module of mass 14 requires 2 fuel. This fuel requires no further fuel (2 divided by 3 and rounded down is 0, which would call for a negative fuel), so the total fuel required is still just 2.
#At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2). 216 then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel. So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
#The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.
def fuel_for_fuel(fuel):
	all_fuel = 0
	fr = fuel_required(fuel)
	while fr > 0:
		all_fuel += fr
		fr = fuel_required(fr)
	return all_fuel

# print fuel_for_fuel(2)
# print fuel_for_fuel(654), "correct: 312"
# print fuel_for_fuel(33583), "correct: 16763"

# Initial tests
# print fuel_required(12), "2"
# print fuel_required(14), "2"
# print fuel_required(1969), "654"
# print fuel_required(100756), "33583"


all_modules = [79620,58052,119910,138477,139102,78373,51937,63751,100937,56664,128939,115929,136981,68215,90317,97455,130858,94009,123221,81390,61726,78271,73354,103061,131261,140510,120555,117319,91154,96009,75491,90245,141689,118783,104601,121969,98547,108924,117114,65916,120037,66166,93973,105777,63501,89199,117551,126021,93466,107901,82323,104471,98794,57270,59457,120558,128142,137648,127375,103353,116578,97950,110725,96438,128425,75503,132178,138363,67009,127873,135747,108109,118818,75396,92822,63886,82973,116243,129066,74185,145298,83483,83417,54682,55648,142206,121420,149890,56561,107108,111376,139885,147373,131657,140634,79704,90263,139892,103841,50730]

def count_up_fuel_required(all_modules):
	all_fuel = 0
	for mass in all_modules:
		fr = fuel_required(mass)
		extra = fuel_for_fuel(fr)
		all_fuel += fr
		all_fuel += extra
	return all_fuel

print count_up_fuel_required(all_modules) # returned 3412094 in part 1, 5115267 in part 2





