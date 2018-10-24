# Problem A 2013 - Connor Mattson

n = int(input("How many scores have to be processed? (enter '0' to exit) "))
while n != 0:
	scores = []
	for i in range(n): scores.append(int(input("Enter score {}: ".format(i + 1))))
	print("The best score was {}".format(min(scores)))
	n = int(input("How many scores have to be processed? (enter '0' to exit) "))