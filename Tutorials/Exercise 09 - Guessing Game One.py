# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)
#
# Extras:
#
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random


def generate_number():
    num = int(random.randint(0, 9))
    print("New Number generated\n")
    return num


def user_input():
    user_exit = False
    num_of_guess = 0
    num = generate_number()
    while not user_exit:
        guess = input("Guess number between 0 and 9: \n")
        if guess.isnumeric():
            guess = int(guess)
            if check_guess(guess, num, num_of_guess):
                num = generate_number()
            else:
                num_of_guess = num_of_guess + 1
        elif guess.lower() == "exit":
            print("Took num_of_guess")
            user_exit = True
        else:
            print("Invalid guess")


def check_guess(guess, num, num_of_guess):
    if guess not in range(0, 9):
        print("")
        return False
    elif guess == num:
        print(f"Guessed correctly took {num_of_guess} guesses")
        return True
    elif guess < num:
        print("Too low\n")
        return False
    elif guess > num:
        print("Too high\n")
        return False
    

user_input()
