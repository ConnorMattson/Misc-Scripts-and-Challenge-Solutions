#Problem B - Connor Mattson

s = input()
for _ in range(int(s)):
	N12 = input()
	N12 = N12.split(' ')
	N1 = N12[0]
	N2 = N12[1]
	N1Score = 0
	N2Score = 0
	draws = 0
	g = input()
	for __ in range(int(g)):
		game = input()
		game = game.split(' ')
		game1 = game[0]
		game2 = game[1]

		if game1 == 'R':
			if game2 == 'S' or game2 == 'L':
				success = 1
				N1Score += 1
			else:
				if game2 == 'P' or game2 == 'K':
					success = 1
					N2Score += 1
				else:
					draws += 1

		if game1 == 'P':
			if game2 == 'R' or game2 == 'K':
				success = 1
				N1Score += 1
			else:
				if game2 == 'S' or game2 == 'L':
					success = 1
					N2Score += 1
				else:
					draws += 1

		if game1 == 'S':
			if game2 == 'P' or game2 == 'L':
				success = 1
				N1Score += 1
			else:
				if game2 == 'R' or game2 == 'K':
					success = 1
					N2Score += 1
				else:
					draws += 1

		if game1 == 'L':
			if game2 == 'P' or game2 == 'K':
				success = 1
				N1Score += 1
			else:
				if game2 == 'R' or game2 == 'S':
					success = 1
					N2Score += 1
				else:
					draws += 1

		if game1 == 'K':
			if game2 == 'S' or game2 == 'R':
				success = 1
				N1Score += 1
			else:
				if game2 == 'P' or game2 == 'L':
					success = 1
					N2Score += 1
				else:
					draws += 1
	print (str(N1) + ' ' + str(N1Score) + ' ' + str(N2) + ' ' + str(N2Score) + ' draws ' + str(draws))