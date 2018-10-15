# Problem B 2009 - Connor Mattson

lineInput = input("Enter the integer length, width, height, and volume (in that order) of a cuboid.\nReplace one value with 0 and this value will be found. Enter '0 0 0 0' to exit: ").split(' ')
while lineInput != ["0", "0", "0", "0"]:
	if lineInput[3] == "0":
		print(*lineInput[0:3], int(lineInput[0]) * int(lineInput[1]) * int(lineInput[2]))

	else:
		integers = [int(x) for x in lineInput[0:3] if x != '0']
		print(' '.join(lineInput).replace('0', str(int(int(lineInput[3]) / (integers[0] * integers[1])))))

	lineInput = input("Enter the integer length, width, height, and volume (in that order) of a cuboid.\nReplace one value with 0 and this value will be found. Enter '0 0 0 0' to exit: ").split(' ')