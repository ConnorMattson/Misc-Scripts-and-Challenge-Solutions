# Problem H - Connor Mattson

machine = 1

lineInput = int(input())
while lineInput != 0:
	machineLevels = {}
	print('Machine', machine)

	for i in range(lineInput):
		machineLevels[i+1] = input()


	people = input()
	while people != '# 0':
		people = people.split(' ')
		Energy = 0
		for i in range(int(people[1])):
			activity = input().split(' ')
			Energy += int(activity[1]) * int((machineLevels[int(activity[0])]))

		print(people[0], Energy)
		people = input()


	machine+= 1
	lineInput = int(input())
