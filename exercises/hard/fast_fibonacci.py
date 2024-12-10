'''In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, 
called the Fibonacci sequence, such that each number is the sum of the two preceding ones, 
starting from 0 and 1:

The beginning of the sequence is thus:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

Examples
fib_fast(5) ➞ 5

fib_fast(10) ➞ 55

fib_fast(20) ➞ 6765

fib_fast(50) ➞ 12586269025'''


def fib_fast(num):
        
        try :
             num = int(num)
        except :
             return "Input is not a number"
        
        if num == 0 :
            return 0
        elif num == 1 :
            return 1
        elif num > 1 :
             return fib_fast(num-1) + fib_fast(num-2) 

	
num = input("Enter the number : ")
print(fib_fast(num))