#Problem F 2014 - Connor Mattson

n = int(input("Enter the size of the puzzle (or 0 to exit): "))
while n != 0:
	puzzle = ['0']
	for i in range(n): puzzle.extend(input("Enter the data stream for line {}: ".format(i + 1)).split(' '))
	print("Ready to go" if set([int(x) for x in puzzle]) == set(range(27)) else "Back to the designer")
	n = int(input("Enter the size of the puzzle (or 0 to exit): "))