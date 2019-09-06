# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.
# For example, say I type the string:
# My name is Michele
# Then I would see the string:
# Michele is name My
# shown back to me.


def reverse_word_order(word):
    split_words = word.split(" ")
    split_words.reverse()
    reversed_word = " ".join(split_words)

    return reversed_word


input_word = input("Input sentence")
print(reverse_word_order(input_word))
