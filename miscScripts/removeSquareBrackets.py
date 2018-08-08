fileToOpen = input('Enter file (e.g. D:\\file.txt): ')

fileOpen = open(fileToOpen, 'r+')

for line in fileOpen:
	lineTemp = list(line)
	if '[' in line and ']' in line:
		lineTemp = list(line)
		lineTemp = lineTemp[:lineTemp.index('[')]
		line = ''.join(lineTemp)

	print (line)
