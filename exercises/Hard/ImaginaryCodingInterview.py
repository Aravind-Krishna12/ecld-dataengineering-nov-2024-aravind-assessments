#Check whether the elements in the list  pass certain condition and also the second argument (total minute) is less than 120


def interview(lst, tot):
    if len(lst) == 8:
        if (lst[0]>5 or lst[1] > 5):
            return "disqualified"  
        elif (lst[2]>10 or lst[3] > 10):
            return "disqualified"  
        elif (lst[4]>15 or lst[5] > 15):
            return "disqualified"  
        elif (lst[6]>20 or lst[7] > 20):
            return "disqualified"  
        elif tot > 120:
            return "disqualified"
        else:  
            return "qualified" 
    else:
        return "disqualified"
    
