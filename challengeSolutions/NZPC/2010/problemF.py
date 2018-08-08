# Problem F - Connor Mattson

lineInput = 0

def run():
	global lineInput
	lineInput = lineInput.split(' ')
	notVisited = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
	visited = []
	
	currentHouse = int(lineInput[0])
	visited.append(currentHouse)
	del notVisited[notVisited.index(currentHouse)]
	del lineInput[0]

	for i in lineInput:
		if i[0] == 'U':
			currentHouse += int(i[1:])
			if currentHouse in visited or currentHouse > 20:
				return 'illegal'
			else:
				visited.append(currentHouse)
				del notVisited[notVisited.index(currentHouse)]
		elif i[0] == 'D':
			currentHouse -= int(i[1:])
			if currentHouse in visited or currentHouse < 1:
				return 'illegal'
			else:
				visited.append(currentHouse)
				del notVisited[notVisited.index(currentHouse)]

	toPrint = str(notVisited[0])
	for i in notVisited[1:]:
		toPrint += ' ' + str(i)
	return toPrint



lineInput = input()
while lineInput != '#':
	print(run())
	lineInput = input()