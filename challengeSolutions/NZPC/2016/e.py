key = int(input())
data = input()

new = ''
for i in data:
	if i in 'abcdefghijklmnopqrstuvwxyz':
		temp = ord(i) - key
		if temp < 97:
			temp = temp - 97 + 123

		new += chr(temp)

		key += 1
		if key > 25:
			key = 1

	else:
		new += i

print(new)