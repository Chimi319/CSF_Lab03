# CSF_Lab03
Aim of the Lab
To develop a clear understanding of control structures in Python by implementing conditional statements,
loops, break and continue statements, and to learn how to define and invoke functions for solving
programming problems in a structured and efficient manner.

List of programs

Part A: Conditional Statements

1. Write a program to check whether a number is positive, negative, or zero.
Expected Output:
Enter a number: 7
The number is positive

Brief Explanation
This program takes a number as input from the user. It uses conditional statements (if, elif, else) to compare the value:

If the number is greater than 0, it prints positive.
If the number is less than 0, it prints negative.
If the number is equal to 0, it prints zero.

So for input 7, the output will be:
The number is positive.

2. Write a program to check whether a number is even or odd.
Expected Output:
Enter a number: 12
The number is even

Brief Explanation
This program checks whether a number is even or odd using the modulus operator (%):

If the number divided by 2 gives a remainder 0, it is even.
Otherwise, it is odd.

So for input 12, the output will be:
The number is even.

3. Write a program to find the largest of two numbers.
Expected Output:
Enter first number: 25
Enter second number: 18
25 is larger

Brief Explanation
This program takes two numbers as input and compares them using an if-else statement:

If the first number is greater than the second, it prints the first number.
Otherwise, it prints the second number as larger.

For input 25 and 18, the output will be:
25 is larger.

4. Write a program to find the largest of three numbers using nested if-else.
Expected Output:
Enter three numbers: 5 9 3
9 is the largest number

Brief Explanation
This program uses nested if-else statements to compare three numbers:

First, it compares a and b.
Then, it compares the larger of those with c.
The greatest value is printed as the largest number.

For input 5 9 3, the output will be:
9 is the largest number.

5. Write a program to take marks as input and display grade.
(A: ≥80, B: 60–79, C: 40–59, Fail: <40)
Expected Output:
Enter marks: 74
Grade B

Brief Explanation
This program takes marks as input and uses if-elif-else statements to assign grades:

Marks 80 or above → Grade A
Marks 60 to 79 → Grade B
Marks 40 to 59 → Grade C
Marks below 40 → Fail

For input 74, the output will be:
Grade B.

6. Write a menu-driven program using if-elif to perform addition, subtraction, multiplication, and
division.
Expected Output:
1. Add
2. Subtract
3. Multiply
4. Divide
Enter choice: 1
Enter two numbers: 10 5
Sum = 15
Part B: Loops (for and while)

Brief Explanation
This menu-driven program lets the user select an operation:

1 → Addition
2 → Subtraction
3 → Multiplication
4 → Division

It then takes two numbers as input and performs the selected operation using if-elif statements. Division by zero is handled to avoid errors.

For input choice 1 and numbers 10 5, the output will be:
Sum = 15.

7. Write a program to print numbers from 1 to 10 using a for loop.
Expected Output:
1 2 3 4 5 6 7 8 9 10

Brief Explanation
This program uses a for loop to print numbers from 1 to 10:

range(1, 11) generates numbers starting from 1 up to 10 (11 is excluded).
end=" " ensures the numbers are printed on the same line separated by a space.

Output:
1 2 3 4 5 6 7 8 9 10

8. Write a program to print all even numbers from 1 to 20.
Expected Output:
2 4 6 8 10 12 14 16 18 20

Brief Explanation
This program prints all even numbers from 1 to 20 using a for loop:

range(2, 21, 2) starts from 2, goes up to 20, and increments by 2 each time.
end=" " prints the numbers on the same line separated by a space.

Output:
2 4 6 8 10 12 14 16 18 20

9. Write a program to find the sum of the first 10 natural numbers.
Expected Output:
Sum = 55

Brief Explanation
This program calculates the sum of the first 10 natural numbers using a for loop:

range(1, 11) generates numbers from 1 to 10.
Each number is added to the variable sum using sum += i.
Finally, the total sum is printed.

Output:
Sum = 55

10. Write a program to display the multiplication table of a given number.
Expected Output:
Enter a number: 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50

Brief Explanation
This program prints the multiplication table of a given number using a for loop:

It takes a number as input.
range(1, 11) is used to multiply the number from 1 to 10.
f-string formatting displays the result in the standard multiplication table format.

For input 5, the output will be:

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50

11. Write a program to print numbers from 1 to 5 using a while loop.
Expected Output:
1
2
3
4
5

Brief Explanation
i starts at 1.
The loop runs while i is less than or equal to 5.
print(i, end=" ") prints the numbers on the same line separated by a space.
i += 1 increments the number each iteration.

Output:
1 2 3 4 5

12. Write a program to calculate the sum from 1 to n using a while loop.
Expected Output:
Enter n: 6
Sum = 21

Brief Explanation
This program calculates the sum of numbers from 1 to n using a while loop:

i starts at 1 and increments until it reaches n.
Each number is added to sum using sum += i.
After the loop, the total sum is printed.

For input 6, the output will be:
Sum = 21

13. Write a program that keeps taking input until the user enters 0.
Expected Output:
Enter number: 4
Enter number: 8
Enter number: 0
Loop ended

Brief Explanation
This program keeps taking integer input from the user until they enter 0:

The while loop continues as long as num is not 0.
Each input is checked; if it is 0, the loop ends.
After exiting the loop, it prints "Loop ended".

Sample Run:

Enter number: 4
Enter number: 8
Enter number: 0
Loop ended

Part C: Break and Continue

14. Write a program to print numbers from 1 to 10 but stop when the number becomes 6 using break.
Expected Output:
1
2
3
4
5

Brief Explanation
This program prints numbers from 1 to 10 using a for loop, but stops when the number reaches 6:

if i == 6: checks if the current number is 6.
break immediately exits the loop when the condition is true.
Numbers 1 to 5 are printed before the loop stops.

Output:

1
2
3
4
5

15. Write a program to print numbers from 1 to 10 but skip 5 using continue.
Expected Output:
1
2
3
4
6
7
8
9
10

Brief Explanation
This program prints numbers from 1 to 10 using a for loop, but skips 5:

if i == 5: checks if the current number is 5.
continue skips the rest of the loop body for that iteration and moves to the next number.
All other numbers from 1 to 10 are printed.

16. Write a program that searches for a number in a list and stops when found using break.
Expected Output:
List: 2 4 6 8 10
Searching for: 8
Number found
4

Brief Explanation
This program searches for a specific number in a list using a for loop:

It iterates through each element in the list numbers.
When the current number matches the search value, it prints "Number found" and breaks the loop immediately.
If the number is not found, the loop completes without printing anything (you can also add a message for "not found" if needed).

Sample Run:

List: 2 4 6 8 10
Searching for: 8
Number found

Part D: Functions

17. Define and call a function that prints “Hello, World!”.
Expected Output:
Hello, World!

Brief Explanation
This program defines a function greet that prints "Hello, World!".

The function is called using greet(), which executes the print statement.

Output:
Hello, World!

18. Define a function that returns the square of a number.
Expected Output:
Enter number: 6
Square = 36

Brief Explanation
This program defines a function square that:

Takes a number as input (num).
Returns its square using num ** 2.

The user is asked to enter a number, and the function is called to calculate and display the square.

For input 6, the output will be:
Square = 36

19. Define a function to add two numbers.
Expected Output:
Enter two numbers: 7 3
Sum = 10

Brief Explanation
This program defines a function add_numbers that:

Takes two arguments a and b.
Returns their sum using a + b.

The user inputs two numbers, the function is called, and the sum is printed.

For input 7 3, the output will be:
Sum = 10

20. Define a function to check whether a number is even or odd.
Expected Output:
Enter number: 11
The number is odd

Brief Explanation
This program defines a function check_even_odd that:

Takes a number as input.
Uses the modulus operator (%) to check if it is divisible by 2.
Prints "The number is even" if divisible by 2, otherwise prints "The number is odd".

For input 11, the output will be:
The number is odd

21. Write a function to calculate factorial of a number.
Expected Output:
Enter number: 5
Factorial = 120

Brief Explanation
This program defines a function factorial that calculates the factorial of a number n:

Initializes result = 1.
Uses a for loop from 1 to n multiplying each value with result.
Returns the factorial.

For input 5, the output will be:
Factorial = 120

22. Write a function to print the multiplication table of a number.
Expected Output:
Enter number: 3
3 x 1 = 3
3 x 2 = 6
...
3 x 10 = 30
5

Brief Explanation
This program defines a function multiplication_table that:

Takes a number as input.
Uses a for loop from 1 to 10.
Prints the multiplication result in standard table format using an f-string.

Part E: Integrated Programs

23. Write a program using a function and loop to print numbers from 1 to n and display whether each
is even or odd.
Expected Output:
Enter n: 5
1 -> Odd
2 -> Even
3 -> Odd
4 -> Even
5 -> Odd

Brief Explanation
This program integrates functions and loops:

The function print_even_odd(n) iterates from 1 to n using a for loop.
It checks each number with modulus operator (%) to determine if it is even or odd.
Prints the result in the format number -> Even/Odd.

24. Create a menu-driven calculator using functions and loop until the user exits.
Expected Output:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
Enter choice: 3
Enter two numbers: 4 5
Product = 20

Brief Explanation
This program is a menu-driven calculator using functions and loops:

Functions add, subtract, multiply, and divide perform the respective operations.
A while loop repeatedly shows the menu until the user chooses Exit (5).
The program asks for two numbers for the selected operation and displays the result.
Division by zero is handled to avoid errors.