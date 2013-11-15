def hangman(secretWord):
    mistakesMade=0
    guessesRemaining=8-mistakesMade
    lettersGuessed=[]
    dostepneLiterki=getAvailableLetters(lettersGuessed)
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is "+ str(len(secretWord)) +" letters long.")
    print('-----------')
    
    while mistakesMade<8:
        guessesRemaining=8-mistakesMade
        print("You have "+str(8-mistakesMade)+" guesses left.")
        print("Available letters: "+str(getAvailableLetters(lettersGuessed)))
        litera= str(raw_input("Please guess a letter: "))
        guessInLowerCase = litera.lower()
    
        if guessInLowerCase in lettersGuessed:
            print("Oops! You've already guessed that letter: "+str(getGuessedWord(secretWord, lettersGuessed)))
        elif guessInLowerCase not in secretWord:
            lettersGuessed+=guessInLowerCase
            print("Oops! That letter is not in my word: "+str(getGuessedWord(secretWord, lettersGuessed)))
            mistakesMade+=1
        elif guessInLowerCase in dostepneLiterki:
            lettersGuessed+=guessInLowerCase
            print("Good guess: "+str(getGuessedWord(secretWord, lettersGuessed)))
            if '_' not in getGuessedWord(secretWord, lettersGuessed):
                break
        dostepneLiterki=getAvailableLetters(lettersGuessed)
        print('-----------')
        
    if '_' not in getGuessedWord(secretWord, lettersGuessed):
        print('-----------')
        print("Congratulations, you won!")
    elif '_' in getGuessedWord(secretWord, lettersGuessed):
        print("Sorry, you ran out of guesses. The word was "+str(secretWord))
    guessesRemaining=8-mistakesMade