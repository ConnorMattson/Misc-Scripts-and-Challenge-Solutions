# Problem G 2009 - Connor Mattson

print("Service Problem                                    Code Points")
print("--------------------------------------------------------------")
print("Lost Luggage                                          L    120")
print("Struck by Stewardess                                  S    150")
print("Overbooked and bumped off flight after checking in    B    150")
print("Not greeted by name                                   N     40")
print("Not given seat in class paid for                      C    160")
print("Drinks trolley ran into passenger                     D    100")
print("Stewardess rude                                       R    100")
print("No space in overhead locker                           O    100")
problems = {"L": 120, "S": 150, "B": 150, "N": 40, "C": 160, "D": 100, "R": 100, "O": 100}

name = input("\n\nEnter flight name or '#' to exit: ")
while name != '#':
	seats = {}
	seat = input("Enter seat number and problem e.g. '03A L' or just '00A' to exit: ").split(' ')
	while seat != ["00A"]:
		seats[seat[0]] = seats[seat[0]] + problems[seat[1]] if seat[0] in seats else problems[seat[1]]
		seat = input("Enter seat number and problem e.g. '03A L' or just '00A' to exit: ").split(' ')
		
	print("Flight", name, "had", str(len([x for x in seats.values() if x >= 200])), "future flight upgrades.")
	name = input("\n\nEnter flight name or '#' to exit: ")