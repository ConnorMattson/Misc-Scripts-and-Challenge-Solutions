# Problem H 2012 - Connor Mattson

# This solution is not yet finished, however its one of the more complex problems and I want to get other problems published.

product = input("What product is being bought? (or '#' to exit) ")
while product != "#":

	def multiply(weights, array, current=0):
		if array: return multiply(weights[1:], array[1:], current + weights[0]*array[0])
		else: return current

	cost = float('.'.join(input("Enter the price in d dollars and c cents as 'd c' e.g. '0 95' for $0.95: ").split(' ')))
	
	numDeals = int(input("How many deals exist? "))
	weights = [1]
	values = [0]
	for i in range(numDeals): 
		data = [int(x) for x in input("Enter deal details e.g. '5 2' for buy 5 get 2 free: ").split(' ')]
		weights.append(data[0])
		weights.append(data[1])

	numPurchases = int(input("How many purchases are being made? "))
	for i in range(numPurchases):
		maxWeight = int(input("How many {} are being bought? ".format(product)))
		maxValue = 0

		arrays = [0 for x in weights]

		# implementing a whole system for solving linear programs seems too much for what is meant to be a simple
		# problem, instead just brute force the solution
		# fill arrays with every viable combination of assignment then continue

		for array in arrays: maxValue = max(multiply(values, array), maxValue)

		print("Buy {} {}, save ${}.".format(maxWeight, product, maxValue*cost))
	product = input("What product is being bought? (or '#' to exit) ")