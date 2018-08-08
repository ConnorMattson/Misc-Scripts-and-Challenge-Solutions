#Problem D 2012 - Connor Mattson

def runScenario():
	global scenarioInput
	scenarioInput = scenarioInput.split(' ')
	maxCars = int(scenarioInput[0])
	currentCars = int(scenarioInput[1])
	
	scenarioData = input()
	scenarioData = list(scenarioData)
	for i in scenarioData:
		if i == 'I':
			if currentCars < maxCars:
				currentCars += 1
		else:
			if i == 'O':
				if currentCars == 0:
					return('error')
				else:
					currentCars -= 1

	return(currentCars)


scenarioInput = input()
while scenarioInput	!= '0 0':
	print(runScenario())
	scenarioInput = input()