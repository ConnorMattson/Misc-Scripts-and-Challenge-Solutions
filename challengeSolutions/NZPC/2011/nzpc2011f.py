# Problem F 2011 - Connor Mattson

weekData = int(input("Enter the number of weeks worth of data: "))
weekNumber = 1
for i in range(weekData):
	rooms = {}

	for i in range(20):
		data = input("{}: Enter the room number and occupant's name e.g. '101 Harry' room numbers 101-120: ".format(i + 1)).split(' ')
		rooms[int(data[0])] = data[1]

	print("""Complaints are formatted as follows:
Even or Odd, followed by a factor of rooms to be eliminated and the first letter of students to be eliminated
e.g. 'O 5 G' to eliminate odd numbered rooms where the room number is a multiple of 5 or the student's name starts with G\n""")

	noisy = {}
	for i in range(5):
		data = input("Enter complaint {}: ".format(i + 1)).split(' ')
		for room in rooms.keys():
			if not (((rooms[room][0].upper() == data[2]) or (room % int(data[1]) == 0)) or (room % 2 == (data[0] == 'O'))):
				noisy[room] = noisy[room] + 1 if room in noisy else 1

	print("Week {}".format(weekNumber), *[rooms[room] for room in sorted(noisy.keys()) if noisy[room] == max(noisy.values())], sep="\n")