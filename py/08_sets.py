# Date: 2025-11-06
# Sets in Python

# A set of data within curly braces
# Unordered and unique elements

# fruits = {"apple", "banana", "cherry"}
# numbers = {1, 2, 3, 4, 5}

# # Set Operations
# fruits.add("orange") # add the element to the set
# fruits.remove("banana") # remove the element from the set
# fruits.discard("cherry") # discard the element from the set
# fruits.clear() # clear the set

# print(fruits) 


# Sets mathematic operations
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}

# print(set1.union(set2)) # {1, 2, 3, 4, 5, 6, 7}
# print(set1.intersection(set2)) # {3, 4, 5}
# print(set1.difference(set2)) # {1, 2}
# print(set1.symmetric_difference(set2)) # {1, 2, 6, 7}

# Exercises 1: Create a system that stores student grades as tuples (name, subject, grade) and uses sets to find unique subjects and students.

grades = [
("Alice", "Math", 85),
("Bob", "Science", 92),
("Alice", "Science", 78),
("Charlie", "Math", 90),
("Bob", "Math", 88),
("Alice", "English", 95)
]

# Solution 1:

# Step 1: Extract unique students and subjects using sets
students = set()
subjects = set()

for name, subject, grade in grades:
    students.add(name)
    subjects.add(subject)

# Step 2: (Optional) Display everything neatly
print("All student grades:")
for record in grades:
    print(record)

print("\nUnique students:", students)
print("Unique subjects:", subjects)
