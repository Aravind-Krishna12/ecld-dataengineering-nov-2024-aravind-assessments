'''Create a function that returns the characters from a list or string r on odd or even positions, 
depending on the specifier s. The specifier will be "odd" for items on odd positions (1, 3, 5, ...) and 
"even" for items on even positions (2, 4, 6, ...).

char_at_pos([2, 4, 6, 8, 10], "even") ➞ [4, 8]
# 4 & 8 occupy the 2nd & 4th positions

char_at_pos("EDABIT", "odd") ➞ "EAI"
# "E", "A" and "I" occupy the 1st, 3rd and 5th positions

char_at_pos(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "odd") ➞ ["A", "B", "T", "A", "I", "Y"]'''

import ast
def char_at_pos(r, s):
    s= s.lower()
    a = []
    if type(r) == list:
        if s == "even":
            for i in range(len(r)):
                if (i + 1) % 2 == 0:
                    a.append(r[i])
            return a
        elif s == "odd":
            for i in range(len(r)):
                if (i + 1) % 2 != 0:
                    a.append(r[i])
            return a
        else:
            return "Invalid Position"
    elif type(r) == str:
        if s == "even":
            for i in range(len(r)):
                if (i + 1) % 2 == 0:
                    a.append(r[i])
            return "".join(a)  
        elif s == "odd":
            for i in range(len(r)):
                if (i + 1) % 2 != 0:
                    a.append(r[i])
            return "".join(a)  
        else:
            return "Invalid Position"
    else:
        return "Invalid Input"
    



input_str = input("Enter the list or a string : ")
try:
    r = ast.literal_eval(input_str) 
    s = input("Enter the position to find : ")
    print(char_at_pos(r,s))
    
except (SyntaxError, ValueError):
    if type(input_str) == str :
        r = input_str
        s = input("Enter the position to find : ")
        print(char_at_pos(r,s))
    else :
        
        print("Invalid input. Please enter a valid list or string")