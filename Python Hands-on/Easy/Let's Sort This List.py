#Sort the list in a given order

def asc_des_none(lst, s):
	if s == "Asc" :
			return sorted(lst)
	if s == "Des" :
			return sorted(lst,reverse=True)
	if s == "None" :
			return lst
	