'''Given a positive number x, if all the positive divisors of x (excluding x) add up to x, 
then x is said to be a perfect number.
Given a positive number x, if all the positive divisors of x add up to a second number y, 
and all the positive divisors of y add up to x, then x and y are said to be a pair of amicable numbers.

Examples
num_type(6) ➞ "Perfect"

num_type(2924) ➞ "Amicable"

num_type(5010) ➞ "Neither"
'''

def num_type(n):
		try:
			n=int(n)
		except:
			return "Only number is allowed"
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

	
n=input("Enter the number : ")
print(num_type(n))