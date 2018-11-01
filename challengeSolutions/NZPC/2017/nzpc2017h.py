# Problem H 2017 - Connor Mattson

teams = {}
for i in range(int(input("How many teams do you wish to enter: "))):
	teams.update({input("Enter team {}'s name: ".format(i + 1)): [int(x) for x in input("Enter team {}'s data: ".format(i + 1)).split(' ')]})

for i in range(int(input("How many matches do you wish to enter: "))):
	homeTeam = input("Enter the name of the home team: ")
	hS = int(input("Enter the score of the home team: "))
	awayTeam = input("Enter the name of the away team: ")
	aS = int(input("Enter the score of the away team: "))
	for i, dataPoint in enumerate([1, hS > aS, hS == aS, hS < aS, hS, aS, 3*(hS > aS) + 1*(hS == aS)]): teams[homeTeam][i] += dataPoint
	for i, dataPoint in enumerate([1, hS < aS, hS == aS, hS > aS, aS, hS, 3*(hS < aS) + 1*(hS == aS)]): teams[awayTeam][i] += dataPoint

for team, data in sorted(teams.items(), key=lambda x: [-x[1][6], -(x[1][4]-x[1][5]), -x[1][4], x[0].lower()]): print(team, data)