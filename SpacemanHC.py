#Spaceman Project
#Henry Calderon

import random
import string


lettersGuessed = []

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    shouldScore = len(list(secret_word))
    score = 0
    for i in secret_word:
        if i in letters_guessed:
            score += 1

    if score == shouldScore:
        return True
    else:
        return False
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    pass

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    #holdString.clear()
    holdString = ""
    holdWord = list(secret_word)
    for l in holdWord:
        if l in letters_guessed:
            holdString += l
        else:
            holdString += "_"

    print(holdString)
    return holdString

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    pass


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
    if guess in secret_word:
        print("Letter Entered is Part of word.")
        return True
    else:
        print("Letter Entered is Not Part of Word.")
        return False

    pass




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    lettersGuessed.clear()
    print("Your Word is "+str(len(secret_word))+" letters long.")
    print("You have 7 guesses to try and figure out the word.")
    numGuess = True
    guessCount = 0
    while numGuess:
        userGuess = input("Letter Guess: ")
        userGuess=userGuess.lower()
        if userGuess in lettersGuessed:
            print("Aleady Guessed. Try again.")
        elif userGuess.isalpha() == True and len(userGuess) <= 1:
            lettersGuessed.append(userGuess)
            is_letter_there = is_guess_in_word(userGuess,secret_word)
            if is_letter_there == True:
                get_guessed_word(secret_word, lettersGuessed)
                win = is_word_guessed(secret_word,lettersGuessed)
                if win == True:
                    print("You Win!")
                    numGuess = False
                else:
                    numGuess = True
            else:
                print("Not a part of Word, Try Again.")
                #print(wordSofar)
                guessCount += 1
        else:
            print("Use something else.")


        if guessCount >= 7:
            print("Game over! The word was: "+secret_word)
            numGuess = False
        else:
            guess_left = 7 - guessCount
            print("You have "+ str(guess_left)+" guesses left.")

            #gameOn = False

#Creating test function to run in the code and to run with Pytest
def test_is_guess_in_word():
    test_word = "dodge"
    test_guess = "d"
    test_part = is_guess_in_word(test_guess, test_word)
    assert test_part == True
    test_guess = "y"
    test_part2 = is_guess_in_word(test_guess, test_word)
    #assert test_part2 == True

def test_get_guessed_word():
    test_word = "dodge"
    test_list = ["d","s","o","y","e","x"]
    test_hold = get_guessed_word(test_word,test_list)
    assert test_hold == "dod_e"
    #assert test_hold == "dode"
    #print("Test List = ")
    #print(test_list)

def test_is_word_guessed():
    test_word = "dodge"
    test_list = ["d","y","o","l","e","g","j","k","f"]
    test_correct = is_word_guessed(test_word,test_list)
    assert test_correct == True
    #assert test_correct == False

def play_spaceman():
    gameOn = True
    while gameOn:
        print("#---------------Menu---------------#")
        print("Play Spaceman!")
        print("The word guessing game! Enter letters to try and find the word.")
        #userMenu = "P"
        userMenu = input("Play or Quit?[P/Q]: ")
        print("#----------------------------------#")
        if userMenu == "P" or userMenu == "Play" or userMenu == "p":
            secret_word = load_word()
            spaceman(secret_word)
        elif userMenu == "Q" or userMenu == "Quit" or userMenu == "q":
            print("Thanks for Playing! Exiting")
            gameOn = False
        else:
            print("Please Enter a Proper Input.")



#test_word = "dodge"
test_is_guess_in_word()
test_get_guessed_word()
test_is_word_guessed()

if __name__ == "__main__":
    play_spaceman()

#Need to use "pytest -s SpacemanHC.py" in order to run the code
#These function calls that will start the game
