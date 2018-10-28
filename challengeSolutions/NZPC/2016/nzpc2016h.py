# Problem H 2016 - Connor Mattson

mp = {}
code = {'S': 10, 'Q': 5, 'A': 7, 'L': -8, 'F': 4, 'D': -5, 'E': 10}

for i in range(int(input("How many politicians are there? "))):
	data = input("Enter politican ID and name, e.g. '3 Bill Bloggs': ").split(' ')
	mp[data[0]] = [' '.join(data[1:]), 0]

for i in range(int(input("How many scores are there? "))):
	data = input("Enter the politican ID followed by an action e.g. '3 S': ").split(' ')
	mp[data[0]][1] += code[data[1]]

scores = sorted([score[1] for score in mp.values()])
print("The best scores were:", scores[-1], *[mp[idn][0] for idn in sorted(mp.keys()) if mp[idn][1] == scores[-1]])
print("The worst scores were:", scores[0], *[mp[idn][0] for idn in sorted(mp.keys()) if mp[idn][1] == scores[0]])