alphabet = {'24': 'y', '25': 'z', '20': 'u', '21': 'v', '22': 'w', '23': 'x', '11': 'l', '10': 'k', '13': 'n', '12': 'm', '15': 'p', '14': 'o', '17': 'r', '16': 'q', '19': 't', '18': 's', '7': 'h', '6': 'g', '5': 'f', '4': 'e', '3': 'd', '2': 'c', '1': 'b', '0': 'a', '9': 'j', '8': 'i'}
alphabetnumbers = {'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, 'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14}

check = 0
string = 'abcdefgh'

def updateString(toUpdate):
	lastNumber = 0

	for letter in alphabetnumbers:
		if letter == toUpdate[-1]:
			lastNumber = int(alphabetnumbers[letter]) + 1
			break

	if lastNumber == 26:
		lastNumber = 0

	toUpdate = list(toUpdate)
	toUpdate[-1] = alphabet[str(lastNumber)]
	toUpdate = ''.join(toUpdate)
	return toUpdate

def convertToNumber(string4):
	string4 = list(string4)
	for i in string4:
		for letter in alphabetnumbers:
			if letter == i:
				string4[string4.index(i)] = int(alphabetnumbers[letter])
				break

	return string4

def findStraight(string2):
	string2 = convertToNumber(string2)

	last = string2[0]
	TwoLast = string2[1]

	for i in string2[2:]:
		if last == i - 2 and TwoLast == i - 1:
			return True
		else:
			last = TwoLast
			TwoLast = i

	return False



def findPairs(string3):
	string3 = convertToNumber(string3)

	last = string3[0]
	counter = 0
	letter = False

	for i in string3[1:]:
		if last == i and letter != i:
			counter += 1
			letter = i
		else:
			last = i
			letter = False

	if counter > 1:
		return True

	return False



while check != 1:
	check = 1

	string = updateString(string)

	if 'i' in string or 'o' in string or 'l' in string:
		check = 0

	else:
		if findStraight(string) == True:
			if findPairs(string) == True:
				pass
			else:
				check = 0

		else:
			check = 0

	print(string)

print('~~~~~~~~~~~~~~~~~~~')
print('Password found: ', string)