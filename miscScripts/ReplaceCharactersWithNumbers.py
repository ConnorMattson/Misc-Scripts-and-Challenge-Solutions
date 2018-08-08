print("Entire sentance to be changed. (each !#! will be replaced)")
stringToModify = input()

print("The number of lines you want.")
timesToModify = input()

lineNumber = 1

while lineNumber <= int(timesToModify):
	stringBeingModified = stringToModify
	if len(timesToModify) == 3:
		if len(str(lineNumber)) == 1:
			stringBeingModified = stringBeingModified.replace("!#!", '00' + str(lineNumber))
		if len(str(lineNumber)) == 2:
			stringBeingModified = stringBeingModified.replace("!#!", '0' + str(lineNumber))
		if len(str(lineNumber)) == 3:
			stringBeingModified = stringBeingModified.replace("!#!", str(lineNumber))
	if len(timesToModify) == 2:
		if len(str(lineNumber)) == 1:
			stringBeingModified = stringBeingModified.replace("!#!", '0' + str(lineNumber))
		else:
			stringBeingModified = stringBeingModified.replace("!#!", str(lineNumber))
	if len(timesToModify) == 1:
		stringBeingModified = stringBeingModified.replace("!#!", str(lineNumber))
	print(stringBeingModified)
	
	lineNumber += 1
	continue