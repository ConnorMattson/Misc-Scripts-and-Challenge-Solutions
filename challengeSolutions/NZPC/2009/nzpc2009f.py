# Problem F 2009 - Connor Mattson

data = input("Enter a line of code to check bracket nesting or '#' to exit: ")
while data != "#":
	data = [x for x in list(data) if x in ['(', ')', '{', '}', '[', ']']]
	brackets = []
	try:
		for i in data:
			if i in [')', '}', ']'] and brackets[-1] == ['(', '{', '['][[')', '}', ']'].index(i)]: brackets.pop()
			else: brackets.append(i)
		print("Illegal" if brackets else "Legal")
		print(brackets)
	except: print("Illegal")

	data = input("Enter a line of code to check bracket nesting or '#' to exit: ")