# Date: 2025-11-06
# Dictionaries in Python

# key value data structure
# key need to be unique and immutable
# value can be duplicate

student = {
    "name": "Ama",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Science", "English"]
}

# Accessing and modifying dictionaries
# print(student["name"])   # print the value of the key "name"
# print(student.get("age"))    # print the value of the key "age"
# student["age"] = 21    # modify the value of the key "age"
# student["email"] = "ama@example.com"    # add a new key-value pair

# print(student)

# Dictionary Methods
# keys = student.keys()       # get all the keys of the dictionary
# values = student.values()   # get all the values of the dictionary
# items = student.items()    # get all the key-value pairs of the dictionary

# # print(keys)
# # print(values)
# print(items)

# # Iterating through a dictionary
# for key in student:
#     print(f"{key}: {student[key]}")

# for key, value in student.items(): #recommended way to iterate through a dictionary
#     print(f"{key}: {value}")


# Nested Dictionaries
# company = {
#     "employee": {
#         "john": {"age": 30,"department": "HR"},
#         "jane": {"age": 25,"department": "IT"},
#         },
#         "departments": ["HR", "IT", "Finance"]
# }

# print(company["employee"].items())
# print(company["departments"])

# Exercises 1: Create a dictionary called student_records with the following information:

# "student_001": name is "John", age is 19, major is "Computer Science", grades are [85, 92, 78]
# "student_002": name is "Sarah", age is 20, major is "Biology", grades are [90, 88, 95] 

#Solution 1:
# Exercises 1: Create a dictionary called student_records

student_records = {
    "student_001": {
        "name": "John",
        "age": 19,
        "major": "Computer Science",
        "grades": [85, 92, 78]
    },
    "student_002": {
        "name": "Sarah",
        "age": 20,
        "major": "Biology",
        "grades": [90, 88, 95]
    }
}

# Access data
print(student_records["student_001"]["name"])     # Output: John
print(student_records["student_002"]["grades"])   # Output: [90, 88, 95]

# Loop through the records
for student_id, info in student_records.items():
    print(f"ID: {student_id}")
    print(f"  Name: {info['name']}")
    print(f"  Age: {info['age']}")
    print(f"  Major: {info['major']}")
    print(f"  Grades: {info['grades']}")
    print()
