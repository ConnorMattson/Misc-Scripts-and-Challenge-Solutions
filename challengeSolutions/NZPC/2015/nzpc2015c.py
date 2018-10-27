# Problem C 2015 - Connor Mattson

name = input("Enter the name of the creature, or '#' to exit: ")
while name != '#':
	base = int(input("Enter the number of appendages the creature has: "))
	decimal = int(input("Enter a decimal number: "))

	def convert(decimal, base, converted=[]):
		return ''.join(converted[::-1]) if decimal == 0 else convert(decimal // base, base, converted + [str(decimal % base) if decimal % base < 10 else chr(55 + decimal % base)])

	def convertTidy(decimal, base, converted=[]):
		# convert() isnt very efficient or easy to read, I just thought it was cool that I could do it in two lines so I left it in
		if decimal == 0: return ''.join(converted[::-1])
		else:
			nextDigit = decimal % base
			converted + [str(nextDigit) if nextDigit < 10 else chr(55 + nextDigit)]
			return convertTidy(decimal, base, converted)

	print("A {} would say {} as {}".format(name, decimal, convertTidy(decimal, base)))
	name = input("Enter the name of the creature, or '#' to exit: ")