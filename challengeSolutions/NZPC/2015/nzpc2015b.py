# Problem B 2015 - Connor Mattson

for i in range(int(input("How many customers do you want to process? "))):

	questions = []
	for questionNum in range(int(input("how many security questions does customer {} have? ".format(i + 1)))): questions.append(input("Enter question {}: ".format(questionNum)).replace(' ',''))
	
	for answer in range(int(input("How many answers do you with to test? "))):
		data = input("Enter answer {} in the form: number of the security question, two indexes of characters, the two characters. e.g. '1 5 7 P R': ").split(' ')
		print("Correct" if (questions[int(data[0]) - 1][int(data[1]) - 1] == data[3] and questions[int(data[0]) - 1][int(data[2]) - 1] == data[4]) else "Error")