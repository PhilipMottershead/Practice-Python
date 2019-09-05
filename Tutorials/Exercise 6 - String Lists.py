# Ask the user for a string and print out whether this string is a palindrome or not.
# A palindrome is a string that reads the same forwards and backwards.

word = input("Enter word: ")
word_reversed = word[::-1]
if word == word_reversed:
    print("palindrome")
else:
    print("not a palindrome")
