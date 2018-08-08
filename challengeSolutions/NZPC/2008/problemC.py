# Problem C - Connor Mattson

lineInput = input()
while lineInput != '#':
	A = 0
	aWin = 0
	B = 0
	bWin = 0
	lineInput = list(lineInput)
	for i in lineInput:
		if i == 'A':
			A += 1
			if A >= 4 and A > B + 1:
				A = 0
				B = 0
				aWin += 1
		else:
			B += 1
			if B >= 4 and B > A + 1:
				B = 0
				A = 0
				bWin += 1

	print('A', aWin, 'B', bWin)


	lineInput = input()