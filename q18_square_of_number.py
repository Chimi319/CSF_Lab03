# Function that returns the square of a number

def square(num):
    return num * num

# Take input from user
number = int(input("Enter  number: "))

# Call the function and display the result
result = square(number)
print(f"Square : {result}")