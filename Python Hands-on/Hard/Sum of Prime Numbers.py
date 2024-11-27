#Find the sum of prime numbers in the given list



def sum_primes(lst):
	lst2=[]
	if lst == [] :
		return None
	else :
		for i in lst :
			lst1=[]
			for j in range(1,i+1):
				if i%j == 0 :
					lst1.append(j)
			if len(lst1) == 2 :
				lst2.append(i)
	return sum(lst2[0:len(lst2)])
					
		
