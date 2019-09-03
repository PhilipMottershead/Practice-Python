#Ask the user for a number.
# Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?
#Extras:
#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num)
# and one number to divide by (check).
# If check divides evenly into num, tell that to the user.
# If not, print a different appropriate message.

number = int(input("Enter number: "))
number_two = int(input("Enter second number: "))
if number % 2 == 0:
    if number % 4 == 0:
        print("Divisible by 4")
    else:
        print("Even")
else:
    print("Odd")
if(number_two%number==0):
    print("Number two divides into Number one equally")
else:
    print("Number two doesn't divides into Number one equally")
