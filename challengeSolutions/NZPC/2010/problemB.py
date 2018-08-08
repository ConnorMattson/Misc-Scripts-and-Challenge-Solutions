# Connor Mattson - Problem B

def run():
	global lineInput
	sequence = []
	lineInput = lineInput.split(' ')
	sequence.append(int(lineInput[0]) + int(lineInput[1]))
	for i in range(100):
		sequence.append(sequence[len(sequence)-1] + int(lineInput[1]))
	if int(lineInput[2]) in sequence:
		return sequence.index(int(lineInput[2])) + 2
	else:
		return 'X'


lineInput = input()
while lineInput != '0 0 0':
	print(run())
	lineInput = input()