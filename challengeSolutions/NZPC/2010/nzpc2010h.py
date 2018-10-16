# Problem H 2010 - Connor Mattson

n = int(input("Enter the number of pairs: "))
scenario = 1
while n != 0:
	people = []
	groups = []
	for i in range(n):
		pair = input("Enter pair {}: ".format(i+1)).split(' ')
		people.extend([person for person in pair if person not in people])
		groups.append(pair)

	for person in people:
		first = None
		for group in [group for group in groups]:
			if person in group:
				if first: 
					first.extend([person for person in group if person not in first])
					groups.remove(group)
				else: first = group

	print("Scenario {} has {} loops.".format(scenario, len(groups)))
	n = int(input("Enter the number of pairs: "))
	scenario += 1