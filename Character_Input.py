#Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
#Extras:
#Add on to the previous program by asking the user for another number
# and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines.
# (Hint: the string "\n is the same as pressing the ENTER button)
import datetime


now = datetime.datetime.now()
name = input("What is your name? ")
age = int(input("What is your age? "))
times_to_print = int(input("Input number of times to print :"))
year_at_100 = now.year + 100 - age
print(f"Hi {name} you will be 100 in the year {year_at_100}\n" * times_to_print)

