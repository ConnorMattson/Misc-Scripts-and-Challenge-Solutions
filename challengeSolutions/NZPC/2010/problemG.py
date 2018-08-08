# Problem G - Connor Mattson

puzzleInput = input()
while puzzleInput != '0':

	words = []
	letters = []
	lettersInWords = []

	for i in range(int(puzzleInput)):
		lineInput = input()
		words.append(lineInput)

	def sort():
		global words
		global letters
		for i in words:
			if len(i) == 9:
				for j in i:
					letters.append(j)

	lettersInWords = letters
	letters.sort()

	for i in words:
		for j in lettersInWords:
			if j not in i:
				del lettersInWords[lettersInWords.index(j)]


	sort()

	letters.sort()
	del letters[letters.index(lettersInWords[0])]
	letters.insert(4, lettersInWords[0])
	print(letters)

	puzzleInput = input()