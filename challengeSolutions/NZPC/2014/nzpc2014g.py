#Problem G 2014 - Connor Mattson

game = 1
gameAmount = int(input("enter the number of games to play: "))
for i in range(gameAmount):
	data = [int(x) for x in input("Enter the start, finish, and two numbers to replace e.g. '1 15 3 5' will replace 3s and 5s between 1 and 15: ").split(' ')]
	print("Game", game)
	for j in range(data[0], data[1] + 1): 
		if j % data[2] == 0 and j % data[3] == 0: print("Fizz Buzz")
		elif j % data[2] != 0 and j % data[3] != 0: print(j)
		else: print("Fizz" if j % data[2] == 0 else "Buzz")
	game += 1