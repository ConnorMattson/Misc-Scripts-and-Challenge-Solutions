#Problem H 2013 - Connor Mattson

n = int(input("Enter the number of card groups to test: "))
for i in range(n):
	d = input("Enter the three cards, e.g. 'RD1F RD1S RD1E': ").split(' ')
	print("Set" if sum([1 for x in [len(set([a,b,c])) for a,b,c in zip(d[0],d[1],d[2])] if x == 1 or x == 3]) == 4 else "Not a set")