# Program: 


# Create a list
list1 = [20, 35, 45, 22, 68]

# Assume first element is largest and smallest
largest = list1[0]
smallest = list1[0]

# Find largest and smallest
for i in list1:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

# Display result
print("List:", list1)
print("Largest Number:", largest)
print("Smallest Number:", smallest)



# Output:-
# List: [20, 35, 45, 22, 68]
# Largest Number: 68
# Smallest Number: 20
