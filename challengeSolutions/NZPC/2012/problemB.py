#Problem B - Connor Mattson

#get input
#split input
#order input
#check if valid
#repeat until "0 0 0"

line = input()
while line != "0 0 0":
	lineSplit = line.split(' ')
	lineSplit = sorted(lineSplit, reverse = 1)

	if lineSplit[0] == lineSplit[1] == lineSplit[2]:
		print('Equilateral')
	else:
		if (int(lineSplit[1]) + int(lineSplit[2])) > int(lineSplit[0]):
			if lineSplit[0] != lineSplit[1] and lineSplit[1] != lineSplit[2]:
				print('Scalene')
			else:
				print('Isoscoles')

		else:
			print('Invalid') 

	line = input()	