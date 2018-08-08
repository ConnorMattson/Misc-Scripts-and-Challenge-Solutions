#Problem C - Connor Mattson

x = 0
while x == 0:
	line = input()
	line = line.split(' ')
	output = 0
	output += int(line[0]) * 10
	output += int(line[1]) * 20
	output += int(line[2]) * 50
	output += int(line[3]) * 100
	output += int(line[4]) * 200
	output += int(line[5]) * 500
	output += int(line[6]) * 1000
	output += int(line[7]) * 2000
	output += int(line[8]) * 5000
	output += int(line[9]) * 10000
	if output == 0:
		x = 1
	else:
		output = str(output)
		output = list(output)
		output.insert(len(output)- 2, '.')
		if len(output) == 3:
			output.insert(0, '0')
		output =''.join(output)
		print ('$' + output)

		