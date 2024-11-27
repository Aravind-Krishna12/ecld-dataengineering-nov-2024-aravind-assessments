#Check whether the squares of the prime factors of a given number divides the number

def is_powerful(n):
	number = n
	factors = []
	d = 2
	b=0
	while (n>=d):
		if n%d == 0 :
			factors.append(d)
			n=n/d
		else :
			d+=1
	set_factors = set(factors)
	for i in set_factors:
		if number%(i**2) == 0 :
			b+=1
		
	return True if len(set_factors)==b else False
			