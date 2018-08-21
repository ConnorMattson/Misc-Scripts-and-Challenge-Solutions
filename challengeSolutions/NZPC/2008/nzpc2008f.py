# Problem F 2018 - Connor Mattson

lineInput = list(input("Enter a sentence (or '#' to exit): "))
while lineInput != ['#']:
	alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

	unique_characters = set(lineInput)

	print("The sentence contains", len(unique_characters & alphabet), "unique letters.")
	lineInput = list(input("Enter a sentence (or '#' to exit): "))