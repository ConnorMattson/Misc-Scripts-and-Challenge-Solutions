problems = input()
compCounter = 1

while problems != "0":
	points = list(input().split(' '))
	teams = int(input())
	teamList = []

	for i in range(teams):
		teamData = {}
		data = input().split(',')
		teamData['name'] = data[0]
		teamData['value'] = 0

		for i in range(len(points)):
			indexOfSlash = data[i+1].index('/')
			if data[i+1][indexOfSlash+1] != '-':
				teamData['value'] += int(points[i])

		teamList.append(teamData)

	teamList = sorted(teamList, key=lambda k: k['value'], reverse=True) 
	rankCounter = 1

	print('Contest', compCounter)
	for i in range(len(teamList)-1):
		print(rankCounter, teamList[i]['name'], teamList[i]['value'])
		if teamList[i]['value'] != teamList[i+1]['value']:
			rankCounter += 1

	print(rankCounter, teamList[-1]['name'], teamList[-1]['value'])

	compCounter += 1
	problems = input()