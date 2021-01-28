import os
import random
from sys import platform
from words import words


def guess(state):

    found_letter = False
    duplicate_and_skip = False

    # Asks user to choose a letter
    current_guess = input("Choose a letter: ").lower()


    # Searches for a match between the chosen word and guessed letter
    for i in range(len(state["chosen_word_letters"])):
        if state["chosen_word_letters"][i].lower() == current_guess:
            state["guessed_word_letters"][i] = current_guess
            found_letter = True

    for letter in state["past_guesses"]:
        if letter == current_guess:
            found_letter = True
            duplicate_and_skip = True
            break

    # If guess is wrong, they lose a life
    if not found_letter:
        state["hangman_lives"] -= 1

    # Checks if this guess was a duplicate from the previous guesses
    if duplicate_and_skip:
        state["last_guess_duplicate"] = True
    else:
        state["last_guess_duplicate"] = False

    state["past_guesses"].append(current_guess)

    return state


def clear_screen():
    if platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

def print_status(state):
    print("You have " + str(state["hangman_lives"]) + " more lives.")
    print("\n")
    print(" ".join(state["guessed_word_letters"]))
    print("\n")

def print_final(state, win = True):
    clear_screen()
    print("\n")
    if win:
        print(" ".join(state["guessed_word_letters"]))
        print("\nGreat job!")
    else:
        print("\n")
        print("Nice effort. However the word was: " + ''.join(state["chosen_word_letters"]))

if __name__ == "__main__":
    # Clears console at start
    clear_screen()

    # Sample list of 10 words
    list_of_words = words

    # Picks first word in shuffled list
    chosen_word = random.choice(words).lower()


    state = {
        "chosen_word_letters" : [letter for letter in chosen_word],
        "guessed_word_letters" : ["_" for _ in chosen_word],
        "hangman_lives" : 6,
        "past_guesses" : [],
        "last_guess_duplicate" : False
    }


    # Guess while loop
    while state["guessed_word_letters"] != state["chosen_word_letters"] and state["hangman_lives"] != 0:

        # Clears past turn
        clear_screen()

        if state["last_guess_duplicate"]:
            print("You already chose that letter. Pick a new one.")

        # Prints # of hangman lives, and the current state of their guesses
        print_status(state)

        # Asks + checks for a letter
        state = guess(state)


    if state["guessed_word_letters"] == state["chosen_word_letters"]:
        # User wins
        print_final(state)
    else:
        # User loses
        print_final(state, win = False)