# Problem G - Team 19

graphs = int(input())
for i in range(graphs):
	data = input().split(' ')
	dataPoints = []
	
	for i in range(10):
		i += 1
		dataPoints.append((int(data[0]) * i) + int(data[1]))
	
	graph = []
	for i in range(dataPoints[-1] + 1):
		graph.append('*')
	
	
	counter = 0
	for i in dataPoints:
		if counter != 0:
			graph[(dataPoints[-1]) - i] = ('*' + counter*' ' + '*')
		else:
			graph[(dataPoints[-1]) - i] = ('*' + '*')
		counter += 1
	
	if int(data[0]) == 0:
		print(data[1])
		graph[(dataPoints[-1]) - int(data[1])] = '***********'
	
	graph[-1] = '***********'
	
	
	print('y = ' + data[0] + 'x + ' + data[1])
	for i in graph:
		print(i)