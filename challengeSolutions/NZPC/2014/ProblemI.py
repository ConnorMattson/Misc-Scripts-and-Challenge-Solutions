# Problem I

sampleInput = ["2229", "100 + 29", "135 + 235",]
expression = input()

roundedNumbers = []
roundedNumbersIndex = []



def removeEmpties(listToClean):
	while listToClean.count("") > 0:
		for i in listToClean:
			if i == "":
				listToClean.remove(i)
				continue

def insertRunt():
	a = 0
	for i in roundedNumbers:
		compiled[roundedNumbersIndex[a]] = i
		a += 1

def splitByOperator(listToUse):
	counter = 0
	for i in listToUse:
		if i == "+" or i == "*" or i == "(" or i == ")":
			listToUse = listToUse[:counter] + " " + listToUse[counter:]
			counter += 1
			listToUse = listToUse[:counter + 1] + " " + listToUse[counter + 1:]
			counter += 1
		counter += 1
	return listToUse

def findBrackets(listToUse):



	listToUse = list(enumerate(listToUse))

	indexOfOpen = []
	indexOfClose = []
	bracketsRemoved = 0
	
	for i in listToUse:
	
		if i[1] == "(":
	
			innerOpen = "None"
			innerClose = "None"
			# indexOfOpen.append (i[0])
	
			for i in listToUse[i[0]:]:
				if i[1] == "(":
					innerOpen = i[0]
				if i[1] == ")":
					innerClose = i[0]
					break
			indexOfOpen.append(innerOpen)
			indexOfClose.append(innerClose)

	indexOfOpen = f7(indexOfOpen)
	indexOfClose = f7(indexOfClose)

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]



compiled = splitByOperator(expression).split(" ")
removeEmpties(compiled)



for i in compiled:
	try:
		i = int(i)
	except ValueError:
		pass
	if type(i) == int:
		i = str(i)
		try:
			if i[1] == "0" or i[1] == "1" or i[1] == "2":
				roundedNumbersIndex.append(compiled.index(i))
				i = list(i)
				for x in i[1:]:
					i.remove(x)
					i.append("0")
				i = "".join(i)
				roundedNumbers.append(i)
			else:
				roundedNumbersIndex.append(compiled.index(i))
				i = list(i)
				y = int(i[0])
				z = y + 1
				i[0] = str(z)
				for x in i[1:]:
					i.remove(x)
					i.append("0")
				i = "".join(i)	
				roundedNumbers.append(i)
		except IndexError:
			pass



insertRunt()
indexOfOpen = []
indexOfClose = []
findBrackets(compiled)


def doOperators ():
	global indexOfOpen
	global indexOfClose
	currentIndex = 1
	stringToSolve = []

	while indexOfOpen[0] + currentIndex != indexOfClose[0]:
		stringToSolve.append(str(compiled[indexOfOpen[0] + currentIndex]))
		currentIndex += 1
	
	stringToSolve = ''.join(stringToSolve)
	stringToSolve = (eval(stringToSolve))
	compiled[indexOfOpen[0]] = str(stringToSolve)
	currentIndex = 1
	
	while indexOfOpen[0] + currentIndex != indexOfClose[0] + 1:
		del compiled[indexOfOpen[0] + currentIndex]
		indexOfClose[0] = indexOfClose[0] - 1
	findBrackets(compiled)

while len(indexOfOpen) > 0:
	doOperators()

compiled = ''.join(compiled)
compiled = eval(compiled)
print (compiled)

	#while indexOfOpen[0] != indexOfClose[0] - 2:
		# if compiled[indexOfOpen[0] + currentIndex] == '*' or compiled[indexOfOpen[0] + currentIndex] == '+':
		# 	if compiled[indexOfOpen[0] + currentIndex] == '*':
		# 		currentIndex -= 1
		# 		compiled[indexOfOpen[0] + currentIndex] = (int(compiled[indexOfOpen[0] + currentIndex]) * int(compiled[indexOfOpen[0] + currentIndex + 2]))
		# 		del compiled[indexOfOpen[0] + currentIndex + 1]
		# 		del compiled[indexOfOpen[0] + currentIndex + 1]
		# 		findBrackets(compiled)
		# 	else:
		# 		stringToSolve.append
		# 		currentIndex -= 1
		# 		compiled[indexOfOpen[0] + currentIndex] = (int(compiled[indexOfOpen[0] + currentIndex]) + int(compiled[indexOfOpen[0] + currentIndex + 2]))
		# 		del compiled[indexOfOpen[0] + currentIndex + 1]
		# 		del compiled[indexOfOpen[0] + currentIndex + 1]
		# 		findBrackets(compiled)
		# else:
		# 	currentIndex += 1