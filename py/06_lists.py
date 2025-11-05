# Date: 2025-11-06
# Lists in Python

# fruits = [ "banana", "apple","orange"]
# numbers = [1, 2, 3, 4, 5]
# mixed = ["apple", 1, 2.5, True]
# empty = []

# # Accessing Elements
# print(fruits[0])    # apple 
# print(fruits[-1])   # orange
# print(numbers[1:4])   # [2, 3, 4]
# print(numbers[:3])    # [1, 2, 3]
# print(numbers[3:])    # [3, 4, 5]
# print(numbers[2:])   # [3, 4, 5]

# #List Methods
# fruits.append("grape")
# print(fruits)       # ["banana", "apple", "orange", "grape"] # add the item to the end of the list

# fruits.insert(1, "kiwi")
# print(fruits)       # ["banana", "kiwi", "apple", "orange", "grape"] # insert the item at the index 1

# fruits.remove("orange")
# print(fruits)       # ["banana", "pear", "apple", "grape"] # remove the first occurrence of the item

# fruits.pop()
# print(fruits)       # ["banana", "pear", "apple"] # remove the last item

# fruits.clear()
# print(fruits)       # [] # clear the list

# fruits.sort()
# print(fruits)       # ["apple", "banana", "grape", "kiwi"] # sort the list

# fruits.reverse()
# print(fruits)       # ["kiwi", "grape", "banana", "apple"] # reverse the list

# fruits.count("apple")
# print(fruits)       # 1

#List Operations

# len(fruits) # length of the list
# "apple" in fruits # check if the item is in the list
# fruits + ["mango"] # concatenate two lists
#fruits * 2 # repeat the list twice

#edited_fruits = fruits.copy() # copy the list
#edited_fruits.append("mango") # add the item to the end of the list

#print(edited_fruits) # print the edited list
#print(len(fruits)) # print the length of the list

# print(fruits) # print the original list

#Exercises 1 :
#Create a grocery list and perform various operations.

# Solution 1:
grocery_list = ["petai", "bayam", "kangkung", "bawang putih"]
print(grocery_list) # print the original list

print(len(grocery_list)) # print the length of the list

print("petai" in grocery_list) # check if the item is in the list

grocery_list.append("cili kering") # add the item to the end of the list
print(grocery_list) # print the edited list

grocery_list.remove("kangkung") # remove the item from the list
print(grocery_list) # print the edited list

grocery_list.pop(1) # remove the item at the index 1
print(grocery_list) # print the edited list

grocery_list.sort() # sort the list
print(grocery_list) # print the edited list

grocery_list.reverse() # reverse the list
print(grocery_list) # print the edited list

grocery_list.copy() # copy the list
print(grocery_list) # print the edited list

grocery_list.extend(["kangkung", "bawang putih"]) # extend the list
print(grocery_list) # print the edited list

grocery_list.clear() # clear the list
print(grocery_list) # print the edited list