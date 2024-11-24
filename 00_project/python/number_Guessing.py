# Number Guessing Game 
# 1. Generate a random number between 0 and 100
# 2. Get user input
# 3. Check if the user input is equal to the random number
# 4. If the user input is not equal to the random number, tell the user if they guessed too high or too low
# 5. If the user guesses the number correctly, tell the user they won and exit the game
# date : 2024-11-24
import random


def number_guessing():
    return random.randint(0, 100)


def get_user_input():
    return input("Enter a number to guess or 'q' to quit: ")


def check_guess(number, user_input):
    if number == user_input:
        print("You guessed the number correctly!")
        return True
    elif number > user_input:
        print("You guessed too low.")
    else:
        print("You guessed too high.")
    return False


def main():
    number = number_guessing()
    
    while True:
        user_input = get_user_input()

        if user_input == "":
            print("You did not enter anything!")
            continue

        if user_input.lower() == "q":
            break

        try:
            user_input = int(user_input)
        except ValueError:
            print("Not a valid number.")
            continue

        if check_guess(number, user_input):
            break

    print("Game over. Goodbye!")


if __name__ == "__main__":
    main()

