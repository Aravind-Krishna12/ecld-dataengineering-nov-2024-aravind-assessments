#Check whether the squares of the prime factors of a given number divides the number
'''
Given a positive number x:
p = (p1, p2, …)
# Set of *prime* factors of x


If the square of every item in p is also a factor of x, 
then x is said to be a powerful number.

Examples
is_powerful(36) ➞ True
# p = (2, 3) (prime factors of 36)
# 2^2 = 4 (factor of 36)
# 3^2 = 9 (factor of 36)

is_powerful(27) ➞ True

is_powerful(674) ➞ False'''



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

n = int(input("Enter the number : "))
print(is_powerful(n))
			