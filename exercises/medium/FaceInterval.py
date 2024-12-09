#Create a function that takes a list and returns ":)" if the interval of the list is equal to any other element; otherwise return ":(".


def face_interval(num):
	if type(num) != list :
		return ":/"
	else :
		dif = max(num) - min(num)
	return 	":)" if dif in num else ":("
	