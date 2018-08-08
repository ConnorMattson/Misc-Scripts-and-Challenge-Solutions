f = open("day7Input.txt")
data = []
dataPairs = []
unfinishedData = []

for line in f:
	unfinishedData.append(line)

while len(unfinishedData) != 0:
	unfinishedDataNew = []
	breakCheck = 0

	for line in unfinishedData:
		print(line)

		if 'AND' in line:
			dataInput = line.split(' -> ')
			final = dataInput[1].replace('\n','')
			numbers = dataInput[0].split(' AND ')
			try:
				output = int(dataPairs[data.index(numbers[0])]) & int(dataPairs[data.index(numbers[1])])
			except ValueError:
					unfinishedDataNew.append(line)
					breakCheck = 1

			if breakCheck == 0:
				if final in data:
					dataPairs[data.index(final)] = output
				else:
					data.append(str(final))
					dataPairs.append(output)


		elif 'OR' in line:
			dataInput = line.split(' -> ')
			final = dataInput[1].replace('\n','')
			numbers = dataInput[0].split(' OR ')
			try:
				output = int(dataPairs[data.index(numbers[0])]) | int(dataPairs[data.index(numbers[1])])
			except ValueError:
					unfinishedDataNew.append(line)
					breakCheck = 1

			if breakCheck == 0:
				if final in data:
					dataPairs[data.index(final)] = output
				else:
					data.append(str(final))
					dataPairs.append(output)

		elif 'LSHIFT' in line:
			dataInput = line.split(' -> ')
			final = dataInput[1].replace('\n','')
			numbers = dataInput[0].split(' LSHIFT ')
			try:
				output = int(dataPairs[data.index(numbers[0])]) << int(numbers[1])
			except ValueError:
					unfinishedDataNew.append(line)
					breakCheck = 1

			if breakCheck == 0:
				if final in data:
					dataPairs[data.index(final)] = output
				else:
					data.append(str(final))
					dataPairs.append(output)

		elif 'RSHIFT' in line:
			dataInput = line.split(' -> ')
			final = dataInput[1].replace('\n','')
			numbers = dataInput[0].split(' RSHIFT ')
			try:
				output = int(dataPairs[data.index(numbers[0])]) >> int(numbers[1])
			except ValueError:
					unfinishedDataNew.append(line)
					breakCheck = 1

			if breakCheck == 0:
				if final in data:
					dataPairs[data.index(final)] = output
				else:
					data.append(str(final))
					dataPairs.append(output)

		elif 'NOT' in line:
			dataInput = line.split(' -> ')
			final = dataInput[1].replace('\n','')
			numbers = dataInput[0].replace('NOT ', '')
			try:
				output = ~ int(dataPairs[data.index(numbers)])
				output = int(str(output)[1:]) - 1
			except ValueError:
					unfinishedDataNew.append(line)
					breakCheck = 1

			if breakCheck == 0:
				if final in data:
					dataPairs[data.index(final)] = output
				else:
					data.append(str(final))
					dataPairs.append(output)


		# Handles '->' command
		else:
			dataInput = line.split(' -> ')
			dataInput[1] = dataInput[1].replace('\n','')


			try:
				dataInput[0] = (int(dataInput[0]))
			except:
				try:
					dataInput[0] = dataPairs[data.index(dataInput[0])]
				except ValueError:
					unfinishedDataNew.append(line)
					breakCheck = 1

			if breakCheck == 0:
				if dataInput[1] in data:
					dataPairs[data.index(dataInput[1])] = dataInput[0]
				else:
					data.append(str(dataInput[1]))
					dataPairs.append(dataInput[0])

	unfinishedData = unfinishedDataNew



# print(int(dataPairs[data.index('f')]))

print(data)
print(dataPairs)


