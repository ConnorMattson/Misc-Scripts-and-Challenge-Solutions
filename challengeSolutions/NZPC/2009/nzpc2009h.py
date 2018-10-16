# Problem H 2009 - Connor Mattson
# I'm not really happy with this one, but I want to move onto the next problem

n = int(input("Enter the number of words to follow: "))
while n != 0:
	wordFrequencies = {}
	wordNumber = {}
	wordActual = {}

	for i in range(n):
		word = input("Enter word: ")
		wordHash = ''.join(sorted(word))
		wordFrequencies[wordHash] = wordFrequencies[wordHash] + 1 if wordHash in wordFrequencies else 0
		if wordHash not in wordNumber: wordNumber[wordHash] = i
		if wordHash not in wordActual: wordActual[wordHash] = word

	maxsorted = {word: wordNumber[word] for word in wordFrequencies.keys() if wordFrequencies[word] == max(wordFrequencies.values())}
	minsorted = [word for word in maxsorted.keys() if maxsorted[word] == min(maxsorted.values())][0]
	print(wordActual[minsorted], wordFrequencies[minsorted])
	n = int(input("Enter the number of words to follow: "))