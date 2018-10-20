# Problem A 2011 - Connor Mattson

data = input("Enter two integers or '0 0' to exit: ").split(' ')
while data != ['0', '0']:
	if int(data[1]) % int(data[0]) == 0: print("{} is a factor of {}.".format(data[0], data[1]))
	elif int(data[0]) % int(data[1]) == 0: print("{} is a multiple of {}.".format(data[0], data[1]))
	else: print("{} is not a factor or a multiple of {}.".format(data[0], data[1]))
	data = input("Enter two integers or '0 0' to exit: ").split(' ')