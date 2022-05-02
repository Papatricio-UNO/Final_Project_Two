# Hangman game based on NeuralNine's video: https://youtu.be/5x6iAKdJB6U
# Version with random word selection
# Ideas for tweaking: Add error exceptions for integers, words, etc & retry option

import random

with open('wordlist.txt', 'r') as f:
    words = f.readlines()

word = random.choice(words)[:-1]


def main():
    allowed_errors = 14
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

        guess = input(f"Allowed Errors Left {allowed_errors}, Next Guess: ")
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


if __name__ == "__main__":
    main()
