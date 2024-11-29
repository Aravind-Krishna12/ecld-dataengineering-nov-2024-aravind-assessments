#Check whether the count of unique element is greater than n/2(n - length of the list)

'''Examples
majority_vote(["A", "A", "B"]) ➞ "A"

majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A"

majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None'''

def majority_vote(lst):
      print(lst)
      len_list = len(lst)
      set_list = set(lst)
      for item in set_list:
          count = lst.count(item)
          if count > len_list/2:
              return item 
      return None 
  
lst_1 =input("Enter the elements separated by comma : ")
lst  = lst_1.split(",")
print(majority_vote(lst))

