# Problem A 2010 - Connor Mattson

n = int(input("Enter the number of clothes to classify: "))
while n != 0:
	clothes = [0, 0, 0, 0, 0]
	for i in range(n):
		data = input("Enter clothing size or X for unreadable: ")
		if data == "X": clothes[4] += 1
		elif data.isdigit():
			if int(data) >= 12: clothes[1] += 1
			else: clothes[2] += 1
		else: 
			if data == 'M' or data == 'L': clothes[0] += 1
			else: clothes[3] += 1

	print("Joe has", str(clothes[0]), "clothes.\nJean has", str(clothes[1]), "clothes.\nJane has", str(clothes[2]), "clothes.\nJames has", str(clothes[3]), "clothes\n" + str(clothes[4]), "clothes were unreadable.")
	n = int(input("Enter the number of clothes to classify: "))