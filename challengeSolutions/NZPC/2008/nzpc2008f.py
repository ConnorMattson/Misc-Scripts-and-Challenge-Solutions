# Problem F 2018 - Connor Mattson

lineInput = list(input("Enter a sentence (or '#' to exit): "))
while lineInput != ['#']:
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	letters = 0

	for i in lineInput:
		if i.lower() in alphabet:
			letters += 1
			alphabet[alphabet.index(i.lower())] = None

	print("The sentence contains", letters, "unique letters.")
	lineInput = list(input("Enter a sentence (or '#' to exit): "))