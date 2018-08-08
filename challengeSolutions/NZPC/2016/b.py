holes = {'A': 1, 'B': 2, 'D': 1, 'O': 1, 'P': 1, 'Q': 1, 'R': 1,}

for i in range(int(input())):
	data = input()
	holecounter = 0
	for i in data:
		if i in holes.keys():
			holecounter += holes[i]
	print(holecounter)