def multiples(number):
    
    #create and empty set to house unique numbers
    seen = set()
    
    # loop captures all numbers from 1 to input number and return those numbers
    # that are multiples of 3 and 5, they are added to the set to create unique numbers
    for elems in range(1, int(number)):
        if (elems % 3) == 0 or (elems % 5) == 0:
            seen.add(elems)
    return sum(seen)

    
    
'''
Create a function that will return the sum of all the multiples of 3 or
5 below the number passed in.  
Nots: if the number is a multiple of both 3 and 5, only count it once.
'''
