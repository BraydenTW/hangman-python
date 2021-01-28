import os
import random
from sys import platform
from words import words


def guess():

    global hangman_lives, past_guesses, last_guess_duplicate
    found_letter = False
    duplicate_and_skip = False

    # Asks user to choose a letter
    current_guess = input("Choose a letter: ")

    # Searches for a match between the chosen word and guessed letter
    for i in range(len(chosen_word_letters)):
        if chosen_word_letters[i].lower() == current_guess.lower():
            guessed_word_letters[i] = current_guess.lower()
            found_letter = True

    for letter in past_guesses:
        if letter == current_guess.lower():
            found_letter = True
            duplicate_and_skip = True
            break

    # If guess is wrong, they lose a life
    if not found_letter:
        hangman_lives -= 1

    # Checks if this guess was a duplicate from the previous guesses
    if duplicate_and_skip:
        last_guess_duplicate = True
    else:
        last_guess_duplicate = False

    past_guesses.append(current_guess.lower())


def clear_screen():
    if platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


if __name__ == "__main__":
    # Clears console at start
    os.system('cls')

    # Sample list of 10 words
    list_of_words = words

    # Picks first word in shuffled list
    chosen_word = random.choice(words)

    chosen_word_letters = []
    guessed_word_letters = []

    # Sets up chosen word and guess arrays
    for letter in chosen_word:
        chosen_word_letters.append(letter)
        guessed_word_letters.append("_")

    hangman_lives = 6
    output_string = ""
    current_guess = ""
    past_guesses = []
    last_guess_duplicate = False


    # Guess while loop
    while guessed_word_letters != chosen_word_letters and hangman_lives != 0:

        # Clears past turn
        clear_screen()

        if last_guess_duplicate:
            print("You already chose that letter. Pick a new one.")

        # Prints # of hangman lives, and the current state of their guesses
        print("You have " + str(hangman_lives) + " more lives.")
        print("\n")
        print(" ".join(guessed_word_letters))
        print("\n")

        # Asks + checks for a letter
        guess()


    if guessed_word_letters == chosen_word_letters:
        # User wins
        clear_screen()
        print("\n")
        print(" ".join(guessed_word_letters))
        print("\nGreat job!")
    else:
        # User loses
        clear_screen()
        print("\n")
        print("Nice effort. However the word was: " + chosen_word)
