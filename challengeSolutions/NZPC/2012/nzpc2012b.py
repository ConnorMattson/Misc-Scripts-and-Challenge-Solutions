#Problem B 2012 - Connor Mattson

data = sorted(input("Enter the length of each side of the triangle, e.g. '6 5 4' or '0 0 0' to exit: ").split(' '))
while data != ['0', '0', '0':

	if data[0] == data[1] == data[2]: print("This is an equilateral triangle.")
	else:
		if (int(data[1]) + int(data[2])) > int(data[0]): print("This is a scalene triangle" if (data[0] != data[1] and data[1] != data[2]) else "This is an isoscoles triangle")
		else: print('These lengths cannot be combined to make a valid triangle.') 

	data = sorted(input("Enter the length of each side of the triangle, e.g. '6 5 4' or '0 0 0' to exit: ").split(' '))