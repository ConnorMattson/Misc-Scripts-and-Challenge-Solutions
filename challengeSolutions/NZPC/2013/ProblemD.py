#Problem D - Connor Mattson

x = 0
while x == 0:
	age = input()
	if age == '0':
		x = 1
	else:
		age = int(age)
		age = str(bin(age))[2:]
		numberOf1 = 0
		for i in age:
			if i == '1':
				numberOf1 += 1
		print (str(len(age)) + ' ' + str(numberOf1))