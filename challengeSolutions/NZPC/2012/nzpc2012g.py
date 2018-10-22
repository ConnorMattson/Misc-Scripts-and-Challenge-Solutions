# Problem G 2012 - Connor Mattson

print("Colour codes:\nB = Blue    K = Black    N = Brown\nO = Orange  P = Purple   R = Red\nW = White\n")

n = int(input("How many shirts does the wife have? (or 0 to exit) "))
while n != 0:
	clothes = []
	
	for i in range(n): clothes.append(input("Enter shirt {}'s size (S, M, or L) and colour e.g. 'SB' for small blue: ".format(i + 1)))
	n = int(input("How many shirts does the husband have? "))
	for i in range(n): clothes.append(input("Enter shirt {}'s size (S, M, or L) and colour e.g. 'SB' for small blue: ".format(i + 1)))

	sizeOrdering = ['S', 'M', 'L']
	print(sorted(clothes, key=lambda x: (sizeOrdering.index(x[0]), x[1])))
	n = int(input("How many shirts does the wife have? (or 0 to exit) "))