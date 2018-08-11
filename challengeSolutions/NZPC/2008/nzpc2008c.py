# Problem C 2008 - Connor Mattson
print("Format scores as 'AAB' for player A winning two points then B winning one point")
lineInput = input("Enter a list of scores ('#' to exit): ")

while lineInput != '#':
	scores = {"A": 0, "B": 0}
	wins = {"A": 0, "B": 0}

	for i in list(lineInput):
		scores[i] += 1
		# A player wins if they have at least four points and are two points ahead
		if scores[i] >= 4 and sum(scores.values()) < 2*scores[i] - 1:
			wins[i] += 1
			scores = {"A": 0, "B": 0}

	print("A", wins["A"], "B", wins["B"])
	lineInput = input("Enter a list of scores ('#' to exit): ")