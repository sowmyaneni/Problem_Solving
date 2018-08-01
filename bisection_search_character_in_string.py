def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''

    if aStr == '':
        if char == '':
            return True
        else:
            return False
    if len(aStr) == 1:
        if char == aStr:
            return True
        else:
            return False
    aStr = aStr.lower()
    new_str = ''.join(sorted(aStr))
    if char == new_str[len(new_str)//2]:
        return True
    else:
        if char < new_str[len(new_str)//2]:
            return isIn(char, new_str[:len(new_str)//2])
        else:
            return isIn(char, new_str[len(new_str)//2:])
