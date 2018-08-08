#Problem B - Connor Mattson

timesToRun = input()

for i in range(int(timesToRun)):
	sequence = input()
	sequence = sequence.split(' ')

	ratio = int(sequence[1]) / int(sequence[0])

	index = 1
	ratioYes = 1

	for i in sequence[index:]:
		if int(sequence[index]) / int(sequence[index - 1]) == ratio:
			pass
		else:
			ratioYes = 0
		index += 1

	if ratioYes == 1:
		print("Yes " + str(int(ratio)))
	else:
		print("No")