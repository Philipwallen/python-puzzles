def get_sum(a,b):
	
	# check the numbers and if they are the same return one of them
	if a == b:
		return a
		
	# create and empty list to hold our elements
	capture = []
	
	# to capture the elems properly using the range function you must
	# ensure that your first parameter is less than your second. 
	# To ensure this I included a conditional statement.
	
	if a > b:
		for elems in range(b, a+1):
			capture.append(int(elems))
	else:
		for elems in range(a, b+1)):
			capture.append(int(elems))
			
	# using the sum function to add the captured numbers in the list
	return sum(capture)

'''
Given two integers, which can be positive and negative, find the sum of
all numbers between either end including the ends.  If both numbers are 
equal return a or b.
'''
