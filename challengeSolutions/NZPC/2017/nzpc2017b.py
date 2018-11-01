# Problem B 2017 - Connor Mattson

scores = [[input("Enter the name of team one: "), 0], [input("Enter the name of team two: "), 0]]
print("S - a shot that misses.\nH - a shot that goes in the hoop.\nD - a shot goes in for two points.\nO - a shot that scores for the opponent.")
data = list(input("Enter the results, e.g. 'SSSHSDOSSH': "))
for i in range(len(data)): 
	if data[i] == 'O': scores[i % 2 == 0][1] += 1
	elif data[i] != 'S': scores[i % 2 == 1][1] += 1 + (data[i] == 'D')

print(scores[0][0], min(scores[0][1], 7), scores[1][0], str(min(scores[1][1], 7)) + ".", scores[scores[1][1] > scores[0][1]][0] + " is winning."*(scores[scores[1][1] > scores[0][1]][1] <= 6) + " has won."*(scores[scores[1][1] > scores[0][1]][1] >= 7))