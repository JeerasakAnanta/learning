#Dat
def main():
    import random

    word_list = ["python", "hangman", "programming", "developer", "code"]
    chosen_word = random.choice(word_list)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")

    while attempts > 0:
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in chosen_word])
        print("Word:", display_word)

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in chosen_word:
            guessed_letters.append(guess)
            print("Good job! You guessed a letter.")
        else:
            guessed_letters.append(guess)
            attempts -= 1
            print("Sorry, that letter is not in the word. Attempts left:", attempts)

        if all(letter in guessed_letters for letter in chosen_word):
            print("Congratulations! You've guessed the word:", chosen_word)
            break
    else:
        print("You've run out of attempts! The word was:", chosen_word)

main()
