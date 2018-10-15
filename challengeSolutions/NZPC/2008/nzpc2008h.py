# Problem H 2008 - Connor Mattson

machine = 1
lineInput = int(input("How many levels does the machine have? (0 to exit): "))

while lineInput != 0:
	machineLevels = {}
	print('Machine', machine)

	for i in range(lineInput):
		machineLevels[i+1] = input("Enter the energy expended per minute at level {}: ".format(i + 1))


	people = input("Enter 'name numberOfExercies' or '# 0' to exit: ").split()
	while people != ['#', '0']:

		Energy = 0
		for i in range(int(people[1])):
			activity = input("enter 'exerciseLevel durationInMinutes' for exercise {}: ".format(i + 1)).split(' ')
			Energy += int(activity[1]) * int((machineLevels[int(activity[0])]))

		print(people[0], "expended", str(Energy) + "J of energy.")
		people = input("Enter 'name numberOfExercies' or '# 0' to exit: ").split()


	machine += 1
	lineInput = int(input("How many levels does the machine have? (0 to exit): "))