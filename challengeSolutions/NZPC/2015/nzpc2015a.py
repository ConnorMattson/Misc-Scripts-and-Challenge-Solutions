# Problem A 2015 - Connor Mattson

numberLines = int(input("How many names to compare? (or 0 to exit) "))
while numberLines != 0:
	names = {}

	for i in range(numberLines):
		data = input("Enter a name and height, e.g. 'John 1.75': ").split(' ')
		names[data[0]] = data[1]

	tallest = [name for name in names if names[name] == max(names.values())][0]
	print("The tallest person is {} with a height of {}.".format(tallest, names[tallest]))
	numberLines = int(input("How many names to compare? (or 0 to exit) "))