# Problem B - Connor Mattson

def solveLine():
	global lineInput
	cheryl = 0
	tania = 0

	for i in lineInput:
		if i == '*':
			break
		if i == 'A':
			cheryl += 1
		elif int(i) % 2 == 0:
			tania += 1
		else:
			cheryl+= 1

	if tania > cheryl:
		return "Tania"
	elif cheryl > tania:
		return 'Cheryl'
	else:
		return 'Draw'



lineInput = input().split(' ')
while lineInput != ['#']:
	print(solveLine())
	lineInput = input().split(' ')