# Problem H - Connor Mattson

counterMap = {"1": '*', '2': '?', '3': '/', '4': '+', '5': '!'}

def solveLine():
	global lineInput
	lettersRepeated = {}
	letterFound = []
	counter = 0
	howFar = 0

	for i in lineInput:
		howFar += 1

		if i in letterFound:
			if i not in lettersRepeated:
				counter += 1
				lettersRepeated[i] = counter
			lineInput[howFar - 1] = counterMap[str(lettersRepeated[i])]
		else:
			letterFound.append(i)

lineInput = list(input().lower())
while lineInput != ['#']:
	solveLine()
	print(''.join(lineInput))
	lineInput = list(input().lower())