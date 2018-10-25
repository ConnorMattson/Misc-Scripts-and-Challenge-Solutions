# Problem E 2014 - Connor Mattson

print("Misdemeanor                  Code Points")
print("----------------------------------------")
print("Bringing food into the lab     FD     10")
print("Using Facebook                 FB     25")
print("Using a mobile phone           FH     40")
print("Excessive talking              TK     15")
print("Plagiarism                     CP     30")
print("Equipment damage               DM     50")
print("Playing loud music             MS     20")
problems = {"FD": 10, "FB": 25, "FH": 40, "TK": 15, "CP": 30, "DM": 50, "MS": 20}

n = int(input("How many misdemeanors must be entered? (or '0' to exit) "))
week = 1
while n != 0:
	students = {}
	order = []

	for i in range(n):
		student = input("Enter student name and misdemeanor e.g. 'Matt FD': ").split(' ')
		students[student[0]] = students[student[0]] + problems[student[1]] if student[0] in students else problems[student[1]]
		if student[0] not in order: order.append(student[0])
		
	print("Week", week, ' '.join([student for student in order if students[student] > 50]))
	n = int(input("How many misdemeanors must be entered? (or '0' to exit) "))
	week += 1