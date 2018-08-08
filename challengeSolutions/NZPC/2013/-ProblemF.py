#Problem F - Connor Mattson

numberOfScenarios = input()
totalLine = []
totalLineToFind = []
found = []
test = ['a', 'p', 't']


def runScenario():
	numberOfLines = input()
	for j in range(int(numberOfLines)):
		runLine()
	numberOfLines2 = input()
	for k in range(int(numberOfLines2)):
		runLine2()

	for l in range(len(totalLineToFind)):
		notFound = 'false'
		

		for m in range(len(totalLine)):

			if notFound == 'true':
				notFound = 'false'
				lettersToFind = list(totalLineToFind[l])

				if totalLine[m] != '':
					lettersToSearch = list(totalLine[m])


					print(lettersToSearch)

					while len(lettersToFind) > 0:
						try:
							indexofLetter = lettersToSearch.index(lettersToFind[0]) 
							del lettersToSearch[indexofLetter]
							del lettersToFind[0]
						except ValueError:
							lettersToFind = []
							found.append(totalLineToFind[l] + ' <none>')
							notFound = 'true'

			if notFound == 'false':
				found.append(totalLineToFind[l] + ' ' + totalLine[m])
				totalLine[m] = ''

	print(found)
	
def runLine():

	currentLine = input()
	totalLine.append(currentLine)

def runLine2():
	currentLine = input()
	totalLineToFind.append(currentLine)

for i in range(int(numberOfScenarios)):
	runScenario()