# Problem A - Connor Mattson

def solveProblem():
	global problem
	problem = problem.split(' ')
	if int(problem[1]) % int(problem[0]) == 0:
		return 'factor'
	elif int(problem[0]) % int(problem[1]) == 0:
		return 'multiple'
	else:
		return 'neither'


problem = input()
while problem != '0 0':
	print(solveProblem())
	problem = input()