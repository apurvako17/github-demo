#Add implementation
def add(x,y) :
	return x+y

#Subtract implementation
def subtract(x,y) :
	return x-y	#On Master Branch

#Multiply implementaion
def multiply(x,y) :
	return x*y	#On Bug456

#Divide implementaion
def divide(x,y) :
	if y=0:		#On Bug456
		return DIV_BY_0_ERR
	else:
		return x/y

