def interview(lst, tot):
    if len(lst) == 8:
        if (lst[0]>5 and lst[1] > 5):
            return "disqualified"  
        elif (lst[2]>10 and lst[3] > 10):
            return "disqualified"  
        elif (lst[4]>15 and lst[5] > 15):
            return "disqualified"  
        elif (lst[6]>20 and lst[7] > 20):
            return "disqualified"  
        elif tot > 120:
            return "disqualified"
        else:  
            return "qualified" 
    else:
        return "disqualified"