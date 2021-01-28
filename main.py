import os
import random
from sys import platform
from words import words


def guess(hangman_lives, past_guesses, last_guess_duplicate):

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

    return hangman_lives, past_guesses, last_guess_duplicate


def clear_screen():
    if platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

def print_status(hangman_lives, guessed_word_letters):
    print("You have " + str(hangman_lives) + " more lives.")
    print("\n")
    print(" ".join(guessed_word_letters))
    print("\n")

def print_final(win = True):
    clear_screen()
    print("\n")
    if win:
        print(" ".join(guessed_word_letters))
        print("\nGreat job!")
    else:
        print("\n")
        print("Nice effort. However the word was: " + chosen_word)

if __name__ == "__main__":
    # Clears console at start
    clear_screen()

    # Sample list of 10 words
    list_of_words = words

    # Picks first word in shuffled list
    chosen_word = random.choice(words)

    chosen_word_letters = [letter for letter in chosen_word]
    guessed_word_letters = ["_" for _ in chosen_word]

    hangman_lives = 6
    past_guesses = []
    last_guess_duplicate = False


    # Guess while loop
    while guessed_word_letters != chosen_word_letters and hangman_lives != 0:

        # Clears past turn
        clear_screen()

        if last_guess_duplicate:
            print("You already chose that letter. Pick a new one.")

        # Prints # of hangman lives, and the current state of their guesses
        print_status(hangman_lives, guessed_word_letters)

        # Asks + checks for a letter
        hangman_lives, past_guesses, last_guess_duplicate = guess(hangman_lives, past_guesses, last_guess_duplicate)


    if guessed_word_letters == chosen_word_letters:
        # User wins
        print_final()
    else:
        # User loses
        print_final(win = False)