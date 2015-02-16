def laceStrings(s1, s2):
    """
    s1 and s2 are strings.
    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    numberloop = min(len(s1),len(s2))
    stringsum = ''
    for i in range(numberloop):
        stringsum += s1[i] + s2[i]
    
    if len(s1) > numberloop:
        stringsum += s1[numberloop:]
    elif len(s2) > numberloop:
        stringsum += s2[numberloop:]
    
    return stringsum
    
s1 = 'abc'
s2 = 'efghi'
print laceStrings(s1, s2)
s1 = 'abcde'
s2 = 'ghi'
print laceStrings(s1, s2)
s1 = 'wer'
s2 = ''
print laceStrings(s1, s2)