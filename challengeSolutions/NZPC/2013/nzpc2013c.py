#Problem C 2013 - Connor Mattson

values = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100]
print("values available	are: $" + " $".join([str(value) for value in values]))

data = [int(x) for x in input("Enter the list of each value e.g. '1 2 0 0 0 0 0 0 0 0' for 1 10c coin and 2 20c coins.\nEnter all 0's to exit: ").split(' ')]
while data != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
	print("${0:.2f}".format(sum([a*b for a,b in zip(data, values)])))
	data = [int(x) for x in input("Enter the list of each value e.g. '1 2 0 0 0 0 0 0 0 0' for 1 10c coin and 2 20c coins.\nEnter all 0's to exit: ").split(' ')]