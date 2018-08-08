#Problem E - Connor Mattson

weekNumber = 0
n = 1
name = []
demerits = []
banned = []

def week():
	global weekNumber
	global n
	weekNumber += 1
	banned = []
	bannedStr = ''
	name = []
	demerits = []
	for _ in range(int(n)):
		x = input()
		x = x.split(' ')
		if x[1] == 'FD':
			x[1] = 10
		else:
			if x[1] == 'FB':
				x[1] = 25
			else:
				if x[1] == 'PH':
					x[1] = 40
				else:
					if x[1] == 'TK':
						x[1] = 15
					else:
						if x[1] == 'CP':
							x[1] = 30
						else:
							if x[1] == 'DM':
								x[1] = 50
							else:
								x[1] = 20
		nameCounter = 0
		if len(name) != 0:
			while nameCounter != len(name):
				if name[nameCounter] == x[0]:
					demerits[nameCounter] = int(x[1]) + int(demerits[nameCounter])
					nameCounter = len(name)
					nameFound = 1
				else:
					nameCounter += 1
					nameFound = 0
			if nameFound == 0:
				name.append(x[0])
				demerits.append(x[1])
		else:
			name.append(x[0])
			demerits.append(x[1])
	demeritCounter = 0		
	while demeritCounter != int(len(demerits)):
		if int(demerits[demeritCounter]) == 50 or int(demerits[demeritCounter]) > 50:
			banned.append(name[demeritCounter])
			demeritCounter += 1
		else:
			demeritCounter += 1
	if len(banned) == 0:
		print ('Week ' + str(weekNumber) + ' No pupils banned')
	else:
		bannedStr = ' '.join(banned)
		print ('Week ' + str(weekNumber) +  ' ' + bannedStr)

while n != 0:
	n = input()
	if n == '0':
		break
	else:
		week()