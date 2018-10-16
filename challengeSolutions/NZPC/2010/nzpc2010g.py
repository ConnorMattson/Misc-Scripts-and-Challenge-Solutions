# Problem G 2010 - Connor Mattson

n = input("Enter the number of solutions or '0' to exit: ")
while n != '0':

	alphabet = list('abcdefghijklmnopqrstuvwxyz')

	for i in range(int(n)):
		word = input("Enter solution {}: ").format(i + 1)
		if len(word) == 9: letters = list(word.upper())
		alphabet = [letter for letter in alphabet if letter in word]

	letters = sorted([letter for letter in letters if letter not in alphabet])
	print(*letters[0:4], alphabet[0].upper(), *letters[4:])

	n = input("Enter the number of solutions or '0' to exit: ")