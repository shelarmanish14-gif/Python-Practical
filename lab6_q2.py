# Question 2:
# Write a Python function to check whether a number is prime or not.

# Function to check prime number
def prime(num):

    # Numbers less than or equal to 1 are not prime
    if num <= 1:
        return False

    # Check divisibility from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            return False

    return True

# Take input from the user
number = int(input("Enter a number: "))

# Check and display result
if prime(number):
    print(number, "is a Prime Number")
else:
    print(number, "is Not a Prime Number")


# Output:
# Enter a number: 17
# 17 is a Prime Number
