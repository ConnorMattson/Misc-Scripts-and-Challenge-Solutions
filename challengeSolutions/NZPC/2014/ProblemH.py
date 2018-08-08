#ProblemH - Connor Mattson

textToTranslate = input()
textToTranslate = textToTranslate.split(' ')
timesToTranslate = len(textToTranslate) - 1
wordCount = 0

message = []

def tom():
	if word[0] == 'a':
		message.append('c')
	if word[0] == 'b':
		message.append('a')
	if word[0] == 'c':
		message.append('b')
	if word[0] == 'd':
		message.append('f')
	if word[0] == 'e':
		message.append('d')
	if word[0] == 'f':
		message.append('e')
	if word[0] == 'g':
		message.append('i')
	if word[0] == 'h':
		message.append('g')
	if word[0] == 'i':
		message.append('h')
	if word[0] == 'j':
		message.append('l')
	if word[0] == 'k':
		message.append('j')
	if word[0] == 'l':
		message.append('k')
	if word[0] == 'm':
		message.append('o')
	if word[0] == 'n':
		message.append('m')
	if word[0] == 'o':
		message.append('n')
	if word[0] == 'p':
		message.append('s')
	if word[0] == 'q':
		message.append('p')
	if word[0] == 'r':
		message.append('q')
	if word[0] == 's':
		message.append('r')
	if word[0] == 't':
		message.append('v')
	if word[0] == 'u':
		message.append('t')
	if word[0] == 'v':
		message.append('u')
	if word[0] == 'w':
		message.append('z')
	if word[0] == 'x':
		message.append('w')
	if word[0] == 'y':
		message.append('x')
	if word[0] == 'z':
		message.append('y')
	if word[0] != 'a' and word[0] != 'b' and word[0] != 'c' and word[0] != 'd' and word[0] != 'e' and word[0] != 'f' and word[0] != 'g' and word[0] != 'h' and word[0] != 'i' and word[0] != 'j' and word[0] != 'k' and word[0] != 'l' and word[0] != 'm' and word[0] != 'n' and word[0] != 'o' and word[0] != 'p' and word[0] != 'q' and word[0] != 'r' and word[0] != 's' and word[0] != 't' and word[0] != 'u' and word[0] != 'v' and word[0] != 'w' and word[0] != 'x' and word[0] != 'y' and word[0] != 'z':
		message.append(word[0]) 
	del word[0]

def jerry():
	if word[0] == 'a':
		message.append('b')
	if word[0] == 'b':
		message.append('c')
	if word[0] == 'c':
		message.append('a')
	if word[0] == 'd':
		message.append('e')
	if word[0] == 'e':
		message.append('f')
	if word[0] == 'f':
		message.append('d')
	if word[0] == 'g':
		message.append('h')
	if word[0] == 'h':
		message.append('i')
	if word[0] == 'i':
		message.append('g')
	if word[0] == 'j':
		message.append('k')
	if word[0] == 'k':
		message.append('l')
	if word[0] == 'l':
		message.append('j')
	if word[0] == 'm':
		message.append('n')
	if word[0] == 'n':
		message.append('o')
	if word[0] == 'o':
		message.append('m')
	if word[0] == 'p':
		message.append('q')
	if word[0] == 'q':
		message.append('r')
	if word[0] == 'r':
		message.append('s')
	if word[0] == 's':
		message.append('p')
	if word[0] == 't':
		message.append('u')
	if word[0] == 'u':
		message.append('v')
	if word[0] == 'v':
		message.append('t')
	if word[0] == 'w':
		message.append('x')
	if word[0] == 'x':
		message.append('y')
	if word[0] == 'y':
		message.append('z')
	if word[0] == 'z':
		message.append('w')
	if word[0] != 'a' and word[0] != 'b' and word[0] != 'c' and word[0] != 'd' and word[0] != 'e' and word[0] != 'f' and word[0] != 'g' and word[0] != 'h' and word[0] != 'i' and word[0] != 'j' and word[0] != 'k' and word[0] != 'l' and word[0] != 'm' and word[0] != 'n' and word[0] != 'o' and word[0] != 'p' and word[0] != 'q' and word[0] != 'r' and word[0] != 's' and word[0] != 't' and word[0] != 'u' and word[0] != 'v' and word[0] != 'w' and word[0] != 'x' and word[0] != 'y' and word[0] != 'z':
		message.append(word[0]) 
	del word[0]


if textToTranslate[0] == 'T':
	del textToTranslate[0]
	for _ in range(int(timesToTranslate)):
		word = []
		for i in textToTranslate[wordCount]:
			word.append(i)
		letterCount = len(word)
		for __ in range(letterCount):
			tom()
		if wordCount != timesToTranslate - 1:
			message.append(' ')	
		wordCount += 1
else:
	if textToTranslate[0] == 'J':
		del textToTranslate[0]
		for _ in range(int(timesToTranslate)):
			word = []
			for i in textToTranslate[wordCount]:
				word.append(i)
			letterCount = len(word)
			for __ in range(letterCount):
				jerry()
			if wordCount != timesToTranslate - 1:
				message.append(' ')	
			wordCount += 1
	else:
		pass


message2 = ""
for i in message:
    message2 += str(i)
print (message2)
