data = int(input())

while data != 0:

	attempts = ['25']
	counter = 25
	lower = 1
	upper = 50
	while counter != data:
		if counter > data:
			upper = counter -1
			counter = (upper + lower) // 2
		elif counter < data:
			lower = counter +1
			counter = (upper + lower) // 2
		attempts.append(str(counter))	

	print(' '.join(attempts))
	data = int(input())

