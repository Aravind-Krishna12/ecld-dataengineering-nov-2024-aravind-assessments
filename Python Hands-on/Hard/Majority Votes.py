#Check whether the count of unique element is greater than n/2(n - length of the list)

def majority_vote(lst):
      print(lst)
      len_list = len(lst)
      set_list = set(lst)
      a = []
      b = 0
      for item in set_list:
          count = lst.count(item)
          if count > len_list/2:
              return item 
      return None 
  
lst_1 =input("Enter the elements separated by comma : ")
lst  = lst_1.split(",")
print(majority_vote(lst))



#user_list = [int(x) for x in input(&quot;Enter elements separated by space:&quot;).split('')]
#print(user_list)