def anagram(s1, s2):
	
	# clean up our strings
	s1 = s1.replace(' ','').lower()
	s2 = s2.replace(' ','').lower()
	
	# create and empty dictionary to capture our strings
	count = {}
	
	for elems in s1:
		if elems in count:
			count[elems] += 1
		else:
			count[elems] = 1
			
	for elems in s2:
		if elems in count:
			count[elems] -= 1
		else:
			count[elems] = 1
			
	for keys in count:
		if count[keys] != 0:
			return False
	return True
	
	
'''
Given two strings, check to see if they are anagrams.  An anagram is when
two strings can be written using the exact same letters.
'''
