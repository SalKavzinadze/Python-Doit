import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    print("I am thinking of a number between 1 and 100.")
    
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10  # მაქსიმალური მცდელობები

    while attempts < max_attempts:
        guess = input("Enter your guess: ")

        
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break
    else:
        print(f"Sorry, you didn't guess the number. It was {number_to_guess}.")

guess_the_number()
