def sum_pairs(arr,k):
	
	# check the length of the arr is > 2
	if len(arr) < 2:
		return 'invalid input' 
	
	# create sets for tracking
	seen = set()
	output = set()
	
	for elems in arr:
		target = k - elems
		
		if target not in seen:
			seen.add(elems)
		else:
			output.add( (min(elems, target), (max(elems, target))))
			
	return '\n'.join(output)
	

	
'''
Given an integer array, output all the unique pairs that sum up to a 
specific value k. 
'''


