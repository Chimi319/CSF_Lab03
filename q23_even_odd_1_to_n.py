# Function to print numbers from 1 to n and display whether each is even or odd

def check_even_odd_range(n):
    print(f"\nNumbers from 1 to {n} with even/odd status:")
    print("=" * 40)
    for num in range(1, n + 1):
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")

# Take input from user
number = int(input("Enter a number (n): "))

# Call the function
check_even_odd_range(number)