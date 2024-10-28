# Guess a number between
#!/usr/bin/env python
# 2024-10-28
#
import random


def main():
    number = random.randrange(100)
    print("-----------------------------------")
    print("Guess a number between 1 and 100")
    print("-----------------------------------")
    print("Press X : exite")
    print("===================================")

    while True:
        guess = input("Your guess: ")

        if guess == "x":
            break

        try:
            guess = int(guess)
        except ValueError:
            print("Not a number")
            continue

        if guess == number:
            print("Correct! You win")
            break

        elif guess < number:
            print("Too low")

        else:
            print("Too high")

    print("---------------------------------------------")
    print("             Game Over                       ")
    print("---------------------------------------------")


if __name__ == "__main__":
    main()
