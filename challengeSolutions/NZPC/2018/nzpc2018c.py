# Problem C 2018 - Connor Mattson

gameData = {'R': [], 'S': []}
for i in range(int(input("How many games were played? "))):
	data = input("Enter the door chosen by the contestant, the door behind which is the car, and either R or S for switching or remaining: ").split(' ')
	gameData[data[2]].append(1 if (data[0] == data[1] and data[2] == 'R') or (data[0] != data[1] and data[2] == 'S') else 0)

switch = sum(gameData['S'])/len(gameData['S'])
remain = sum(gameData['R'])/len(gameData['R'])
print("Switching is better."*(switch > remain) + "Switching is worse."*(switch < remain) + "No preference."*(switch == remain))