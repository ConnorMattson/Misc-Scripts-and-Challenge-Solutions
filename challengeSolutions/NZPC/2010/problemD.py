# Problem D - Connor Mattson

stockCode = input()
while stockCode != '#':
	warehouseSpace = input()
	warehouseSpace = warehouseSpace.split(' ')

	currentStock = int(warehouseSpace[1])
	warehouseSpace = int(warehouseSpace[0])

	transactions = input()

	for i in range(int(transactions)):
		lineInput = input()
		lineInput = lineInput.split(' ')
		if lineInput[0] == 'S':
			currentStock -= int(lineInput[1])
			if currentStock < 0:
				currentStock = 0
		elif lineInput[0] == 'R':
			currentStock += int(lineInput[1])
			if currentStock > warehouseSpace:
				currentStock = warehouseSpace

	print(stockCode, currentStock)
	stockCode = input()