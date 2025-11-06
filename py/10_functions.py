# Date: 2025-11-06
# Functions in Python

# Reusable blocks of code that perform a specific task.


# Functions are defined using the def keyword.
# Functions are called using the function name and parentheses.
# Functions can be called multiple times.
# Functions can be passed arguments.
# Functions can return values.

# Functions with parameters
# def greet_person(name):
#     print(f"Hello, {name}!")

#     greet_person("Alice")

# # Functions with return values
# def add_numbers(a, b):
#     return a + b

# result = add_numbers(5, 3)
# print(result)

# #Default Parameters
# def greet_with_title(name, title="Mr."):
#     return f"Hello, {title} {name}!"

# print(greet_with_title("Alice")) # Hello, Mr. Alice!
# print(greet_with_title("Bob", "Dr.")) # Hello, Dr. Bob!


# Function Arguments
# access by index: args[0], args[1], etc.
#unpacking: func(*list)

#*args - variable length argument list
def sum_all(*args):
    return sum(args)

    print(sum_all(1, 2, 3, 4, 5)) # 15

# Functions kwargs: access by key: kwargs["name"], kwargs["age"], etc.
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
print_info(name="Alice", age=25, city="New York") # Alice: 25, New York:

#combining args and kwargs
def flexible_function(*args, **kwargs):
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")
    
flexible_function(1, 2, 3, name="Alice", age=25) # Positional arguments: (1, 2, 3), Keyword arguments: {'name': 'Alice', 'age': 25}


# Lambda functions
    # anonymous functions
    # small function
    # A lambda function is just a small, unnamed function that you can write in one line.
    # It is useful when you need a function for a short period of time.
    # It is also useful when you need to pass a function as an argument to another function.

# square = lambda x: x ** 2
# print(square(5)) # 25

# add = lambda x, y: x + y
# print(add(5, 3)) # 8

# Exercises 1 : Write a function that checks if a number is prime.

# What is a prime number?

# A prime number is a number greater than 1 that has no divisors other than 1 and itself.

# def is_prime(number):
#     """
#     Check if a number is prime.
    
#     Args:
#         number (int): The number to check.
    
#     Returns:
#         bool: True if prime, False otherwise.
#     """
#     if number <= 1:
#         return False  # 0 and 1 are not prime numbers
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False  # divisible by i → not prime
#     return True  # no divisors found → number is prime

# # Example usage
# print(is_prime(2))    # True
# print(is_prime(9))    # False
# print(is_prime(17))   # True
# print(is_prime(1))    # False


# Exercises 2 : Build a temperature converter function. (Celsius to Fahrenheit

# Formula: Fahrenheit = (Celsius * 9/5) + 32


def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius.
        
    Returns:
        float: Temperature in Fahrenheit.
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Example usage
print(celsius_to_fahrenheit(0))     # 32.0
print(celsius_to_fahrenheit(25))    # 77.0
print(celsius_to_fahrenheit(100))   # 212.0
