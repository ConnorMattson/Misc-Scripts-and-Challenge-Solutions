#2012 Problem J - Connor Mattson

def runSimulation(simulationTime, powerThreshold, timeThreshold):
	for i in range(simulationTime):
		lineInput = input()
		lineInput = lineInput.split(' ')
		appliance = lineInput[0]
		secondsSince = lineInput[1]
		changeInPower = lineInput[2]


simulationStart = input()
simulationStart = simulationStart.split(' ')

runSimulation(simulationStart[0], simulationStart[1], simulationStart[2])