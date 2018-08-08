# Problem C - Connor Mattson

lineInput = input()
while lineInput != '# 0':
	lineInput = lineInput.split(' ')
	route = lineInput[0]
	maxSize = int(lineInput[1])
	passengers = int(input())

	stops = int(input())
	for i in range(stops):
		stopInput = input().split(' ')
		passengers -= int(stopInput[0])
		passengers += int(stopInput[1])
		if passengers > maxSize:
			passengers = maxSize

	print(route, passengers)
	lineInput = input()