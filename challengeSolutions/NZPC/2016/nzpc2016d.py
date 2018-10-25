data = input()

while data != '#':
	word = None
	for i in range(len(data)):
		temp = list(data)
		
		del temp[i]
		if temp == temp[::-1]:
			word = temp
			break

	if word:
		print(''.join(word))
	else:
		print('not possible')


	data = input()