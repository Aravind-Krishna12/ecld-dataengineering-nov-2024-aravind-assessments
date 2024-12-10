'''Create a function that sums up all the elements in the list recursively. 
The use of the sum() built-in function is not allowed, thus, the approach is recursive.

Examples
recur_add([1, 2, 3, 4, 10, 11]) ➞ 31

recur_add([-3, 4, 11, 10, 21, 32, -9]) ➞ 66

recur_add([-21, -7, 19, 3, 4, -8]) ➞ -10'''


import ast
def recur_add(data):

  if not data:  
    return 0
  else:
    return data[0] + recur_add(data[1:]) 


input_str = input("Enter the list : ")
try:
  data = ast.literal_eval(input_str) 
  print("Sum of elements:", recur_add(data))
except ValueError:
  print("Invalid input")



