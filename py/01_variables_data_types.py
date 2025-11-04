# Date: 2025-11-03
# Variables and Data Types in Python

# String
# Integer
# Float
name = "Bob"            # String
age = 10                # Integer
weight = 20.5           # Float
is_female = False       # Boolean

print(name)
print(type(name))

# Math Operations

x = 10
y = 3

print(x + y)  # Addition
print(x - y)  # Subtraction
print(x * y)  # Multiplication
print(x / y)  # Division
print(x // y) # Floor division
print(x % y)# Modulus
print(x ** y) # Exponentiation

print(type(x + y))  # Addition
print("2" + "3")  # String concatenation

# Exercises:

# 1. Create variables that consist String, Integer, Float, and Boolean data types.

print("")#new line for better readability
print("Exercises:1")

item = "Apple"  # string
quantity = 5    # Integer
price = 1.50    # Float
is_fresh = True # Boolean

# 1. Create variables that consist String, Integer, Float, and Boolean data types. Print value for each key.
print(f"Item: {item} (Type: {type(item)})")
print(f"Quantity: {quantity} (Type: {type(quantity)})")
print(f"Price: {price} (Type: {type(price)})")
print(f"Is Fresh: {is_fresh} (Type: {type(is_fresh)})")
print("")#new line for better readability


# 2. Convert Celsius to Fahrenheit. (F = C * 9/5 + 32)
celsius = 25
fahrenheit = celsius * 9/5 + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")



