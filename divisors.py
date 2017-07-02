def divisors(n):
	#create an empty list to capture the elems
	count = []
	
	# loop thru the numbers starting at 2, remember that the range function 
	# doesn't include the last number of the range
	for elems in range(2, n+1):
		if (n % elems) == 0:
			count.append(int(elems))
	
	# conditional statement to seperate the prime numbers	
	if len(count) == 1:
		print(str(n) + ' is prime')
	else:
		print(count[:-1])



divisors(15)

''' 
Create a function that takes an integer and returns an array with all
of the integer's divisors(except for 1 and the number itself.) If the 
number prime return the string' (integer) is prime'
'''	
