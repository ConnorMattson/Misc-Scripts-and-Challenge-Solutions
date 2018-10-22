#Problem E 2012 - Connor Mattson

import re

data = input("Enter the HTML: ")
while data != '#':
	stack = []
	foundError = False

	for tag in re.findall("<[^>]*>", data):
		tag = re.sub("\\w+=\"[^\"]*\"", '', tag)
		tag = re.sub("[\\s<>]", '', tag)

		if '/' not in tag: stack.append(tag)
		elif tag[0] == '/' and stack[-1] == tag[1:]: stack.pop()
		elif tag[-1] != '/': 
			foundError = True
			break

	print("Illegal" if foundError or stack else "Legal")
	data = input("Enter the HTML: ")