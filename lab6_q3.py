# Question 3:
# Write a Python function to print the Fibonacci series.

# Function to print Fibonacci series
def fibonacci(n):

    # First two numbers of the series
    a = 0
    b = 1

    print("Fibonacci Series:")

    # Print Fibonacci numbers
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

# Take input from the user
num = int(input("Enter the number of num: "))

# Call the function
fibonacci(num)


# Output:
# Enter the number of num: 10
# Fibonacci Series:
# 0 1 1 2 3 5 8 13 21 34
