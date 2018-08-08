# Problem E - Connor Mattson

pointScore = {'TT': 75, 'TX': 50, 'PR': 80, 'RT': 30, 'AP': 25, 'PX': 60}

firstInput = input()
while firstInput != '0 0':
	firstInput = firstInput.split(' ')
	week = firstInput[0]
	entries = int(firstInput[1])
	weekNames = []
	weekScores = []
	bannedNames = []

	for i in range(entries):
		lineInput = input()
		lineInput = lineInput.split(' ')
		if lineInput[0] in weekNames:
			indexOfName = weekNames.index(lineInput[0])
			weekScores[indexOfName] = int(weekScores[indexOfName]) + pointScore[lineInput[1]]
		else:
			weekNames.append(lineInput[0])
			weekScores.append(pointScore[lineInput[1]])

		for i in weekScores:
			if i > 100:
				indexOfName = weekScores.index(i)
				if weekNames[indexOfName] not in bannedNames:
					bannedNames.append(weekNames[indexOfName])

	if len(bannedNames) > 0:
		printMessage = ('Week ' + week)
		for i in bannedNames:
			printMessage += (',' + i)
		print(printMessage)
	else:
		print('Week ' + week + ' No phones confiscated')

	firstInput = input()