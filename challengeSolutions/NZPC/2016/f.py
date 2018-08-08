letters = []

for i in range(int(input())):
	data = input().strip()
	for j in data:
		if j not in letters and j != ' ':
			letters.append(j)

print(''.join(letters))