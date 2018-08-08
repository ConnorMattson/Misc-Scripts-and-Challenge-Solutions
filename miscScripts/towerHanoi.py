
	# Show moves for perfect game

# S = {'1': '1'}
# def solve(x):
# 	for i in range(x+1)[2:]: S[str(i)] = S[str(i-1)] + str(i) + S[str(i-1)]
# 	return (S[str(x)])
# print(solve(int(input())))



	# Minimum moves required for perfect game

# def solve(x):
# 	if x == 1: return 1
# 	else: return (2*solve(x-1)+1)
# print(solve(int(input())))

import builtins; (lambda builtins: (lambda __d, __print, __y: [__print(__d.solve(__d.int(__d.input()))) for __d.solve in [(lambda x:[(lambda __after: 1 if __d.x==1 else ((2*__d.solve((__d.x-1)))+1))(lambda __d: None) for __d.x in [(x)]][0])]][0])(type('StateDict',(),builtins.__dict__)(), builtins.__dict__['print'], (lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args))))))(__import__('builtins'))