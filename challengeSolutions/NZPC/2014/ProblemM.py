#Problem M - Connor Mattson



def firstLine():
	global strands
	global line
	global wellFormed
	strands = 0
	line = input()
	line = list(line)
	wellFormed = 0
	characterCount = 0
	print(line)

	while characterCount != int(len(line)) - 1:
		if line[characterCount] == '|':
			if line[characterCount + 1] == '|':
				strands += 1
				wellFormed = 1
				characterCount += 1
			else:
				if line[characterCount - 1] == '|':
					wellFormed = 1
					characterCount += 1
				else:
					wellFormed = 0
		else:
			characterCount += 1			

	if line[characterCount] == '|':
		if line[characterCount - 1] == '|':
			wellFormed = 1
			characterCount += 1
		else:
			wellFormed = 0



def middleLines():
	line2 = input()
	print (line2)
	line2 = list(line2)
	global line
	print (line2)
	characterCount = 0
	while characterCount != len(line):
		found = 0


		if line[characterCount] == '|':

			if line2[characterCount] == '|':
				if line2[characterCount + 1] == '|' or line2[characterCount - 1] == '|':
					characterCount += 1
					found = 1

			if line2[characterCount] == '\\':
				if line2[characterCount + 1] == 'd' or line2[characterCount + 1] == 'u':
					if line2[characterCount + 1] == 'd':
						if line2[characterCount + 2] == '\\' and line[characterCount + 1] == '|' and line2[characterCount + 3] == 'u':
							characterCount += 1
							found = 1
					if line2[characterCount + 1] == 'u':
						if line2[characterCount - 2] == '\\' and line[characterCount - 1] == '|' and line2[characterCount - 1] == 'd':
							characterCount += 1
							found = 1
				else:
					if line2[characterCount - 1] == 'd' or line2[characterCount - 1] == 'u':
						if line2[characterCount - 1]:
							pass
					
					if line2[characterCount - 1] == '/' and line[characterCount -1]:
						pass

			if line2[characterCount] == '/':
				if line2[characterCount + 1] == 'd' or line2[characterCount + 1] == 'u':
					if line2[characterCount + 1] == 'd':
						if line2[characterCount - 2] == '\\' and line[characterCount - 1] == '|':
							characterCount += 1
							found = 1
					if line2[characterCount + 1] == 'u':
						if line2[characterCount + 2] == '\\' and line[characterCount + 1] == '|':
							characterCount += 1
							found = 1
				else:
					#SEE NOTES, DIAGRAM 3
					pass


		# if line[characterCount] == '/':
		# if line[characterCount] == '\\':
		# if line[characterCount] == 'u':
		# if line[characterCount] == 'd':
	pass



timesToRun = input()
for _ in range(int(timesToRun)):
	linesToRun = input()

	if int(linesToRun) > 1:
		firstLine()
		if wellFormed == 1:
			for __ in range(int(linesToRun) - 1):
				middleLines()
		else:
			print('Not well formed')		
	
	if int(linesToRun) == 1:
		firstLine()
		if wellFormed == 1:
			print('Well formed with ' + str(strands) + ' strands')
		else:
			print('Not well formed')
