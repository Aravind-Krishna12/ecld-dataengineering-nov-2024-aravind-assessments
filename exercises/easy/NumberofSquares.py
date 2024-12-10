#Create a function that calculates the number of different squares in an n * n square grid.
#sum of squares

def numberSquares(n) :
	if n == 0:
		return n
	else :
		return n**2 + numberSquares(n-1) 