# Problem F - Connor Mattson

lineInput = input()
while lineInput != '#':
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	letters = 0

	lineInput = list(lineInput)
	for i in lineInput:
		if i.lower() in alphabet:
			letters += 1
			del alphabet[alphabet.index(i.lower())]

	print(letters)
	lineInput = input()



