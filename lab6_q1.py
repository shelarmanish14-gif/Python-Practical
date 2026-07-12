# Question 1:
# Write a Python function to calculate the factorial of a number.
# Function to calculate factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

# Take input from the user
num = int(input("Enter a number: "))

# Display the factorial
print("Factorial =", factorial(num))

# Output:
# Enter a number: 5
# Factorial = 120
