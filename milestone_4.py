import random


class Hangman:
   def __init__(self, word_list, num_lives = 5):
    # A fruit is selected at random
    self.word = random.choice(word_list)
    
    # Initialize the number of lives
    self.num_lives = num_lives
    # Initialize word_guessed with underscores for each letter in the word
    self.num_letters = len(set(self.word))  # Count unique letters in the word
    self.word_guessed = ["_"] * len(self.word)  # Create underscores for each letter in the word
    self.list_of_guesses = []  # List to keep track of guessed letters

    def check_guess(self, guess): # performs a check of the guessed letter against the chosen word.
        if guess.lower() in self.word: #If sucessfull
            print(f"Good guess! {guess} is in the word.") #Affirms guessed letter is in word. 
            for idx, letter in enumerate(self.word): #Cycles through every letter within the chosen word
                if letter == guess.lower(): #When the letter is found
                    self.word_guessed[idx] = guess.lower() #Updates the word guessed with the leeter in the correct place
            self.num_letters -= 1 # reduces the number of unique letters left by 1.
        else: #if not in the word.
            self.num_lives -= 1 #reduces the number of lives by 1.
            print(f"Sorry, {guess} is not in the word.") 
            print(f"You have {self.num_lives} lives left.") 

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if not guess.isalpha() and len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
            return guess
    ask_for_input()