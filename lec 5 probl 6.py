def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    ans = 0
    for char in aStr:
        ans += 1
    return ans    
    
#print lenIter('k')

    
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
      returns: True if char is in aStr; False otherwise
      '''
    if aStr == '':
        return False
    elif len(aStr) == 1:
        return char == aStr
    else:
        mid = len(aStr)/2
        if char == aStr[mid]:
            return True
        elif char < aStr[mid]:
            return isIn(char, aStr[:mid])
        else:
            return isIn(char, aStr[mid+1:]) 
            
print isIn('v', 'abcdefg')