#!usr/bin/env python
# Date: 2024-10-28

import random


def main():
    words = [
        "rainbow",
        "computer",
        "science",
        "programming",
        "python",
        "mathematics",
        "player",
        "condition",
        "reverse",
        "water",
        "board",
        "geeks",
    ]

    rand_word = random.choice(words)
    print("Guess the characters")
    print("_ " * len(rand_word))
    guess = input()
    guess_count = 1
    guess_limit = 3

    while guess != rand_word and guess_count < guess_limit:
        print("Wrong!")
        guess = input()
        guess_count += 1
    if guess == rand_word:
        print("You won")

    print("-----------------------")
    print("     Game Over!!       ")
    print("-----------------------")


if __name__ == "__main__":
    main()
