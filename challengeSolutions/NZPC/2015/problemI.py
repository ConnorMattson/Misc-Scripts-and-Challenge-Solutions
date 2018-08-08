# Problem I - Team 19

continueCheck = True
playerScores = 0

def runCheck():
	cards = str(input())
	if cards == '#':
		continueCheck = False
		return
	
	busted = []
	cardSets = []
	stuck = []
	setCards = []
	
	players = input().split(' ')
	playersToDealTo = len(players) + 1
	dealIndex = playersToDealTo - 1
	
	scores = []
	for i in range(len(players) + 1):
		scores.append(0)
	
	for i in cards:
		setCards.append(i)
	
	for i in range(playersToDealTo):
		thisSet = ''
		counter = 0
		for j in setCards[i: (2 * playersToDealTo) - 1]:
			if i < playersToDealTo and j == 2 * dealIndex:
				return
			if counter == 0:
				thisSet = thisSet + str(j)
			counter += 1
			if counter == 4:
				counter = 0
			
			thisSet = thisSet + str(j)
		cardSets.append(thisSet)
	print('players are:', players)
	print('playersToDealTo is:', playersToDealTo)
	print('scores are:', scores)
	print('setCards are:', setCards)
	print('cardSets is:', cardSets)
	for i in range(2 * playersToDealTo):
		SetCards.remove(i)
	
	personCounter = -1
	for i in cardSets:
		runningTotal = 0
		aceCounter = 0
		personCounter += 1
		for j in i:
			if isalpha(j) == True:
				print('ISALPHA IS FALSE')

while continueCheck == True:
	potato = runCheck()