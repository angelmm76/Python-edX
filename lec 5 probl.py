def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    return base*recurPower(base, exp-1)
    
#print recurPower(2,0)

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    if exp == 0:
        return 1
    elif exp > 0 and exp % 2 == 0:
        return recurPower(base*base, exp/2)
    else:
        return base*recurPower(base, exp-1)
    
#print recurPowerNew(2,4)

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    ans = min (a,b)
    while ans > 1:
       if a%ans == 0 and b%ans == 0:
           return ans
       else:
           ans -= 1
    return 1
    
#print gcdIter(12,9)

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b ==0:
       return a
    else:
       return gcdRecur(b,a%b)
    
print gcdRecur(9,12)
