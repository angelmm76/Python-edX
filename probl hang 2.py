def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    ans = ''
    for ca in secretWord:
        coinc = False
        for le in lettersGuessed:
            if ca == le:
                coinc = True 
        if coinc == True:
            ans = ans + ca
        else:
            ans = ans + ' _ '      
    return ans
      
        
secre ='carrot'
letras = ['z','x','q','c','r','o',]
print getGuessedWord(secre, letras)