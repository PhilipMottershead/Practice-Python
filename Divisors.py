# Create a program that asks the user for a number and
# then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

input_number = int(input("Input number: "))
y = []
for num in range(1, input_number):
    if input_number % num  == 0:
        y.append(num)
print(y)
