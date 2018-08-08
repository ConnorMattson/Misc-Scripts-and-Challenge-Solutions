f = open('day2Input.txt')
total = 0
totalRibbon = 0

for line in f:
	line = line.split('x')
	l = int(line[0])
	w = int(line[1])
	h = int(line[2])

	totalForPresent = (2*l*w) + (2*w*h) + (2*h*l)
	ordered = sorted([l, w, h])
	totalForPresent += ordered[0]*ordered[1]
	print(totalForPresent)
	total += totalForPresent

	totalRibbonForPresent = 2*ordered[0] + 2*ordered[1]
	totalRibbonForPresent += l*w*h
	print(totalRibbonForPresent)
	totalRibbon += totalRibbonForPresent


print('total size is:', total)
print('total ribbon is:', totalRibbon)