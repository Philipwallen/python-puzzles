def alphabet_position(text):

    
    # create a list to capture the elems of our text parameter is lower case form
    capture = []
    for elems in text:
        capture.append(elems.lower())

    # create dictionary housing our alphabets
    alpha = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    }
    
    #create a list to catch and release our transform alphabets
    release = []
    for letters in capture:
        if letters in alpha:
            release.append(str(alpha[letters]))
            
    return ' '.join(release)
    
'''
You are given a string, replace every letter with its position in the 
alphabet.  If anything in the text isn't a letter, ignore and don't
return it.
'''
