# Hangman game based on NeuralNine's video: https://youtu.be/5x6iAKdJB6U
# with improvements from Kite's videos:  https://youtu.be/m4nEnsavl6w
# Version with random word selection
# Additions: A retry option with
# new words after finishing game

import random
from hangman_words import word_selection


def get_word():
    word = random.choice(word_selection)
    return word


def play(word):
    allowed_errors = 7
    guesses = []
    done: bool = False

    while not done:
        for letter in word:
            if letter.lower() in guesses:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print("")

        guess = input(f"Let's Guess That Word! \n"
                      f"Allowed Errors: {allowed_errors} \n"
                      f"Guess a letter to find that word: ")
        guesses.append(guess.lower())
        if guess.lower() not in word.lower():
            allowed_errors -= 1
            if allowed_errors == 0:
                break

        done = True
        for letter in word:
            if letter.lower() not in guesses:
                done = False
    if done:
        print(f"You found the word! The word was {word}!")
    else:
        print(f"Game Over! The word was {word}.")


def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
