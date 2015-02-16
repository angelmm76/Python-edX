animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: The key with the largest number of values associated with it
    '''
    
    result=None
    number=0
    for key in aDict.keys():
        if len(aDict[key])>=number:
            result = key 
            number = len(aDict[key])     
    return result
    
print biggest(animals)