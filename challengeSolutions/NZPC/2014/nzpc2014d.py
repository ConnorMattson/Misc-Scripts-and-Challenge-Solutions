#Problem D - Connor Mattson

imageWidth, imageLines = [int(x) for x in input("Enter the width and number of lines of the image e.g. '20 22' or '0 0' to exit: ").split(' ')]
imageNum = 1

while (imageWidth != 0 or imageLines != 0):
	image = []
	for line in range(imageLines):
		image.append(list(input("Enter line {}: ".format(line + 1))))

	message = "Image {}:\n".format(imageNum)
	for line in image:
		symbol = ['.', 'X']
		for i in line:
			if i != "_": message += int(i)*symbol[0]
			symbol = symbol[::-1]
		message += "\n"

	print(message)
	imageNum += 1
	imageWidth, imageLines = [int(x) for x in input("Enter the width and number of lines of the image e.g. '20 22' or '0 0' to exit: ").split(' ')]