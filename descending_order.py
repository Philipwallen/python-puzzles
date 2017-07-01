def descending_order(num):
	
	# create an empty list
	capture = []
	
	for elems in str(num):
		capture.append(elems)
		
	capture.sort()
	
	print(''.join(capture[::-1]))
	
	
print(descending_order(21445))
