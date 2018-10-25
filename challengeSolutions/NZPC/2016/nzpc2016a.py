

times = input()
prices = []


for i in range(int(times)):
	prices.append(float(input()))

output = str(sorted(prices)[1])
temp = output[::-1]

if '.' in output:
	while temp.index('.') != 2:
		output += '0'
		temp = output[::-1]

print(output)