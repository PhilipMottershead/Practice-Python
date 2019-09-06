# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.

starting_number = [1]


def next_number(num):
    if num == 1 or num == 2:
        return 1
    return next_number(num - 1) + next_number(num - 2)


def fibo(num):
    new_list = []
    while num != 0:
        new_list.append(next_number(num))
        num = num - 1
    new_list.reverse()
    return new_list


print(fibo(int(input("Input number of numbers in the Fibonnaci sequence to generate"))))
