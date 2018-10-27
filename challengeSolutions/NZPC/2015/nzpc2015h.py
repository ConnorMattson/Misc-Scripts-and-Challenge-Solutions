# Problem H 2015 - Connor Mattson

problems = int(input("How many problems does this competition have? (or '0' to exit): "))
while problems != 0:
	points = [int(x) for x in input("How many points is each question worth? e.g. '1 1 3 5 10': ").split(' ')]
	
	teams = {}
	for i in range(int(input("How many teams competed? "))):
		teamData = input("""Enter the team name, followed by the number of submissions and minutes after which a successful submission was made, seperated with '/'
if no submission is successful, enter '-' in place of the minutes e.g. \"Connor's team,0/-,4/-,10/-\": """).split(',')
		teamPoints = sum([a*b for a,b in zip([1 if '-' not in x else 0 for x in teamData[1:]], points)])
		teams[teamPoints] = teams[teamPoints] + [teamData[0]] if teamPoints in teams else [teamData[0]]
		
	for i in range(len(teams)):
		for team in sorted(teams[sorted(teams.keys(), reverse=True)[i]]):
			print(str(i + 1), team, sorted(teams.keys(), reverse=True)[i])

	problems = int(input("How many problems does this competition have? (or '0' to exit): "))