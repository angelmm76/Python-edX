def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''    
    ans=()
    contador = 0
    for elem in aTup:
        if contador %2 == 0:
            ans = ans + (aTup[contador],)
        contador += 1
    return ans
    
print oddTuples((3, 5, 6, 1, 'a'))