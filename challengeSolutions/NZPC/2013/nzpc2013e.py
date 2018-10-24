#Problem E 2013 - Connor Mattson

def subtractionFunction(data, n=0):
	if data == [0, 0, 0, 0]: return n
	else: return subtractionFunction([abs(data[0]-data[1]), abs(data[1]-data[2]), abs(data[2]-data[3]), abs(data[3]-data[0])], n + 1)

data = [int(x) for x in input("Enter the initial sequence or '0 0 0 0' to exit: ").split(' ')]
while data != [0, 0, 0, 0]:
	print(subtractionFunction(data, 0))
	data = [int(x) for x in input("Enter the initial sequence or '0 0 0 0' to exit: ").split(' ')]