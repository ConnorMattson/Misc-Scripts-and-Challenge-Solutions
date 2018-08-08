#Problem F - Connor Mattson

s = 1

def validate():
	presentLetters = []
	for _ in range(int(s)):
		line = input()
		line = line.split(' ')
		for i in line:
			letterCounter = 0
			if len(presentLetters) != 0:
				while letterCounter != len(presentLetters):
					if presentLetters[letterCounter] == i:
						letterCounter = len(presentLetters)
						letterFound = 1
					else:
						letterCounter += 1
						letterFound = 0
				if letterFound == 0:
					presentLetters.append(i)
			else:
				presentLetters.append(i)
	if len(presentLetters) == 27:
		print ('Ready to go')
	else:
		print ('Back to the designer')


while s != 0:
	s = input()
	if s == '0':
		break
	else:
		validate()