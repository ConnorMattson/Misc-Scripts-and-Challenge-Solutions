#Problem G 2013 - Connor Mattson

n = int(input("Enter the number of students in the class or '0' to exit: "))
while n != 0:
	studentScores = {}
	for i in range(n):
		data = input("Enter the student {}'s ID and name, e.g. '106 Connor Mattson': ".format(i + 1)).split(' ')
		studentScores[data[0]] = [0, 0, 0, 0]

	data = input("Enter the student's ID, which paper (A, B, C, or D, and whether it was a pass or fail. e.g. '106 A P' or '106 D F' enter '0 # #' to exit: ").split(' ')
	while data != ['0', '#', '#']:
		studentScores[data[0]][['A', 'B', 'C', 'D'].index(data[1])] -= 1
		if data[2] == 'P': 
			if studentScores[data[0]][['A', 'B', 'C', 'D'].index(data[1])] < -3: studentScores[data[0]][['A', 'B', 'C', 'D'].index(data[1])] = 1
			else: studentScores[data[0]][['A', 'B', 'C', 'D'].index(data[1])] = 7 + 2*studentScores[data[0]][['A', 'B', 'C', 'D'].index(data[1])]
		data = input("Enter the student's ID, which paper (A, B, C, or D, and whether it was a pass or fail. e.g. '106 A P' or '106 D F' enter '0 # #' to exit: ").split(' ')

	print("The class had {} A grades".format(len([total for total in [sum([score for score in student if score > 0]) for student in studentScores.values()] if total >= 16])))
	n = int(input("Enter the number of students in the class or '0' to exit: "))