# Problem A 2017 - Connor Mattson

for i in range(int(input("How many triangles do you want to check? "))):
	data = input("Enter the angles of each corner, e.g. '59 60 60': ")
	print(data + " Seems OK" if sum([int(x) for x in data.split(' ')]) == 180 else data + " Check")