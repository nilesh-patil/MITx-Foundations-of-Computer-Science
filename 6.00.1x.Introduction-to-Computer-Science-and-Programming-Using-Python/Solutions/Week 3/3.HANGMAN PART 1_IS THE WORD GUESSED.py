def isWordGuessed(secretWord, lettersGuessed):
    if secretWord=='':
        return True
    
    for c in secretWord:
        if c in lettersGuessed:
            return isWordGuessed(secretWord[1:], lettersGuessed)
        elif c not in lettersGuessed:
            return False