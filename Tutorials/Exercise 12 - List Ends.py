# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# makes a new list of only the first and last elements of the given list.


def get_first_and_last_list(input_list):
    new_list = [input_list[0], input_list[len(input_list)-1]]
    return new_list


print(get_first_and_last_list([5, 10, 15, 20, 25]))
