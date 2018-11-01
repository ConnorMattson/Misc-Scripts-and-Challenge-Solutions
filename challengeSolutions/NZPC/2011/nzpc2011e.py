# Problem E 2011 - Connor Mattson

print("Instructions:\nEnter the smallest and largest house number followed by 0 to indicate 0 gaps, e.g. '10 20 0' to supply houses 10-20")
print("In place of 0, insert n for n gaps followed by the smallest and largest house numbers in the gap followed by A (all), E (even) or O (odd)")
print("to indicate which houses in this gap are exempt. e.g. '1 50 1 12 18 E' indicates houses 1-50 with 1 gap exempt, the even houses 12-18")

data = input("\nEnter supply details or '0 0 0' to exit: ").split(' ')
while data != ['0', '0', '0']:
	houses = [x for x in range(int(data.pop(0)), int(data.pop(0)) + 1)]
	del data[0]
	toRemove = []
	while data:
		low = int(data.pop(0))
		high = int(data.pop(0)) + 1
		exemptType = data.pop(0)
		if exemptType == 'A': toRemove = [x for x in range(low, high)]
		else: toRemove = [x for x in range(low, high) if x % 2 == int(exemptType == 'O')]
		if data: del data[0]

	for i in toRemove: houses.remove(i)
	digits = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
	for char in ''.join([str(house) for house in houses]): digits[char] = digits[char] + 1
	print(*[digits[str(char)] for char in range(0,10)])
	data = input("\nEnter supply details or '0 0 0' to exit: ").split(' ')