# Write a password generator in Python.
# Be creative with how you generate passwords -
# strong passwords have a mix of:
#   lowercase letters
#   uppercase letters
#   numbers
#   symbols
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.
#
# Extra:
#
# Ask the user how strong they want their password to be.
# For weak passwords, pick a word or two from a list.

import random
import string

from random_words import RandomWords

lower = string.ascii_lowercase
upper = string.ascii_uppercase
symbol = string.punctuation
types = [lower, upper, symbol, string.digits]
r = RandomWords()


def generate_password_strong(length):
    word = "a"
    for num in range(length):
        type_of_letter = random.randint(0, 3)
        letter = random.choice(types[type_of_letter])
        word = word+letter
    return word


def generate_password_weak(num_of_words):
    password = ""
    while num_of_words != 0:
        password = password + r.random_word()
        num_of_words -= 1
    return password


def menu():
    input_string = input("Weak or Strong?\nW for Weak \nS for Strong\n").capitalize()
    choice = ["W", "S"]
    while input_string not in choice:
        print("Invalid input try again")
        input_string = input("Weak or Strong?\nW for Weak \nS for Strong\n").capitalize()
    if input_string == "W":
        weak_menu()
    elif input_string == "W":
        strong_menu()


def strong_menu():
    length = input("Enter length of password: \n")
    while not length.isnumeric():
        print("Invalid entry")
        length = input("Enter length of password: \n")

    print(generate_password_strong(int(length)-1))


def weak_menu():
    num_of_words = input("Enter number of words in password: \n")
    while not num_of_words.isnumeric():
        print("Invalid")
        num_of_words = input("Enter number of words in password: \n")
    print(generate_password_weak(int(num_of_words)))


menu()
