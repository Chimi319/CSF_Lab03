# Function to print the multiplication table of a number

def multiplication_table(num, range_limit):
    print(f"\nMultiplication table of {num}:")
    print("=" * 30)
    for i in range(1, range_limit + 1):
        print(f"{num} x {i} = {num * i}")

# Take input from user
number = int(input("Enter a number: "))
limit = int(input("Enter the range (up to which number): "))

# Call the function
multiplication_table(number, limit)