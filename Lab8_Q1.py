""" Program: . Write a Python program and calculate the mean of the below dictionary. 

test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4} 

test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}
"""
total = 0
count = 0

for value in test_dict.values():
    total = total + value
    count = count + 1

mean = total / count

print("Dictionary:", test_dict)
print("Mean:", mean)


# Output:-
# Dictionary: {'A': 6, 'B': 9, 'C': 5, 'D': 7, 'E': 4}
# Mean: 6.2
