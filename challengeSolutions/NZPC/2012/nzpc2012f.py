# Problem F 2010 = Connor Mattson

import re

for i in range(int(input("How many scenarios do you want to run? "))):
	patternHeight, patternWidth = [int(x) for x in input("Enter the height and width of the pattern, e.g. '2 3': ").split(' ')]
	pattern = []
	for i in range(patternHeight): pattern.append(input("Enter row {} of the pattern: ".format(i + 1)).replace('.', '\\.'))
	
	gridHeight, gridWidth = [int(x) for x in input("Enter the height and width of the grid, e.g. '2 3': ").split(' ')]
	grid = ""
	for i in range(gridHeight): grid += input("Enter row {} of the grid: ".format(i + 1))

	total = len(re.findall((".{" + str(gridWidth - patternWidth) + '}').join(pattern), grid))
	print("The pattern occurs {} times in the grid.".format(total))