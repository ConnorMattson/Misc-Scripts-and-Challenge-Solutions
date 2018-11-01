# Problem E 2018 - Connor Mattson

contestants = {}
for i in range(int(input("How many contestants are entering? "))): contestants[input("Enter the name of contestant {}: ".format(i + 1))] = [0,0,0]
for i in range(len(contestants)*3):
	data = input("Enter the contestant name, the meal type (E, M, or D) and the score e.g. 'Harry M 9': ").split(' ')
	contestants[data[0]][['E','M','D'].index(data[1])] = int(data[2])
	
bonus = ['E','M','D'].index(input("Which round is the bonus round E, M, or D? "))
bonusWinner = [x for x in contestants if contestants[x][bonus] == max([b[bonus] for b in contestants.values()])][0]
for i in contestants: contestants[i] = sum(contestants[i]) + 5*(i == bonusWinner)

print([x for x in contestants if contestants[x] == max(contestants.values())][0], "gets immunity.")
print([x for x in contestants if contestants[x] == min(contestants.values())][0], "goes home.")