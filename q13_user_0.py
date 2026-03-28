# Program that keeps taking input until the user enters 0

print("Enter numbers (enter 0 to stop):")

while True:
    num = int(input("Enter a number: "))
    
    if num == 0:
        print("You entered 0. Program terminated!")
        break
    else:
        print(f"You entered: {num}")

print("Thank you for using the program!")