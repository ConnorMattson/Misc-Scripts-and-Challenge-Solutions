# Problem K - Connor Mattson

def getValues(widthIn, heightIn):
	for i in range(heightIn):
		lineInput = input().split(' ')

firstLineInput = input()
while firstLineInput != '0 0 0 0':
	firstLineInput = firstLineInput.split(' ')
	widthIn = int(firstLineInput[0])
	heightIn = int(firstLineInput[1])
	widthOut = int(firstLineInput[2])
	heightOut = int(firstLineInput[3])

	getValues(widthIn, heightIn)

	firstLineInput = input()
