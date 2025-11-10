# Date: 2025-11-07
# Modules and Library in Python

# Modules - A file containing Python code that can be imported into another Python file.
# Create math_utils.py

# from math_utils import add, multiply, factorial, PI, Calculator

# result = add(5, 3)
# result = multiply(5, 3)
# result = factorial(5)

# result_calculator = Calculator()
# print(f"Addition: {result}")



# Library - A collection of modules.

# Importing modules
import os
import sys
import datetime
import random

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

now = datetime.datetime.now()
today = datetime.date.today()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

print(f"Now date: {now}")
print(f"Today date: {today}")
print(f"Current Date and Time: {formatted_date}")

random_number = random.randint(1, 100)
random_choice = random.choice(["rock", "paper", "scissors"])
random_shuffle = random.shuffle([1, 2, 3, 4, 5])

print(f"Random number: {random_number}")
print(f"Random choice: {random_choice}")
print(f"Shuffled list: {[1, 2, 3, 4, 5]}")