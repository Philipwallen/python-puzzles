def getCount(inputStr):
    
    #create a list that holds our vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    #create an empty list to hold our elems
    count = []
    
    for elems in str(inputStr):
        if elems in vowels:
            count.append(elems)
            
    # count the contents of you once empty list   
    num_vowels = len(count)
    return num_vowels
	
'''
Return the number (count) of vowels in the given string.
Vowels are a,e,i,o,u
'''
