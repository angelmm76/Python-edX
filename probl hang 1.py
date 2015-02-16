def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    numbcoinciden = 0
    for ca in secretWord:
        for le in lettersGuessed:
            if ca == le:
                numbcoinciden += 1        
    print numbcoinciden
    if numbcoinciden >= len(secretWord):
        return True
    else:
        return False
      
        
secre ='carrot'
letras = ['z','x','q','c','a','r','r','o','t']
print isWordGuessed(secre, letras)