# Function to check whether a number is even or odd

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Take input from user
number = int(input("Enter a number: "))

# Call the function and display the result
result = check_even_odd(number)
print(f"The number is {result}")