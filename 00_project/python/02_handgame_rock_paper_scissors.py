#!/usr/bin/python3
# 02_handgame_rock_paper_scissors.py
# date: 2024-11-25
# author: @jeerasak
# description: a simple rock, paper, scissors game
# ---------------------------------------------------

import random

def rock_paper_scissors():
    choices = {"1": "Rock", "2": "Scissors", "3": "Paper"}
    win_conditions = {"1": "2", "2": "3", "3": "1"}

    while True:
        print("=" * 40)
        print("Rock, Paper, Scissors, shoot!")
        for key, value in choices.items():
            print(f"{key}.{value}")
        print("Press 'q' to quit")
        print("=" * 40)

        user_choice = input("Enter your choice 1,2,3 or 'q' to quit: ").lower()

        if user_choice == 'q':
            print("Quitting the game. Goodbye!")
            break

        if user_choice not in choices:
            print("Invalid choice. Please enter 1, 2, 3, or 'q' to quit.")
            continue

        computer_choice = random.choice(list(choices.keys()))
        print(f"Computer choice: {choices[computer_choice]}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif win_conditions[user_choice] == computer_choice:
            print("You win!")
        else:
            print("You lose!")

    print("Thanks for playing!")

def main():
    rock_paper_scissors()

if __name__ == "__main__":
    main()
