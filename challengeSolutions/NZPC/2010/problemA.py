# Problem A - Connor Mattson




Joe = 0
James = 0
Jean = 0
Jane = 0
Unassigned = 0
lineInput = input()
lineInput = input()
while lineInput != '0':
	if lineInput == 'M' or lineInput == 'L':
		Joe += 1
	elif lineInput == 'S':
		James += 1
	elif lineInput == 'X':
		Unassigned += 1
	elif int(lineInput) >= 12:
		Jean += 1
	else:
		Jane += 1
	
	lineInput = input()

print(Joe,Jean,Jane,James,Unassigned)
