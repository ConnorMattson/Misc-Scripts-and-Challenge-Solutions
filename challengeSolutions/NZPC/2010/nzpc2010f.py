# Problem F 2010 - Connor Mattson

def testLine(data):
	position = int(data[0])
	visited = [position]
	for sequence in data[1:]:
		position = position + int(sequence[1]) if sequence[0] == 'U' else position - int(sequence[1])
		if position in visited or position > 20 or position < 1: return "illegal"
		visited.append(position)
	return "Did not visit: " + ' '.join([str(x) for x in range(1,21) if x not in visited])

data = input("Enter Route e.g. '3 U2 D1' for starting at house 3 of 20, going up 2 houses, then down one house (3 -> 5 -> 4) or '#' to exit: ").split(' ')
while data != ['#']:
	print(testLine(data))
	data = input("Enter Route e.g. '3 U2 D1' for starting at house 3 of 20, going up 2 houses, then down one house (3 -> 5 -> 4) or '#' to exit: ").split(' ')