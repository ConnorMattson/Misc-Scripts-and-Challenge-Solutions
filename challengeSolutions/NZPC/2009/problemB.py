# Problem B - Connor Mattson

lineInput = input()
while lineInput != '0 0 0 0':
	lineInput = lineInput.split(' ')
	l = int(lineInput[0])
	w = int(lineInput[1])
	h = int(lineInput[2])
	v = int(lineInput[3])
	print(l, w, h, v)

	if v == 0:
		v = int(l*w*h)

	elif l == 0:
		l = int(v/(w*h) )

	elif w == 0:
		w = int(v/(l*h))

	elif h == 0:
		h = int(v/(w*l))

	print(l, w, h, v)
	lineInput = input()