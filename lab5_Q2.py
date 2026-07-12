# Question 2: Using input() function take two numbers from the user and then swap the numbers.

# Taking the first number as input from the user
a = int(input("Enter the first number: "))

# Taking the second number as input from the user
b = int(input("Enter the second number: "))

# Displaying the numbers before swapping
print(f"Before swapping: a = {a}, b = {b}")

# Swapping the two numbers
a, b = b, a

# Displaying the numbers after swapping
print(f"After swapping: a = {a}, b = {b}")

# Output:-
# Enter the first number: 10
# Enter the second number: 25
# Before swapping: a = 10, b = 25
# After swapping: a = 25, b = 10
