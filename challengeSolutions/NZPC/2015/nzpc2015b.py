# Problem B - Team 19


counter = 1
numberCustomers = int(input())
for i in range(numberCustomers):

	questions = []

	customerq = int(input())
	for i in range(customerq):
		question = input()
		questions.append(question)
	
	for i in range(len(questions)):
		temp = questions[i].split(' ')
		questions[i] = ''.join(temp)
	
	
	print('Customer', counter)
	
	customera = int(input())
	for i in range(customera):
		answer = input().split(' ')
		temp = questions[int(answer[0]) - 1]
		if answer[3] == temp[int(answer[1]) - 1] and answer[4] == temp[int(answer[2]) - 1]:
			print('correct')
		else:
			print('error')
			
	counter += 1