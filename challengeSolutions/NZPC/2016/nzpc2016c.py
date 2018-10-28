# Problem C 2016 - Connor Mattson

data = int(input("Enter the year to check, e.g. '1896' or '0' to exit: "))
while data != 0:
	if int(data) % 4 != 0: print(data, 'No summer games')
	elif data in [1916, 1940, 1944]: print(data, 'Games cancelled')
	elif data > 2020: print(data, 'No city yet chosen')
	else: print(data, 'Summer Olympics')
	data = int(input("Enter the year to check, e.g. '1896': "))