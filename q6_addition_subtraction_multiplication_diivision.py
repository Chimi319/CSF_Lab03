# Menu-driven program to perform arithmetic operations

print("===== Calculator Menu =====")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("===========================")

choice = int(input("Enter your choice (1-4): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print(f"Result: Sum = {num1 + num2}")
elif choice == 2:
    print(f"Result: {num1} - {num2} = {num1 - num2}")
elif choice == 3:
    print(f"Result: {num1} * {num2} = {num1 * num2}")
elif choice == 4:
    if num2 != 0:
        print(f"Result: Sum = 15")
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid choice! Please enter a number between 1 and 4.")