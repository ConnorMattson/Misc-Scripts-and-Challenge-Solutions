#Problem F 2013 - Connor Mattson

scenario = int(input("How many scenarios do you wish to run? "))
for i in range(scenario):
	
	anagrams = {}
	for j in range(int(input("How many anagrams will you be entering? "))):
		data = input("Enter anagram {}: ".format(j + 1))
		anagrams[''.join(sorted(data))] = data

	for j in range(int(input("How many words will you be entering? "))):
		word = input("Enter word {}: ".format(j + 1))
		print("{} is an anagram of {}".format(word, anagrams[''.join(sorted(word))] if ''.join(sorted(word)) in anagrams else "<none>"))