# Problem F 2016 - Connor Mattson

letters = []
for i in range(int(input("How many lines are to be entered? "))):
	sentence = list(input("Enter line {}: ".format(i + 1)))
	letters.extend(sorted(set([x for x in sentence if x not in letters and x != ' ']), key=sentence.index))
print(''.join(letters))