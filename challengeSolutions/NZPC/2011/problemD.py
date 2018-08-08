# Problem D - Connor Mattson

def runWeek():
	global weekNumber
	global week
	townCount = 0
	townList = []

	for i in range(int(weekNumber)):
		town = input()
		if town in townList:
			pass
		else:
			townList.append(town)
			townCount += 1

	toReturn = ['Week ',str(week),' ',str(townCount)]
	toReturn = ''.join(toReturn)
	return toReturn

weekNumber = input()
week = 1
while weekNumber != '0':
	print(runWeek())
	week += 1
	weekNumber = input()
