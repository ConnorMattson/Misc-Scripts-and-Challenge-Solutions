import codecs

f = open('day8Input.txt')
total = 0
totalInQuotes = 0

for line in f:
	line = line.replace('\n','')
	inQuotes = line[1:len(line)-1]

	# inQuotes = inQuotes.replace('\\"', '"')
	# inQuotes = inQuotes.replace(r"""\\x""", '\\a')
	# inQuotes = inQuotes.replace(r"""\\""", '\\')

	# if r'\x' in inQuotes:
	# 	totalInQuotes += len(inQuotes)-4
	# else:
	# 	totalInQuotes += len(inQuotes)

	# while '\\x' in inQuotes:
	# 	inQuotes = eval(inQuotes)
	# 	print(inQuotes)
	# 	pos = inQuotes.index('\\x')
	# 	asciiLetter = inQuotes[pos+2:pos+4]
	# 	print(asciiLetter)
	# 	asciiLetter = int(asciiLetter, 16)

	# 	inQuotes = list(inQuotes)
	# 	del inQuotes[pos]
	# 	del inQuotes[pos]
	# 	del inQuotes[pos]
	# 	inQuotes[pos] = (chr(int(asciiLetter)))

	# 	print(inQuotes)
	# 	for i in inQuotes:
	# 		totalInQuotes += 1

	# else:
	# 	totalInQuotes += len(inQuotes)

	total += len(line)
	print(eval(line))
	print(len(eval(line)))
	totalInQuotes += line.count('\\') + line.count('"') + 2



print(total)
print(totalInQuotes)