# Date: 2025-11-07
# Error Handling in Python

# Error Handling - Process of anticipating, catching, and managing errors in a program.

# Basic Error Handling
# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
#     print(f"Result: {result}")
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")

# print("\n--------------------------------\n")

#Example 2:

print("\n--------------------------------\n")

try: 
  file = open("data.txt", "r")
except FileNotFoundError:
    print("File not found!")
else:
    # Execute if no error
    content = file.read()
    print(f"File read successfully: {content}")
finally:
    

    if 'file' in locals() and not file.closed:
        file.close()
        print("Cleanup completed.")

print("\n--------------------------------\n")

