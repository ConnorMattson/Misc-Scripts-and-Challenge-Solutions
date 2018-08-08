# inputs:
# 	collumns and rows
# 	width of the lines to draw
# 	number of points connected by a line:
# 		x index
# 		y index

# output:
# 	blank line
# 	each line start and finish with '|'

def runScenario():
	initialInput = input().split(' ')
	
	for i in range(int(initialInput[1])):
		graph.append([])

		for j in range(int(initialInput[0])):
			graph[i].append(' ')

		graph[i][0] = '|'
		graph[i][len(graph[i])-1] = '|'
		
	width = int(initialInput[2])
	pointsToLink = int(initialInput[3])
	x = []
	y = []

	for i in range(pointsToLink):
		coordinates = input().split(' ')
		x.append(int(coordinates[0]))
		y.append(int(coordinates[1]))
		
		graph[y[len(y)-1]][x[len(x)-1]] = '@'

		if len(x) > 1:
			
			if x[len(x)-1] > x[len(x)-2]:
				print('line goes right')
			
			if x[len(x)-1] < x[len(x)-2]:
				print('line goes left')

			if y[len(y)-1] > y[len(y)-2]:
				print('line goes down')

			if y[len(y)-1] < y[len(y)-2]:
				print('line goes up')








	for i in range(int(initialInput[1])):
		print(graph[i])


scenariosToRun = input()
for i in range(int(scenariosToRun)):
	graph = []
	runScenario()
	print()

