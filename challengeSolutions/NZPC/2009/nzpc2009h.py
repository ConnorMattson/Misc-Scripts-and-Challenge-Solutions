# Problem H 2009 - Connor Mattson

# I'm in the middle of updating this one! I haven't ran tests/tidied it up yet

n = int(input("Enter the number of words to follow: "))
while n != 0:
	wordFrequencies = {}
	wordNumber = {}
	wordActual = {}

	for i in range(n):
		word = input("Enter word: ")
		wordFrequencies[set(word)] = wordFrequencies[set(word)] + 1 if set(word) in wordFrequencies else 0
		if set(word) not in wordNumber: wordNumber[set(word)] = i
		if set(word) not in wordActual: wordActual[set(word)] = word

	maxSet = {word: wordNumber[word] for word in wordFrequencies.keys() if wordFrequencies[word] == max(wordFrequencies.values())}
	minSet = [word for word in maxSet.keys() if maxSet[word] == min(maxSet.values())][0]
	print(wordActual[minSet], wordFrequencies[minSet])
	n = int(input("Enter the number of words to follow: "))