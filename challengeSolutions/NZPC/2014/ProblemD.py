#Problem D - Connor Mattson

CL = input()
CL = CL.split(' ')
C = CL[0]
L = CL[1]

def line():
	global lineInput
	lineInput = input()
	lineInput = list(lineInput)
	
	z = 0
	while z != len(lineInput):
		if lineInput[z] == '_':
			lineInput[z-1] = int(lineInput[z-1]) + int(lineInput[z+1])
			del lineInput[z]
			del lineInput[z]
		else:
			z += 1
	dot()

def dot():
	for __ in range(int(lineInput[0])):
		finalLine.append('.')
	del lineInput[0]
	if len(lineInput) > 0:
		cross()
	else:
		print (finalLine)

def cross():
	for __ in range(int(lineInput[0])):
		finalLine.append('x')
	del lineInput[0]
	if len(lineInput) > 0:
		dot()
	else:
		print (finalLine)

for _ in range(int(L)):
	finalLine = []
	line()
