# Problem Y - Team 19

runningTotal = 0
allNumbers = []
allTotals = []

lineInput = int(input())
while lineInput != 0:
	runningTotal += lineInput
	allNumbers.append(lineInput)
	allTotals.append(runningTotal)
	lineInput = int(input())
	
for i in allNumbers[:-1]:
	print('N =', i, 'Partial Sum =', allTotals[allNumbers.index(i)]

print('N =', allNumbers[-1], 'Final Sum  =', allNumbers[-1]