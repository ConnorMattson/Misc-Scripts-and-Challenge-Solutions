# Problem B 2011 - Connor Mattson

lineInput = [int(x) for x in input("Enter the sequence of cards ending in * e.g. 'A 2 5 A *' or '#' to exit: ").replace("A", "1").split(' ')[:-1]]
while len(lineInput) != 0:
	odd = len([number for number in lineInput if number % 2 == 1])
	even = len([number for number in lineInput if number % 2 == 0])
	print("There were more odd cards than even"*(odd > even) + "There were more even cards than odd"*(odd < even) + "There were the same number of even and odd cards"*(odd == even))
	lineInput = [int(x) for x in input("Enter the sequence of cards ending in * e.g. 'A 2 5 A *' or '#' to exit: ").replace("A", "1").split(' ')[:-1]]