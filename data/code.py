import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while attempts < max_attempts - 1:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: "))
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
                return
        except ValueError:
            print("That's not a valid number! Please enter a number between 1 and 100.")
    
    
    print("\nLast chance! Here are 5 numbers, one of them is correct.")
    final_choices = random.sample(range(1, 101), 4)  
    final_choices.append(secret_number)  
    random.shuffle(final_choices)  
    
    print(f"Choose from: {final_choices}")
    
    final_guess = int(input("Enter your final guess: "))
    
    if final_guess == secret_number:
        print(f"Congratulations! You've guessed the right number: {secret_number}")
    else:
        print(f"Sorry, the correct number was: {secret_number}. Better luck next time!")
        
guess_the_number()
