# Question 1: Using input() function take one number from the user and using ternary operators check whether the number is even or odd.

# Taking one number as input from the user
n = int(input("Enter a number: "))

# Checking whether the number is even or odd using the ternary operator
print(f"{n} is Even" if n % 2 == 0 else f"{n} is Odd")

# Output
# Enter a number: 4
# 4 is Even

# Enter a number: 7
# 7 is Odd
