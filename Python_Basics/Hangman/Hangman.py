# Take User input
# check letter against word
# if its in the word reveal the letter in its position
# if not lose a life

import random

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
word_list = ["cinema", "table", "haberdashery", "jumble", "sparta", "hangman"]


def hangman():
    word = random.choice(word_list)
    word_guess = []
    for char in word:
        word_guess.append('_')
    print(word_guess)
    letters_guessed = []
    lives = 10
    game_active = True
    while game_active:
        letter_choice = input("Pick your letter: ")
        letters_guessed.append(letter_choice)
        if letter_choice in word:
            print("correct letter")
            for i in range(len(word)):
                if letter_choice == word[i]:
                    word_guess.__setitem__(i, letter_choice)
                    print(letter_choice)
                    print(word_guess)
                else:
                    continue
            print(f"You have picked {letters_guessed}")
        else:
            lives -= 1
            print(f"you have {lives} left")
        string_guess = ""
        for char in word_guess:
            string_guess += char
        if word == string_guess:
            game_active = False
            print("congratulations you win!")
        if lives <= 0:
            game_active = False
            print("Game over! You are out of lives.")
hangman()