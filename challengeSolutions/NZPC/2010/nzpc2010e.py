# Problem E 2010 - Connor Mattson

print("Misdemeanor                  Code Points")
print("----------------------------------------")
print("Texting while teacher talks    TT     75")
print("Texting during exercises       TX     50")
print("Phone rings                    PR     80")
print("Receiving texts                RT     30")
print("Argues about phone use         AP     25")
print("Takes pictures                 PX     60")
problems = {"TT": 75, "TX": 50, "PR": 80, "RT": 30, "AP": 25, "PX": 60}

week = [int(x) for x in input("\n\nEnter week number and number of students e.g. '1 4' or '0 0' to exit: ").split(' ')]
while week != [0, 0]:
	students = {}
	order = []

	for i in range(week[1]):
		student = input("Enter student name and misdemeanor e.g. 'Matt PR': ").split(' ')
		students[student[0]] = students[student[0]] + problems[student[1]] if student[0] in students else problems[student[1]]
		if student[0] not in order: order.append(student[0])
		
	print("Week", week[0], ', '.join([student for student in order if students[student] > 100]))
	week = [int(x) for x in input("\nEnter week number and number of students e.g. '1 4' or '0 0' to exit: ").split(' ')]