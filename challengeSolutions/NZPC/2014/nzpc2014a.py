#Problem A 2014 - Connor Mattson

for i in range(int(input("Enter the number of members to test: "))):
	data = input("Enter the members age and handicap e.g. '61 12': ").split(' ')
	print("This member should be in the '{}' category".format("senior" if (int(data[0]) >= 55 and int(data[1]) >= 8) else "open"))