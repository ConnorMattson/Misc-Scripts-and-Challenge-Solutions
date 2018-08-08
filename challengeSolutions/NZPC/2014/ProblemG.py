#ProblemG - Connor Mattson

gameNumber = input()

def game ():
	line = input()
	line = line.split(" ")
	
	first = int(line[0])
	last = int(line[1])
	variable1 = int(line[2])
	variable2 = int(line[3])
	print ('Game ' + gameNumber)
	while first <= last:
		if first % variable1 == 0:
			if first % variable2 == 0:
				print('Fizz Buzz')
			else:
				print('Fizz')
		else:
			if first % variable2 == 0:
				print('Buzz')
			else:
				print(first)
		first += 1


for _ in range(int(gameNumber)):
	game()