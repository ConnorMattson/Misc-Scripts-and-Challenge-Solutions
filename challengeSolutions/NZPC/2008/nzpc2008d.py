# Problem D 2008 - Connor Mattson

lineInput = input("Enter 'flightNumber seatsBooked' or '# 0' to exit: ")
while lineInput != '# 0':
	lineInput = lineInput.split(' ')
	booked = int(lineInput[1])

	print("Enter 'B n' to book n seats, 'C n' to cancel n seats, or 'X 0' to exit: ")
	transaction = input()
	while transaction != 'X 0':
		transaction = transaction.split(' ')
		if transaction[0] == 'B' and booked + int(transaction[1]) <= 68:
			booked += int(transaction[1])

		elif transaction[0] == 'A' and booked >= int(transaction[1]):
				booked -= int(transaction[1])

		transaction = input()

	print("Flight", lineInput[0], "has", booked, "seats booked.")


	lineInput = input()