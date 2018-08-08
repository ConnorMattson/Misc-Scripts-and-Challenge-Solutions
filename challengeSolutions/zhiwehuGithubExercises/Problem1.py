# problem 1

values = []

for i in range(2000, 3201):
	if i % 7 == 0:
		if i % 5 !=0:
			values.append(i)

print(values)