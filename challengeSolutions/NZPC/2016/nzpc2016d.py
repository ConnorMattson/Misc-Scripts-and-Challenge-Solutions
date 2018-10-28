# Problem D 2016 - Connor Mattson

data = list(input("Enter the word to check or '#' to exit: "))
while data != ['#']:
	message = ""
	for i in range(len(data)):
		if (data[:i] + data[i + 1:]) == (data[:i] + data[i + 1:])[::-1]:
			message = ''.join(data[:i] + data[i + 1:])
			break
	
	print(message if message else "You cannot make a palindrome from this word.")
	data = list(input("Enter the word to check or '#' to exit: "))