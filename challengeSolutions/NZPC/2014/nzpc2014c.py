#Problem C 2014 - Connor Mattson

for i in range(int(input("How many lines to process? "))):
	data = input("'10 15 1' will find all the 1s appearing in numbers between 10 and 15 inclusive: ".format(i + 1)).split(' ')
	print("There are {} {}'s between {} and {}.".format(''.join([str(x) for x in range(int(data[0]), int(data[1]) + 1)]).count(data[2]), data[2], data[0], data[1]))