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

words = [
    "apple",
    "banana",
    "cherry",
    "lemon",
    "lime",
    "blueberry",
    "orange",
    "epoxy",
    "marionberry"
]

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
    play_again = input("Play again? (yes/no)")
    play_again.lower
    if play_again[0] == 'y':
        start()

# game init function
def start():
    global words
    global secret
    global status
    global failed_guesses
    # set the secret word
    secret = list(words[random.randint(0, (len(words)-1))])
    # set the status to an empty number of spaces the same length as the word
    status = secret.copy()
    for i in range(len(secret)):
        status[i] = '_'
    # reset failed guesses
    failed_guesses = []
    # start game with 6 turns
    turn(6)

def turn(guess_left):
    global drawings
    global status
    # check for win
    print(drawings[6 - guess_left])
    if not '_' in status:
        print("YOU WON!")
        print("The word was indeed", print_word(secret, "")) 
        play_again()
        return
    # draw pictures based on guesses left
    # print("DEV TOOLS: the secret is", print_word(secret, ""))
    print("Status: ", print_word(status, " "))
    print("Failed guesses: ", print_word(failed_guesses, " "))
    # if they still have guesses left, run turn
    if guess_left > 0:
        guess = input("Your next guess: ")
        guess = guess.lower()
        # if it's not a letter then restart
        if not guess in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            print("You need to type a letter. Please try again.")
            turn(guess_left)
        # if the guessed letter is in the secret word
        elif guess in secret:
            # update status
            for i in range(len(secret)):
                if secret[i] == guess:
                    status[i] = guess
            #run next turn, no guesses deducted
            turn(guess_left)
        # start a new turn with a guess deducted
        elif guess in failed_guesses:
            print("You already guessed that one")
            turn(guess_left)
        else:
            print("NOPE")
            # add guess to failed guesses
            failed_guesses.append(guess)
            turn(guess_left-1)
    else:
        #display lose and restart game
        print("YOU LOSE. PRESS F TO PAY RESPECTS")
        print("the word was", print_word(secret, ""))
        play_again()

start()

