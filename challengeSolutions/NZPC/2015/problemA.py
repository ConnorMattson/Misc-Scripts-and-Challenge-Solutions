# Problem A - Team 19

numberLines = int(input())
while numberLines != 0:

	names = []
	heights = []

	for i in range(numberLines):
		data = input().split(' ')
		names.append(data[0])
		heights.append(float(data[1]))

	maxValue = 0.0
	for i in heights:
		if i > maxValue:
			maxValue = i

	msg = []

	for i in names:
		if heights[names.index(i)] == maxValue:
			msg.append(i)

	msg = ' '.join(msg)
	print(msg)
	
	numberLines = int(input())