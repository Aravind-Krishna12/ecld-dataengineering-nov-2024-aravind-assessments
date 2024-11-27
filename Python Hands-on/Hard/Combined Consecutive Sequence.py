#Combine two lists and Check whether all the elements in sorted list are consecutive numbers

def consecutive_combo(lst1, lst2):
    lst3 = lst1 + lst2
    lst3.sort() 
    b = True
    for i in range(0, len(lst3) - 1):  
        if lst3[i] != lst3[i + 1] - 1:  
            b = False
            break 
    return b