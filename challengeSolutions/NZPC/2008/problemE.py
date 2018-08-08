# Problem E - Connor Mattson

lineInput = input()
while lineInput != '# 0':

	lineInput = lineInput.split(' ')
	fontWidth = int(lineInput[1])
	books = input()
	counter = 1

	print(lineInput[0], 'Library')

	for i in range(int(books)):
		bookInput = input()
		bookInput = bookInput.split(' ')
		
		if len(bookInput[1])*fontWidth+2 <= int(bookInput[0]):
			print('Book', counter, 'horizontal')
		else:
			print('Book', counter, 'vertical')
		counter += 1



	lineInput = input()