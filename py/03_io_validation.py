# # Date: 2025-11-04
# # Input/Output Validation in Python

# name = input("Enter your name: ")
# height = float(input("Enter your height: ")) #convert to float

# # # Input Validation
# while True:
#     try:
#         age = int(input("Enter your age: "))
#         if age < 0:
#             print("Age must be positive!")
#         else:
#             print(f"Your age is {age}.")
#             break
#     except ValueError:
#         print("Invalid input. Please enter a valid age.")
        
# # Output Formatting
# print(f"Hello, {name}!")
# print(f"You are {age} years old and {height:.2f} m tall.")

# Exercises:

# 1. Create a simple calculator that takes two number and an operation from user.


# # Solution 1:
# while True:
#     try:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#         operation = input("Enter operation (+, -, *, /): ")
        
#         if operation == '+':
#             result = num1 + num2
#         elif operation == '-':
#             result = num1 - num2
#         elif operation == '*':
#             result = num1 * num2
#         elif operation == '/':
#             if num2 == 0:
#                 print("Cannot divide by zero!")
#                 continue
#             result = num1 / num2
#         else:
#             print("Invalid operation!")
#             continue
        
#         print(f"The result of {num1} {operation} {num2} is {result}.")
#         break
#     except ValueError:
#         print("Please enter valid numbers!")
#     except Exception as e:
#         print(f"An error occurred: {e}")
        
        
        
# 2. Create a simple quiz program with 3 questions. At the end of the quiz, display score.
        
# Solution 2:
score = 0
questions = {
    "Q1: What is the capital of Malaysia?": "Kuala Lumpur",
    "Q2: What is the National Flower of Malaysia?": "Hibiscus",
    "Q3: What is the currency used in Malaysia?": "Ringgit"
}

for question, answer in questions.items():
    user_answer = input(f"{question} ")
    if user_answer.strip().lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {answer}.")

print(f"Your final score is {score}/{len(questions)}.")