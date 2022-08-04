import random

def guessing_game():
    num_guesses = 0
    while True:
        num = random.randint(1, 101)
        guess = int(input("Guess the number from 1-100"))
        if guess > num:
            print("The number is too high")
            num_guesses = num_guesses +1
        if guess < num:
            print("The number is too low")
            num_guesses = num_guesses +1
        if guess == num:
            print("You guessed it right")
            num_guesses = num_guesses +1