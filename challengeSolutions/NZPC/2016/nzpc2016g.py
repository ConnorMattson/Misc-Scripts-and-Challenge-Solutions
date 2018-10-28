# Problem G 2016 - Connor Mattson

data = int(input("Which box (1-50) is the rabbit hidden in? enter '0' to exit: "))
while data != 0:

	attempts = [25]
	lower, upper = [1, 50]
	while attempts[-1] != data:
		lower, upper = [lower, attempts[-1] - 1] if attempts[-1] > data else [attempts[-1] + 1, upper]
		attempts.append((upper + lower) // 2)

	print("search in the order: " + ' '.join([str(x) for x in attempts]))
	data = int(input("Which box (1-50) is the rabbit hidden in? enter '0' to exit: "))