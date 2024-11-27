#Check whether an element in a list occurs more than once ,then return a set with plurals for those and singular for the others


def pluralize(lst):
    set_lst = set()  
    for i in lst:
        tot = lst.count(i)
        if tot > 1:
            set_lst.add(i + "s")  
        else:
            set_lst.add(i)  
    return set_lst  