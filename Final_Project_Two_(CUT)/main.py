# Hangman game based on NeuralNine's and Kite's  videos: https://youtu.be/5x6iAKdJB6U  & https://youtu.be/m4nEnsavl6w
# Version with random word selection
# Ideas for tweaking: Add error exceptions for integers, words, etc & retry option

import random
from hangman_words import word_selection

word = random.choice(word_selection)


def play():
    allowed_errors = 10
    guesses = []
    done = False

    while not done:
        for letter in word:
            if letter.lower() in guesses:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print("")
        done = True

        guess = input(f"You have {allowed_errors} to guess that word. "
                      f"Enter letter to guess the word: ")

        try:
            guesses.append(guess.lower().strip())
            if guess.lower() not in word.lower():
                allowed_errors -= 1
                guess = input(f"Wrong letter. You have {allowed_errors} left. "
                              "Please enter a letter to guess again: ")
                if allowed_errors == 0:
                    break
            elif guess.lower() is int:
                raise TypeError('Invalid Input')
        except TypeError as e:
            guess = input(f'{e} is an invalid input. Please enter a letter: ')

        done = True
        for letter in word:
            if letter.lower() not in guesses:
                done = False

    if done:
        print(f'You found the word! The word was {word}!')
    else:
        print(f'Game Over! The word was {word}.')


def main():
    play()
    while input("Play again? (Y/N) ").upper() == "Y":
        play()


if __name__ == "__main__":
    main()
