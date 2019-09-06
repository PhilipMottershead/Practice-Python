# Take two lists, say for example these two:
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list
# that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
#
# Extras:
# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
import random
a = random.sample(range(1, 101), 25)
b = random.sample(range(1, 101), 25)


def check_for_duplicates(list_a, list_b):
    list_result = []
    for num in list_a:
        if num in list_b and num not in list_result:
            list_result.append(num)
    return list_result


print(check_for_duplicates(a, b))
