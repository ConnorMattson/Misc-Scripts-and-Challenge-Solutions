mp = {}
code = {'S': 10, 'Q': 5, 'A': 7, 'L': -8, 'F': 4, 'D': -5, 'E': 10}

ids = int(input())
for i in range(ids):
	data = input().split(' ')
	name = ' '.join(data[1:])
	mp[data[0]] = [name, 0]

for i in range(int(input())):
	data = input().split(' ')
	mp[data[0]][1] += code[data[1]]

scores = []
for i in range(ids):
	scores.append(mp[str(i+1)][1])

best = sorted(scores)[-1]
worst = sorted(scores)[0]
output1 = str(best)
output2 = str(worst)

for i in range(ids):
	if mp[str(i+1)][1] == best:
		output1 += ' ' + mp[str(i+1)][0]
	if mp[str(i+1)][1] == worst:
		output2 += ' ' + mp[str(i+1)][0]

print(output1)
print(output2)