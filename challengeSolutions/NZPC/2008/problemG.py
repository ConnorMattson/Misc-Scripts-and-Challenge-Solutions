# Problem G - Connor Mattson

Scenario = 1
lineInput = input()

while lineInput != '0 0':
	day = 1
	print('Scenario', Scenario)

	lineInput = lineInput.split(' ')
	Becs = []
	Cas = []
	print(lineInput[0])
	
	BecsRemoved = int(input())
	for i in range(int(lineInput[0])):
		Becs.append(i)

	CasRemoved = int(input())
	for i in range(int(lineInput[0])):
		Cas.append(i)

	if BecsRemoved != 0:
		del Becs[BecsRemoved - 1]
	if CasRemoved != 0:
		del Cas[CasRemoved - 1]

	for i in range(int(lineInput[1])):
		dayInput = input()
		dayInput = dayInput.split(' ')
		if Becs[int(dayInput[0])-1] == Cas[len(Cas) - int(dayInput[1])]:
			print('Day', day, 'ALERT')
		else:
			print('Day', day, 'OK')
		day += 1


	Scenario += 1
	lineInput = input()