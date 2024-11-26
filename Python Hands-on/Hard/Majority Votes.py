def majority_vote(lst):
      len_list = len(lst)
      set_list = set(lst)
      a = []
      b = 0
      for item in set_list:
          count = lst.count(item)
          if count > len_list/2:
              return item 
      return None   