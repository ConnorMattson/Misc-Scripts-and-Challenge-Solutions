#Problem J - Connor Mattson



def runProblem():
	whcs = input()
	whcs = whcs.split(' ')
	w = whcs[0]
	h = whcs[1]
	c = whcs[2]
	s = whcs[3]
	for _ in range(int(s)):
		whp = input()
		whp = whp.split(' ')
		w = whp[0]
		h = whp[1]
		p = whp[2]
		

numberOfProblems = input()
for _ in range(int(numberOfProblems)):
	runProblem()