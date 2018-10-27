# Problem G 2015 - Connor Mattson

for i in range(int(input("How many graphs will you be entering? "))):
	data = [int(x) for x in input("Enter 'm c' for the equation y = mx + c, e.g. '2 2': ").split(' ')]
	
	print("y = {}x + {}".format(*data))
	dataPoints = []
	for x in range(1,11): dataPoints.append(data[0] * x + data[1])
	for y in range(max(dataPoints), 0, -1): print("*" + " "*(dataPoints.index(y)) + "*" if y in dataPoints else '*')
	print("***********")