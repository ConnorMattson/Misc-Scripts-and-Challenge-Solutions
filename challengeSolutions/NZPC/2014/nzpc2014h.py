# Problem H 2014 - Connor Mattson

keys = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

data = input("Enter the line of text or '#' to exit: ").split(' ')
while data != '#':
	message = list(' '.join(data[1:]))
	for i in range(len(message)):
		for key in keys:
			if message[i] in key:
				message[i] = str(key[(key.index(message[i]) + 1 - 2*(data[0] == 'T')) % len(key)])

	print(''.join(message))
	data = input("Enter the line of text or '#' to exit: ").split(' ')