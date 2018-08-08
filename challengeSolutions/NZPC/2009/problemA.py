# Problem A - Connor Mattson

lineInput = input()
while lineInput != '0 0':

	listOfPeople = []
	lineInput = lineInput.split(' ')
	k = int(lineInput[1])
	
	for i in range(int(lineInput[0])):
		listOfPeople.append(i+1)

	x = 0
	listToRemove = []
	while len(listToRemove) < len(listOfPeople):
		x += 3

		

	while len(listOfPeople) > 4:
		numberToRun = 0
		timesK = len(listOfPeople) / k
		while timesK >= 1:
			timesK -= 1
			numberToRun += 1

		print(numberToRun)
		for i in range(numberToRun):
			print(i)
			print(listOfPeople)
			del(listOfPeople[(i+1)*k-1])
			listOfPeople.insert((i+1)*k-1, "0")

		while '0' in listOfPeople:
			del(listOfPeople)



	print(listOfPeople)
	lineInput = input()