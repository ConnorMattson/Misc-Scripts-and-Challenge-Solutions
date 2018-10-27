# Problem D 2015 - Connor Mattson

strideLength = int(input("What is the person's stride length in cm (enter '0' to exit)? ")) / 100000
while strideLength != 0:

	distance = []
	for i in range(int(input("How many data points do you wish to enter? "))):
		distance.append(strideLength * int(input("Enter the number of steps taken at point {}: ".format(i + 1))))

	print("You have travelled {0} km for a total of {1:.5f} km.".format(' km, '.join(['%.5f' % x for x in distance]), sum(distance)))
	strideLength = int(input("What is the person's stride length in cm (enter '0' to exit)? ")) / 100000