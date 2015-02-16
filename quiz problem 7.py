def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    
    if n == 0 or n == 6 or n == 9 or n == 20:
        return True
    
    for a in range(n/6 + 1):
        for b in range(n/9 + 1):
            for c in range(n/20 + 1):
                if (6*a + 9*b + 20*c) == n and (a!=0 or b!=0 or c!=0):
                    print a, b, c
                    return True
                    
    return False
        
print McNuggets(0), 0
print McNuggets(6), 6
print McNuggets(9), 9
print McNuggets(20), 20
print McNuggets(15), 15
print McNuggets(35), 35
print McNuggets(21), 21
print McNuggets(25), 25
print McNuggets(8), 8
print McNuggets(28), 28
print McNuggets(31), 31
print McNuggets(45), 45
print McNuggets(28), 28
print McNuggets(32), 32
print McNuggets(2), 2