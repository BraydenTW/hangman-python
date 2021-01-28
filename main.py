import os
import random
from sys import platform
from words import words


def guess(state):

    # Asks user to choose a letter
    current_guess = input("Choose a letter: ").lower()

    # Check if guess is a duplicate
    state["last_guess_duplicate"] =  False
    if current_guess in state["past_guesses"]:
        state["last_guess_duplicate"] =  True
        return state
    else:
        state["past_guesses"].append(current_guess)


    # Check if guess is in chosen word, if not subtract a life and return
    if current_guess not in state["chosen_word_letters"]:
        state["hangman_lives"] -= 1
        return state

    # Searches for a match between the chosen word and guessed letter
    state["guessed_word_letters"] = [letter if letter in state["past_guesses"] else "_" for letter in state["chosen_word_letters"]]

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

def main(state):
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

if __name__ == "__main__":
    # Clears console at start
    clear_screen()

    # Picks first word in shuffled list
    chosen_word = random.choice(words).lower()


    state = {
        "chosen_word_letters" : [letter for letter in chosen_word],
        "guessed_word_letters" : ["_" for _ in chosen_word],
        "hangman_lives" : 6,
        "past_guesses" : [],
        "last_guess_duplicate" : False
    }


    main(state)