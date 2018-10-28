# Problem E 2016 - Connor Mattson

key = int(input("Enter the key to use: "))
message = list(input("Enter the message to decrypt: "))

for i in range(len(message)):
	if ord(message[i]) > 96 and ord(message[i]) < 123:
		message[i] = chr((ord(message[i]) - 97 - key) % 26 + 97)
		key = key % 25 + 1
print(''.join(message))