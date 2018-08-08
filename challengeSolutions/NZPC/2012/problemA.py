#Problem A - Connor Mattson

year = int(input())

while year != 0:
	if year % 4 == 0:
		print('leap')
	else:
		print('common')

	year = int(input())