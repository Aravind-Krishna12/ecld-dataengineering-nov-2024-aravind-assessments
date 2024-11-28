'''Given a positive number x, if all the positive divisors of x (excluding x) add up to x, 
then x is said to be a perfect number.
Given a positive number x, if all the positive divisors of x add up to a second number y, 
and all the positive divisors of y add up to x, then x and y are said to be a pair of amicable numbers.'''

def num_type(n):
	def sum_div(num):
		lst = []
		for i in range(1,num) :
			if num%i == 0:
				lst.append(i)
		return sum(lst)
	s = sum_div(n)
	if s == n:
		return "Perfect"
	elif sum_div(s)==n :
		return "Amicable"
	else :
		return "Neither"