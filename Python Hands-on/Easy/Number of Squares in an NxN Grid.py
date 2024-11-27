def numberSquares(n) :
	if n == 0:
		return n
	else :
		return n**2 + numberSquares(n-1) 