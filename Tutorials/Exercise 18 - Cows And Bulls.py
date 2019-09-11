# Create a program that will play the “cows and bulls” game with the user. The game works like this:
#
# Randomly generate a 4-digit number.
# Ask the user to guess a 4-digit number.
# For every digit that the user guessed correctly in the correct place, they have a “cow”.
# For every digit the user guessed correctly in the wrong place is a “bull.”
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
# Once the user guesses the correct number, the game is over.
# Keep track of the number of guesses the user makes throughout the game
# tell the user at the end.

import random


def menu():
    while True:
        guess = input_guess()
        if not guess.isnumeric():
            print("Not a number")
        elif len(guess) != 4:
            print("Not 4 Digits")
        else:
            break
    return guess


def input_guess():
    guess = input("Guess the 4 digit number\n" +
                  "Cows mean a correct digit, Bulls mean a incorrect digit\n"
                  "Enter a 4 digits i.e. 1234: ")
    return guess


def cow_bull(target):
    correctly_guessed = False
    guesses = 0
    while not correctly_guessed:
        index = 0
        cow = 0
        bull = 0

        guess = menu()
        guesses = guesses + 1
        while index != len(guess):
            if guess[index] == target[index]:
                cow += 1
            else:
                bull += 1
            index += 1
        if cow == 4:
            correctly_guessed = True
        else:
            print(f"Cows: {cow} Bull: {bull}")
    print(f"Guessed correctly with {guesses} guesses")


def generate_number():
    return str(random.randint(1000, 9999))


if __name__ == "__main__":
    target_number = generate_number()
    cow_bull(target_number)
