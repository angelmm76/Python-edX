def lenRecur(aStr):
    '''
    aStr: a string
  
    returns: int, the length of aStr
    '''
    
    if aStr == '':
        return 0
    return lenRecur(aStr[1:])+1
    
    
print 'longitud ' + str(lenRecur("dsh67t"))