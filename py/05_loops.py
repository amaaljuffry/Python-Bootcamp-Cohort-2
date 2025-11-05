# Date: 2025-11-05
# Loops in Python

# For and While Loops

# For Loop: Known iterations
# While Loop: Unknown iterations

# Rule of thumb:
# if you can count the number of iterations, use for loop
# if you are waiting for a condition to be met, use while loop

# break
# Stops the loop immediately
# if i == 3: break

# continue
# Skips current iteration, continues next one
# if i == 3: continue

# pass
# Placeholder (does nothing)
# Used when loop is required syntactically but no code yet

# for loop
# You know how many times to repeat
# for i in range(10)

# while loop
# Repeat until a condition is false
# while count < 10

# # For Loop

# for i in range(5):  #0, 1, 2, 3, 4
#     print(i)

# for i in range(1,6): #1, 2, 3, 4, 5
#     print(i)

# for i in range (0,10,2): #0, 2, 4, 6, 8
#     print(i)

# # While Loop
# count = 0
# while count < 5:
#     print(count)
#     count += 1

# # Loop Control Statements
# for i in range(10):
#     if i == 5:
#         continue  #Skip this iteration 
#     if i == 7:
#         break #Stop the loop
#     print(i)

# # Nested Loops
# for i in range(2):
#     for j in range(3):
#         print(f"i: {i}, j: {j}")



# Exercises 1: Create a multiplication table generator

# Solution 1:

# Enter a number: 5
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50


# # Multiplication Table Generator

# # Step 1: Ask user for a number

# num = int(input("Enter a number: "))  # input() always returns a string, so we use int() to convert it.

# # Step 2: Loop through 1 to 10
# for i in range(1, 11):  # range(1, 11) means 1 to 10 # We use a for loop to repeat from 1 to 10.

#     result = num * i  # Calculate the result of the multiplication

#     # Step 3: Calculate and print result
#     print(f"{num} x {i} = {result}")

# Prime Number Finder

# Exercises 2: Write a program that finds all prime numbers up to a given number. (limit = 20)

# Solution 2:
# Step 1 Input limit
limit = int(input("Enter the limit: "))

#Step 2 Outer loop: Go through all numbers
for num in range(2, limit + 1):  # Start from 2, because 1 is not prime # We use a for loop to repeat from 2 to limit.

#Step 3 Inner loop: Check if number is prime
    is_prime = True
    for i in range(2, num):
        if num % i == 0: # if divisible by any number, not prime
            is_prime = False
            break

#Step 4 Print prime numbers
    if is_prime:
        print(num)
