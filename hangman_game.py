from hangman_art import hangman_state, game_start_image
import random


print(game_start_image)

play = input("Would you like to play a round of hangman? Y or N\n").upper()

if play == "Y":
    game_on = True
else:
    game_on = False

# letters for validation
alphabet = list("abcdefghijklmnopqrstuvwxyz")

# importing words and formatting them and grabbing the game word
with open('words.txt', 'r') as file:
    words = file.readlines()
    word = random.choice(words)[:-1]

    number_of_guesses = 0

    # set up the display
    display = []

    for letter in word:
        display.append("_")

    # game loop starts and loops until the number of guesses run out or until the player wins
    while game_on:
        if number_of_guesses >= 6:
            game_on = False
            print("you lost")
            break
        if "_" not in display:
            game_on = False
            print("you won")
            break
        
        # grabs the users guess. if the letter is in the word replace those spaces in the display
        guess = input("Pick a letter\n").lower()
        if guess in word and guess not in display:
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = word[i]
        # if the letter has been guessed, ask again
        elif guess in display:
            print("you've already guessed this letter, please try again.")
        # if the guess isn't a valid choice, ask for another guess
        elif guess not in alphabet:
            print("not a valid guess, try again")
        # otherwise the guess isn't valid
        # increment the number of wrong guesses
        # print out the visual representation
        else:
            number_of_guesses += 1
            print(hangman_state[number_of_guesses])
        # after each loop print the state of the guesses
        print(display)