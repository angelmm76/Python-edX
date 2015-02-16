def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alfabeto = 'abcdfghjlmnoqtuvwxyz'
    
    total = ''
    for ca in alfabeto:
       coinciden = False
       for le in lettersGuessed:
           if ca == le:
                coinciden = True
       if coinciden == False:
            total = total + ca
        
    return total
    
letras = ['p', 'y', 'w', 'f', 't', 'n', 'v', 'b', 'c', 'j', 'u', 'z']
print getAvailableLetters(letras)