# Date: 2025-11-04
# Conditional Statements in Python

# Fundamental conditional statement
# age = 18



# age = 18
# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")

# Multiple conditionals statements
# score = 60

# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")

#     print(f"Your score is: {score}")



# Conditional Statements with Logical Operators
# and, or, not
# and : both conditions must be true
# or  : at least one condition must be true

# user_age = 20
# has_license = True

# if user_age >= 18 and has_license:
#     print("User is eligible to drive.")
# else:
#     print("User is not eligible to drive.")
    
# day = "Saturday"
# if day == "Saturday" or day == "Sunday":
#     print("It's the weekend!")
# else:
#     print("It's a weekday.")
    
# # Conditional Statements with Nested Conditionals
# weather = "sunny"
# temperature = 75

# if weather == "sunny":
#     if temperature > 80:
#         print("It's a hot sunny day.")
#     else:
#         print("It's a pleasant sunny day.")
        
# Conditional Statements Operators
# '=' : assignment
# '==' : equality comparison
# '!=' : inequality comparison
# '>' : greater than
# '<' : less than
# '>=' : greater than or equal to
# '<=' : less than or equal to

# Exercise
# 1. Write a program that categorizes BMI (Body Mass Index) into underweight(<18.5), normal weight(<24.9), overweight(<29.9), and obesity(<30.0). (formula = kg/m^2)

# BMI Categorizer Program

# Get user input
weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in meters (m): "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display BMI value
print(f"\nYour BMI is: {bmi:.2f}")

# Determine BMI category
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 24.9:
    print("Category: Normal weight")
elif bmi < 29.9:
    print("Category: Overweight")
else:
    print("Category: Obesity")
