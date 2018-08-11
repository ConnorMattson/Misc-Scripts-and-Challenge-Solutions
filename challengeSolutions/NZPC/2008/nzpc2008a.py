# Problem A 2008 - Connor Mattson

lineInput = int(input("Enter a triangle size (0 to exit): "))
while lineInput != 0:
	for i in range(lineInput):
		print((i + 1) * '*')

	lineInput = int(input("Enter a triangle size (0 to exit): "))