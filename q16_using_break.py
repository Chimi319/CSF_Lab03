# Program that searches for a number in a list and stops when found using break

numbers = [2 ,4, 6, 8, 10]
search_num = int(input("Enter a number to search: "))

found = False

for num in numbers:
    if num == search_num:
        print(f"Number {search_num} found ")
        found = True
        break

if not found:
    print(f"Number {search_num} not found ")