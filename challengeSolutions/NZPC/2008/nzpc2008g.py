# Problem G 2008 - Connor Mattson

Scenario = 1
lineInput = input("Enter 'numberOfOutfits numberOfDays' or '0 0' to exit: ").split(' ')

while lineInput != ['0', '0']:
	day = 1
	print('Scenario', Scenario)
	
	Becs = [x for x in range(int(lineInput[0]))]
	Cas = list.copy(Becs)

	BecsRemoved = int(input("Which numbered outfit has Becs removed from her wardrobe? (0 if none): "))
	if BecsRemoved != 0: del Becs[BecsRemoved - 1]
	CasRemoved = int(input("Which numbered outfit has Cas removed from her wardrobe? (0 if none): "))
	if CasRemoved != 0: del Cas[CasRemoved - 1]

	for i in range(int(lineInput[1])):
		dayInput = input("Enter 'outfitNumberPickedByBecs outfitNumberPickedByCas': ").split(' ')
		if Becs[int(dayInput[0])-1] == Cas[len(Cas) - int(dayInput[1])]:
			print('Day', i + 1, 'ALERT')
		else:
			print('Day', i + 1, 'OK')

	Scenario += 1
	lineInput = input("Enter 'numberOfOutfits numberOfDays' or '0 0' to exit: ").split(' ')