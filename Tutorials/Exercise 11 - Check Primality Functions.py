# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to help you.

input_number = int(input("Input number: "))


def check_if_prime(num):

    if find_divisors(num) <= 1 and num != 0:
        print("Is Prime")
    else:
        print("Is Not Prime")


def find_divisors(num):
    y = []
    for num in range(1, input_number):
        if input_number % num == 0:
            y.append(num)
    return y.__len__()


check_if_prime(input_number)
