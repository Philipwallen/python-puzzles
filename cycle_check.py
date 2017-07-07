def cycle_check(node):
	
	marker1 = node
	marker2 = node
	
	while marker2 != None and marker2.nextnode != None:
		
		marker1 = marker1.nextnode
		marker2 = marker2.nextnode.nextnode
		
		if marker2 == marker1:
			return True
			
	return False
	
	
'''
SIngly linked list cycle check.  Write a function which takes in the first
node in a singly linked list and returns a boolean indicating if the 
linked list contains a 'cycle'.

A cycle is when a node's next point actually point back to a previous
node in the list.  This is also known as a circularly linked list.
'''
