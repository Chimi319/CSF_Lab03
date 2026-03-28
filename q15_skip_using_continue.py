# Program to print numbers from 1 to 10 but skip 5 using continue

for num in range(1, 11):
    if num == 5:
        continue
    print(num)

print("Loop ended")