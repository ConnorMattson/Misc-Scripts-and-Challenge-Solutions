# Problem G 2018 - Connor Mattson

import re

data = input("Enter the line to translate or '#' to exit: ")
while data != '#':
	data =  [x for x in re.split(r'(\d+\.\d+)|(\d+)', data) if x != None]
	for i in range(len(data)):
		if i % 2 == 1: data[i] = data[i][::-1]

	print(''.join(data)[::-1])
	data = input("Enter the line to translate or '#' to exit: ")