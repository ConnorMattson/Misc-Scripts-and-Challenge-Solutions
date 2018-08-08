# Problem D - Connor Mattson

lineInput = input()
while lineInput != '# 0':
	lineInput = lineInput.split(' ')
	booked = int(lineInput[1])

	transaction = input()
	while transaction != 'X 0':
		transaction = transaction.split(' ')
		if transaction[0] == 'B':
			booked += int(transaction[1])
			if booked > 68:
				booked -= int(transaction[1])
		else:
			booked -= int(transaction[1])
			if booked < 0:
				booked += int(transaction[1])

		transaction = input()

	print(lineInput[0], booked)


	lineInput = input()