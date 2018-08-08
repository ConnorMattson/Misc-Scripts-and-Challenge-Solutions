# Problem A - Connor Mattson

lineInput = int(input())
while lineInput != 0:
	n = 1

	for i in range(lineInput):
		print((n)*'*')
		n+= 1

	lineInput = int(input())