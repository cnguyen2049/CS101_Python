#return biggest number

# Make sure your procedure has a return statement.
def bigger(a,b):
	if a>b:
		return a
	else:
	return b
def biggest(a,b,c):
	return bigger(a,bigger(b,c))
def mean(a,b,c):
	big = biggest(a,b,c)