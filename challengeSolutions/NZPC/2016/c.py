
data = int(input())
while data != 0:
	if int(data) % 4 != 0:
		print(data, 'No summer games')
	elif (data > 1914 and data < 1918) or (data >= 1939 and data <= 1945):
		print(data, 'Games cancelled')
	elif data > 2020:
		print(data, 'No city yet chosen')
	else:
		print(data, 'Summer Olympics')

	data = int(input())