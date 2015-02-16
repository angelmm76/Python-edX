def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    if x == 1:
        return 0
        
    if x % b == 0:
        return myLog(x/b, b) + 1
    else:
        return myLog(x-1, b)
    
x=171
b=8
print myLog(x, b)
import math
print 'log bueno ' + str(math.log(x, b))