# Date: 2025-11-04
# String Manipulation in Python


# # String Manipulation

# # String creation
# single_quote_str = 'Hello, World!'
# double_quote_str = "Hello, Python!"
# triple_quote_str = """Hello,
# This is a multi-line string."""

# print(single_quote_str)
# print(double_quote_str)
# print(triple_quote_str)


# #String indexing and slicing
# text = "Python Programming"

# print(text[0])          # First character
# print(text[-1])         # Last character
# print(text[0:6])        # Slice from 0 to 5
# print(text[:6])         # from start to index 5
# print(text[7:])         # 7 to end



# # String methods
# #name - "bob the builder"
# name = " bob the builder "

# print(len(name))                     # Length of the string
# print(name.strip())                  # Remove whitespace
# print(name.upper())                  # Convert to UPPERCASE
# print(name.lower())                  # Convert to lowercase
# print(name.title())                  # Convert to Title Case
# print(name.replace("bob", "jane"))   # Replace substring

# # String formatting
# name = "John Doe"
# age = 30

# message_1 = f"My name is {name} and I am {age} years old."                              #f-string
# message_2 = "My name is {name} and I am {age} years old.".format(name=name, age=age)    #str.format()
# message_3 = "My name is %s and I am %d years old." % (name, age)                        #% formatting

#Exercises:
# 1. Build a simple text analyzer that counts words, characters, and sentences in a given text.

import re


text = """Python is a powerful programming language. It's easy to learn
and versatile!
You can use Python for web development, data science, and
automation. The syntax is clean and readable.
This makes Python perfect for beginners and experts alike."""

#Solution:


# Count characters
characters = len(text)
print("Characters:", characters)

# Count words
words = text.split()  # splits text by spaces into a list of words
print("Words:", len(words))

# Count sentences
sentences = text.count('.') + text.count('!') + text.count('?')
print("Sentences:", sentences)

print("Characters:", characters)
print("Words:", words)
print("Sentences:", sentences)