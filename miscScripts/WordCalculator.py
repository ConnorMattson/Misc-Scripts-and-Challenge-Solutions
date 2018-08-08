# TODO:
# Fix and problem
# Fix hundreds etc.

wordList = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "zero": 0, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19}
operationList = {'plus': '+', 'minus': '-', 'times': '*', 'divided by': '/', 'divided': '/', 'divide': '/'}
wordListTens = {'twenty': 20, 'thirty': 30, 'fourty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90}
wordListTensExtra = {'twenty': 2, 'thirty': 3, 'fourty': 4, 'fifty': 5, 'sixty': 6, 'seventy': 7, 'eighty': 8, 'ninety': 9}
wordListHundreds = {'hundred': "00", 'thousand': "000", 'million': "000000", 'billion': "000000000", 'trillion': "000000000000"}
wordListHundredsExtra = {'hundred': "0", 'thousand': "00", 'million': "00000", 'billion': "00000000", 'trillion': "00000000000"}
wordListHundredsExtra2 = {'hundred': "", 'thousand': "0", 'million': "0000", 'billion': "0000000", 'trillion': "0000000000"}

def calculate():
	global problem
	global wordList
	for i in problem:

		if i in wordList:
			problem[problem.index(i)] = str(wordList[i])

		elif i in wordListTens:
			try:
				if problem[problem.index(i) + 1] in wordList:
					problem[problem.index(i)] = str(wordListTensExtra[i])
				else:
					problem[problem.index(i)] = str(wordListTens[i])
			except:
				problem[problem.index(i)] = str(wordListTens[i])
		
		elif i in operationList:
			problem[problem.index(i)] = str(operationList[i])			

		# elif i == 'and':
		# 	problem[problem.index(i)] = ''

		elif i in wordListHundreds:
			try:
				if problem[problem.index(i) + 1] in wordList:
					problem[problem.index(i)] = str(wordListHundredsExtra[i])
				elif problem[problem.index(i) + 1] in wordListTens:
					problem[problem.index(i)] = str(wordListHundredsExtra2[i])
				else:
					problem[problem.index(i)] = str(wordListHundreds[i])
			except:
				problem[problem.index(i)] = str(wordListHundreds[i])

	print(problem)
	problem = "".join(problem)
	print(eval(problem))





problem = input().lower().split(' ')
while problem != '#':
	while 'and' in problem:
		del(problem[problem.index('and')])

	calculate()
	problem = input().lower().split(' ')