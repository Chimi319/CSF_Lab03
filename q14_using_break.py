# Program to print numbers from 1 to 10 but stop when the number becomes 6 using break

for num in range(1, 11):
    if num == 6:
        print("Stopping at 6!")
        break
    print(num)

print("Loop ended")