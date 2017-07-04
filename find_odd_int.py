def find_it(seq):

    # create an empty dictionary
    count = {}
    
    # loop through elems and place them into our dictionary
    for elems in seq:
        if elems in count:
            count[elems] += 1
        else:
            count[elems] = 1
            
    # loop through our dictionary, if any elements are divisble by 2(even)
    # then return it.
    for keys in count:
        if count[keys] % 2 != 0:
            return keys
    return None







'''
Given an array, find the int that appears an odd number of times.
There will always be only one integer that appears an odd number of tiems.
Return it.
'''
