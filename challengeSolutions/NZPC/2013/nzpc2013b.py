#Problem B 2013 - Connor Mattson

whatBeatsWhat = {"S": ["P", "L"],
         "P": ["R", "K"],
         "R": ["L", "S"],
         "L": ["K", "P"],
         "K": ["S", "R"]}

for gameNumber in range(int(input("How many games need to be played? "))):
	names = input("Enter the names of the players in game {} e.g. 'John Sally': ".format(gameNumber + 1)).split(' ')
	scores = [0, 0]
	roundNumber = int(input("How many rounds were in game {}? ".format(gameNumber + 1)))
	for rounds in range(roundNumber):
		score = input("Enter the score of round {}: ".format(rounds + 1)).split(' ')
		scores[score[1] not in whatBeatsWhat[score[0]]] += 0 if score[0] == score[1] else 1
	print(names[0], scores[0], names[1], scores[1], "draws", roundNumber - sum(scores))