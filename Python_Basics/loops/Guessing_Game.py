#Number Guessing Game

import random

game_random_number = random.randint(1, 100)
game_active = True

while game_active:
    user_guess = int(input("Pick a number between 1 - 100? :"))
    if user_guess == game_random_number:
        print("you guessed correctly")
        game_active = False
    elif user_guess < game_random_number:
        print("Too low, try again")
    else:
        print("Too high, guess again")
