# Problem D 2009 - Connor Mattson

lineInput = input("Enter a sentence or '#' to exit: ").split(' ')
while lineInput != ['#']:
	for i in range(len(lineInput)): 
		if len(lineInput[i]) > 2: lineInput[i] = lineInput[i][0] + lineInput[i][len(lineInput[i]) - 2:0:-1] + lineInput[i][len(lineInput[i]) - 1]
	lineInput = input(' '.join(lineInput) + "\nEnter a sentence or '#' to exit: ").split(' ')