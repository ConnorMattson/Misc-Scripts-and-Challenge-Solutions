#Problem G 2013 - Connor Mattson

scoreValues = { 1: 5, 2: 3, 3: 1}

def runTerm():
	#Create dictionary of student ID's
	students = {}
	for i in range(0, int(studentsInTerm)):
		studentName = input()
		studentName = studentName.split(' ')
		students[studentName[0]] = [0, 0, 0, 0, 0]

	AGrades = 0
	studentData = input()
	while studentData != '0 # #':
		studentData = studentData.split(' ')

		if studentData[1] == 'A':
			students[studentData[0]][0] += 1
			if studentData[2] == 'P':
				if students[studentData[0]][0] > 2:
					students[studentData[0]][4] += 1
				else:
					students[studentData[0]][4] += scoreValues[students[studentData[0]][0]]

		if studentData[1] == 'B':
			students[studentData[0]][1] += 1
			if studentData[2] == 'P':
				if students[studentData[0]][1] > 2:
					students[studentData[0]][4] += 1
				else:
					students[studentData[0]][4] += scoreValues[students[studentData[0]][1]]
		
		if studentData[1] == 'C':
			students[studentData[0]][2] += 1
			if studentData[2] == 'P':
				if students[studentData[0]][2] > 2:
					students[studentData[0]][4] += 1
				else:
					students[studentData[0]][4] += scoreValues[students[studentData[0]][2]]			
		
		if studentData[1] == 'D':
			students[studentData[0]][3] += 1
			if studentData[2] == 'P':
				if students[studentData[0]][3] > 2:
					students[studentData[0]][4] += 1
				else:
					students[studentData[0]][4] += scoreValues[students[studentData[0]][3]]

		studentData = input()

	for i in students:
		if students[i][4] >= 16:
			AGrades += 1
	print('Term',termNumber,'A grades',AGrades)

termNumber = 0
studentsInTerm = input()
while studentsInTerm != '0':
	termNumber += 1
	runTerm()
	studentsInTerm = input()