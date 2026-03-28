# Menu-driven calculator using functions

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Cannot divide by zero!"

def display_menu():
    print("\n===== Calculator Menu =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("===========================")

# Main program
while True:
    display_menu()
    choice = int(input("Enter your choice (1-5): "))
    
    if choice == 5:
        print("Thank you for using the calculator! Goodbye!")
        break
    
    if choice in [1, 2, 3, 4]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == 1:
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == 2:
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == 3:
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == 4:
            print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")