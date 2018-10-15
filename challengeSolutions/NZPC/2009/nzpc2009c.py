# Problem C 2009 - Connor Mattson

route = input("Enter the bus number and capacity e.g. '36A 26': ").split(' ')
while route != ['#', '0']:
	currentPassengers = int(input("How many passengers are on the bus now? "))

	stops = int(input("How many stops will the bus visit? "))
	for i in range(stops):
		stopInput = input("Stop {}. What was the change in passengers? e.g. '2 3' for 2 leaving and 3 getting on: ".format(i + 1)).split(' ')
		currentPassengers += int(stopInput[1]) - int(stopInput[0])
		if passengers > maxSize: passengers = maxSize

	print(route, passengers)
	route = input("Enter the bus number and capacity e.g. '36A 26': ").split(' ')