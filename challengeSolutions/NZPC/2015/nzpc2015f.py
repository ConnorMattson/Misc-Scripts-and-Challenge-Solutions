# Problem F 2015 - Connor Mattson

dateInput = input("What is todays date? e.g. '25 12 2015' or '0 0 0' to exit: ").split(' ')
while dateInput != ['0', '0', '0']:
	cypher = (int(dateInput[0]) + int(dateInput[1]) + int(dateInput[2])) % 25 + 1
	message = list(input("What is the message you would like to translate? "))

	for i in range(len(message)): 
		message[i] = chr((ord(message[i]) - 97 - cypher) % 26 + 97) if (ord(message[i]) > 96 and ord(message[i]) < 123) else message[i]
	print(''.join(message))
	dateInput = input("What is todays date? e.g. '25 12 2015' or '0 0 0' to exit: ").split(' ')