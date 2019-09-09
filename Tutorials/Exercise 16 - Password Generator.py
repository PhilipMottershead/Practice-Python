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
import RandomWords
import flask
import string
lower = string.ascii_lowercase
upper = string.ascii_uppercase
symbol = string.punctuation
types = [lower, upper, symbol, string.digits]


def generate_password_strong(length):
    word = "a"
    for num in range(length):
        type_of_letter = random.randint(0, 3)
        letter = random.choice(types[type_of_letter])
        word = word+letter
    return word


def generate_password_weak():
    r = RandomWords()
    return r.get_random_words(3)


print(generate_password_weak())
