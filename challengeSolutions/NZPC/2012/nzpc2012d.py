#Problem D 2012 - Connor Mattson

scenario = [int(x) for x in input("Enter the carpark capacity followed by the current number of cars, e.g. '50 12' or '0 0' to exit: ").split(' ')]
while scenario != [0, 0]:
	data = input("Enter data stream e.g. 'IIIOOI' for 3 cars trying to enter, followed by 2 leaving, and another trying to enter: ")
	errorFlag = False

	for i in data:
		scenario[1] = min(scenario[1] + 1, scenario[0]) if i == 'I' else scenario[1] - 1
		if scenario[1] < 0: errorFlag = True

	print("Error, cars inside the carpark went below negative" if errorFlag else "There were {} cars present at the end of the data stream".format(scenario[1]))
	scenario = [int(x) for x in input("Enter the carpark capacity followed by the current number of cars, e.g. '50 12' or '0 0' to exit: ").split(' ')]