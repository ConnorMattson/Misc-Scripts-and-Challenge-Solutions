# Problem E 2017 - Connor Mattson

data = []
for i in range(int(input("How many bytes are to follow? ")) + 1): data.append([int(x) for x in input("Enter byte {}: ".format(i + 1)).split(' ')])

odd = (sum(data[-1]) % 2 == 1)
for i in range(len(data) - 1):
	if sum(data[i]) % 2 != int(odd): byte = i + 1
for i in range(8): 
	if sum([row[i] for row in data[:-1]]) % 2 != data[-1][i]: bit = i + 1

print("Parity is {}, byte {} is broken, bit {} is broken.".format("odd" if odd else "even", byte, bit))