#Problem H - Connor Mattson



def addToDictionary(card):
	for i in colour:
		if i == card[0]:
			colour[i] += 1

	for i in number:
		if i == card[1]:
			number[i] += 1

	for i in shape:
		if i == card[2]:
			shape[i] += 1

	for i in fill:
		if i == card[3]:
			fill[i] += 1


def isSet():
	cardGroup = input()
	cardGroup = cardGroup.split(' ')
	card1, card2, card3 = cardGroup[0], cardGroup[1], cardGroup[2]

	addToDictionary(card1)
	addToDictionary(card2)
	addToDictionary(card3)

	print(colour)
	print(number)
	print(shape)
	print(fill)

	for i in colour:
		if colour[i] == 3:
			set = 1

	for i in number:
		if number[i] == 3:
			set = 1

	for i in shape:
		if shape[i] == 3:
			set = 1

	for i in fill:
		if fill[i] == 3:
			set = 1

	if sum(colour.values()) == 0 and sum(number.values()) == 0 and sum(shape.values()) == 0 and sum(fill.values()) == 0:
		set = 1

timesToRun = input()
for i in range(int(timesToRun)):
	colour = {"R":0,"G":0,"B":0}
	number = {"1":0,"2":0,"3":0}
	shape = {"D":0,"O":0,"S":0}
	fill = {"F":0,"S":0,"E":0}

	set = 0
	
	isSet()

	if set == 1:
		print('Set')
	else:
		print('Not a set')