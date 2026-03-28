# Program to calculate the sum from 1 to n using a while loop

n = int(input("Enter n: "))

sum = 0
num = 1

while num <= n:
    sum += num
    num += 1

print(f"Sum : {sum}")