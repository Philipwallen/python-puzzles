def square_digits(num):

    # transform num into a string
    num = str(num)
    
    # create 2 empty list
    capture = []
    restore = []
    
    # transform str(num) into an int and pass into a list
    for elems in num:
        capture.append(int(elems)**2)
        
    #tranform int(num) into a str and pass to another list  
    for elems in capture:
        restore.append(str(elems))
        
    #join the contents of our list together, this can only be done on a str.   
    answer = ''.join(restore)
    return int(answer)
    
'''
Square every digit of a numer
For example, if we run 9119 through the function, 811181 will come out.
Note: The function accepts an integer and returns an integer.
'''
