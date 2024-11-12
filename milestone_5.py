import random

fruits = ["banana", "mango", "pineapple", "strawberry", "grape"]

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        # A fruit is selected at random
        self.word = random.choice(self.word_list)
        # Initialize word_guessed with underscores for each letter in the word
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))  # number of unique letters in the word
        self.list_of_guesses = []

    def check_guess(self, guess):  # performs a check of the guessed letter against the chosen word
        if guess.lower() in self.word:  # If the guess is successful
            print(f"Good guess! {guess} is in the word.")
            # Update the word_guessed list with the guessed letter at the correct positions
            for i, letter in enumerate(self.word):
                if letter == guess.lower():
                    self.word_guessed[i] = guess.lower()
            self.num_letters -= 1  # reduce the number of unique letters left
            return True
        else:  # if the guess is not in the word
            self.num_lives -= 1  # reduces the number of lives by 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            return False

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if not guess.isalpha() or len(guess) != 1:  # check for invalid input
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:  # check if the letter has already been guessed
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                return guess  # return the valid guess to be checked by check_guess

def play_game(word_list):
    game = Hangman(word_list)
    print("Welcome to Hangman!")
    while True:
        if game.num_lives == 0:  # if the player runs out of lives, they lose
            print("You lost!")
            print(f"The word was: {game.word}")
            break
        elif "_" not in game.word_guessed:  # if the player has guessed all letters correctly
            print("Congratulations, You won the game!")
            print(f"The word was: {game.word}")
            break
        else:
            print("Current word: " + " ".join(game.word_guessed))
            guess = game.ask_for_input()  # ask the player for their guess
            if not game.check_guess(guess):  # check the guess and update the game state
                if game.num_lives == 0:  # if lives are 0, the player loses
                    print("You lost!")
                    print(f"The word was: {game.word}")
                    break

play_game(fruits)
