# Problem C 2010 - Connor Mattson

toys = [int(x) for x in input("Enter the total toys and the toys left outside e.g. '7 3' if Sarah has 7 toys but left 3 outside or '0 0' to exit: ").split(' ')]
while toys != [0, 0]:
	three = 1 if (toys[0] - toys[1]) % 2 == 1 and (toys[0] - toys[1]) > 2 else 0
	print(str((toys[0] - toys[1] - 3*three) // 2), "pairs" + " and one group of 3"*three) 
	toys = [int(x) for x in input("Enter the total toys and the toys left outside e.g. '7 3' if Sarah has 7 toys but left 3 outside or '0 0' to exit: ").split(' ')]