#!/usr/bin/env python3
"""Number Guessing Game | Step 3"""

import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Ask the user for their guess
def Attempt():
    guess_temp = input("Guess the number between 1 and 10: ")

    if guess_temp == "Ten" or guess_temp == "ten" or guess_temp == "10":
        guess = int(10)
    elif guess_temp == "Nine" or guess_temp == "nine" or guess_temp == "9":
        guess = int(9)
    elif guess_temp == "Eight" or guess_temp == "eight" or guess_temp == "8":
        guess = int(8)
    elif guess_temp == "Seven" or guess_temp == "seven" or guess_temp == "7":
        guess = int(7)
    elif guess_temp == "Six" or guess_temp == "six" or guess_temp == "6":
        guess = int(6)
    elif guess_temp == "Five" or guess_temp == "five" or guess_temp == "5":
        guess = int(5)
    elif guess_temp == "Four" or guess_temp == "four" or guess_temp == "4":
        guess = int(4)
    elif guess_temp == "Three" or guess_temp == "three" or guess_temp == "3":
        guess = int(3)
    elif guess_temp == "Two" or guess_temp == "two" or guess_temp == "2":
        guess = int(2)
    elif guess_temp == "One" or guess_temp == "one" or guess_temp == "1":
        guess = int(1)
    else:
        guess = 0
        print("ERROR ERROR ERROR. Please guess within the bounds next time!")


# Check the user's guess and provide hints

    if guess == secret_number:
        print("You guessed it! Great job!")
    elif guess > secret_number:
        print("Too high! Try Again!")
        Attempt()
    elif guess == 0:
        print("Let's try that again")
        Attempt()
    elif guess < secret_number:
        print("Too low! Try Again!")
        Attempt()
    else:
        print("Let's try that again")
        Attempt()
        

Attempt()



