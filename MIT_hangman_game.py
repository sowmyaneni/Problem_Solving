import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    if set(secretWord) <= set(lettersGuessed):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word = []

    for letter in secretWord:
        if letter in lettersGuessed:
            word.append(letter)
        else:
            word.append('_')
    return ' '.join(word)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...

    S1=string.ascii_lowercase
    S1=list(S1)
    S2=lettersGuessed
    for char in S2:
        if char in S1:
            newString = S1.remove(char)
    newString = ''.join(S1)
    return newString

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    availableGuesses = 8
    lettersGuessed = []

    # FILL IN YOUR CODE HERE...
    print('Welcome to the game, Hangman!' + '\n'+ 'I am thinking of a word that is ' +str(len(secretWord)) + ' letters long.')
    print('----------------')

    while availableGuesses > 0:
        print('You have ', availableGuesses, ' guesses left.')
        availableLetters = getAvailableLetters(lettersGuessed)
        print('Available letters: ', availableLetters)

        guess = (input('Please guess a letter: '))
        guess = guess.lower()

        if guess in lettersGuessed:

           print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
           print('-----------')
        elif guess in secretWord:
             lettersGuessed.append(guess)
             print("Good guess: ", getGuessedWord(secretWord, lettersGuessed))
             print('-----------')

                 #print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
        elif guess not in secretWord:
             availableGuesses = availableGuesses - 1
             print("Oops! That letter is not in my word: ", getGuessedWord(secretWord, lettersGuessed))
             print('-----------')
        lettersGuessed.append(guess)

        if isWordGuessed(secretWord, lettersGuessed) is True:
            print("Congratulations, you won!")
            return
    print("Sorry, you ran out of guesses. The word was " +str(secretWord)+".")

secretWord = chooseWord(wordlist).lower()
#secretWord = 'y'
hangman(secretWord)
