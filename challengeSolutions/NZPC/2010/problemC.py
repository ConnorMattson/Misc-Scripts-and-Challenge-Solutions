# problem C - Connor Mattson

lineInput = input()
while lineInput != '0 0':
	lineInput = lineInput.split(' ')
	totalToys = int(lineInput[0]) - int(lineInput[1])
	if totalToys == 1:
		print('0 0')
	else:
		if totalToys % 2 == 0:
			toyPairs = totalToys / 2
			print(str(int(toyPairs)) + ' 0')
		else:
			toyPairs = ((totalToys - 1) / 2) - 1
			print(str(int(toyPairs)) + ' 1')
	lineInput = input()
