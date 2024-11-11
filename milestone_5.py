import random

fruits = ["banana", "mango", "pinapple", "stawberry", "grape"]

class Hangman:
   def __init__(self, word_list, num_lives):
    # A fruit is selected at random
    word = random.choice(word_list)
    # creating a set list for the number of letters in the randomly chosen word
    num_letters = len(set(word))
    # creating a list of underscores for every character in word.
    blank = ""
    for letter in word:
        blank += "_"
    word_guessed = list(blank)
    num_lives = int
    #creating a repository for each guess
    list_of_guesses=[]

    def check_guess(guess): # performs a check of the guessed letter against the chosen word.
        x=0
        if guess.lower() in word: #If sucessfull
            print(f"Good guess! {guess} is in the word.") #Affirms guessed letter is in word.
            for letter in word: #Cycles through every letter within the chosen word
                if guess.lower == word[x]: #When the letter is found
                    word_guessed[x] = guess.lower #Updates the word guessed with the leeter in the correct place
            num_letters = num_letters - 1 # reduces the number of unique letters left by 1.
        else: #if not in the word.
            num_lives = num_lives - 1 #reduces the number of lives by 1.
            print(f"Sorry, {guess} is not in the word.") #Relays to the user.
            print(f"You have {num_lives} lives left.") #Reduces life count by 1.

    def ask_for_input():
        while True:
            guess = input("Guess a letter: ")
            if guess.isalpha() == False and len(guess) == 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in list_of_guesses:
                print("You already tried that letter!")
            else:
                check_guess(guess)
                list_of_guesses.append(guess)
    ask_for_input()

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    game(word_list, num_lives)
    while True:
        if num_lives == 0:
            print("You lost!")
        if game.num_letters > 0:
            game.ask_for_input()
        if num_lives != 0 and game.num_letters == 0:
            print("Congratulations, You won the game!")

play_game(fruits)