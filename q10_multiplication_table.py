# Program to display the multiplication table of a given number

number = int(input("Enter a number: "))
range_limit = int(input("Enter the range (up to which number): "))

print(f"\nMultiplication table of {number}:")
print("=" * 30)

for i in range(1, range_limit + 1):
    print(f"{number} x {i} = {number * i}")