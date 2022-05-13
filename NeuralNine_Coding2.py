# Hangman game based on NeuralNine's video: https://youtu.be/5x6iAKdJB6U
# Additions based from Kite's video:  https://youtu.be/m4nEnsavl6w
# Kite's coding from GitHub: https://github.com/kiteco/python-youtube-code/tree/master/build-hangman-in-python

# Modified Version of NeuralNine's coding with random word selection
# Additions: A retry option with new words after finishing the game
# management for incorrect guessed letters where
# no errors are added when the same wrong letter is repeated
# as well as for entering integers or more than one letter.

import random
from hangman_words import word_selection


def get_word():
    word: str = random.choice(word_selection)
    return word


def prompt(word, guesses):
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")


def play(word):
    allowed_errors: int = 7
    guesses = []
    done: bool = False

    while not done:
        prompt(word, guesses)
        guess = input("Let's Guess That Word! \n"
                      f"Allowed Errors: {allowed_errors} \n"
                      "Guess a letter to find that word: ")
        while guess in guesses or len(guess) != 1:
            if len(guess) != 1 or guess != int:
                prompt(word, guesses)
                print("Invalid input. Please enter one character.")
                guess = input(f"Allowed Errors: {allowed_errors} \n"
                              "Guess a letter to find that word: ")
            elif guess in guesses:
                prompt(word, guesses)
                print("You already guessed the letter", guess)
                guess = input(f"Allowed Errors: {allowed_errors} \n"
                              "Guess a letter to find that word: ")
        guesses.append(guess.lower().strip())
        if guess.lower() not in word.lower():
            allowed_errors -= 1
            if allowed_errors == 0:
                break

        done = True
        for letter in word:
            if letter.lower() not in guesses:
                done = False
    if done:
        prompt(word, guesses)
        print(f"You found the word! The word was {word}!")
    else:
        print(f"Game Over! The word was {word}.")


def main():
    word: str = get_word()
    play(word)
    while True:
        user_input = input("Play Again? (Y/N): ").upper().strip()
        if user_input == "Y":
            word: str = get_word()
            play(word)
        elif user_input == "N":
            break
        else:
            print('Invalid input. Please enter (Y/N): ')
    print('The game is over.')


if __name__ == "__main__":
    main()
