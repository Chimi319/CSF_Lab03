# Function to calculate factorial of a number

def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers"
    elif num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

# Take input from user
number = int(input("Enter a number: "))

# Call the function and display the result
result = factorial(number)
print(f"Factorial : {result}")