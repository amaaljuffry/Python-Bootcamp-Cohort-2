# Date: 2025-11-07
# Classes and Objects in Python

# Class - Template for creating objects
# Object - Instance of a class

# Basic class definition
# class Person:
#     # Class attributes (shared by all instances)
#     species = "Homo Sapiens"

#     # Constructor method
#     def __init__(self, name, age):
#         # Instance attributes (unique to each instance)
#         self.name = name
#         self.age = age

#     # Instance method
#     def introduce(self):
#         return f"Hello, my name is {self.name} and I am {self.age} years old."
    
#     # Method with default parameter
#     def have_birthday(self):
#         self.age += 1
#         return f"Happy birthday! I am now {self.age} years old."

# # Creating objects
# person1 = Person("Ama", 30)
# person2 = Person("Noni", 25)

# # Accessing attributes and methods
# print(person1.name)
# print(person1.age)

# # Calling methods
# print(person1.introduce())
# print(person1.have_birthday())

# # Class attributes
# print(Person.species)
# print(person1.species)

# class BankAccount:
#     def __init__(self, account_number, owner, balance=0):
#         self.account_number = account_number
#         self.owner = owner
#         self.balance = balance
#         self.transactions = []

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             self.transactions.append(f"Deposited: {amount}")
#             return f"Deposited ${amount}. New balance: ${self.balance}"
#         else:
#             return "Invalid deposit amount. Please enter a positive number."

#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             self.transactions.append(f"Withdrew: {amount}")
#             return f"Withdrew ${amount}. New balance: ${self.balance}"
#         else:
#             return "Invalid withdrawal amount. Please enter a smaller number." 

#     def get_balance(self):
#         return f"Account balance: ${self.balance}"
    
#     def get_transactions(self):
#         return f"Transaction history: {self.transactions}"
# # Using the BankAccount class
# account = BankAccount("1234567890", "Ama", 1000)
# print(account.deposit(500))
# print(account.withdraw(200))
# print(account.get_balance())

# Exercise 1:Create a simple game character class with health, attack and heal methods.

class Pokemon:
    def __init__(self, name, hp, attack_power, move):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.move = move

    def attack(self, target):
        target.hp -= self.attack_power
        return f"{self.name} used {self.move}! It dealt {self.attack_power} damage to {target.name}. {target.name} has {target.hp} HP remaining."

    def heal(self):
        self.hp += 10
        return f"{self.name} used a Potion! {self.name} recovered 10 HP and now has {self.hp} HP."

    def get_status(self):
        return f"{self.name} has {self.hp} HP left."

# Example battle
pikachu = Pokemon("Pikachu", 100, 15, "Thunderbolt")
charmander = Pokemon("Charmander", 90, 12, "Flamethrower")

print(pikachu.attack(charmander))
print(charmander.heal())
print(charmander.get_status())
