def add(n1, n2):
		if n1 == "" or n2 is None :
			return "Invalid Operation"
		elif type(n1) == str and type(n2) == str :
			return str(int(n1)+int(n2))
		else :
			return "Invalid Operation"