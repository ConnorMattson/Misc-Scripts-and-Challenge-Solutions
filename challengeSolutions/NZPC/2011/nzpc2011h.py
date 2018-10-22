# Problem H 2010 - Connor Mattson

counterMap = {0: '*', 1: '?', 2: '/', 3: '+', 4: '!'}

data = list(input("Enter the word to modify or '#' to exit: ").lower())
while data != ['#']:

	lettersRepeated = []
	lettersFound = []

	for i in range(len(data)):
		if data[i] in lettersFound:
			if data[i] not in lettersRepeated: lettersRepeated.append(data[i])
			data[i] = counterMap[lettersRepeated.index(data[i])]
		else: lettersFound.append(data[i])

	print("The modified word is:", ''.join(data))
	data = list(input("Enter the word to modify or '#' to exit: ").lower())