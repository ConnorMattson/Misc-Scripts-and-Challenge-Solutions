# Problem B 2010 - Connor Mattson

sequence = [int(x) for x in input("Enter the start, difference, and an integer. Finds if the integer is in that arithmetic sequence.\nE.g. '3 2 11' finds 11 if it's in [3,5,7...]. Enter '0 0 0' to exit: ").split(' ')]
while sequence != [0, 0, 0]:
	message = "is number " + str(int((sequence[2] - sequence[0]) / sequence[1]) + 1) + " in the sequence."  if ((sequence[2] - sequence[0]) % sequence[1] == 0) else "is not in the sequence."
	print(str(sequence[2]), message)
	sequence = [int(x) for x in input("\nEnter the start, difference, and an integer. Finds if the integer is in that arithmetic sequence.\nE.g. '3 2 11' finds 11 if it's in [3,5,7...]. Enter '0 0 0' to exit: ").split(' ')]