#Problem E - Connor Mattson

#1 Every opening tag has to have a corresponding closing tag
#2 All tags must be properly nested.

#get input
#find all tags
#check that tags are nested properly
#see which opening tags do not have a closing tag

def checkIfCorrect(lineInput):
	splitLineInput = list(lineInput)
	tagsFound = []

	for i in splitLineInput:
		tempArray = []
		if i == '<':
			indexOfSmallerThan = splitLineInput.index('<')
			try:
				indexOfGreaterThan = splitLineInput.index('>') + 1
			except:
				return 'illegal1'
			
			for j in splitLineInput[indexOfSmallerThan:indexOfGreaterThan]:
				tempArray.append(j)
			tempArray = ''.join(tempArray)
			tagsFound.append(tempArray)
			splitLineInput = splitLineInput[indexOfGreaterThan:]

	tagList = []
	lastTagOpened = []

	def removeExtraCode(i):
			try:
				splitTag = list(i)
				del splitTag[splitTag.index(' '):splitTag.index('>')]
				splitTag = ''.join(splitTag)
				tagsFound[tagsFound.index(i)] = splitTag
			except:
				pass


	for i in tagsFound:
		closingTag = list(i)
		try:

			if closingTag.index('/') > 1:
				pass
				#Tag that does not need to be closed
			else:

				removeExtraCode(i)
				closingTag = list(i)
				closingTag.remove('/')
				closingTag = ''.join(closingTag)
				print(closingTag)
				print(lastTagOpened[len(lastTagOpened)-1])
				if lastTagOpened[len(lastTagOpened)-1] == closingTag:
					if closingTag in tagList:
						print(i)
						print(closingTag)
						print('stop')
						tagList.remove(closingTag)
						del lastTagOpened[len(lastTagOpened)-1]
					else:
						return 'illegal2'
				else:
					return 'illegal3'

		except:
			removeExtraCode(i)
			tagList.append(i)
			lastTagOpened.append(i)

	if len(tagList) != 0:
		print(tagList)
		return 'illegal4'
	else:
		return 'legal'	

lineInput = input()
while lineInput != '#':
	print(checkIfCorrect(lineInput))
	lineInput = input()