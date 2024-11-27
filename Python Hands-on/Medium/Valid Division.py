#Given a math division ,check whether its a valid division



def valid_division(d):
	d_list = d.split("/")
	return "invalid" if int(d_list[1]) == 0 else True if int(d_list[0])%int(d_list[1]) == 0 else True if int(d_list[0]) == 0  else False
	