#Problem A - Connor Mattson
# N = number of lines
# A = age
# H = handicap

def process():
	age = int(lineInput.split(' ')[0])
	handicap = int(lineInput.split(' ')[1])

	if age > 54:
		if handicap < 8:
			print ("Open")
		else:
			print ("Senior")
	else:
		print("Open")

timesToRun = input()
for _ in range(int(timesToRun)):
	lineInput = input()
	process()