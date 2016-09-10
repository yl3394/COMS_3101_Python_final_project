# Author: Yanjin Li (UNI: yl3394)
# COMS W3101 Final Project 
# Due Date: 20160516 
'''
Usage:
python main.py 
input file: words.txt
'''

"""
----------------------------------Introduction---------------------------------
    
    In this problem, I will implement two version of word games, named 6.00 
wordgram. This type of game is similar to Srabble or Words with Friends. Letters
are dealt to players, who then construct one or more words out of their letters.
Each valid word receieve a score, based on the length and contents of the word.

- Game Rules:
    (1) A player is dealt a hand of n letters chosen at random 
    (2) The player arranges the hand into as many words as they want out of the
    letters, using each letter at most once. 
    (3) Some letters may remain unused which will not be scored of course 

- Scoring:
    (1) The score for the hand is the sum of the scores for each word formed 
    (2) The score for a word is the sum of the points for letters in the word,
    multiplied by the length of the word, adding 50 points if all n letters are 
    used on the first word created. 
    (3) Letters are scored as in Scrabble:
        A = 1     B = 3     C = 3     D = 2
        E = 1     F = 4     G = 2     H = 4
        I = 1     J = 8     K = 5     L = 1
        M = 3     N = 1     O = 1     P = 3
        Q = 10    R = 1     S = 1     T = 1
        U = 1     V = 4     W = 4     X = 8
        Y = 4     Z = 10
        We have defined the dictionary SCRABBLE_LETTER_VALUES that maps each
        lowercase letter to its Scrabble letter value. 
    (4) For example, 'weed' would be worth 32 points ((4+1+1+2) for the four 
    letters, then multiply by len('weed') thus 8*4 = 32).
    (5) As another example, if n = 7 and you make the word 'waybill' on the 
    first try, it would be worth 155 points by
        (4 + 1 + 4 + 3 + 1 + 1 + 1)*7 + 50 = 155
    where the bonus point 50 is for using all n letters in the first try.     

-------------------------------------------------------------------------------   
"""
import random
import string
import os.path

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------------------------------------------------
"""============================================================================
Part A: Loading Words from the External Textfile
============================================================================"""
#WORDLIST_FILENAME = "/Users/yanjin1993/Desktop/words.txt"
#open(os.path.expanduser("~/Desktop/words.txt"))

def loadWords():
    """
    Load words from textfile named words.txt, which contains all valid words in
    our wordgame. Due to the volumn of our word textfile, the program may take 
    a while. 
    
    Function Parameters:
        (1) None
    Returns:
        (1) A list of valid words
    """
    print("Loading word list from file...")
    # inFile: file
    #inFile = open(WORDLIST_FILENAME, 'r', 0)
    inFile = open(os.path.expanduser("~/Desktop/words.txt"))
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

loadWords()


"""============================================================================
Part B: Socring a Word 
============================================================================"""

def getWordScore(word, n):
    """
    Assuming the word given is valid, the program will return a corresponding 
    score to each word. The scoring standard is shown as following:
    
    1. Sum of the points for each letter, multiplied by the length of the word
    2. PLUS 50 points if all n letters are used.
    
    Function Parameters: 
        (1) string (lowercase letters)
        (2) n: integer (HAND_SIZE, changale as the game ongoing)
    Returns: 
        (1) int >= 0
    """
    word_list = list(word)
    result = 0
    for i in word_list:
        #print(i)
        result += SCRABBLE_LETTER_VALUES.get(i)
        #print(result)
    result = result * len(word) 
    if len(word) == n:
        result += 50
    return(result)
        


"""============================================================================
Part C: Generating and Displaying a Hand 
============================================================================"""

""" C-1 Generating a Hand """ 
def dealHand(n):
    """
    Randomly generates a hand with lowercase letters. To make the game easier to
    play, the program automatically generates a random hand containing at least
    3/n vowels letters each time. 
    
    Function Parameters: 
        (1) n >= 0: length of a hand 
    Returns: 
        (1) dictionary (hand):The keys are letters and the values are the number 
        of times the particular letter is repeated in that hand.
    """
    hand={}
    numVowels = int(n / 3)
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return(hand)

""" C-2 Displaying a Hand """
def displayHand(hand):
    """
    Displays the letters currently in the hand. 
    
    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    Function Parameters: 
        (1) Hand: a dictionary randomly generized by  
    Returns: 
        (1) int >= 0
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,)              
    print()                               

""" C-3 Counting Frequency """ 
def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    Function Parameters:
        (1) sequence: string or list
    Return: 
        (1) dictionary: keys are elements and values are integer counts, for 
        the number of times that an element is repeated in the sequence
    """
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return(freq)


"""============================================================================
Part D: Updating a Hand 
============================================================================"""
def updateHand(hand, word):
    """
    After each round of playing the wordgame, the program will automatically 
    update the hand by removing the used letters for futures rounds. Here, the 
    updating process happens in the values of hand dictionary, by substracting 
    number of freqency of letters in a word given by player from the original
    values in the dictionary. 

    Function Parameters:
        (1) string (word): given by players
        (2) dictionary (hand): randomly generated by the program in the first 
        round, and then modified automatically by this function in later runs.   
    Returns: 
        (1) dictionary (hand): recently updated version
    """
    hand_copy = hand.copy()
    word_list = list(word)
    for k, v in hand_copy.items():
        for i in word_list:
            if i == k:
                hand_copy[k] -= 1
    return(hand_copy)

        
"""============================================================================
Part E: Updating a Hand 
============================================================================"""
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely composed of letters 
    in the hand. Otherwise, returns False.

    Function Parameters:
        (1) string (word)
        (2) dictionary (hand)
        (3) list (wordList)
    Returns:
        (1) TRUE/FALSE: depends on wether our word in the word list and whether 
        comes from hand list. 
    """
    #Test (1) whether in the word list 
    word = word.lower()
    count = 0
    if word == '':
        return(False)
    if word in wordList:
        count += 1 
        
    #Test (2) whether comes from Hand list 
    word_list = list(word)
    word_num = 0 
    for i in word_list:
        if i in hand.keys():
            word_num += 1 
    if word_num == len(word):
        count += 1
    if count == 2:
        return(True)
    else:
        return(False)
        
"""============================================================================
Part F: Playing a Hand 
============================================================================"""
""" E-1 Calculating Hand Length """
def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    Function Parameters:
        (1) dictionary (hand)
    Returns:
        (1) integer (n): length or a hand 
    """
    count = 0
    for k, v in hand.items():
        count += v
    return(count)

""" E-2 Playing a Hand """
def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."
      
    Function Parameters:
        (1) dictionary (hand)
        (2) list (wordList)
        (3) integer (n): HANDSIZE currently updated 
    Inputs:
        (1) string (word): given by players 
    """
    # Keep track of the total score
    score = 0
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
        # Display the hand
        print("Current Hand: ")
        displayHand (hand)
        
        # Ask user for input
        word = input('Enter word, or a "." to indicate that you are finished: ')
        
        # If the input is a single period:
        if word == '.':
            
            # End the game (break out of the loop)
            return() #exit function             
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if isValidWord(word, hand, wordList) == False: 
                # Reject invalid word (print a message followed by a blank line)
                print("Invalid word, please try again.")
                print()
                playHand(hand, wordList, n)

            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                score += getWordScore(word, n)                
                print('"'+word+'" earned %d points.' %getWordScore(word, n))
                print("Total score: %d points" %score)
                # Update the hand 
                hand = updateHand(hand, word)                

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print("Run out of letters. Total score: %d points" %score)

"""============================================================================
Part G: Playing a Game 
============================================================================"""

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1 
    """
    # variable to keep track if this is the first game the user played
    firstGame = True
    while True:
        # ask user to input 'n' or 'r' or 'e'.
        print("Enter n to deal a new hand, r to replay the last hand, or e to end game:"),
        option = input()
        # If the user inputs 'n', let the user play a new (random) hand.
        if option == 'n':
            firstGame = False
            # deal hand
            hand = dealHand(HAND_SIZE)
            #print(hand)
            # start game
            playHand(hand, wordList, HAND_SIZE)
        # If the user inputs 'r', let the user play the last hand again.
        elif option == 'r':
            # if this is user's first game
            if firstGame == True:
                print("You have not played a hand yet. Please play a new hand first!")
                print
            else:
                playHand(hand, wordList, HAND_SIZE)
        # If the user inputs 'e', exit the game.
        elif option == 'e':
            break
        # Otherwise, tell them their input was invalid.
        else:
            print("Invalid command.")

"""============================================================================
Part H: Playing Our WordGame!!
============================================================================"""
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)