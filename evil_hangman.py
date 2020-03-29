# this one cheats and changes the word if you guessed a letter in it
import random

drawings = [
    " ____\n|    |\n|    \n|   \n|    \n|-\n",
    " ____\n|    |\n|    O\n|   \n|    \n|-\n",
    " ____\n|    |\n|    O\n|    |\n|    \n|-\n",
    " ____\n|    |\n|    O\n|   -|\n|    \n|-\n",
    " ____\n|    |\n|    O\n|   -|-\n|    \n|-\n",
    " ____\n|    |\n|    O\n|   -|-\n|    /\n|-\n",
    " ____\n|    |\n|    O\n|   -|-\n|    /\\\n|-\n"
]

# words = [
#     "apple",
#     "banana",
#     "cherry",
#     "lemon",
#     "lime",
#     "blueberry",
#     "orange",
#     "epoxy",
#     "marionberry"
# ]

words = open('dictionary.txt', 'r').read().split('\n')

# the following code i used to see what the longest wordlength in the file was
# maxlen = 0
# for word in words:
#     if len(word) > maxlen:
#         maxlen = len(word)
#         print(word)
# print("the max length is", maxlen)

secret = ""

# displays state of secret word
status = []

failed_guesses = []

# takes an list of characters and returns a string to print
def print_word(word, filler):
    string_word = ""
    for letter in word:
        string_word = string_word + letter + filler
    return string_word

def show_drawings():
    for drawing in drawings:
        print(drawing)

# sequence to restart game
def play_again():
    play_again = input("Play again? (yes/no) ")
    play_again = play_again.lower()
    if play_again[0] == 'y':
        start()


def get_length():
    length = int(input("How long of a word would you like to guess? "))
    if int(length) < 2 or int(length) > 29:
        print("You need to enter a number between 2 and 29.")
        get_length()
    else: 
        return length

# removes words from words list that contain a given letter
# if none or one word remains set the new secret
def remove_words(letter):
    global secret
    global words
    words_temp = words.copy()
    if len(words) > 1:
        # loop through array and remove words containing that letter
        i = 0
        while i < len(words):
            if letter in words[i]:
                words.pop(i)
                i -= 1
            i += 1
        # reset to a random word in copy if no words left
        if len(words) == 0:
            secret = words_temp[random.randint(0, (len(words_temp)-1))]
        else:
            secret = words[random.randint(0, (len(words)-1))]

# game init function
def start():
    global words
    words = open('dictionary.txt', 'r').read().split('\n')
    global secret
    global status
    global failed_guesses
    # reset failed guesses
    failed_guesses = []
    # set the word length
    word_length = get_length()
    i = 0
    while i < len(words):
        if len(words[i]) != word_length:
            words.pop(i)
            i -= 1
        i += 1
    # set the secret word
    secret = list(words[random.randint(0, (len(words)-1))])
    # set the status to an empty number of spaces the same length as the word
    status = secret.copy()
    for i in range(len(secret)):
        status[i] = '_'
    # start game with 6 turns
    turn(6)

def turn(guess_left):
    global drawings
    global status
    global secret
    # check for win
    print(drawings[6 - guess_left])
    if not '_' in status:
        print("YOU WON!")
        print("The word was indeed", print_word(secret, "")) 
        play_again()
        return
    # draw pictures based on guesses left
    # print("DEV TOOLS: words left", words)
    # print("DEV TOOLS: the secret is", print_word(secret, ""))
    print("Status: ", print_word(status, " "))
    print("Failed guesses: ", print_word(failed_guesses, " "))
    # if they still have guesses left, run turn
    if guess_left > 0:
        guess = input("Your next guess: ")
        guess = guess.lower()
        # if it's not a letter then restart
        if not guess in "abcdefghijklmnopqrstuvwxyz" or len(guess) > 1:
            print("You need to type a letter. Please try again.")
            turn(guess_left)
        elif guess in failed_guesses:
            print("You already guessed that one")
            turn(guess_left)
        # if the guessed letter is in the secret word
        else:
            remove_words(guess)
            if guess in secret:
                # update status
                for i in range(len(secret)):
                    if secret[i] == guess:
                        status[i] = guess
                # run next turn, no guesses deducted
                turn(guess_left)
            else:
                print("NOPE")
                # add guess to failed guesses
                failed_guesses.append(guess)
                # start a new turn with a guess deducted
                turn(guess_left-1)
    else:
        #display lose and restart game
        print("YOU LOSE. PRESS F TO PAY RESPECTS")
        print("The word was", print_word(secret, ""))
        play_again()

start()

