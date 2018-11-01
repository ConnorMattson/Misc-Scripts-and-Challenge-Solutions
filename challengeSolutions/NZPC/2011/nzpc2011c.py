# Problem C 2011 - Connor Mattson

coordinates = input("Enter dig length and width, e.g. '4 8' or '0 0' to exit: ")
while coordinates != "0 0":
	items = {}
	count = 0
	for i in range(int(input("Enter the number of items found: "))):
		cell = input("Enter the coordinates of the cell in which item {} was found: ".format(i + 1))
		items[cell] = items[cell] + 1 if cell in items else 1
	for i in range(int(input("Enter a list of coordinates to check: "))):
		cell = input("Enter the coordinate {} to check: ".format(i + 1))
		count += items[cell] if cell in items else 0
	print("There were {} items in the coordinates checked.".format(count))
	coordinates = input("Enter dig length and width, e.g. '4 8' or '0 0' to exit: ")