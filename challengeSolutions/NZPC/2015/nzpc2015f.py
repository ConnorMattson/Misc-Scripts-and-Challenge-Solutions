# Problem F - Team 19

encrypted = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
decrypted = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

dateInput = input()
while dateInput != '0 0 0':
	dateInput = dateInput.split(' ')
	cypher = int(dateInput[0]) + int(dateInput[1]) + int(dateInput[2])
	cypher = (cypher % 25) + 1
	
	message = input()
	realMessage = []
	
	for i in message:
		if i in encrypted:
			new = encrypted[i] - cypher
			if new > 26:
				new -= 26
			realMessage.append(decrypted[new])
		else:
			realMessage.append(i)
			
	print(''.join(realMessage))
	
	dateInput = input()