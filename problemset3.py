# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

# WORDLIST_FILENAME = "C:/Users/carlo/.spyder-py3/words.txt"
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

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    the_string=''
    for i in secretWord:
        if i in lettersGuessed:
            the_string+=i
        else:
            the_string+="_"
    return the_string


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    the_string=''
    for i in range(97,123):
        if chr(i) not in lettersGuessed:
            the_string+=chr(i)
    return the_string
# 65-90, 97-122

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
    print("Welcome to the game, Hangman!\nI am thinking of a word that is", len(secretWord) ,"letters long.")
    lettersGuessed = []
    guesses_left = 8
    print("-------------")
    while guesses_left > 0:
        print("You have", guesses_left, "guesses left.")
        print("Available letters:", getAvailableLetters(lettersGuessed))
        inputt = input("Please guess a letter: ")
        inputt = inputt.lower()
        if inputt in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        elif inputt in secretWord:
            lettersGuessed.append(inputt)
            print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
        else:
            guesses_left -= 1
            lettersGuessed.append(inputt)
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
        print("-------------")
        if isWordGuessed(secretWord, lettersGuessed) or guesses_left == 0:
            if isWordGuessed(secretWord, lettersGuessed):
                print("Congratulations, you won!")
                break
            else:
                print("Sorry, you ran out of guesses. The word was",secretWord+".")
                break
    return None


secretWord = "aloha"
hangman(secretWord)

# =============================================================================
#     #print("This is the length of the word you need to guess:\n\tLength:\t"+len(secretWord))
#     # os.system('cls')
#     print("""
# █████████████▀▀▀▀▀███████▀▀▀▀▀█████████████
# █████████▀░░▀▀█▄▄▄▄▄▄██▄▄▄▄▄▄█▀░░▀█████████
# ████████▄░░▄▄████▀▀▀▀▀▀▀▀▀████▄▄░░▄████████
# ████▀▀▀▀█████▀░░░░░░░░░░░░░░░▀█████▀▀▀▀████
# ██▀░░░░░░██▀░░░░░░██░░░██░░░░░░▀██░░░░░░▀██
# █░░░▀▀▀▀███░░░░░░░██░░░██░░░░░░░███▀▀▀▀░░░█
# █▄▄░░░░░░██░░░░▄░░▀▀░░░▀▀░░▄░░░░██░░░░░░▄▄█
# ████▄░░░░▀██░░░░███████████░░░░██▀░░░░▄████
# ██████████▀██▄░░░▀███████▀░░░▄██▀██████████
# ███████▀░░░████▄▄░░░░░░░░░▄▄████░░░▀███████
# ██████░░░▄▀░░▀▀▀███████████▀▀▀░░▀▄░░░██████
# ██████░░░▀░░░░░░░░▄▄▄█▄▄▄░░░░░░░░▀░░░██████
# ████████▄▄▄▄▄▄███████████████▄▄▄▄▄▄████████
# ██████████████████▀░░▀█████████████████████
# █████████████████▀░░░▄█████████████████████
# █████████████████░░░███████████████████████
# ██████████████████░░░▀█████████████████████
# ███████████████████▄░░░████████████████████
# █████████████████████░░░███████████████████
# 
#           HIIII MY NAME IS HANGY AND I WANNA PLAY A GAME :D
#               
#   HERE'S THE RUNDOWN OF THE RULES:
#     * At the start of the game, I will let you know how many 
#       letters the SpecialWord(TM) contains, but I will remind you
#       at the beggining of each round so no worries.
# 
#     * I will ask you to supply one guess (i.e. letter) per round.
# 
#     * I will tell you after each guess about whether you guess 
#       appears in the SpecialWord(TM).
# 
#     * After each round, I will also tell you the bits you've guessed
#       of the SpecialWord(TM), as well as letters that you have yet
#       to choose from for future rounds.
#           """)
#     length=len(secretWord)
#     print("\n\n\nToday's SpecialWord(TM) is",length,"letters long.\n")
#     print("You're in luck! Just the other day we had a 27 letter-long one")
#     print("Imagine how that one went!")
#     # while():    
#         
# # =============================================================================
# #     ▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬▬
# # 
# #            Who's      watching   This  In    April    2017 
# # 
# # ▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬▬﻿
# # =============================================================================
#     
#     return None
# 
# # When you've completed your hangman function, uncomment these two lines
# # and run this file to test! (hint: you might want to pick your own
# # secretWord while you're testing)
# 
# # secretWord = chooseWord(wordlist).lower()
# # hangman(secretWord)
# 
# =============================================================================
