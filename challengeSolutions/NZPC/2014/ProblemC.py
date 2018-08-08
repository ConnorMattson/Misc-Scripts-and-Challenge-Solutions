#Problem C - Connor Mattson

lineNumber = input()
lineCount = 0

def count():
	line = input()
	line = line.split(" ")

	s = line[0]
	f = line[1]
	c = line[2]
	global lineCount
	while int(s) <= int(f):
		s2 = len(s)
		if s2 == 1:
			if s[0] == c:
				lineCount += 1
			else:
				pass
		else:
			pass
		if s2 == 2:
			if s[0] == c:
				lineCount += 1
			else:
				pass
			if s[1] == c:
				lineCount += 1
			else:
				pass
		else:
			pass
		if s2 == 3:
			if s[0] == c:
				lineCount += 1
			else:
				pass
			if s[1] == c:
				lineCount += 1
			else:
				pass
			if s[2] == c:
				lineCount += 1
			else:
				pass
		else:
			pass
		if s2 == 4:
			if s[0] == c:
				lineCount += 1
			else:
				pass
			if s[1] == c:
				lineCount += 1
			else:
				pass
			if s[2] == c:
				lineCount += 1
			else:
				pass
			if s[3] == c:
				lineCount += 1
			else:
				pass
		else:
			pass
		if s2 == 5:
			if s[0] == c:
				lineCount += 1
			else:
				pass
			if s[1] == c:
				lineCount += 1
			else:
				pass
			if s[2] == c:
				lineCount += 1
			else:
				pass
			if s[3] == c:
				lineCount += 1
			else:
				pass
			if s[4] == c:
				lineCount += 1
			else:
				pass
		else:
			pass
		
		s = int(s)
		s += 1
		s = str(s)

for _ in range(int(lineNumber)):
    count()
    print(lineCount)
    lineCount = 0