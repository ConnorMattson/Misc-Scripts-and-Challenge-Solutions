# Problem D 2018 - Connor Mattson

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for i in range(int(input("How many dates do you wish to check? "))):
	date = input("Enter the day, month, and name of the eventoccuring then e.g. '15 September NZPC': ").split(' ')
	if months.index(date[1])*100 + int(date[0]) == 815: print(*date[2:], "is today!")
	else: print(*date[2:], "falls", "after" if months.index(date[1])*100 + int(date[0]) > 815 else "before", "the 15th September.")