# Problem C 2017 - Connor Mattson

visited = [int(input("What station does Hilary start at? e.g. '4' "))]
data = list(input("Enter Hilary's movement, e.g. 'A3' to move anticlockwise 3 stations or 'C4' to move clockwise 4. enter '#' to exit: "))
while data != ['#']:
	visited.append((visited[-1] + ((-1)**(data[0] == 'A')) * int(data[1]) - 1) % 8 + 1)
	data = list(input("Enter Hilary's movement, e.g. 'A3' to move anticlockwise 3 stations or 'C4' to move clockwise 4. enter '#' to exit: "))

print(' '.join([str(x) for x in visited]) + " reject"*(len(set(visited)) < 5 or len(set(visited)) != len(visited)))