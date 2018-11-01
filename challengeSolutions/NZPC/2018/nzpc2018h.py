# Problem H 2018 - Connor Mattson

scores = []
players = []
for i in range(int(input("How many players competed? "))):
	data = input("Enter player {}'s name and their scores against each player, e.g. 'Andrew 5 X 7 7': ".format(i + 1)).split(' ')
	players.append([data[0], [0,0]])
	scores.append(data[1:])

maxScore = 0
maxDifference = 0
for i in range(len(players)):
	players[i][1][0] = sum([int(x) for x in scores[i] if x.isdigit()]) - sum([int(row[i]) for row in scores if row[i] != 'X'])
	for j in range(len(players)):
		if scores[i][j] != 'X' and int(scores[i][j]) > int(scores[j][i]): players[i][1][1] += 1
	if players[i][1][1] >= maxScore:
		if players[i][1][1] > maxScore: maxScore = players[i][1][1]
		if players[i][1][1] > maxScore or players[i][1][0] > maxDifference: maxDifference = players[i][1][0]

print(*[player[0] for player in players if player[1][1] == maxScore and player[1][0] == maxDifference], "won with {} wins and {} points difference.".format(maxScore, maxDifference))