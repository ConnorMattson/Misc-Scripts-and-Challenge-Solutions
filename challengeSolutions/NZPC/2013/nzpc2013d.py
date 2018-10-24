#Problem D 2013 - Connor Mattson

data = int(input("Enter a number: "))
while data != 0:
	print("Represented in binary, {} has {} digits, {} of which are ones.".format(data, len(bin(data)) - 2, list(bin(data))[2:].count('1')))
	data = int(input("Enter a number: "))