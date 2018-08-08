f = open('day5Input.txt')
nice = 0
vowelList = ['a','e','i','o','u']

# for line in f:
# 	if 'ab' in line or 'cd' in line or 'pq' in line or 'xy' in line:
# 		pass


# 	else:
# 		vowels = 0
# 		for i in line:
# 			if i in vowelList:
# 				vowels += 1
# 		if vowels > 2:
# 			last = line[0]
# 			check = 0

# 			for i in line[1:]:
# 				if i == last:
# 					check = 1
# 				last = i
# 			if check == 1:
# 				nice += 1

# print('done, number of nice results are:', nice)


for line in f:
	line = line.replace('\n', '')
	twoBack = line[0]
	oneBack = line[1]
	check = 0

	for i in line[2:]:
		if i == twoBack:
			check = 1
			break
		twoBack = oneBack
		oneBack = i

	if check == 1:
		check = 0
		pairList = []
		last = line[0]
		pair = str(last)

		for i in line[1:]:
			pair += str(i)
			pairList.append(pair)
			last = i
			pair = str(last)


		delete = []
		for i in range(len(pairList)):
			if pairList[i] == last:
				delete.append(i-1)
				delete.append(i)
			else:
				last = pairList[i]

		delete = sorted(list(set(delete)))
		counter = 0
		for i in delete:
			pairList.pop(i-counter)
			counter += 1


		pairList = sorted(pairList)
		last = pairList[0]
		for i in pairList[1:]:
			if i == last:
				check = 1
				break
			else:
				last = i

		if check == 1:
			nice += 1

print('done, nice results =', nice)
print('please note this didnt work right, you have to print out each pairlist before and after deleting parts, add 1 to nice for all of the three time occuring pairs that were deleted')
print('(i missed 3, the real nice is 55)')
print('also this would have been way easier if i had just used regex')