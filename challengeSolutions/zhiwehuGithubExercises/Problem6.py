# Problem 6, level 2 - Connor Mattson
# Q = Square root of [(2 * C * D)/H]
# C = 50
# H = 30
# D = Input
import math

data = input
values = [data]

def equation(D):
	Q = math.sqrt((2 * 50 * int(D)) / 30)
	Q = Q * 100
	Q = int(Q)
	Q = float(Q) / 100
	return Q

for i in input:
	print(equation(i))