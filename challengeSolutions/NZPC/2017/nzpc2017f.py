# Problem F 2017 - Connor Mattson

players = {}
for i in range(int(input("How many players will be playing? "))): players[input("Enter name {}: ".format(i + 1))] = i + 1

for i in range(int(input("How many rounds will be played? "))):
	data = input("Enter the seat to be removed and the number of moves before the music stops, e.g. '3 6': ").split(' ')
	for player in players: 
		players[player] = (players[player] + int(data[1]) - 1) % len(players) + 1
		if players[player] == int(data[0]): toDelete = player
	
	print("{} has been eliminated".format(toDelete))
	del players[toDelete]
	for player in players: players[player] = players[player] if players[player] < int(data[0]) else players[player] - 1

print("{} has won.".format(*players.keys()) if len(players.keys()) == 1 else "Players left are " + ' '.join(players.keys()))