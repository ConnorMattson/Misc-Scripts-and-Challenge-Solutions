grid = [[0]*1000 for i in range(1000)]

f = open('day6Input.txt')


for line in f:
	if line[6] == 'f':
		operation = 1
		coords = line[9:].split(' through ')
	elif line[6] == 'n':
		operation = 2
		coords = line[8:].split(' through ')
	else:
		operation = 3
		coords = line[7:].split(' through ')



	start = coords[0].split(',')
	end = coords[1].replace('\n', '').split(',')



	if operation == 2:
		for i in range(int(end[0])-int(start[0])+1):
			for j in range(int(end[1])-int(start[1])+1):
				grid[i+int(start[0])][j+int(start[1])] += 1

	if operation == 1:
		for i in range(int(end[0])-int(start[0])+1):
			for j in range(int(end[1])-int(start[1])+1):
				grid[i+int(start[0])][j+int(start[1])] -= 1
				if grid[i+int(start[0])][j+int(start[1])] == -1:
					grid[i+int(start[0])][j+int(start[1])] = 0

	if operation == 3:
		for i in range(int(end[0])-int(start[0])+1):
			for j in range(int(end[1])-int(start[1])+1):
				# change += 2 to -= 1 for first part
				grid[i+int(start[0])][j+int(start[1])] += 2
				if grid[i+int(start[0])][j+int(start[1])] == -1:
					grid[i+int(start[0])][j+int(start[1])] = 1

print(sum(map(sum, grid)))