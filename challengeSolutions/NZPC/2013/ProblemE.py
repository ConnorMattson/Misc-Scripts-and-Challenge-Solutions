#Problem E - Connor Mattson

def calculate():
	global w
	global x
	global y
	global z
	global timesApplied
	w2 = abs(int(w) - int(x))
	x2 = abs(int(x) - int(y))
	y2 = abs(int(y) - int(z))
	z2 = abs(int(z) - int(w))
	w = w2
	x = x2
	y = y2
	z = z2
	timesApplied += 1


def lineInput():
	global w
	global x
	global y
	global z
	global timesApplied
	line = input()
	line = line.split(' ')
	w = line[0]
	x = line[1]
	y = line[2]
	z = line[3]
	timesApplied = 0
	while int(x) + int(y) + int(w) + int(z) != 0:
		calculate()
	if timesApplied != 0:
		print (timesApplied)
		lineInput()

lineInput()