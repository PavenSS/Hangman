import random

word_list = ["banana", "mango", "pinapple", "stawberry", "grape"]

word = random.choice(word_list)

print(word)

guess = input("enter a single letter: ")
if len(guess) == 1:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

