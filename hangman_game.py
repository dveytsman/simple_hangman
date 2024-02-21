from hangman_art import hangman_state, game_start_image
import random


print(game_start_image)

play = input("Would you like to play a round of hangman? Y or N\n").upper()

if play == "Y":
    game_on = True
else:
    game_on = False

# choose a word
alphabet = list("abcdefghijklmnopqrstuvwxyz")
with open('words.txt', 'r') as file:
    words = file.readlines()
    word = random.choice(words)[:-1]
    #TODO: remove the hint
    print(f"psst the word is {word}")
    number_of_guesses = 0
# set up the display
    display = []

    for letter in word:
        display.append("_")

    while game_on:
        if number_of_guesses >= 6:
            game_on = False
            print("you lost")
            break
        if "_" not in display:
            game_on = False
            print("you won")
            break

        guess = input("Pick a letter\n").lower()
        if guess in word and guess not in display:
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = word[i]
        elif guess in display:
            print("you've already guessed this letter, please try again.")
        elif guess not in alphabet:
            print("not a valid guess, try again")
        else:
            number_of_guesses += 1
            print(hangman_state[number_of_guesses])

        print(display)