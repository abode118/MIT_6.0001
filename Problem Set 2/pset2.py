# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
        if char in letters_guessed:
            foundword = True
        else:
            foundword = False
            break
    return foundword


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ""
    for char in secret_word:
        if char in letters_guessed:
            guessed_word += char
        else:
            guessed_word += "_ "
    return guessed_word

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = string.ascii_lowercase
    remaining_letters = ""
    for char in alphabet:
        if char not in letters_guessed:
            remaining_letters += char
    return(remaining_letters)
            
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''

    letters_guessed = []
    vowels = ['a','e','i','o','u']
    guesses = 6
    warnings = 3

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word),"letters long.")
    print(get_guessed_word(secret_word,letters_guessed))
    print("You have", warnings, "warnings left.")
    while guesses > 0 and is_word_guessed(secret_word,letters_guessed) == False:
        print("--------------------")
        print("You have", guesses,"guesses left.")
        print("Available letters:",get_available_letters(letters_guessed))
        user_guess = str.lower(input("Please guess a letter: "))
        if str.isalpha(user_guess) == False:
            if warnings > 0:
                warnings -= 1
                print("Oops! That is not a valid letter. You have", warnings,
                      "warnings left:")
                print(get_guessed_word(secret_word,letters_guessed))
            else:
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess.")
                print(get_guessed_word(secret_word,letters_guessed))
                guesses -= 1
        elif user_guess in letters_guessed:
            if warnings > 0:
                warnings -= 1
                print("Oops! You've already guessed that letter. You now have",
                      warnings, "warnings left:")
                print(get_guessed_word(secret_word,letters_guessed))
            else:
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess.")
                print(get_guessed_word(secret_word,letters_guessed))
                guesses -= 1
        else:
            letters_guessed += user_guess
            if user_guess in secret_word:
                print("Good guess:", get_guessed_word(secret_word,letters_guessed))
            else:
                print("Oops! that letter is not in my word:",
                      get_guessed_word(secret_word,letters_guessed))
                if user_guess in vowels:
                    guesses -=2
                else:
                    guesses -= 1
    print("------------")
    if is_word_guessed(secret_word,letters_guessed) == True:
        unique_letters = []
        for char in secret_word:
            if char not in unique_letters:
                unique_letters += char
        total_score = guesses * len(unique_letters)
        print("Congratulations, you won!")
        print("Your total score for this game is:", total_score)
    else:
        print("Sorry, you ran out of guesses. The word was " + secret_word + ".")
    return(is_word_guessed)

# -----------------------------------

def strip(string):
    stripped = ""
    for char in string:
        if char != " ":
            stripped += char
    return stripped
    

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    i = 0
    stripped_my_word = strip(my_word)
    while i < len(stripped_my_word):
        char = stripped_my_word[i]
        if char == other_word[i] or (char == "_" and \
                             other_word[i] not in stripped_my_word) and \
                             len(stripped_my_word) == len(other_word):
            match = True
            i += 1
        else:
            match = False
            break
    return match

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matches = ""
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word) == True:
            possible_matches += (" " + other_word)
    if possible_matches == "":
        print("No matches found")
    else:
        print(possible_matches)
    return possible_matches

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = []
    vowels = ['a','e','i','o','u']
    guesses = 6
    warnings = 3

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word),"letters long.")
    print(get_guessed_word(secret_word,letters_guessed))
    print("You have", warnings, "warnings left.")
    while guesses > 0 and is_word_guessed(secret_word,letters_guessed) == False:
        print("--------------------")
        print("You have", guesses,"guesses left.")
        print("Available letters:",get_available_letters(letters_guessed))
        user_guess = str.lower(input("Please guess a letter: "))
        if user_guess == "*":
            print("Possible word matches are:")
            my_word = get_guessed_word(secret_word,letters_guessed)
            show_possible_matches(my_word)
        elif str.isalpha(user_guess) == False:
            if warnings > 0:
                warnings -= 1
                print("Oops! That is not a valid letter. You have", warnings, "warnings left:")
                print(get_guessed_word(secret_word,letters_guessed))
            else:
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess.")
                print(get_guessed_word(secret_word,letters_guessed))
                guesses -= 1
        elif user_guess in letters_guessed:
            if warnings > 0:
                warnings -= 1
                print("Oops! You've already guessed that letter. You now have", warnings, "warnings left:")
                print(get_guessed_word(secret_word,letters_guessed))
            else:
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess.")
                print(get_guessed_word(secret_word,letters_guessed))
                guesses -= 1
        else:
            letters_guessed += user_guess
            if user_guess in secret_word:
                print("Good guess:", get_guessed_word(secret_word,letters_guessed))
            else:
                print("Oops! that letter is not in my word:", get_guessed_word(secret_word,letters_guessed))
                if user_guess in vowels:
                    guesses -=2
                else:
                    guesses -= 1
    print("------------")
    if is_word_guessed(secret_word,letters_guessed) == True:
        unique_letters = []
        for char in secret_word:
            if char not in unique_letters:
                unique_letters += char
        total_score = guesses * len(unique_letters)
        print("Congratulations, you won!")
        print("Your total score for this game is:", total_score)
    else:
        print("Sorry, you ran out of guesses. The word was " + secret_word + ".")
    return(is_word_guessed)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


#if __name__ == "__main__":
#    #pass
#
#    # To test part 2, comment out the pass line above and
#    # uncomment the following two lines.
#    
#   secret_word = choose_word(wordlist)
#    hangman(secret_word)
#
################
#    
#    # To test part 3 re-comment out the above lines and 
#    # uncomment the following two lines. 
    
secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)
