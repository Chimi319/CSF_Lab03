# Program to take marks as input and display grade

marks = int(input("Enter marks: "))

if marks >= 80:
    print(f"Grade: A")
elif marks >= 60:
    print(f"Grade: B")
elif marks >= 40:
    print(f"Grade: C")
else:
    print(f"Grade: Fail")