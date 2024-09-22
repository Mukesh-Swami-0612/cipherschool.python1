# cipherschool.python1
import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the right number: {secret_number}")
                print(f"It took you {attempts} attempts.")
                break
        except ValueError:
            print("That's not a valid number! Please enter a number between 1 and 100.")

guess_the_number()
