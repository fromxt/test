
def conflict(state, nextX):
	'''nextY is the vertical position (y coordinate, or row) of the next queen
	   nextX is the the suggested horizontal position (x coordinate, or column) of the next queen
	'''
	nextY = len(state)
	for i in range(nextY):
		'''It is true if the horizontal distance between the next queen 
		   and the previous one under consideration is either zero (same column) 
		   or equal to the vertical distance (on a diagonal). Otherwise, it is false.
		'''
		if abs(state[i] - nextX) in (0, nextY - i):
			return True
	return False

def queens(num, state =()):
	'''
	The num parameter is the number of queens in total, 
	The state parameter is the tuple of positions for the previous queens
	The pos parameter is the the horizonta positions (column)for the num queen
	'''
	if len(state) == num-1:
		for pos in range(num):
			if not conflict(state, pos):
				yield (pos,)
	else:
		for pos in range(num):
			if not conflict(state, pos):
				for result in queens(num, state + (pos,)):
					yield (pos,) + result

def prettyprint(solution):
        def line(pos, length=len(solution)):
                return '. ' * (pos) + 'X ' + '. ' * (length-pos-1)
        for pos in solution:
                print(line(pos))

for solution in queens(8):
	print("{}".format(solution))
	print("Drawing as following")
	prettyprint(solution)
