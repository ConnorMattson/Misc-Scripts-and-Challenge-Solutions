#Problem B 2014 - Connor Mattson

for i in range(int(input("How many sequences do you want to test? "))):
	sequence = input("Enter sequence {}: ".format(i + 1)).split(' ')

	ratio = int(sequence[1]) / int(sequence[0])
	noErrors = True
	for index in range(2, len(sequence)):
		if int(sequence[index]) / int(sequence[index - 1]) != ratio: noErrors = False

	print("This is a geometric progression with common ratio {}.".format(int(ratio)) if noErrors else "This is not a geometric progression.")