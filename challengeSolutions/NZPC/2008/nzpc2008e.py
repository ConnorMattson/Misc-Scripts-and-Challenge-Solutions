# Problem E 2018 - Connor Mattson

lineInput = input("enter 'libraryName fontWidthInMM' or '# 0' to exit: ").split(' ')
while lineInput != ["#", "0"]:

	books = input("How many books do you want to process? ")
	print(lineInput[0], "Library", "\nEnter 'bookWidthInMM text' eg '200 Hello': ")

	for i in range(int(books)):
		bookInput = input().split(' ')
		
		if len(' '.join(bookInput[1:])) * lineInput[1] + 2 <= int(bookInput[0]):
			print("Book", i + 1, "horizontal")
		else:
			print("Book", i + 1, "vertical")

	lineInput = input("enter 'libraryName fontWidth' or '# 0' to exit: ").split(' ')