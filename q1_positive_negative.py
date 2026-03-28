# Program to check whether a number is positive, negative, or zero

# Get input from the user
number = float(input("Enter a number: "))

# Check the sign of the number
if number > 0:
    print(f"{number} is a positive number")
elif number < 0:
    print(f"{number} is a negative number")
else:
    print(f"{number} is zero")
