def duplicate_count(text):
	
	#create an empty dictionary
	count = {}
	emptylist = []
	
	for elems in text:
		if elems in count:
			count[elems] += 1
		else:
			count[elems] = 1
			
	for keys in count:
		if count[keys] > 1:
			emptylist.append(keys)
			
	print(emptylist)		
	return len(emptylist)
	
print(duplicate_count('indivisibility22'))
