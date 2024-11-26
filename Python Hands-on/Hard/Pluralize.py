def pluralize(lst):
    set_lst = set()  
    for i in lst:
        tot = lst.count(i)
        if tot > 1:
            set_lst.add(i + "s")  
        else:
            set_lst.add(i)  
    return set_lst  