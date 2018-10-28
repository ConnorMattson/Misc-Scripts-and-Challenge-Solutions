# Problem B 2016 - Connor Mattson

holes = {'A': 1, 'B': 2, 'D': 1, 'O': 1, 'P': 1, 'Q': 1, 'R': 1,}
for i in range(int(input("How many sentences do you wish to process?"))):
	holecounter = 0

	word = input("Enter sentence {}: ".format(i))
	for letter in word:
		holecounter += holes[letter] if letter in holes else 0
			
	print("'{}' contains {} holes".format(word, holecounter))