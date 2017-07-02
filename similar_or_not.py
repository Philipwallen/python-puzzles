def comp(array1, array2):
    # your code
    # if array1 or array2 have None values return False
    if array1 == None or array2 == None:
        return False
    
    if len(array1) == 0 or len(array2) == 0:
        return True
    
    # create empty list to capture the elems
    #create empty dictionary to track the number of occurences
    squared = []
    count = {}
    for elems in array1:
        squared.append(elems ** 2)
    
    for elems in squared:
        if elems in count:
            count[elems] += 1
        else:
            count[elems] = 1
            
    for elems in array2:
        if elems in count:
            count[elems] -= 1
        else:
            count[elems] = 1
            
    for keys in count:
        if count[keys] != 0:
            return False
    return True	

'''
Given two arrays write a function that check whether the two arrays have
the 'same' elements.  'Same' in this case means that the elements in array2
are the elements in a squared, regardless of the order.
'''
