def balanced(s):
    
    opening = set('[{(')
    closing = set(']})')
    
    # create a stack or empty list
    stack = []
    
    
    # check for opening if present append to stack
    for elems in s:
        if elems in opening:
            stack.append(elems)
            
    # check for closing if present pop from stack
    # if stack is empty or closing appears first return false
    for elems in s:
        if elems in closing:
            stack.pop()
        else:
            if stack != opening:
                return False
    
    # ensure of stack holds no more contents
    return len(stack) == 0
        
        
'''
Balancend parantheses, bracket , curly braces.
Check the input and ensure that your string has balanaced opening and
closing parentheses, brackets or curlt braces.
'''
