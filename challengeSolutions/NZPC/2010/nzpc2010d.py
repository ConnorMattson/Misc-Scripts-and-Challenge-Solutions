# Problem D 2010 - Connor Mattson

stockCode = input("Enter stock code or '#' to exit: ")
while stockCode != '#':
	warehouseSpace, currentStock = [int(x) for x in input("Enter warehouse capacity and current stock of " + stockCode + " e.g. '100 64': ").split(' ')]
	n = input("How many transactions occured? ")
	for i in range(int(n)):
		transaction = input("Enter transaction details. e.g. 'S 4' to sell 4 units or 'R 25' to restock 25 units: ").split(' ')
		currentStock = min(currentStock + int(transaction[1]), warehouseSpace) if transaction[0] == 'R' else max(currentStock - int(transaction[1]), 0)
	print(stockCode, currentStock)
	stockCode = input("Enter stock code or '#' to exit: ")