# Problem D 2010 - Connor Mattson

n = int(input("Enter the number of towns Bob has visited: "))
week = 1
while n != 0:
	towns = []
	for i in range(n): towns.append(input("Enter the name of town {}: ".format(i + 1)))
	print("Week {} {}".format(week, len(set(towns))))
	week += 1
	n = int(input("Enter the number of towns Bob has visited: "))