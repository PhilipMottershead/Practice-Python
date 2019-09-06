# Write a program (function!) that takes a list
# returns a new list that contains all the elements of the first list minus all the duplicates.
#
# Extras:
#
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.


def remove_duplicates_set(new_list):
    return set(new_list)


def remove_duplicates_loop(list_a):
    list_result = []
    for num in list_a:
        if num not in list_result:
            list_result.append(num)
    return list_result


print(remove_duplicates_set([1, 1, 2, 2, 3, 3]))

print(remove_duplicates_loop([1, 1, 2, 2, 3, 3]))


