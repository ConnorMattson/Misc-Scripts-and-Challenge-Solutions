# Problem A 2009 - Connor Mattson

lineInput = input("Enter n number of people and kth number to remove as 'n k' e.g. '9 3' (don't include quotes, '0 0' to exit): ").split(' ')
while lineInput != ['0', '0']:
	k = int(lineInput[1]) - 1
	n = int(lineInput[0])
	index = k
	listToPrint = []
	listOfPeople = [(x + 1) for x in range(n)]

	for i in range(n - 1):
		if (n <= 4): listToPrint.append(listOfPeople[index])
		del listOfPeople[index]
		n -= 1
		index += k
		if (index > n): index = index % n

	print(*listToPrint, listOfPeople[0])
	lineInput = input("Enter n number of people and kth number to remove as 'n k' e.g. '9 3' (don't include quotes, '0 0' to exit): ").split(' ')